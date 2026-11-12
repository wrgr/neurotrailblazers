export const licenseURL = 'https://creativecommons.org/licenses/by/4.0/';
export const independence = 'Independent product. No affiliation with or endorsement by NIH, BICAN or BRAIN CONNECTS.';
export const words = text => text.trim().split(/\s+/u).filter(Boolean).length;
export const seconds = text => Math.round(words(text) * 60 / 130);
export const sentence = text => /[.!?]$/u.test(text.trim()) ? text.trim() : text.trim() + '.';
export const questions = [
  ['problem','What problem are you working on?','Explain why the question matters in everyday language.',34],
  ['question','What did you want to find out?','Ask one question. Name the species, sample or setting where it matters.',18],
  ['contribution','What did your team contribute?','Name the tool, method, dataset or insight you added. Put each contribution on its own line.',32],
  ['finding','What did you observe?','State the main finding and what changed. For work without results, say results are pending.',34],
  ['basis','What evidence supports that statement?','Name the comparison, measurement, sample or study milestone. Keep numbers in context.',27],
  ['limit','Where does the evidence stop?','Name an uncertainty, limitation or boundary on what can be generalized.',24],
  ['relevance','What could this help us understand or do?','Describe a possible use or next step. Keep any untested hypothesis conditional.',26]
];
export const sections = [
  ['headline','Hook',10,88], ['problem','Why it matters',30,230],
  ['question','The big question',20,150], ['contribution','What we contributed',32,245],
  ['finding','What we found',44,320], ['next','Limits and next steps',50,355]
];
export const example = {
  audience:'General public', theme:'Cell types and connections', citation:'Fictional teaching example • simulated mouse cortex maps',
  problem:'Brain maps can show what kinds of cells are present and how those cells connect. Putting both kinds of information together is difficult.',
  question:'Can we link cell identities to wiring in a small patch of mouse brain?',
  contribution:'We built a workflow to align simulated cell labels with a wiring map.',
  finding:'The workflow recovered the cell groups we had planted in our simulated maps.',
  basis:'We compared its labels with the known labels in the simulation.',
  limit:'We tested simulated maps only. Accuracy in real tissue is still unknown.',
  relevance:'With testing in real tissue, this could help researchers compare how different cell types connect.',
  status:'simulation'
};
export function scope(status) {
  return {observed:'Observed result', preliminary:'Preliminary result', simulation:'Simulation result', pending:'Results pending'}[status];
}
export const localEditorial = {
  pitch({problem,question,contribution,finding,basis,limit,relevance,status,audience}) {
    const intro = { 'High school students': 'Here’s the question we asked.', 'Undergraduate students': 'Our study asked:', 'General public': '' }[audience] ?? '';
    const result = status === 'pending' ? 'We don’t have results yet.' : sentence(finding);
    const qualifier = {preliminary:'These results are preliminary.', simulation:'This was a simulation study.'}[status] ?? '';
    return [sentence(problem), intro, sentence(question), contribution.split(/\n+/u).filter(line => line.trim()).map(sentence).join(' '), qualifier, result, sentence(basis), sentence(limit), sentence(relevance)].filter(Boolean).join(' ');
  },
  poster(facts, approvedPitch) {
    const firstQuestion = approvedPitch.match(/[^.!?]*\?/u)?.[0]?.trim();
    const hook = firstQuestion && words(firstQuestion) <= 10 && firstQuestion.length <= 88 ? firstQuestion : '';
    return {headline:hook, problem:facts.problem, question:facts.question, contribution:facts.contribution,
      finding:(facts.status === 'pending' ? 'Results are pending.' : sentence(facts.finding)) + ' ' + sentence(facts.basis),
      next:sentence(facts.limit) + ' ' + sentence(facts.relevance)};
  }
};
export function licenseLines(credit, granted) {
  return ['Attribution: ' + credit, ...(granted ? ['Original author-owned material licensed under CC BY 4.0.', licenseURL, 'Third-party material excluded.'] : ['No Creative Commons license applied.'])];
}
export function validEmail(value) {
  return /^[^\s@]+@[^\s@.]+(?:\.[^\s@.]+)+$/u.test(value) && value.length <= 254;
}
