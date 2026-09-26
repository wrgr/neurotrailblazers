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

// Check the primary navigation plus representative pages using shared layouts.
const routes = [
  '/', '/start-here/', '/neuronauts/', '/neuronauts/kids/', '/core/',
  '/core/connects-ecosystem/', '/content-library/', '/technical-training/dictionary/',
  '/content-library/journal-papers/', '/technical-training/atlas-connectomics-reference/',
  '/hidden-curriculum/', '/datasets/', '/initiatives/', '/initiatives/outreach/',
  '/tracks/', '/modes/', '/tracks/core-concepts-methods/', '/tracks/research-in-action/',
  '/tracks/career-and-community/', '/technical-training/',
  '/technical-training/proofreading-tutorials/', '/concepts/', '/side-quests/',
  '/open-problems/', '/modules/', '/teaching/', '/teaching/lectures/',
  '/teaching/sessions/', '/teaching/pathways/', '/teaching/pathways/orientation-answers/',
  '/teaching/syllabi/', '/teaching/syllabi/10-week/', '/teaching/syllabi/16-week/',
  '/teaching/lectures/ethics-and-governance-answers/',
  '/teaching/answers/module18/', '/teaching/assessment/', '/notebooks/microns-lab/',
  '/tools/', '/ask-an-expert/', '/tools/connectome-quality/',
  '/about/', '/avatars/', '/avatars/undergradstudent/', '/models/', '/license/',
];

async function checkPage(browser, base, route, width, largeText = false) {
  const page = await browser.newPage();
  try {
    await page.setViewport({ width, height: 1000 });
    const response = await page.goto(base + route, { waitUntil: 'load' });
    assert.equal(response.status(), 200, route);
    await page.evaluate(() => document.fonts.ready);
    if (largeText) await page.addStyleTag({ content: 'html { font-size: 200%; }' });
    const findings = await page.evaluate(() => {
      const errors = [];
      const main = document.querySelector('main');
      if (document.documentElement.scrollWidth > innerWidth + 2) errors.push('Page overflows horizontally');
      if (main.querySelector('a section, strong section')) errors.push('Unclosed inline markup contains a section');
      if (/<\/?(?:section|div|article)\b|\*\*\[[^\]]+\]\(/.test(main.innerText)) errors.push('Raw HTML or Markdown appears in the copy');
      const overlaps = (a, b) => {
        const x = a.getBoundingClientRect(), y = b.getBoundingClientRect();
        return Math.min(x.right, y.right) - Math.max(x.left, y.left) > 1 &&
          Math.min(x.bottom, y.bottom) - Math.max(x.top, y.top) > 1;
      };
      for (const head of document.querySelectorAll('.nn-act-head')) {
        if (overlaps(head.querySelector('h2'), head.querySelector('.nn-leg-badge'))) errors.push('Story heading overlaps its badge');
      }
      for (const item of document.querySelectorAll('.nn-tl-item')) {
        if (overlaps(item.querySelector('.nn-tl-body'), item.querySelector('.nn-tl-art'))) errors.push('Timeline text overlaps artwork');
      }
      for (const panel of document.querySelectorAll('.nn-panel')) {
        const caption = panel.querySelector('.nn-panel-caption');
        if (!caption || parseFloat(getComputedStyle(caption).fontSize) < 16) errors.push('Illustration caption is missing or too small');
        else if (overlaps(caption, panel.querySelector('svg'))) errors.push('Caption overlaps illustration');
      }
      return errors;
    });
    assert.deepEqual(findings, [], `${route} at ${width}px${largeText ? ' with enlarged text' : ''}`);
  } finally {
    await page.close();
  }
}

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await puppeteer.launch({
      executablePath: process.env.CHROME_BIN || undefined,
      headless: true,
      args: ['--no-sandbox'],
    });
    const base = process.env.SITE_BASE_URL || `http://127.0.0.1:${server.address().port}`;
    for (const width of [320, 390, 768, 1440]) {
      for (const route of routes) await checkPage(browser, base, route, width);
      console.log(`PASS ${routes.length} pages at ${width}px: no page overflow, leaked markup, or story text overlap`);
    }
    for (const width of [860, 960, 1280]) await checkPage(browser, base, '/neuronauts/', width);
    await checkPage(browser, base, '/neuronauts/', 768, true);
    console.log('PASS Neuronauts at intermediate widths and with 200% text');
  } finally {
    if (browser) await browser.close();
    server.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
