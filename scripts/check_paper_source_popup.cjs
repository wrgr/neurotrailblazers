// Exercise the actual Liquid card and JavaScript graph renderer, including native no-JS controls.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const puppeteer = require('puppeteer');
const root = path.resolve('_site');
const doi = '10.1038/s41586-024-07558-y';
const records = JSON.parse(fs.readFileSync('_data/paper_evidence.json', 'utf8'));
const index = JSON.parse(fs.readFileSync(path.join(root, 'technical-training/journal-club/index-data.json')));
const paper = index.find(p => p.doi === doi);
assert(paper && records[doi], 'The example paper must have source-checked evidence');
const card = JSON.parse(fs.readFileSync(path.join(root, `technical-training/journal-club/details/${paper.chunk}.json`)))[paper.id];
const fixture = '<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="/assets/css/usability.css">' + card;
const server = http.createServer((req, res) => {
  let name = new URL(req.url, 'http://localhost').pathname;
  if (name === '/__source-popup-fixture/') return res.setHeader('Content-Type', 'text/html; charset=utf-8').end(fixture);
  if (name.endsWith('/')) name += 'index.html';
  const file = path.resolve(root, '.' + name);
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file)) return res.writeHead(404).end();
  res.setHeader('Content-Type', ({'.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.json':'application/json'})[path.extname(file)] || 'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
async function exercise(page, container, width) {
  const trigger = container + ' .paper-source-trigger';
  await page.waitForSelector(trigger, {visible:true});
  assert.equal(await page.$('.paper-source-popover:popover-open'), null);
  assert(!(await page.$eval(container, el => el.innerText)).includes(records[doi].evidence_basis), 'Long source metadata must be hidden until requested');
  await page.focus(trigger); await page.keyboard.press('Enter');
  await page.waitForSelector('.paper-source-popover:popover-open', {visible:true});
  const actual = await page.$eval('.paper-source-popover:popover-open', el => ({text:el.innerText, href:el.querySelector('a').href, role:el.getAttribute('role'), title:document.getElementById(el.getAttribute('aria-labelledby'))?.textContent, bounds:{left:el.getBoundingClientRect().left,right:el.getBoundingClientRect().right,top:el.getBoundingClientRect().top,bottom:el.getBoundingClientRect().bottom}, overflow:el.scrollWidth>el.clientWidth+1}));
  for (const field of ['evidence_basis','source_locator','checked_by','checked_on']) assert(actual.text.includes(records[doi][field]), field);
  assert.equal(actual.href, records[doi].source_url); assert.equal(actual.role,'dialog'); assert.equal(actual.title,'Source and review details');
  assert(actual.bounds.left>=0 && actual.bounds.right<=width+1 && actual.bounds.top>=0 && actual.bounds.bottom<=1000 && !actual.overflow, 'Popup fits the viewport');
  assert(await page.$eval('.paper-source-close', el => document.activeElement === el), 'Close receives focus');
  await page.keyboard.press('Escape');
  assert.equal(await page.$('.paper-source-popover:popover-open'), null);
  assert(await page.$eval(trigger, el => document.activeElement === el), 'Escape restores focus to the trigger');
  if (container === '#jcg-panel') assert(!(await page.$eval(container, el => el.classList.contains('hidden'))), 'Escape must leave the paper drawer open');
  await page.click(trigger); await page.click('.paper-source-popover:popover-open .paper-source-close');
  assert.equal(await page.$('.paper-source-popover:popover-open'), null);
  await page.click(trigger); await page.mouse.click(2,2);
  assert.equal(await page.$('.paper-source-popover:popover-open'), null);
  if (process.env.SOURCE_POPUP_SCREENSHOTS) {
    await page.click(trigger);
    await page.screenshot({path:path.join(process.env.SOURCE_POPUP_SCREENSHOTS, `source-${container === '#jcg-panel' ? 'graph' : 'card'}-${width}.png`)});
    await page.keyboard.press('Escape');
  }
}
(async () => {
  await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
  let browser;
  try {
    browser = await puppeteer.launch({executablePath:process.env.CHROME_BIN || undefined,headless:true,args:['--no-sandbox']});
    const local = `http://127.0.0.1:${server.address().port}`;
    const base = process.env.SITE_BASE_URL || local;
    for (const width of [320,390,1440]) {
      const page = await browser.newPage(); await page.setViewport({width,height:1000});
      const errors=[]; page.on('pageerror',error => errors.push(error.message));
      await page.goto(base+'/technical-training/journal-club/?paper='+encodeURIComponent(paper.id),{waitUntil:'load'});
      await exercise(page,'#jc-grid',width);
      await page.goto(base+'/technical-training/journal-club/graph/?paper='+encodeURIComponent(paper.id),{waitUntil:'load'});
      await exercise(page,'#jcg-panel',width);
      assert.deepEqual(errors,[]);
      await page.close(); console.log(`PASS ${width}px: card/map source popups, preserved provenance, keyboard focus, Escape, close, outside dismissal and viewport bounds`);
    }
    const page=await browser.newPage(); await page.setJavaScriptEnabled(false); await page.setViewport({width:390,height:1000});
    await page.goto(local+'/__source-popup-fixture/'); await exercise(page,'article.jc-card',390); await page.close();
    console.log('PASS native source popup works with JavaScript disabled');
  } finally { if(browser) await browser.close(); server.close(); }
})().catch(error => { console.error(error); process.exitCode=1; });
