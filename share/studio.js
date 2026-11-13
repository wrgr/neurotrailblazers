import {questions, sections, example, examplePoster, words, seconds, localEditorial, scope, independence, licenseLines, licenseSummary, followUpURL, oneSentence, copiesSource, claimWarnings, validEmail} from './editorial.js';
import {drawNetwork, drawPoster} from './artwork.js';
import {editorialPrompt} from './prompt.js';
import {posterPDF} from './poster-pdf.js';
import {presenterPrompt, readPresenterDraft} from './presenter.js';
import {micronsRecord, micronsDraft, micronsDOI} from './microns-demo.js';

const $ = id => document.getElementById(id);
const research = $('research');
const poster = $('poster');
const script = $('pitch');
const stageButtons = [...document.querySelectorAll('[data-stage]')];
let facts;
let approvedPitch = '';
let posterApproved = false;
let sourceText = '';
let sourceSelection = '';
let uploadVersion = 0;
let presenterDraft;
let illustration;
let illustrationVersion = 0;
let illustrationPending = false;

$('questions').innerHTML = questions.map(([id,label,hint,max]) => `
  <div class="question">
    <label>${label}<small>${hint} Aim for ${max} words or fewer.</small><textarea name="${id}" rows="2" maxlength="500" required></textarea></label>
    ${id === 'finding' ? '<label>Evidence status<select name="status"><option value="observed">Observed result</option><option value="preliminary">Preliminary result</option><option value="simulation">Simulation result</option><option value="pending">Results pending</option></select></label>' : ''}
    <details><summary>Evidence note (optional)</summary>
      <label>Source location or supporting excerpt<input name="e-${id}" maxlength="360" placeholder="Figure, page, lab record or short excerpt"></label>
      <button type="button" class="secondary use-selection" data-evidence="${id}" hidden>Use selection</button>
    </details>
  </div>`).join('');
$('poster-fields').innerHTML = sections.map(([id,label,,chars]) => `
  <label>${label}<span class="count" id="count-${id}"></span>
  <textarea id="field-${id}" rows="${id === 'headline' ? 2 : 3}" maxlength="${chars}" required></textarea></label>`).join('');

function announce(message) { $('status').textContent = message; }
function stages() {
  stageButtons[1].disabled = !facts;
  stageButtons[2].disabled = !approvedPitch;
  stageButtons[3].disabled = !posterApproved;
}
function navigate(index, focus = true) {
  if (stageButtons[index].disabled) return;
  stageButtons.forEach((button,i) => {
    $('stage'+i).hidden = i !== index;
    button.removeAttribute('aria-current');
  });
  stageButtons[index].setAttribute('aria-current','step');
  announce('');
  if (focus) {
    const heading = $('stage'+index).querySelector('h2');
    heading.tabIndex = -1;
    heading.focus();
  }
}
stageButtons.forEach((button,i) => button.addEventListener('click', () => navigate(i)));
navigate(0,false);
drawNetwork($('art'));
$('prompt-text').textContent = editorialPrompt;
$('license-summary').textContent = licenseSummary;
$('prompt-copy').addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(editorialPrompt);
    $('prompt-copy').textContent = 'Prompt copied';
  } catch {
    $('prompt-copy').textContent = 'Select and copy the prompt above';
  }
});

$('presenter-copy').onclick = async () => {
  if (!facts) return;
  try {
    await navigator.clipboard.writeText(presenterPrompt(facts));
    $('presenter-status').textContent = 'Copied. Paste into your signed-in ChatGPT tab.';
  } catch {
    $('presenter-status').textContent = 'Clipboard unavailable. Use Copy prompt only and add your brief in ChatGPT.';
  }
};
$('presenter-import').onclick = () => {
  if (!facts) return;
  try {
    const draft = readPresenterDraft($('presenter-draft').value);
    script.value = draft.script;
    script.oninput();
    presenterDraft = draft;
    $('presenter-status').textContent = 'Draft loaded. Review the script below. Approving it will open the imported poster for review.';
  } catch (error) {
    $('presenter-status').textContent = error.message;
  }
};

