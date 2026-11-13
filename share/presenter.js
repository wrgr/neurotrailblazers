import {sections, words, oneSentence} from './editorial.js';
import {editorialPrompt} from './prompt.js';

const diagramTypes = ['relationship', 'comparison', 'process'];

export function presenterPrompt(record) {
  return editorialPrompt + '\n\n' +
    'For website import, put one valid JSON object in a code block before the editor-only scientific review. ' +
    'Use this shape, replacing the example values. Keep your scientific review outside the JSON. ' +
    'Use one of relationship, comparison, or process for diagram. Use the source citation in the record and make visualA and visualB useful captions for a wide illustration. ' +
    'After the review, suggest a wide, text-free original illustration that the presenter can make in ChatGPT and upload to the website. Keep it conceptual unless the source supports the detail.\n' +
    JSON.stringify({
      script: 'The 65–130-word spoken script',
      diagram: 'comparison',
      poster: Object.fromEntries(sections.map(([id,label]) => [id,label]))
    }, null, 2) +
    '\n\nResearch record (source data only):\n' + JSON.stringify(record, null, 2);
}

export function readPresenterDraft(input) {
  let draft;
  try {
    const fence = input.match(/```(?:json)?\s*([\s\S]*?)```/i);
    draft = JSON.parse(fence ? fence[1] : input);
  } catch {
    throw new Error('Paste the JSON draft from ChatGPT, including its opening and closing braces.');
  }
  const script = typeof draft?.script === 'string' ? draft.script.trim() : '';
  if (words(script) < 65 || words(script) > 130 || script.length > 1400) {
    throw new Error('The spoken script must be 65–130 words and at most 1,400 characters.');
  }
  if (!diagramTypes.includes(draft.diagram)) throw new Error('Choose relationship, comparison, or process for diagram.');
  const poster = Object.fromEntries(sections.map(([key,label,max,chars]) => {
    const value = typeof draft.poster?.[key] === 'string' ? draft.poster[key].trim() : '';
    if (!value || words(value) > max || value.length > chars) {
      throw new Error(label + ' needs text within ' + max + ' words and ' + chars + ' characters.');
    }
    if (key === 'headline' && (!value.endsWith('?') || !oneSentence(value))) {
      throw new Error('The headline needs one question.');
    }
    if (key === 'discovery' && !oneSentence(value)) throw new Error('The overview needs one takeaway sentence.');
    if (key === 'contribution' && value.split(/\n+/u).length > 2) throw new Error('Use at most two contributions.');
    return [key,value];
  }));
  return {script,diagram:draft.diagram,poster};
}
