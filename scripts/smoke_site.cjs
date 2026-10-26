const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const puppeteer = require('puppeteer-core');

const site = path.resolve(process.env.SITE_DIR || '_site');
const chrome = process.env.CHROME_PATH || (process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' : '/usr/bin/google-chrome');
const types = {'.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.json':'application/json', '.svg':'image/svg+xml', '.png':'image/png', '.jpg':'image/jpeg', '.woff2':'font/woff2'};

async function main() {
  assert(fs.existsSync(path.join(site, 'index.html')), 'Build the site first or set SITE_DIR.');
  const server = http.createServer((request, response) => {
    let target;
    try { target = path.resolve(site, '.' + decodeURIComponent(new URL(request.url, 'http://localhost').pathname)); }
    catch { response.writeHead(400).end(); return; }
    if (!target.startsWith(site + path.sep) && target !== site) { response.writeHead(403).end(); return; }
    if (fs.existsSync(target) && fs.statSync(target).isDirectory()) target = path.join(target, 'index.html');
    if (!fs.existsSync(target)) { response.writeHead(404).end(); return; }
    response.setHeader('Content-Type', types[path.extname(target)] || 'application/octet-stream');
    fs.createReadStream(target).pipe(response);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await puppeteer.launch({executablePath:chrome, headless:true, args:process.env.CI ? ['--no-sandbox'] : []});
    const page = await browser.newPage();
    const base = `http://127.0.0.1:${server.address().port}`;
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    const visit = async route => {
      const response = await page.goto(base + route, {waitUntil:'domcontentloaded'});
      assert.equal(response.status(), 200, route);
      await page.waitForSelector('main, section[data-marpit-pagination]');
    };
    const visibleCount = selector => page.$$eval(selector, elements => elements.filter(element => element.getClientRects().length && getComputedStyle(element).display !== 'none').length);
    const menuGroup = label => `details.nav-group:has(summary[data-nav-label="${label}"])`;
    const openGroup = async label => {
      const selector = menuGroup(label);
      await page.click(`${selector} > summary`);
      await page.waitForSelector(`${selector}[open] .dropdown`, {visible:true});
      return selector;
    };
    const follow = async selector => {
      await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}), page.click(selector)]);
    };
    await page.setViewport({width:1280,height:900});
    await visit('/');
    assert.equal(await page.$$eval('.nav-item', elements => elements.length), 7);
    assert.equal(await page.$eval('.nav-item > a[href="/technical-training/journal-club/"]', el => el.textContent.trim()), 'Papers');
    assert(await page.$$eval('.home-refresh .card', cards => cards.every(c => getComputedStyle(c).opacity === '1')), 'Homepage task cards are visible');
    await page.focus(`${menuGroup('Learn')} > summary`);
    await page.keyboard.press('Enter');
    await page.waitForSelector(`${menuGroup('Learn')}[open] .dropdown`, {visible:true});
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(() => document.activeElement.getAttribute('href')), '/technical-training/');
    await page.keyboard.press('Escape');
    assert.equal(await page.$eval(menuGroup('Learn'), element => element.open), false);
    assert.equal(await page.evaluate(() => document.activeElement.tagName), 'SUMMARY');
    await openGroup('Learn');
    await follow(`${menuGroup('Learn')} a[href="/technical-training/"]`);
    assert(new URL(page.url()).pathname === '/technical-training/');
    await follow('main a.btn-primary[href="/technical-training/01-why-map-the-brain/"]');
    assert.equal(new URL(page.url()).pathname, '/technical-training/01-why-map-the-brain/');
    await openGroup('Teach');
    await follow(`${menuGroup('Teach')} a[href="/teaching/sequence/"]`);
    await follow('main a[href="/teaching/lectures/connectomics-01-introduction/#teach-a-90-minute-session"]');
    await page.waitForSelector('#teach-a-90-minute-session');
    await follow('main a[href="/teaching/lectures/introduction-activity/"]');
    assert((await page.$eval('main', element => element.textContent)).includes('invented teaching data'));
    await follow('main a[href="/teaching/lectures/introduction-answers/"]');
    await page.waitForSelector('#worked-calculations');
    await visit('/teaching/sequence/');
    await follow('main a[href="/teaching/lectures/synapse-detection/"]');
    await follow('main a[href="/teaching/lectures/synapse-detection-activity/"]');
    assert((await page.$eval('main', element => element.textContent)).includes('invented counts'));
    await follow('main a[href="/teaching/lectures/synapse-detection-answers/"]');
    await page.waitForSelector('[id="1-metrics"]');
    await visit('/teaching/sequence/');
    await follow('main a[href="/teaching/lectures/connectomics-02-tools-and-methods/#teach-a-90-minute-session"]');
    await page.waitForSelector('#teach-a-90-minute-session');
    await follow('main a[href="/teaching/lectures/tools-and-methods-activity/"]');
    const queryResponse = await page.evaluate(async () => {
      const response = await fetch('/assets/worksheets/lectures/tools-and-methods-query.py');
      return {status:response.status, text:await response.text()};
    });
    assert.equal(queryResponse.status, 200);
    assert(queryResponse.text.includes('synthetic-teaching-only'));
    await follow('main a[href="/teaching/lectures/tools-and-methods-answers/"]');
    await page.waitForSelector('[id="1-query-results"]');
    await visit('/teaching/sequence/');
    await follow('main a[href="/teaching/lectures/connectomics-03-algorithms-and-applications/#teach-a-90-minute-session"]');
    await page.waitForSelector('#teach-a-90-minute-session');
    await follow('main a[href="/teaching/lectures/algorithms-and-applications-activity/"]');
    const graphResponse = await page.evaluate(async () => {
      const response = await fetch('/assets/worksheets/lectures/algorithms-and-applications-query.py');
      return {status:response.status, text:await response.text()};
    });
    assert.equal(graphResponse.status, 200);
    assert(graphResponse.text.includes('synthetic-four-neuron-graph-v1'));
    await follow('main a[href="/teaching/lectures/algorithms-and-applications-answers/"]');
    await page.waitForSelector('[id="1-graph-construction"]');
    await openGroup('Teach');
    await follow(`${menuGroup('Teach')} a[href="/technical-training/slides/"]`);
    await follow('main a[href="/course/decks/marp/out/lectures/synapse-detection.html"]');
    await page.waitForSelector('section');
    assert(await page.$$eval('section', elements => elements.length > 1));
    await visit('/teaching/sessions/');
    assert(await page.$('main a[href="/teaching/sessions/module01/"]'));
    await follow('main a[href="/teaching/sessions/module01/"]');
    const deck = await page.$('main a[href*="/out/modules/module01.html"]');
    assert(deck, 'Session kit links to its presentation deck');

    await visit('/technical-training/dictionary/');
    const terms = await visibleCount('.dict-entry');
    assert(terms > 100);
    await page.type('#dict-search', 'synapse');
    assert((await visibleCount('.dict-entry')) > 0 && (await visibleCount('.dict-entry')) < terms);
    await page.click('#dict-search', {clickCount:3});
    await page.type('#dict-search', 'zzzz-no-such-term');
    assert.equal(await visibleCount('.dict-entry'), 0);
    await page.click('#dict-search', {clickCount:3});
    await page.keyboard.press('Backspace');
    await page.click('.dict-cat:not([data-cat="all"])');
    assert(await page.$eval('.dict-cat:not([data-cat="all"])', element => element.classList.contains('is-active')));
    assert((await visibleCount('.dict-entry')) > 0 && (await visibleCount('.dict-entry')) < terms);
    await page.click('.dict-cat[data-cat="all"]');
    assert.equal(await visibleCount('.dict-entry'), terms);

    await visit('/modules/');
    const modules = await visibleCount('.module-card');
    assert.equal(modules, 25);
    await page.select('#stage-select', 'Foundations');
    assert((await visibleCount('.module-card')) > 0 && (await visibleCount('.module-card')) < modules);
    await page.select('#stage-select', '');
    assert.equal(await visibleCount('.module-card'), modules);

    await page.type('#module-search', 'Python');
    await page.waitForFunction(() => document.getElementById('module-count').textContent.startsWith('1 of'));
    assert.equal(await visibleCount('.module-card'), 1);
    await page.select('#module-status-filter', 'in_development');
    await page.click('#module-search', {clickCount:3});
    await page.keyboard.press('Backspace');
    await page.waitForFunction(() => document.getElementById('module-count').textContent.startsWith('8 of'));
    assert.equal(await visibleCount('.module-card'), 8);
    await visit('/modules/module03/');
    assert((await page.$eval('.module-status-notice', e => e.textContent)).includes('Materials available; practice in development'));
    assert((await page.$eval('.module-status-notice', e => e.textContent)).includes('lesson, guided activity, and teaching materials are available'));
    assert.equal(await page.$$eval('.nt-progress-step', checks => checks.length), 3);
    assert.equal(await page.$('.nt-task-submit'), null);
    await page.click('.nt-progress-step[data-step-index="0"]');
    assert.equal(await page.$eval('.nt-progress-text', e => e.textContent), '33% of self-reported activities checked');
    await page.reload({waitUntil:'domcontentloaded'});
    assert.equal(await page.$eval('.nt-progress-text', e => e.textContent), '33% of self-reported activities checked');
    await page.click('.nt-progress-reset');
    assert.equal(await page.$eval('.nt-progress-text', e => e.textContent), '0% of self-reported activities checked');
    await visit('/modules/module10/');
    await page.click('input[name="task-choice"][value="2"]');
    await page.click('.nt-task-submit');
    assert(await page.$eval('.nt-progress-step[data-step-index="4"]', e => e.checked), 'Practice completion updates the correct progress step');

    await visit('/resources/');
    await page.waitForSelector('#site-search:not([disabled])');
    await page.type('#site-search', 'synapse');
    await page.waitForSelector('#site-search-results a');
    assert((await page.$eval('#site-search-status', e => e.textContent)).includes('matching pages'));
    await page.click('#site-search', {clickCount:3});
    await page.type('#site-search', 'zzzz-no-such-resource');
    await page.waitForFunction(() => document.getElementById('site-search-status').textContent.startsWith('No pages match'));
    assert.equal(await page.$$('#site-search-results a').then(a => a.length), 0);

    await visit('/start-here/');
    assert.equal(await page.$eval('#background-options', e => e.open), false, 'Optional background guidance is collapsed');
    assert(await page.$eval('#pf-tab-maya', e => e.closest('#background-options') !== null));
    await page.click('#background-options > summary');
    assert.equal(await page.$eval('#pf-tab-maya', element => element.closest('a')), null);
    await page.click('#pf-tab-maya');
    assert.equal(await page.$eval('#pf-tab-maya', element => element.getAttribute('aria-selected')), 'true');
    await page.waitForSelector('#pf-panel-maya', {visible:true});
    await page.focus('#pf-tab-maya');
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.$eval('#pf-tab-amir', element => element.getAttribute('aria-selected')), 'true');

    await visit('/technical-training/journal-club/');
    assert.equal(await page.$eval('#jc-empty', element => element.closest('.jc-card')), null, 'Paper metadata must not swallow page structure');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.includes('2000 of 2000'));
    for (const id of ['jc-search', 'jc-dimension', 'jc-organism', 'jc-tier', 'jc-era', 'jc-sort', 'jc-graph-view']) {
      await page.waitForSelector('#' + id, {visible:true});
    }
    assert.equal(await page.$eval('.paper-view-links [aria-current]', el => el.textContent), 'Paper list');
    assert.equal(await page.$$eval('#jc-grid > .jc-card', elements => elements.length), 20);
    assert.equal(await page.$eval('#jc-prompt-modal', element => getComputedStyle(element).display), 'none');
    const firstTitle=await page.$eval('#jc-grid h3', e=>e.textContent);
    await page.click('#jc-next');
    assert.notEqual(await page.$eval('#jc-grid h3', e=>e.textContent), firstTitle);
    assert.equal(await visibleCount('.jc-card'),20);
    await page.select('#jc-tier', '500');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('500 of'));
    await page.type('#jc-search', '10.1109/tmi.2024.3400276');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('1 of'));
    assert((await page.$eval('#jc-grid', e=>e.textContent)).includes('WASPSYN'));
    await page.click('[data-details]');
    assert(await page.$eval('#jc-prompt-modal', e => e.classList.contains('hidden')), 'Paper details must not hit overlapping filter controls');
    await page.waitForFunction(() => !document.querySelector('[data-details]'));
    assert(await page.$('#jc-grid .jc-card-details[open]'));
    await page.click('#jc-search', {clickCount:3});
    await page.type('#jc-search', 'zzzz-no-such-paper');
    await page.waitForSelector('#jc-empty', {visible:true});
    assert.equal(await visibleCount('.jc-card'),0);
    await page.click('#jc-reset');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('2000 of'));
    await page.click('#jc-prompt-btn');
    await page.waitForSelector('#jc-prompt-modal', {visible:true});
    assert((await page.$eval('#jc-prompt-textarea', element => element.value)).includes('First 35 of 2000'));
    await page.keyboard.press('Escape');
    await page.waitForSelector('#jc-prompt-modal', {hidden:true});
    await openGroup('Resources');
    await follow(`${menuGroup('Resources')} a[href="/datasets/"]`);

    await page.setViewport({width:390,height:844,isMobile:true,hasTouch:true});
    await visit('/');
    await page.waitForSelector('.nav-toggle', {visible:true});
    assert.equal(await page.$eval('.nav-toggle', element => element.getAttribute('aria-expanded')), 'false');
    await page.tap('.nav-toggle');
    assert.equal(await page.$eval('.nav-toggle', element => element.getAttribute('aria-expanded')), 'true');
    await openGroup('Teach');
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'No horizontal mobile overflow');
    await follow(`${menuGroup('Teach')} a[href="/technical-training/slides/"]`);
    await page.tap('.nav-toggle');
    await openGroup('Learn');
    await openGroup('Resources');
    assert.equal(await page.$eval(menuGroup('Learn'), element => element.open), false);
    await page.click('main h1');
    assert.equal(await page.$eval('.nav-toggle', element => element.getAttribute('aria-expanded')), 'false');
    await page.setJavaScriptEnabled(false);
    await visit('/');
    await page.click(`${menuGroup('Learn')} > summary`);
    await page.waitForSelector(`${menuGroup('Learn')} .dropdown`, {visible:true});
    assert.equal(errors.length, 0, errors.join('\n'));
    console.log('PASS: desktop/keyboard/mobile navigation, no-JS fallback, course and teaching journeys, deck links, persona tabs, dictionary search/categories, module filtering, journal filtering and modal.');
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}
main().catch(error => { console.error(error); process.exitCode = 1; });