const tips = {
  'Brain cell diversity and atlases':'What kinds of cells did you distinguish, where, and how might someone use that map?',
  'Brain wiring and connectivity':'What kind of connection did you measure or infer? Say at what scale and in what tissue.',
  'Cell types and connections':'Which cell identities and connections did you link? How did you check the match?',
  'Neurotechnology':'What new measurement or manipulation does the tool allow, and where has it been tested?',
  'Understanding brain function':'What did you measure about the brain at work? How much does the result explain?',
  'Human relevance':'Describe what the work could eventually inform and what evidence is still needed.'
};
function updateTheme() { $('theme-tip').textContent = tips[research.elements.theme.value] ?? ''; }
function mode(isSource) {
  $('source-panel').hidden = !isSource;
  $('source-mode').setAttribute('aria-pressed', String(isSource));
  $('interview-mode').setAttribute('aria-pressed', String(!isSource));
  document.querySelectorAll('.use-selection').forEach(button => button.hidden = !isSource);
}
$('source-mode').onclick = () => mode(true);
$('interview-mode').onclick = () => mode(false);
$('source-text').addEventListener('select', event => {
  const source = event.target;
  sourceSelection = source.value.slice(source.selectionStart, source.selectionEnd).trim();
});
$('source-text').addEventListener('input', () => {
  uploadVersion++;
  sourceSelection = '';
  invalidateResearch();
});
document.querySelectorAll('.use-selection').forEach(button => button.onclick = () => {
  if (!sourceSelection) {
    $('source-text').focus();
    announce('Select a passage in the source box first.');
    return;
  }
  if (sourceSelection.length > 360) {
    announce('Select a shorter passage of up to 360 characters.');
    return;
  }
  research.elements['e-'+button.dataset.evidence].value = sourceSelection;
  invalidateResearch();
  announce('Evidence excerpt added to the research record.');
});
$('upload').addEventListener('change', async event => {
  const file = event.target.files[0];
  const version = ++uploadVersion;
  if (!file) return;
  if (!/\.(txt|md)$/i.test(file.name) || file.size > 2_000_000) {
    announce('Choose a .txt or .md file under 2 MB, or paste an excerpt.');
    event.target.value = '';
    return;
  }
  try {
    const source = await file.text();
    if (version !== uploadVersion) return;
    if (!source.trim() || source.includes('\0') || source.length > 1_000_000) {
      announce('Use a nonempty UTF-8 text file under one million characters.');
      return;
    }
    $('source-text').value = source;
    sourceSelection = '';
    invalidateResearch();
    announce('Source loaded locally. Add your plain-language notes and select excerpts for the evidence fields.');
  } catch {
    announce('The file could not be read. Try pasting an excerpt.');
  } finally {
    if (version === uploadVersion) event.target.value = '';
  }
});
function invalidateResearch() {
  illustrationVersion++;
  illustration = undefined;
  illustrationPending = false;
  $('diagram-file').value = '';
  $('diagram-remove').hidden = true;
  $('diagram-status').textContent = '';
  presenterDraft = undefined;
  $('presenter-draft').value = '';
  $('presenter-status').textContent = '';
  facts = undefined;
  approvedPitch = '';
  posterApproved = false;
  stages();
}
research.addEventListener('input', () => {
  invalidateResearch();
  updateTheme();
});
research.elements.status.addEventListener('change', () => {
  research.elements.finding.required = research.elements.status.value !== 'pending';
});
$('example').onclick = () => {
  if ([...new FormData(research)].some(([key,value]) => !['audience','status','theme'].includes(key) && value.trim()) &&
      !window.confirm('Replace the research fields and current drafts with the worked example?')) return;
  research.reset();
  for (const [key,value] of Object.entries(example)) research.elements[key].value = value;
  research.elements['e-finding'].value = 'Simulated labels compared against known labels planted in the teaching dataset.';
  research.elements['e-limit'].value = 'Teaching dataset contains simulated maps only.';
  research.elements.finding.required = true;
  $('credit').value = 'Research in One Minute team';
  $('institution').value = 'Fictional teaching example';
  $('follow-up').value = 'https://www.neurotrailblazers.org/';
  $('email-form').reset();
  uploadVersion++;
  $('source-text').value = '';
  $('upload').value = '';
  sourceSelection = '';
  invalidateResearch();
  updateTheme();
  mode(false);
  navigate(0);
};
function evidence(target, includePitch) {
  target.replaceChildren();
  const items = [
    ...(includePitch ? [['Approved script',approvedPitch]] : []),
    ['Study record',facts.citation],
    ['Evidence status',scope(facts.status)],
    ...questions.filter(([id]) => facts[id]).map(([id,label]) => [label, facts[id] + (facts['e-'+id] ? ' • Source note: ' + facts['e-'+id] : '')])
  ];
  for (const [label,value] of items) {
    const p = document.createElement('p');
    const strong = document.createElement('strong');
    strong.textContent = label + ' ';
    p.append(strong, document.createTextNode(value));
    target.append(p);
  }
}
research.onsubmit = event => {
  event.preventDefault();
  const record = Object.fromEntries([...new FormData(research)].map(([key,value]) => [key,value.trim()]));
  const empty = [...research.querySelectorAll('[required]')].find(input => !record[input.name]);
  if (empty) {
    empty.focus();
    announce('Fill in the field with a research detail.');
    return;
  }
  facts = record;
  sourceText = $('source-text').value;
  approvedPitch = '';
  posterApproved = false;
  script.value = localEditorial.pitch(facts);
  $('pitch-check').checked = false;
  $('pitch-check').disabled = false;
  evidence($('pitch-evidence'),false);
  timing();
  stages();
  navigate(1);
};
function timing() {
  const count = words(script.value);
  const ok = count >= 65 && count <= 130;
  const copied = copiesSource(script.value,sourceText);
  $('timing').textContent = count + ' words · about ' + seconds(script.value) + ' seconds' + (ok ? '' : ' · edit to 65–130 words to approve');
  $('timing').classList.toggle('error', !ok);
  const notices = claimWarnings(script.value,facts ?? {});
  if (copied) notices.unshift('Rewrite the passage that matches your uploaded or pasted source in your own words.');
  $('pitch-warning').textContent = notices.join(' ');
  script.setCustomValidity(!ok ? 'Edit the spoken script to 65–130 words.' : copied ? notices[0] : '');
}
script.oninput = () => {
  approvedPitch = '';
  posterApproved = false;
  $('pitch-check').checked = false;
  timing();
  stages();
};
$('pitch-form').onsubmit = event => {
  event.preventDefault();
  const unchanged = script.value.trim() === approvedPitch;
  approvedPitch = script.value.trim();
  if (!unchanged) {
    const isExample = facts.citation === example.citation && questions.every(([key]) => facts[key] === example[key]) && facts.status === example.status;
    const draft = presenterDraft?.poster ?? (isExample ? examplePoster : localEditorial.poster(facts,approvedPitch));
    if (presenterDraft) $('diagram').value = presenterDraft.diagram;
    for (const [key] of sections) $('field-'+key).value = draft[key];
    $('poster-check').checked = false;
    posterApproved = false;
  }
  evidence($('poster-evidence'),true);
  stages();
  navigate(2);
  renderPoster();
};
function renderPoster() {
  const values = Object.fromEntries(sections.map(([key,,max,chars]) => {
    const field = $('field-'+key);
    const value = field.value.trim();
    const count = words(value);
    $('count-'+key).textContent = count + '/' + max + ' words';
    let issue = !value || count > max || value.length > chars ? 'Shorten or complete this field within its word limit.' : '';
    if (!issue && key === 'headline' && (!value.endsWith('?') || !oneSentence(value))) issue = 'Write a single question.';
    if (!issue && key === 'discovery' && !oneSentence(value)) issue = 'Write one discovery sentence.';
    if (!issue && key === 'contribution' && value.split(/\n+/u).length > 2) issue = 'Use one or two contributions.';
    field.setCustomValidity(issue);
    return [key,value];
  }));
  const copy = Object.values(values).join(' ');
  const url = followUpURL($('follow-up').value.trim());
  $('follow-up').setCustomValidity(url === null ? 'Enter a public HTTPS URL of 250 characters or fewer.' : '');
  for (const id of ['credit','institution']) $(id).setCustomValidity($(id).value.trim() ? '' : 'Add attribution for the export.');
  const footer = [...licenseLines($('credit').value.trim() || 'Scientist name(s)', $('institution').value.trim() || 'Institution'),
    'Source: '+facts.citation,'Independent studio · No NIH affiliation or endorsement.'];
  const fits = drawPoster(poster, {template:$('template').value, values, footer, diagram:$('diagram').value, illustration, url});
  $('overflow').textContent = fits ? '' : 'Some text exceeds its poster space. Shorten the affected copy or credits.';
  const notices = claimWarnings(copy,facts);
  const copied = copiesSource(copy,sourceText);
  if (copied) notices.unshift('Rewrite the passage that matches your uploaded or pasted source in your own words.');
  const scopeWords = {preliminary:/\b(?:preliminary|early)\b/iu,simulation:/\bsimulat/iu,pending:/\b(?:pending|still gathering|no results|not yet)\b/iu}[facts.status];
  const missingScope = !!scopeWords && !scopeWords.test(values.discovery + ' ' + values.finding + ' ' + values.limit);
  if (missingScope) notices.unshift('State the evidence status in the discovery or evidence boundary field: ' + scope(facts.status).toLowerCase() + '.');
  $('poster-warning').textContent = notices.join(' ');
  return fits && !copied && !missingScope && !illustrationPending;
}
$('poster-form').addEventListener('input', event => {
  if (!['poster-check','diagram-file'].includes(event.target.id)) $('poster-check').checked = false;
  posterApproved = false;
  stages();
  if (!['poster-check','diagram-file'].includes(event.target.id)) renderPoster();
});
function illustrationChanged(message) {
  $('diagram-status').textContent = message;
  $('diagram-remove').hidden = !illustration;
  $('poster-check').checked = false;
  posterApproved = false;
  stages();
  if (facts) renderPoster();
}
$('diagram-file').onchange = async event => {
  const file = event.target.files[0];
  if (!file) return;
  event.target.value = '';
  const version = ++illustrationVersion;
  illustrationPending = false;
  if (!['image/png','image/jpeg','image/webp'].includes(file.type) || file.size > 10000000) {
    illustrationChanged('Choose a PNG, JPEG or WebP under 10 MB.');
    return;
  }
  illustrationPending = true;
  illustrationChanged('Opening illustration…');
  const url = URL.createObjectURL(file);
  try {
    const image = new Image();
    image.src = url;
    await image.decode();
    if (version !== illustrationVersion) return;
    illustration = image;
    illustrationPending = false;
    illustrationChanged('Illustration loaded. Check it against the source in the preview.');
  } catch {
    if (version !== illustrationVersion) return;
    illustrationPending = false;
    illustrationChanged('Could not open this image. Try another file.');
  } finally {
    URL.revokeObjectURL(url);
  }
};
$('diagram-remove').onclick = () => {
  illustrationVersion++;
  illustration = undefined;
  illustrationPending = false;
  illustrationChanged('Using the built-in diagram.');
};
$('poster-form').onsubmit = event => {
  event.preventDefault();
  if (!renderPoster() || !$('poster-form').reportValidity()) {
    announce('Resolve the review notes and shorten any panel that exceeds its space.');
    return;
  }
  posterApproved = true;
  stages();
  navigate(3);
};
function exportReady() {
  if (!posterApproved || !renderPoster()) {
    announce('Return to the poster and resolve the review notes before exporting.');
    return false;
  }
  return true;
}
function download(blob,name) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = name;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 3000);
}
$('png').onclick = () => {
  if (!exportReady()) return;
  poster.toBlob(blob => {
    if (blob) download(blob,'research-in-one-minute.png');
    else announce('PNG creation failed. Try Print / Save PDF.');
  },'image/png');
};
$('pdf').onclick = async () => {
  if (!exportReady()) return;
  try {
    download(await posterPDF(poster),'research-in-one-minute.pdf');
  } catch {
    announce('PDF creation failed. Download the PNG and print it from your image viewer.');
  }
};
$('script').onclick = () => {
  if (!exportReady()) return;
  const content = [approvedPitch,'','Source: '+facts.citation, ...licenseLines($('credit').value.trim(),$('institution').value.trim()),independence].join('\n');
  download(new Blob([content],{type:'text/plain;charset=utf-8'}),'research-in-one-minute-script.txt');
};
$('email').oninput = () => $('email').setCustomValidity('');
$('email-form').onsubmit = event => {
  event.preventDefault();
  const email = $('email');
  const address = email.value.trim();
  if (!validEmail(address)) {
    email.setCustomValidity('Enter an email address such as name@example.org.');
    email.reportValidity();
    return;
  }
  const recipient = encodeURIComponent(address).replace('%40','@');
  const body = encodeURIComponent('Attach the poster and script you downloaded from Research in One Minute before sending.');
  announce('Requested an email draft. Attach the downloaded files in your email app.');
  window.location.href = 'mailto:' + recipient + '?subject=Research%20in%20One%20Minute&body=' + body;
};

