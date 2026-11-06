/* Genesis - tabbed viewer chrome. Independent of the simulation renderer. */
(() => {
  const ui = document.getElementById('ui');
  const reopen = document.getElementById('ui-reopen');
  const tabs = Array.from(document.querySelectorAll('.ui-tab[data-panel]'));
  const panels = Array.from(document.querySelectorAll('.ui-panel[data-panel]'));
  const close = document.getElementById('ui-close');
  const overlay = document.getElementById('overlay');
  const overlayClose = document.getElementById('overlay-close');
  let active = 'world';

  function showPanel(name) {
    active = name || 'world';
    for (const tab of tabs) {
      const on = tab.dataset.panel === active;
      tab.classList.toggle('active', on);
      tab.setAttribute('aria-selected', String(on));
    }
    for (const panel of panels) {
      panel.classList.toggle('active', panel.dataset.panel === active);
    }
    ui.hidden = false;
    reopen.hidden = true;
  }

  for (const tab of tabs) {
    tab.addEventListener('click', () => showPanel(tab.dataset.panel));
  }

  close.addEventListener('click', () => {
    ui.hidden = true;
    reopen.hidden = false;
  });

  reopen.addEventListener('click', () => showPanel(active));

  if (overlayClose) {
    overlayClose.addEventListener('click', () => overlay.classList.add('hidden'));
  }

  document.addEventListener('keydown', (event) => {
    if (event.code !== 'Escape') return;
    if (!overlay.classList.contains('hidden')) {
      overlay.classList.add('hidden');
      return;
    }
    if (!ui.hidden) {
      ui.hidden = true;
      reopen.hidden = false;
    }
  });

  showPanel('world');
})();
