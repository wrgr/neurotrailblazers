import {questions, sections, example, words, seconds, localEditorial, scope, independence, licenseLines, validEmail} from './editorial.js';
import {drawNetwork, drawPoster} from './artwork.js';
import {editorialPrompt} from './prompt.js';

const $ = id => document.getElementById(id);
const research = $('research');
const poster = $('poster');
const script = $('pitch');
const stageButtons = [...document.querySelectorAll('[data-stage]')];
let facts;
let approvedPitch = '';
let posterApproved = false;
let exampleLoaded = false;
let sourceSelection = '';
let uploadVersion = 0;

$('questions').innerHTML = questions.map(([id,label,hint,max]) => `
  <div class="question">
    <label>${label}<small>${hint} Aim for ${max} words or fewer.</small><textarea name="${id}" rows="2" maxlength="500" required></textarea></label>
    ${id === 'finding' ? '<label>Evidence status<select name="status"><option value="observed">Observed result</option><option value="preliminary">Preliminary result</option><option value="simulation">Simulation result</option><option value="pending">Results pending</option></select></label>' : ''}
    <details><summary>Evidence note (optional)</summary>
      <label>Source location or supporting excerpt<input name="e-${id}" maxlength="360" placeholder="Figure, page, lab record or short excerpt"></label>
      <button type="button" class="secondary use-selection" data-evidence="${id}" hidden>Use selection</button>
    </details>
  </div>`).join('');
$('poster-fields').innerHTML = sections.map(([id,label,max,chars]) => `
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
$('prompt-copy').addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(editorialPrompt);
    $('prompt-copy').textContent = 'Prompt copied';
  } catch {
    $('prompt-copy').textContent = 'Select and copy the prompt above';
  }
});

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
    announce('Source loaded locally. Add your plain-language notes and select excerpts for the evidence fields.');
  } catch {
    announce('The file could not be read. Try pasting an excerpt.');
  } finally {
    if (version === uploadVersion) event.target.value = '';
  }
});
function invalidateResearch() {
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
  $('credit').value = '';
  $('license').checked = false;
  $('email-form').reset();
  uploadVersion++;
  $('source-text').value = '';
  $('upload').value = '';
  sourceSelection = '';
  exampleLoaded = true;
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
  $('timing').textContent = count + ' words · about ' + seconds(script.value) + ' seconds' + (ok ? '' : ' · edit to 65–130 words to approve');
  $('timing').classList.toggle('error', !ok);
  script.setCustomValidity(ok ? '' : 'Edit the spoken pitch to 65–130 words.');
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
    const draft = localEditorial.poster(facts,approvedPitch);
    if (facts.citation === example.citation && exampleLoaded && !draft.headline) draft.headline = 'What if brain maps could show both?';
    for (const [key,,,max] of sections) {
      const field = $('field-'+key);
      field.value = draft[key].length > max ? '' : draft[key];
      field.placeholder = draft[key].length > max ? 'Summarize this section using the approved research notes.' : '';
    }
    $('poster-check').checked = false;
    posterApproved = false;
  }
  evidence($('poster-evidence'),true);
  stages();
  navigate(2);
  renderPoster();
};
function renderPoster() {
  const values = Object.fromEntries(sections.map(([key,,max]) => {
    const field = $('field-'+key);
    const value = field.value.trim();
    const count = words(value);
    $('count-'+key).textContent = count + '/' + max + ' words';
    field.setCustomValidity(!value || count > max ? 'Use between 1 and ' + max + ' words.' : '');
    return [key,value];
  }));
  const footer = ['Source: '+facts.citation, ...licenseLines($('credit').value.trim() || 'Add author credit at export', $('license').checked), independence];
  const fits = drawPoster(poster, {template:$('template').value, scope:scope(facts.status), values, sections, footer});
  $('overflow').textContent = fits ? '' : 'Some text exceeds the poster layout. Shorten the headline or body text.';
  return fits;
}
$('poster-form').addEventListener('input', event => {
  if (event.target.id !== 'poster-check') $('poster-check').checked = false;
  posterApproved = false;
  stages();
  if (event.target.id !== 'poster-check') renderPoster();
});
$('poster-form').onsubmit = event => {
  event.preventDefault();
  if (!renderPoster()) {
    announce('Shorten the poster text before approving.');
    return;
  }
  posterApproved = true;
  stages();
  navigate(3);
};
function exportReady() {
  const credit = $('credit');
  credit.setCustomValidity(credit.value.trim() ? '' : 'Add the name to credit on the output.');
  if (!credit.reportValidity()) return false;
  if (!posterApproved || !renderPoster()) {
    announce('The poster exceeds the layout. Shorten the poster or attribution.');
    return false;
  }
  return true;
}
$('credit').oninput = () => $('credit').setCustomValidity('');
function download(blob,name) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = name;
  link.click();
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
  const image = new Image();
  image.src = poster.toDataURL('image/png');
  try {
    await image.decode();
    $('print-area').replaceChildren(image);
    document.body.classList.add('print-ready');
    window.print();
  } catch {
    announce('Print preview could not open. Download the PNG and print it from your image viewer.');
  }
};
window.addEventListener('afterprint', () => {
  document.body.classList.remove('print-ready');
  $('print-area').replaceChildren();
});
$('script').onclick = () => {
  if (!exportReady()) return;
  const content = [approvedPitch,'','Source: '+facts.citation, ...licenseLines($('credit').value.trim(),$('license').checked),independence].join('\n');
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
