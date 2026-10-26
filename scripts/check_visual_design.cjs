/* Run on the built _site. Normal pointer/keyboard interactions, not DOM click bypasses. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const puppeteer = require(process.env.CHROME_BIN ? 'puppeteer-core' : 'puppeteer');
const root = path.resolve('_site');
const evidence = path.resolve('tmp/visual-review');
fs.mkdirSync(evidence, {recursive:true});
const measurements = [];
const server = http.createServer((req,res) => {
  let name = new URL(req.url,'http://localhost').pathname;
  if(name.endsWith('/')) name += 'index.html';
  const file = path.resolve(root,'.'+name);
  if(!file.startsWith(root+path.sep) || !fs.existsSync(file)){ res.writeHead(404).end(); return; }
  res.setHeader('Content-Type',({'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml'})[path.extname(file)]||'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
(async()=> {
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 let browser;
 try {
  browser=await puppeteer.launch({headless:true,executablePath:process.env.CHROME_BIN||undefined,args:['--no-sandbox']});
  const base='http://127.0.0.1:'+server.address().port;
  for(const width of [320,390,768,1440]){
   const page=await browser.newPage(); await page.setViewport({width,height:1000});
   for(const route of ['/','/modules/','/resources/','/teaching/sessions/']){
    await page.goto(base+route); await page.evaluate(()=>document.fonts.ready);
    const result=await page.evaluate(()=>{
     const errors=[], cards=[];
     if(document.documentElement.scrollWidth>innerWidth+2) errors.push('horizontal overflow');
     document.querySelectorAll('.cards-grid > .card, .modules-grid > .card').forEach(card=>{
      if(!card.getClientRects().length)return;
      const c=card.getBoundingClientRect(), grid=card.parentElement;
      // auto-fit retains collapsed, empty 0px tracks in the computed value.
      // Compare actual cards with occupied tracks, not those empty slots.
      const cols=getComputedStyle(grid).gridTemplateColumns.split(' ').map(parseFloat).filter(n=>Number.isFinite(n)&&n>0);
      if(!cols.length || !cols.some(col=>Math.abs(col-c.width)<=3)) errors.push('card fails to fill occupied grid column');
      cards.push({width:c.width,columns:cols});
     }); return {errors,cards,scrollWidth:document.documentElement.scrollWidth};
    });
    assert(result.cards.length>0,`${route} must exercise real cards`);
    measurements.push({route,width,...result});
    fs.writeFileSync(path.join(evidence,'geometry.json'),JSON.stringify(measurements,null,2));
    assert.deepEqual(result.errors,[],`${route} ${width}px`);
    if(width===390 || width===1440) {
     const label=route==='/'?'home':route.replace(/^\/+|\/+$/g,'').replace(/\//g,'-');
     await page.screenshot({path:path.join(evidence,`${label}-${width}.png`)});
     if(route==='/modules/') {
      await page.$eval('.modules-grid',el=>el.scrollIntoView({block:'start',behavior:'instant'}));
      await page.screenshot({path:path.join(evidence,`modules-cards-${width}.png`)});
     }
    }
   }
   for(const num of ['03','04','06','07','09']){
    await page.goto(base+`/course/decks/marp/out/modules/module${num}.reader.html`);
    assert.equal(await page.$$eval('h1',els=>els.length),1);
    await page.addStyleTag({content:':root {font-size:36px !important;}'});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),`reader ${num} ${width}px with 200% text`);
    assert.equal(await page.$$eval('foreignObject',els=>els.length),0);
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(()=>document.activeElement.textContent),'Skip to slides');
    await page.keyboard.press('Enter');
    assert.equal(await page.evaluate(()=>document.activeElement.id),'reading-content');
    if(num==='06'){
     const link=await page.$('.visual-images img'); assert(link);
     const note=await page.$('.visual-images ~ .teaching-notes summary');
     assert(note, 'Figure description must be available');
     await note.click(); assert(await page.$eval('.visual-images ~ .teaching-notes',e=>e.open));
    }
   }
   await page.close(); console.log(`PASS visual layout and reflow at ${width}px; 200% reader text; card widths; keyboard entry`);
  }
  // Check visible bounds of each NEW visual slide, not only its page container.
  const page=await browser.newPage(); await page.setViewport({width:1280,height:720});
  for(let n=2;n<=9;n++){
   const num=String(n).padStart(2,'0');
   await page.goto(base+`/course/decks/marp/out/modules/module${num}.html`); await page.evaluate(()=>document.fonts.ready);
   const ids=await page.$$eval('section.visual-lesson',els=>els.map(e=>e.id)); assert.equal(ids.length,2);
   for(const id of ids){
    await page.goto(base+`/course/decks/marp/out/modules/module${num}.html#${id}`); await page.evaluate(()=>document.fonts.ready);
    const errors=await page.$eval('section[id="'+id+'"]',section=>{
     const r=section.getBoundingClientRect(); const errors=[];
     for(const el of section.querySelectorAll('img,h2,.visual-question,.source,.visual-steps,.visual-code,.visual-tree,table')){
      const b=el.getBoundingClientRect(); if(b.bottom>r.bottom+2 || b.right>r.right+2 || b.left<r.left-2)errors.push(el.className||el.tagName);
     }
     const q=section.querySelector('.visual-question').getBoundingClientRect(); const s=section.querySelector('.source').getBoundingClientRect();
     if(q.bottom>s.top-2) errors.push('question/source overlap');
     return errors;
    }); assert.deepEqual(errors,[],`Module ${num}, visual slide ${id}`);
    await page.screenshot({path:path.join(evidence,`module${num}-slide${id}.png`)});
   }
  }
  await page.close(); console.log('PASS bounds for all 16 new visual slides; screenshots saved under tmp/visual-review');
 } finally {if(browser)await browser.close();server.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
