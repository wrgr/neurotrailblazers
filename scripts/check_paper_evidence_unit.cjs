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
const publicationLinks = JSON.parse(fs.readFileSync('_data/paper_publication_links.json','utf8'));
const correctionDoi = '10.1016/j.neuron.2023.04.003';
const pair = publicationLinks[correctionDoi];
check(() => { const html=api.renderPublicationLinks(pair,correctionDoi); assert.match(html,/Original paper/); assert.match(html,/Correction notice/); assert(html.includes(pair.original.url)); assert(html.includes(pair.correction.pdf_url)); });
check(() => assert.equal(api.renderPublicationLinks(pair,'10.9999/unrelated-sem'),''));
check(() => assert.equal(api.publicationRelationship({...pair,kind:'original'},correctionDoi),null));
check(() => assert.equal(api.publicationRelationship({...pair,relationship_source_url:'javascript:alert(1)'},correctionDoi),null));
check(() => { const html=api.renderPublicationLinks({...pair,original:{...pair.original,title:'<script>alert(1)</script>'}},correctionDoi); assert(!html.includes('<script>')); assert(html.includes('&lt;script&gt;')); });
for (const url of ['javascript:alert(1)','//example.com/a.pdf','/assets/papers/../secret.pdf','https://user:password@example.com/a.pdf']) check(() => assert.equal(api.publicationPdfUrl(url),''));
check(() => { const prompt=api.reviewPrompt([{doi:correctionDoi,title:pair.correction.title,abstract:'WRONG_MAIN_ABSTRACT',publication_links:pair}], 'synthesis',1); assert(prompt.includes(pair.original.url) && prompt.includes(pair.correction.url)); assert(!prompt.includes('WRONG_MAIN_ABSTRACT')); assert(prompt.includes('Do not attribute')); });
console.log('PASS: '+cases+' evidence eligibility, negative-association, escaped-rendering and prompt tests.');
