(() => {
  const area = document.querySelector('.site-breadcrumbs a:nth-of-type(2)');
  if (area) document.querySelectorAll('summary[data-nav-label]').forEach(el => el.classList.toggle('active', el.dataset.navLabel === area.textContent.trim()));
  const input = document.getElementById('session-search');
  if (input) {
    const status = document.getElementById('session-status'), count = document.getElementById('session-count');
    const cards = [...document.querySelectorAll('.session-card')].map(el => ({el, text:el.textContent.toLowerCase()}));
    let timer;
    const filter = () => { let shown=0; const q=input.value.trim().toLowerCase(); cards.forEach(({el,text}) => { el.hidden=!(text.includes(q) && (status.value==='all' || el.dataset.status===status.value)); if(!el.hidden) shown++; }); count.textContent=shown+' of '+cards.length+' session plans'+(shown ? '.' : '. Clear the search or change status.'); };
    input.addEventListener('input', () => { clearTimeout(timer); timer=setTimeout(filter,180); }); status.addEventListener('change',filter); filter();
  }
  const actions=document.querySelector('.lesson-actions');
  if(actions) {
    const headings=[...document.querySelectorAll('main h2[id]')].filter(el => !el.closest('details'));
    for(const [label, pattern] of [['Learn', /what you|why this|resolution argument/i], ['Practice', /^lab:|studio activity/i], ['Check your work', /rubric|self.check/i]]) {
      const h=headings.find(el => pattern.test(el.textContent));
      if(h){const a=document.createElement('a'); a.href='#'+h.id; a.textContent=label; actions.appendChild(a);}
    }
  }
  const draft=document.getElementById('first-observation');
  if(draft){
    const message=document.getElementById('first-save-status'), key='nt-first-observation-v1';
    try {draft.value=localStorage.getItem(key)||'';} catch(_){message.textContent='Local saving is unavailable. Copy your answer before leaving.';}
    draft.addEventListener('input',()=>{try{localStorage.setItem(key,draft.value); message.textContent='Draft saved in this browser only.';}catch(_){message.textContent='Not saved. Copy your answer before leaving.';}});
    document.getElementById('first-clear').addEventListener('click',()=>{draft.value='';try{localStorage.removeItem(key);}catch(_){} message.textContent='Draft cleared.';});
  }
})();
