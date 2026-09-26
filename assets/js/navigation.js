(() => {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  const button = nav.querySelector('.nav-toggle');
  const menu = nav.querySelector('.nav-menu');
  const groups = [...nav.querySelectorAll('.nav-group')];
  nav.setAttribute('data-collapsible', '');
  button.hidden = false;

  const closeGroups = except => {
    groups.forEach(group => { if (group !== except) group.open = false; });
  };
  const closeMenu = () => {
    menu.removeAttribute('data-open');
    button.setAttribute('aria-expanded', 'false');
    closeGroups();
  };
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    menu.toggleAttribute('data-open', !expanded);
    button.setAttribute('aria-expanded', String(!expanded));
    if (expanded) closeGroups();
  });
  groups.forEach(group => {
    group.querySelector('summary').addEventListener('click', () => closeGroups(group));
  });
  document.addEventListener('click', event => {
    if (!nav.contains(event.target)) closeMenu();
  });
  nav.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const opened = groups.find(group => group.open);
    if (opened) {
      opened.open = false;
      opened.querySelector('summary').focus();
    } else if (button.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      button.focus();
    }
    event.preventDefault();
  });
  nav.addEventListener('focusout', event => {
    if (!nav.contains(event.relatedTarget)) closeMenu();
  });
  window.matchMedia('(max-width: 900px)').addEventListener('change', closeMenu);
})();
