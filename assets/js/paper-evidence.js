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
  function publicationPdfUrl(value) {
    return safeSourceUrl(value) || (/^\/assets\/papers\/[A-Za-z0-9_-][A-Za-z0-9._-]*\.pdf$/.test(String(value || '')) ? value : '');
  }
  function publicationRelationship(record, doi) {
    const key = String(doi || '').trim().toLowerCase();
    if (!record || record.doi !== key || !['original','correction'].includes(record.kind)) return null;
    if (!safeSourceUrl(record.relationship_source_url)) return null;
    for (const role of ['original','correction']) {
      const p = record[role];
      if (!p || !/^10\.\d{4,9}\/.+/.test(p.doi || '') || !p.title || !safeSourceUrl(p.url)) return null;
    }
    if (record.original.doi === record.correction.doi || record[record.kind].doi !== key) return null;
    return record;
  }
  function renderPublicationLinks(record, doi) {
    const pair = publicationRelationship(record, doi);
    if (!pair) return '';
    return '<section class="jc-publication-links" aria-label="Original paper and correction">' +
      (pair.kind === 'correction' ? '<p><strong>Correction notice.</strong> Read the original paper together with this correction.</p>' : '') +
      '<p>' + esc(pair.correction_note || '') + '</p>' + ['original','correction'].map(role => {
        const p = pair[role], full = safeSourceUrl(p.full_text_url), pdf = publicationPdfUrl(p.pdf_url);
        return '<p><strong>' + (role === 'original' ? 'Original paper' : 'Correction') + ':</strong> ' +
          '<a href="' + esc(p.url) + '" target="_blank" rel="noopener">' + esc(p.title) + '</a>' +
          (full ? ' · <a href="' + esc(full) + '" target="_blank" rel="noopener">Full text</a>' : '') +
          (pdf ? ' · <a href="' + esc(pdf) + '" target="_blank" rel="noopener">PDF</a>' : '') + '</p>';
      }).join('') + '</section>';
  }
  function eligible(record, doi) {
    const key = String(doi || '').trim().toLowerCase();
    if (!/^10\.\d{4,9}\/.+/.test(key) || !record || record.status !== 'source_checked' || record.doi !== key) return false;
    if (!fields.every(k => typeof record[k] === 'string' && record[k].trim())) return false;
    return !!safeSourceUrl(record.source_url);
  }
  function render(record, doi) {
    if (!eligible(record, doi)) return '<p class="jcg-hint">A source-checked contribution note is not available. Read the abstract and publication for this paper\'s findings.</p>';
    return '<section class="jcg-paper-evidence"><h4>What this paper demonstrated</h4><p>' + esc(record.contribution) + '</p>' +
      [['Reported result','result'],['Test context','context'],['Limits','limitation']].map(([label,k]) => '<p><strong>' + label + ':</strong> ' + esc(record[k]) + '</p>').join('') +
      '<p class="jcg-hint">Source-checked against <a href="' + esc(record.source_url) + '" target="_blank" rel="noopener">' + esc(record.evidence_basis) + ': ' + esc(record.source_locator) + '</a>. ' + esc(record.checked_by) + ' (' + esc(record.checked_on) + ').</p></section>';
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
        const pair = publicationRelationship(p.publication_links, p.doi);
        const correction = pair && pair.kind === 'correction';
        if (pair) text += '\nPublication relationship: ' + pair.kind + '. Read both sources. Original paper: ' + pair.original.url + '\nCorrection: ' + pair.correction.url + '\nCorrection notice: ' + pair.correction_note + '\nDo not attribute the original study\'s findings to its correction notice.';
        if (p.abstract && !correction) text += '\nAbstract recorded in corpus (not full text): ' + p.abstract;
        if (!correction && eligible(p.evidence,p.doi)) {
          const e = p.evidence;
          text += '\nSource-checked site note, not independent validation:\nContribution: ' + e.contribution + '\nReported result: ' + e.result + '\nTest context: ' + e.context + '\nLimits: ' + e.limitation + '\nSource: ' + e.source_url + ' (' + e.source_locator + '; ' + e.evidence_basis + '). ' + e.checked_by + ' (' + e.checked_on + ').';
        }
        return text;
      }).join('\n\n');
  }
  return Object.freeze({eligible, render, reviewPrompt, safeSourceUrl, publicationPdfUrl, publicationRelationship, renderPublicationLinks});
});
