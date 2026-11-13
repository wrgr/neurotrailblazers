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
  ['headline','Overview · memorable question',12,90],
  ['discovery','Overview · one-sentence takeaway',24,170],
  ['problem','The puzzle · what readers need to know',29,200],
  ['contribution','What we did · method or contribution',29,200],
  ['visualA','Diagram · first label',5,30],
  ['visualB','Diagram · second label',5,30],
  ['finding','What the evidence showed · include the comparison',29,200],
  ['relevance','Why it matters · realistic implication or next step',29,200],
  ['limit','Evidence boundary · what the study can’t establish',24,160],
  ['invitation','Invite students to ask a specific question',10,65]
];
export const examplePoster = {
  headline:'Can a brain map show who talks to whom?',
  discovery:'We tested whether one map could show both cell types and their wiring.',
  problem:'Some brain maps show which kinds of cells are present. Others show how cells connect. It is hard to line up the two views.',
  contribution:'We built a method to match cell labels to a wiring map. We tried it on a simulated patch of mouse brain.',
  visualA:'Cell types',
  visualB:'Wiring map',
  finding:'We checked the match against cell groups we had planted in the simulation. The method recovered those groups.',
  relevance:'If it works on real tissue, this approach could help researchers compare how different kinds of brain cells connect.',
  limit:'We tested simulated maps only. We still don’t know how accurately the method works on real brain tissue.',
  invitation:'Ask me how we checked the match.'
};
export const invitation = 'Ask me how we tested this.';
export const licenseSummary = 'CC BY 4.0 by default for newly created material you have rights to license. Source and third-party material retain their existing terms.';
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
  pitch({problem,question,contribution,finding,basis,limit,relevance,status}) {
    const result = status === 'pending' ? 'We’re still gathering results.' : sentence(finding);
    const qualifier = {preliminary:'These results are preliminary.', simulation:'We tested this in a simulation.'}[status] ?? '';
    return [sentence(question), sentence(problem), contribution.split(/\n+/u).filter(line => line.trim()).map(sentence).join(' '), qualifier, result, sentence(basis), sentence(limit), sentence(relevance), invitation].filter(Boolean).join(' ');
  },
  poster(facts, approvedPitch) {
    const firstQuestion = approvedPitch.match(/[^.!?]*\?/u)?.[0]?.trim();
    return {
      headline:firstQuestion ?? facts.question,
      discovery:facts.status === 'pending' ? 'We’re still gathering results.' : sentence(facts.finding),
      problem:sentence(facts.problem),
      contribution:facts.contribution,
      finding:facts.status === 'pending' ? sentence(facts.basis) : sentence(facts.finding) + ' ' + sentence(facts.basis),
      relevance:sentence(facts.relevance),
      limit:sentence(facts.limit),
      invitation, visualA:'Study setup', visualB:'What we measured'
    };
  }
};
export function licenseLines(credit, institution) {
  return ['Scientists: ' + credit + ' · ' + institution, 'CC BY 4.0 · Newly created material the authors have rights to license.', licenseURL, 'Source and third-party material retain their existing terms.'];
}
export function followUpURL(input) {
  if (!input) return '';
  if (input.length > 250 || /[\s\u0000-\u001f]/u.test(input) || !input.startsWith('https://')) return null;
  try {
    const url = new URL(input);
    if (url.protocol !== 'https:' || url.username || url.password || !url.hostname.includes('.') || url.href.length > 250) return null;
    return url.href;
  } catch {
    return null;
  }
}
export function oneSentence(text) {
  if (typeof Intl.Segmenter !== 'function') return !/[.!?]\s+\p{Lu}/u.test(text);
  return Array.from(new Intl.Segmenter('en', {granularity:'sentence'}).segment(text)).length === 1;
}
export function copiesSource(copy, source) {
  const tokenize = value => value.toLowerCase().match(/[\p{L}\p{N}]+/gu) ?? [];
  const tokens = tokenize(copy);
  const size = 12;
  if (!source || tokens.length < size) return false;
  const normalized = ' ' + tokenize(source).join(' ') + ' ';
  return tokens.some((_,i) => i + size <= tokens.length && normalized.includes(' ' + tokens.slice(i,i+size).join(' ') + ' '));
}
export function claimWarnings(copy, record) {
  const number = /(?<![\p{L}\p{N}])[+−-]?\d+(?:[.,]\d+)*(?:\s*%)?/gu;
  const sourceNumbers = new Set(Object.values(record).join(' ').match(number)?.map(value => value.replace(/\s/g,'')) ?? []);
  const unsupported = (copy.match(number) ?? []).some(value => !sourceNumbers.has(value.replace(/\s/g,'')));
  const clinical = /\b(?:cures?|guarantee\w*|proves?|breakthrough|eliminates?|prevents?|will (?:treat|diagnose|improve|help patients)|clinically proven)\b/iu.test(copy);
  return [
    ...(unsupported ? ['A number in this draft is missing from the research record. Add its source and context to the research notes or remove the number.'] : []),
    ...(clinical ? ['Check the wording for unsupported certainty or clinical benefit. Match the study’s evidence and keep possible applications conditional.'] : [])
  ];
}
export function validEmail(value) {
  return /^[^\s@]+@[^\s@.]+(?:\.[^\s@.]+)+$/u.test(value) && value.length <= 254;
}