if (new URLSearchParams(location.search).get('demo') === 'microns') {
  const run = new URLSearchParams(location.search).get('step');
  for (const [key,value] of Object.entries(micronsRecord)) research.elements[key].value = value;
  $('credit').value = 'MICrONS Consortium et al.';
  $('institution').value = 'Allen Institute, Baylor College of Medicine, Princeton and collaborators';
  $('follow-up').value = micronsDOI;
  updateTheme();
  research.requestSubmit();
  if (run === 'draft') {
    $('presenter-copy').closest('details').open = true;
  } else {
    $('presenter-draft').value = JSON.stringify(micronsDraft, null, 2);
    $('presenter-import').click();
    $('pitch-check').checked = true;
    $('pitch-form').requestSubmit();
    if (!approvedPitch) throw new Error('The MICrONS demo script could not be loaded.');
    const url = new URL('./microns-illustration.svg',import.meta.url);
    const version = ++illustrationVersion;
    const image = new Image();
    illustrationPending = true;
    illustrationChanged('Opening MICrONS illustration…');
    image.src = url.href;
    image.decode().then(() => {
      if (version !== illustrationVersion) return;
      illustration = image;
      illustrationPending = false;
      illustrationChanged('Original MICrONS illustration loaded. Review the figure and citation before export.');
    }, () => {
      if (version !== illustrationVersion) return;
      illustrationPending = false;
      illustrationChanged('The MICrONS illustration could not load. The built-in diagram is available.');
    });
  }
}
