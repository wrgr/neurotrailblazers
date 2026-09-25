// Run against a built _site; CI supplies Puppeteer through NODE_PATH.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const puppeteer = require(process.env.CHROME_BIN ? 'puppeteer-core' : 'puppeteer');

const root = path.resolve('_site');
const server = http.createServer((req, res) => {
  let pathname = new URL(req.url, 'http://localhost').pathname;
  if (pathname.endsWith('/')) pathname += 'index.html';
  const file = path.resolve(root, '.' + pathname);
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file)) {
    res.writeHead(404).end();
    return;
  }
  const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript' };
  res.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await puppeteer.launch({
      executablePath: process.env.CHROME_BIN || undefined,
      headless: true,
      args: ['--no-sandbox'],
    });
    const base = process.env.RESEARCH_BASE_URL || `http://127.0.0.1:${server.address().port}`;
    for (const width of [1440, 390]) {
      const page = await browser.newPage();
      await page.setViewport({ width, height: 900 });
      // Visibility on arrival must not depend on JavaScript completing.
      await page.setJavaScriptEnabled(false);
      await page.goto(base + '/technical-training/journal-club/', { waitUntil: 'load' });
      const display = () => page.$eval('#jc-prompt-modal', el => getComputedStyle(el).display);
      assert.equal(await display(), 'none', `${width}px: overlay visible before JS`);
      await page.setJavaScriptEnabled(true);
      await page.reload({ waitUntil: 'load' });
      assert.equal(await display(), 'none', `${width}px: overlay visible on arrival`);
      assert.equal(await page.$eval('#jc-empty', el => getComputedStyle(el).display), 'none');
      for (const dismiss of ['button', 'escape', 'backdrop']) {
        await page.click('#jc-prompt-btn');
        assert.equal(await display(), 'flex', `${width}px: prompt did not open`);
        assert.ok(await page.$eval('#jc-prompt-textarea', el => el.value.length > 100));
        await page.click('#jc-prompt-modal-title');
        assert.equal(await display(), 'flex', 'Content clicks must not dismiss the modal');
        if (dismiss === 'button') await page.click('#jc-prompt-close');
        if (dismiss === 'escape') await page.keyboard.press('Escape');
        if (dismiss === 'backdrop') await page.mouse.click(2, 2);
        assert.equal(await display(), 'none', `${width}px: ${dismiss} did not dismiss`);
      }
      if (width === 1440) {
        await page.click('.jc-card:not(.hidden) .jc-link-ai-prompt');
        assert.equal(await display(), 'flex', 'Per-paper prompt did not open');
        await page.click('#jc-prompt-close');
      }
      await page.click('nav a.logo');
      await page.waitForFunction(() => location.pathname === '/');
      console.log(`PASS ${width}px: hidden on arrival, explicit opening, all dismissal routes, navigation`);
      await page.close();
    }
  } finally {
    if (browser) await browser.close();
    server.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
