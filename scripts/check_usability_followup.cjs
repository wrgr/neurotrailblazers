const assert=require('node:assert/strict'), fs=require('node:fs'), path=require('node:path'), http=require('node:http');
const puppeteer=require('puppeteer');
const site=path.resolve('_site');
const html=fs.readFileSync(path.join(site,'technical-training/journal-club/index.html'),'utf8');
assert(Buffer.byteLength(html)<500000,'Paper entry HTML must stay below 500 KB');
assert.equal((html.match(/class="jc-card"/g)||[]).length,20,'Server renders 20 cards, not 2000');
const index=JSON.parse(fs.readFileSync(path.join(site,'technical-training/journal-club/index-data.json')));
assert.equal(index.length,2000); assert.equal(new Set(index.map(p=>p.id)).size,2000);
const detailIds=new Set();
for(let n=0;n<20;n++){const chunk=JSON.parse(fs.readFileSync(path.join(site,'technical-training/journal-club/details/'+n+'.json'))); assert.equal(Object.keys(chunk).length,100); Object.keys(chunk).forEach(id=>detailIds.add(id));}
assert(index.every(p=>detailIds.has(p.id))); assert(index.every(p=>!('abstract' in p) && !('ocar' in p)));
const server=http.createServer((req,res)=>{let name=new URL(req.url,'http://localhost').pathname;if(name.endsWith('/'))name+='index.html';const file=path.resolve(site,'.'+name);if(!file.startsWith(site+path.sep)||!fs.existsSync(file)){res.writeHead(404).end();return;}const ext=path.extname(file);res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'})[ext]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;try{
 browser=await puppeteer.launch({headless:true,args:['--no-sandbox']}); const base='http://127.0.0.1:'+server.address().port;
 for(const width of [390,1440]){
 const page=await browser.newPage();await page.setViewport({width,height:900});const errors=[];page.on('pageerror',e=>errors.push(e.message));let detailRequests=0;page.on('request',req=>{if(req.url().includes('/journal-club/details/'))detailRequests++;});
 page.on('response',res=>{if(res.url().includes('/journal-club/details/'))console.log('DETAIL RESPONSE',width,res.status(),res.url());});
 await page.goto(base+'/technical-training/journal-club/');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('2000 of'));
 assert.equal(detailRequests,0,'Details should not be fetched on arrival');assert.equal(await page.$$eval('#jc-grid .jc-card',e=>e.length),20);
 await page.type('#jc-search','10.1109/tmi.2024.3400276');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('1 of'));
 await page.click('#jc-graph-view');await page.waitForSelector('.jcg-result-btn');assert.equal(await page.$eval('#jcg-search',e=>e.value),'10.1109/tmi.2024.3400276');
 await page.focus('.jcg-result-btn');await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>document.activeElement.id),'jcg-panel-close');await page.keyboard.press('Escape');assert(await page.$eval('#jcg-panel',e=>e.classList.contains('hidden')));assert(await page.evaluate(()=>document.activeElement.classList.contains('jcg-result-btn')));
 await page.click('#jcg-list-view');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('1 of'));

 await page.evaluate(()=>{window.lastClick='none';document.addEventListener('click',e=>window.lastClick=e.target.outerHTML.slice(0,300),true);});
 await page.click('[data-details]');
 try{await page.waitForSelector('#jc-grid .jc-card-details',{timeout:10000});}catch(error){
 console.log('DETAIL FAILURE',JSON.stringify(await page.evaluate(()=>({button:document.querySelector('[data-details]')?.outerHTML,click:window.lastClick,url:location.href,grid:document.querySelector('#jc-grid')?.innerText,active:document.activeElement?.outerHTML}))), 'requests',detailRequests,'errors',errors);throw error;
 }
 assert.equal(detailRequests,1);assert(await page.$eval('#jc-grid .jc-card-details',e=>e.open));

 await page.goto(base+'/technical-training/journal-club/#paper-author-1990--pnas-0409009101');await page.waitForFunction(()=>document.querySelector('#paper-author-1990--pnas-0409009101 .jc-card-details'));
 await page.goto(base+'/teaching/');assert.equal(await page.$$eval('main a[href^="/modules/module"]',e=>e.length),0,'Teaching hub routes rather than duplicating the catalog');
 await page.goto(base+'/teaching/sessions/');await page.type('#session-search','Python');await page.waitForFunction(()=>document.getElementById('session-count').textContent.startsWith('1 of'));
 await page.goto(base+'/modules/module01/');await page.$$eval('.nt-progress-step:not([disabled])',checks=>checks.forEach(el=>el.click()));assert((await page.$eval('.nt-progress-text',e=>e.textContent)).includes('self-reported'));assert((await page.$eval('.nt-assessment-status',e=>e.textContent)).includes('not yet passed'));assert(await page.$eval('[data-assessment="quiz"]',e=>e.disabled&&!e.checked));
 await page.goto(base+'/start-here/first-activity/');await page.type('#first-observation','The table records four A-to-B synapses.');await page.reload();assert((await page.$eval('#first-observation',e=>e.value)).includes('four'));await page.click('#first-clear');assert.equal(await page.$eval('#first-observation',e=>e.value),'');
 assert.deepEqual(errors,[],width+'px runtime errors');await page.close();console.log('PASS '+width+'px: lazy details, list/map state, drawer keyboard, session search, progress semantics, draft persistence');
 }
 console.log('Paper HTML bytes: '+Buffer.byteLength(html)+'; index bytes: '+fs.statSync(path.join(site,'technical-training/journal-club/index-data.json')).size);
}finally{if(browser)await browser.close();server.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
