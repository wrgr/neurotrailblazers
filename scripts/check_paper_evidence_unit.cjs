// Unit tests for eligibility and public rendering. No claim of scientific review.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const api = require('../assets/js/paper-evidence.js');
const records = JSON.parse(fs.readFileSync('_data/paper_evidence.json','utf8'));
const [doi,e] = Object.entries(records)[0];
let cases = 0;
function check(test) { test(); cases++; }
check(() => assert(api.eligible(e,doi)));
check(() => assert(api.eligible(e,' '+doi.toUpperCase()+' ')));
const bad = [null, {}, {...e,doi:'10.9999/unrelated-sem'}, {...e,status:'generated'}, {...e,status:'expert_curated'}, {...e,source_url:'javascript:alert(1)'}, {...e,source_url:'https://'}, {...e,source_url:'https://user:pass@example.org'}, {classification:'imaging',method:'SEM',dataset:'MICrONS'}];
for (const field of ['contribution','result','context','limitation','source_url','source_locator','evidence_basis','checked_by','checked_on']) {
  for (const value of ['', '   ', null, 12]) bad.push({...e,[field]:value});
}
for (const record of bad) check(() => { assert(!api.eligible(record,doi)); assert(!api.render(record,doi).includes('What this paper demonstrated')); });
check(() => assert(!api.render(e,'10.9999/unrelated-sem').includes(e.result)));
check(() => {const html=api.render({...e,result:'<script>alert(1)</script>'},doi); assert(!html.includes('<script>')); assert(html.includes('&lt;script&gt;'));});
for (const mode of ['synthesis','methods','problems','seminar']) check(() => {
 const prompt = api.reviewPrompt([{doi:'10.9999/unrelated-sem',title:'SEM example',summary:'FORBIDDEN_SUMMARY',ocar:{resolution:'FORBIDDEN_RESULT'},evidence:e}],mode,1);
 assert(!prompt.includes('FORBIDDEN') && !prompt.includes(e.result));
 assert(prompt.includes('SEM does not establish use of MICrONS'));
 assert(prompt.includes('not a representative sample'));
 assert(!prompt.includes('\\n'), 'Use real line breaks, not backslash-n characters');
});
check(() => {const prompt=api.reviewPrompt([{doi,title:'Example',evidence:e}], 'methods', 1); for(const field of ['result','context','limitation','source_url']) assert(prompt.includes(e[field]));});
check(() => assert.match(api.reviewPrompt([], 'synthesis',0),/No publications selected/));
check(() => assert.match(api.reviewPrompt(Array.from({length:50},()=>({doi,title:'Example'})),'synthesis',50),/First 35 of 50/));
check(() => {const html=api.render(e,doi); assert(html.includes('popover="auto"')); assert(html.includes('Source &amp; review details')); assert(!html.includes('Source-checked against')); for(const field of ['source_locator','evidence_basis','checked_by','checked_on']) assert(html.includes(e[field]));});
check(() => {const html=api.render({...e,evidence_basis:'<img onerror=alert(1)>',source_locator:'<script>unsafe</script>',checked_by:'<b>unsafe</b>'},doi); assert(!/<(?:img|script|b)>/.test(html)); assert(html.includes('&lt;script&gt;'));});
console.log('PASS: '+cases+' evidence eligibility, negative-association, escaped-rendering and prompt tests.');
