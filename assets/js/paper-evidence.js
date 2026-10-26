/* Evidence is an editorial record, not an inference from tags or text matches. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.NTPaperEvidence = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const fields = ['contribution','result','context','limitation','source_url','source_locator','evidence_basis','checked_by','checked_on'];
  const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function safeSourceUrl(value) {
    try { const url = new URL(value); return url.protocol === 'https:' && !!url.hostname && !url.username && !url.password ? url.href : ''; }
    catch (_) { return ''; }
  }
  function eligible(record, doi) {
    const key = String(doi || '').trim().toLowerCase();
    if (!/^10\.\d{4,9}\/.+/.test(key) || !record || record.status !== 'source_checked' || record.doi !== key) return false;
    if (!fields.every(k => typeof record[k] === 'string' && record[k].trim())) return false;
    return !!safeSourceUrl(record.source_url);
  }
  function sourceDetails(record, doi) {
    const id = 'graph-paper-source-' + encodeURIComponent(doi);
    return '<button type="button" class="paper-source-trigger" popovertarget="' + id + '" aria-haspopup="dialog">Source &amp; review details</button>' +
      '<div class="paper-source-popover" id="' + id + '" popover="auto" role="dialog" aria-labelledby="' + id + '-title">' +
      '<div class="paper-source-heading"><h4 id="' + id + '-title">Source and review details</h4>' +
      '<button type="button" class="paper-source-close" popovertarget="' + id + '" popovertargetaction="hide" aria-label="Close source and review details" autofocus>&times;</button></div>' +
      '<a class="paper-source-link" href="' + esc(record.source_url) + '" target="_blank" rel="noopener">Open original source &nearr;</a><dl>' +
      [['Review scope','evidence_basis'],['Locations checked','source_locator'],['Checked by','checked_by'],['Checked on','checked_on']].map(([label,k]) => '<dt>' + label + '</dt><dd>' + esc(record[k]) + '</dd>').join('') + '</dl></div>';
  }
  function render(record, doi) {
    if (!eligible(record, doi)) return '<p class="jcg-hint">A source-checked contribution note is not available. Read the abstract and publication for this paper\'s findings.</p>';
    return '<section class="jcg-paper-evidence"><h4>What this paper demonstrated</h4><p>' + esc(record.contribution) + '</p>' +
      [['Reported result','result'],['Test context','context'],['Limits','limitation']].map(([label,k]) => '<p><strong>' + label + ':</strong> ' + esc(record[k]) + '</p>').join('') +
      sourceDetails(record, doi) + '</section>';
  }
  function reviewPrompt(papers, mode, total) {
    const selection = Array.isArray(papers) ? papers.slice(0,35) : [];
    if (!selection.length) return 'No publications selected. Select a paper before preparing a review.';
    const instructions = {synthesis:'Compare the questions, reported findings and limitations.',methods:'Compare only methods actually reported and their validation.',problems:'Identify evidence-supported gaps; label proposed research ideas as hypotheses.',seminar:'Prepare discussion questions that ask readers to identify claims, evidence and limitations.'};
    return 'Review the listed publications using original text where accessible. ' + (instructions[mode] || instructions.synthesis) + '\n' +
      'State which sources you actually accessed. Bibliographic metadata, abstracts and site notes are not independently validated findings. Do not infer datasets, software, protocols, affiliations, benchmarks or outcomes from titles, topic tags, organisms or citation links. In particular, SEM does not establish use of MICrONS. A citation does not establish agreement, dataset use or a demonstrated improvement. For missing details write "not reported in the provided material". Distinguish reported results, interpretation, and untested hypotheses; include source locations. Preserve each result\'s test context and limitations. Do not invent numerical improvements.\n\n' +
      'First ' + selection.length + ' of ' + Math.max(selection.length, Number(total) || selection.length) + ' matching publications in the current order; not a representative sample or an editorial ranking.\n\n' +
      selection.map((p,i) => {
        let text = (i+1) + '. ' + (p.title || 'Title not recorded') + '\n' + (p.authors || 'Authors not recorded') + ' (' + (p.year || 'Year not recorded') + '). ' + (p.journal || '') + '\n' + (p.doi ? 'Publication: https://doi.org/' + p.doi : 'DOI not recorded');
        if (p.abstract) text += '\nAbstract recorded in corpus (not full text): ' + p.abstract;
        if (eligible(p.evidence,p.doi)) {
          const e = p.evidence;
          text += '\nSource-checked site note, not independent validation:\nContribution: ' + e.contribution + '\nReported result: ' + e.result + '\nTest context: ' + e.context + '\nLimits: ' + e.limitation + '\nSource: ' + e.source_url + ' (' + e.source_locator + '; ' + e.evidence_basis + '). ' + e.checked_by + ' (' + e.checked_on + ').';
        }
        return text;
      }).join('\n\n');
  }
  return Object.freeze({eligible, render, reviewPrompt, safeSourceUrl});
});
