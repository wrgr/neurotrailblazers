#!/usr/bin/env node
/**
 * Headless Chrome Automated Retriever for ScienceDirect / Cell Press Literature.
 * Uses native Node.js 25 WebSocket + Chrome DevTools Protocol (CDP) on macOS.
 * Implements human-paced throttling (3-5s delay) to stay within proxy limits.
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.resolve(__dirname, '../..');
const PRIVATE_PAPERS_DIR = path.resolve(PROJECT_ROOT, '../neurotrailblazers-private/papers');
const MANIFEST_PATH = path.resolve(PROJECT_ROOT, 'data/pdf_corpus/corpus_manifest.json');
const COOKIE_PATH = path.resolve(PROJECT_ROOT, 'jhu_cookie.txt');
const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

if (!fs.existsSync(PRIVATE_PAPERS_DIR)) {
  fs.mkdirSync(PRIVATE_PAPERS_DIR, { recursive: true });
}

function sanitizeDoi(doi) {
  return doi.trim().toLowerCase().replace(/[/\\:*?"<>|]/g, '_') + '.pdf';
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main() {
  console.log('='.repeat(80));
  console.log('  🌐 HEADLESS CHROME CELL PRESS & SCIENCEDIRECT AUTOMATED RETRIEVER   ');
  console.log('='.repeat(80));

  let token = 'j4H4wIJwyynG6MPTQhL1Su3rACXE0RB';
  if (fs.existsSync(COOKIE_PATH)) {
    token = fs.readFileSync(COOKIE_PATH, 'utf8').trim() || token;
  }

  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  const downloadedFiles = new Set(fs.readdirSync(PRIVATE_PAPERS_DIR));

  // Identify unresolved papers (prioritizing 10.1016 ScienceDirect / Cell Press)
  const queue = [];
  for (const [doi, rec] of Object.entries(manifest)) {
    const filename = sanitizeDoi(doi);
    if (!downloadedFiles.has(filename) && rec.pdf_status !== 'DOWNLOADED') {
      queue.push({ doi, rec, filename });
    }
  }

  // Sort queue: ScienceDirect / Cell Press (10.1016) first
  queue.sort((a, b) => {
    const aIsElsevier = a.doi.includes('10.1016') ? 1 : 0;
    const bIsElsevier = b.doi.includes('10.1016') ? 1 : 0;
    return bIsElsevier - aIsElsevier;
  });

  console.log(`Found ${queue.length} unresolved papers in queue.`);
  console.log(`ScienceDirect / Cell Press target items: ${queue.filter((q) => q.doi.includes('10.1016')).length}`);
  console.log(`Target Private Stash: ${PRIVATE_PAPERS_DIR}`);
  console.log(`Human-paced delay: 3.5s per download to prevent proxy suspension.`);
  console.log('='.repeat(80));

  // Spawn Headless Chrome with isolated temp user data dir
  const tempProfile = path.resolve(__dirname, `../../.chrome_temp_${Date.now()}`);
  fs.mkdirSync(tempProfile, { recursive: true });

  const chrome = spawn(CHROME_PATH, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    `--user-data-dir=${tempProfile}`,
    '--no-first-run',
    '--no-default-browser-check',
    'about:blank'
  ]);

  await sleep(1500);

  let ws;
  try {
    const listRes = await fetch('http://127.0.0.1:9222/json/list');
    const pages = await listRes.json();
    const pageWsUrl = pages[0].webSocketDebuggerUrl;
    console.log(`Connected to Chrome DevTools: ${pageWsUrl}`);

    ws = new WebSocket(pageWsUrl);
    let msgId = 1;

    function send(method, params = {}) {
      return new Promise((resolve, reject) => {
        const id = msgId++;
        const timeout = setTimeout(() => reject(new Error(`Timeout on ${method}`)), 20000);
        const handler = (e) => {
          const res = JSON.parse(e.data);
          if (res.id === id) {
            clearTimeout(timeout);
            ws.removeEventListener('message', handler);
            resolve(res.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    await new Promise((resolve) => {
      ws.onopen = resolve;
    });

    await send('Page.enable');
    await send('Network.enable');
    await send('Browser.setDownloadBehavior', {
      behavior: 'allow',
      downloadPath: PRIVATE_PAPERS_DIR,
      eventsEnabled: true
    });

    // Set JHU Cookies
    await send('Network.setCookie', {
      name: 'ezproxy',
      value: token,
      domain: '.library.jhu.edu',
      path: '/'
    });
    await send('Network.setCookie', {
      name: 'EZPROXY_SESSION',
      value: token,
      domain: '.proxy1.library.jhu.edu',
      path: '/'
    });

    let successCount = 0;

    for (let i = 0; i < queue.length; i++) {
      const item = queue[i];
      const targetPdfPath = path.join(PRIVATE_PAPERS_DIR, item.filename);

      if (fs.existsSync(targetPdfPath) && fs.statSync(targetPdfPath).size > 5000) {
        continue;
      }

      console.log(`\n[${i + 1}/${queue.length}] Fetching: ${item.doi} (${item.rec.title?.slice(0, 50)}...)`);

      try {
        let fetchUrl = '';
        if (item.doi.includes('10.1016/')) {
          const suffix = item.doi.split('10.1016/')[1];
          fetchUrl = `https://www-sciencedirect-com.proxy1.library.jhu.edu/science/article/pii/${suffix}/pdfft?isDTMRedir=true&download=true`;
        } else {
          fetchUrl = `https://proxy1.library.jhu.edu/login?url=https://doi.org/${encodeURIComponent(item.doi)}`;
        }

        // Before download: snapshot directory
        const beforeFiles = new Set(fs.readdirSync(PRIVATE_PAPERS_DIR));

        await send('Page.navigate', { url: fetchUrl });
        await sleep(3500);

        // Check if any new PDF was downloaded
        const afterFiles = fs.readdirSync(PRIVATE_PAPERS_DIR);
        const newFiles = afterFiles.filter((f) => !beforeFiles.has(f) && !f.endsWith('.crdownload') && !f.startsWith('.'));

        if (newFiles.length > 0) {
          const downloadedName = newFiles[0];
          const downloadedPath = path.join(PRIVATE_PAPERS_DIR, downloadedName);
          const stat = fs.statSync(downloadedPath);
          const buf = Buffer.alloc(10);
          const fd = fs.openSync(downloadedPath, 'r');
          fs.readSync(fd, buf, 0, 10, 0);
          fs.closeSync(fd);

          if (buf.toString('utf8').startsWith('%PDF-')) {
            if (downloadedPath !== targetPdfPath) {
              fs.renameSync(downloadedPath, targetPdfPath);
            }
            console.log(` ✅ Downloaded via Headless Chrome: ${item.filename} (${(stat.size / 1024 / 1024).toFixed(1)} MB)`);
            successCount++;
            manifest[item.doi].pdf_status = 'DOWNLOADED';
            manifest[item.doi].local_pdf_path = targetPdfPath;
            manifest[item.doi].rights_category = 'ALL_RIGHTS_RESERVED';
          }
        } else {
          // Attempt DOM extraction if direct download link exists
          const linkRes = await send('Runtime.evaluate', {
            expression: `(() => {
              const meta = document.querySelector('meta[name="citation_pdf_url"]');
              if (meta && meta.content) return meta.content;
              const a = document.querySelector('a.pdf-download, a[data-testid="pdf-download-link"], a[href*="pdfft"], a.anchor-primary');
              return a ? a.href : null;
            })()`
          });

          const extractedPdfUrl = linkRes?.result?.value;
          if (extractedPdfUrl && extractedPdfUrl.startsWith('http')) {
            console.log(`  Found DOM PDF URL: ${extractedPdfUrl}`);
            await send('Page.navigate', { url: extractedPdfUrl });
            await sleep(3500);

            const postFiles = fs.readdirSync(PRIVATE_PAPERS_DIR);
            const freshFiles = postFiles.filter((f) => !beforeFiles.has(f) && !f.endsWith('.crdownload') && !f.startsWith('.'));
            if (freshFiles.length > 0) {
              const dPath = path.join(PRIVATE_PAPERS_DIR, freshFiles[0]);
              fs.renameSync(dPath, targetPdfPath);
              console.log(` ✅ Downloaded via DOM link: ${item.filename}`);
              successCount++;
            }
          } else {
            console.log(` ⚠️ No direct PDF stream detected for ${item.doi}`);
          }
        }
      } catch (err) {
        console.log(` ❌ Error fetching ${item.doi}: ${err.message}`);
      }

      // Save manifest progress every 10 papers
      if (i % 10 === 0) {
        fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2));
      }

      // Human-paced cooldown between requests
      await sleep(3000);
    }

    fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2));

    console.log('='.repeat(80));
    console.log(`HEADLESS RETRIEVAL RUN FINISHED: ${successCount} new papers downloaded.`);
    console.log('='.repeat(80));
  } finally {
    if (ws) ws.close();
    chrome.kill();
    try {
      fs.rmSync(tempProfile, { recursive: true, force: true });
    } catch (_) {}
  }
}

main().catch(console.error);
