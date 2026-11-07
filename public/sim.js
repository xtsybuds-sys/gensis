(() => {
  'use strict';

  const $ = (selector) => document.querySelector(selector);
  const COLS = 10;
  const ROWS = 7;
  const MAX_TICKS = 24;

  const DEFAULT_LOADOUT = {
    defender: 6,
    cache: 3,
    raider: 5,
    drone: 3,
    armor: 2,
  };

  const LIMITS = {
    defender: { min: 1, max: 16 },
    cache: { min: 0, max: 8 },
    raider: { min: 0, max: 16 },
    drone: { min: 0, max: 8 },
    armor: { min: 0, max: 4 },
  };

  const DEMO_PLACEMENTS = [
    ['defender', 2, 5],
    ['defender', 4, 5],
    ['defender', 6, 5],
    ['defender', 3, 6],
    ['defender', 5, 6],
    ['cache', 1, 5],
    ['cache', 8, 5],
    ['raider', 2, 1],
    ['raider', 5, 1],
    ['raider', 7, 1],
    ['raider', 4, 0],
    ['drone', 3, 2],
    ['drone', 7, 2],
    ['armor', 5, 0],
  ];

  const UNIT_DEFS = {
    defender: {
      name: 'Defender',
      sub: '100-pack',
      team: 'friendly',
      badge: '100',
      prefix: 'D',
      maxHp: 100,
      maxAmmo: 100,
      range: 4,
      damage: 14,
      ammoCost: 8,
    },
    cache: {
      name: '200 cache',
      sub: '200 rounds',
      team: 'friendly',
      badge: '200',
      prefix: '200',
      maxHp: 100,
      maxAmmo: 200,
    },
    raider: {
      name: 'Raider',
      sub: 'ground pressure',
      team: 'enemy',
      badge: 'R',
      prefix: 'R',
      maxHp: 34,
      damage: 6,
      range: 1,
      moveEvery: 1,
    },
    drone: {
      name: 'Drone',
      sub: 'fast air contact',
      team: 'enemy',
      badge: 'U',
      prefix: 'U',
      maxHp: 22,
      damage: 4,
      range: 2,
      moveEvery: 1,
    },
    armor: {
      name: 'Armor',
      sub: 'heavy breakthrough',
      team: 'enemy',
      badge: 'A',
      prefix: 'A',
      maxHp: 80,
      damage: 12,
      range: 1,
      moveEvery: 2,
    },
  };

  const PHASE_LABELS = {
    prep: 'SIM PREP',
    staged: 'STAGED',
    running: 'SIM RUNNING',
    debrief: 'DEBRIEF',
  };

  const GLYPHS = {
    defender: `
      <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
        <path d="M18 20c0-6 2.5-10 6-10s6 4 6 10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>
        <circle cx="24" cy="18" r="5.5" fill="currentColor" opacity=".18"/>
        <path d="M14 40c.7-8 4.3-12 10-12s9.3 4 10 12" fill="currentColor" opacity=".14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M18 22l6 4M28 22l-3 4" stroke="#f6bd63" stroke-width="1.2" stroke-linecap="round"/>
        <rect x="30" y="21" width="10" height="14" rx="2" fill="#f6bd63" stroke="#f6bd63"/>
        <path d="M14 26l-4 8M35 35l3 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>`,
    cache: `
      <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
        <rect x="8" y="18" width="32" height="23" rx="2.5" fill="currentColor" opacity=".12" stroke="currentColor" stroke-width="1.6"/>
        <path d="M8 24h32M18 18v-4h12v4M14 30h8M14 35h14" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
        <circle cx="33" cy="30.5" r="2.2" fill="none" stroke="currentColor" stroke-width="1.2"/>
        <path d="M29 35h8" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
      </svg>`,
    raider: `
      <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
        <circle cx="24" cy="13" r="4.5" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="1.5"/>
        <path d="M17 40c0-9 3-14 7-14s7 5 7 14" fill="currentColor" opacity=".12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M16 22l-2 10M32 22l4 8M20 28h8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M33 20l6-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
      </svg>`,
    drone: `
      <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
        <path d="M14 16l20 20M34 16L14 36" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
        <circle cx="14" cy="16" r="3" fill="currentColor" opacity=".16" stroke="currentColor" stroke-width="1.2"/>
        <circle cx="34" cy="16" r="3" fill="currentColor" opacity=".16" stroke="currentColor" stroke-width="1.2"/>
        <circle cx="14" cy="36" r="3" fill="currentColor" opacity=".16" stroke="currentColor" stroke-width="1.2"/>
        <circle cx="34" cy="36" r="3" fill="currentColor" opacity=".16" stroke="currentColor" stroke-width="1.2"/>
        <circle cx="24" cy="26" r="5.2" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="1.5"/>
        <path d="M24 21v3M24 28v3" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>
      </svg>`,
    armor: `
      <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
        <path d="M8 31V22l6-7h19l7 8v8" fill="currentColor" opacity=".12" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
        <path d="M8 31h32M13 31v5M35 31v5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <circle cx="15" cy="37" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/>
        <circle cx="33" cy="37" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/>
        <path d="M18 22h12M22 22v-5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
        <path d="M36 19l5-2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
      </svg>`,
  };

  const state = {
    phase: 'prep',
    loadout: { ...DEFAULT_LOADOUT },
    units: [],
    selected: null,
    dragPayload: null,
    log: [],
    hint: '',
    tick: 0,
    startedAt: 0,
    timer: null,
    initialUnits: null,
    initialHostiles: 0,
    initialDefenders: 0,
    result: null,
    idSeq: { defender: 0, cache: 0, raider: 0, drone: 0, armor: 0 },
  };

  const escapeHtml = (value) => String(value ?? '').replace(/[&<>"']/g, (char) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
  }[char]));

  const setText = (selector, value) => {
    const element = $(selector);
    if (element) element.textContent = value;
  };

  const pad = (value) => String(value).padStart(2, '0');

  const formatSeconds = (value) => {
    const total = Math.max(0, Math.floor(value || 0));
    return `${pad(Math.floor(total / 60))}:${pad(total % 60)}`;
  };

  const phaseLabel = () => PHASE_LABELS[state.phase] || 'SIM PREP';

  const canEdit = () => state.phase === 'prep' || state.phase === 'staged';

  const getUnits = (kind) => state.units.filter((unit) => unit.kind === kind);

  const getDefenders = () => getUnits('defender');

  const getCaches = () => getUnits('cache');

  const getEnemies = () => state.units.filter((unit) => UNIT_DEFS[unit.kind].team === 'enemy');

  const available = (kind) => Math.max(0, state.loadout[kind] - getUnits(kind).length);

  const unitAt = (col, row) => state.units.find((unit) => unit.col === col && unit.row === row);

  const distance = (a, b) => Math.max(Math.abs(a.col - b.col), Math.abs(a.row - b.row));

  const isFree = (col, row, ignoreId = null) => {
    if (col < 0 || col >= COLS || row < 0 || row >= ROWS) return false;
    return !state.units.some((unit) => unit.id !== ignoreId && unit.col === col && unit.row === row);
  };

  const newUnit = (kind, col, row) => {
    const def = UNIT_DEFS[kind];
    const sequence = state.idSeq[kind] += 1;
    return {
      id: `${def.prefix}-${String(sequence).padStart(2, '0')}`,
      kind,
      col,
      row,
      hp: def.maxHp,
      maxHp: def.maxHp,
      ammo: def.maxAmmo || 0,
      maxAmmo: def.maxAmmo || 0,
    };
  };

  const cloneUnit = (unit) => ({ ...unit });

  const setHint = (message) => {
    state.hint = message;
    setText('#sim-hint', message);
  };

  const addSimLog = (tone, message) => {
    state.log.push({
      time: new Date().toISOString().slice(11, 19),
      tone,
      message,
    });
    if (state.log.length > 60) state.log.shift();
  };

  const unitAria = (unit) => {
    const def = UNIT_DEFS[unit.kind];
    if (def.team === 'friendly') {
      return `${def.name} ${unit.id}, ${unit.ammo} of ${unit.maxAmmo} rounds`;
    }
    return `${def.name} ${unit.id}, ${unit.hp} of ${unit.maxHp} health`;
  };

  const cellAria = (col, row, unit) => {
    const position = `${String.fromCharCode(65 + col)}${row + 1}`;
    if (unit) return `${position}, ${unitAria(unit)}`;
    return state.selected ? `${position}, empty, placement target` : `${position}, empty`;
  };

  const tokenMeter = (unit) => {
    const value = UNIT_DEFS[unit.kind].team === 'enemy' ? unit.hp / unit.maxHp : unit.ammo / unit.maxAmmo;
    return Math.max(0, Math.min(100, Math.round(value * 100)));
  };

  const tokenMarkup = (unit) => {
    const def = UNIT_DEFS[unit.kind];
    return `
      <span class="unit-token team-${def.team} kind-${unit.kind}" data-unit-id="${escapeHtml(unit.id)}" title="${escapeHtml(unitAria(unit))}">
        <span class="unit-badge">${escapeHtml(def.badge)}</span>
        <span class="unit-art">${GLYPHS[unit.kind]}</span>
        <span class="unit-id">${escapeHtml(unit.id)}</span>
        <span class="unit-meter"><i style="width:${tokenMeter(unit)}%"></i></span>
      </span>`;
  };

  function renderPhase() {
    const label = phaseLabel();
    const section = $('#sim');
    if (section) section.dataset.phase = state.phase;

    setText('#sim-state', label);
    setText('#board-state', label);
    setText('#hero-phase', label);

    const elapsed = state.phase === 'running'
      ? (Date.now() - state.startedAt) / 1000
      : (state.result ? state.result.seconds : 0);
    setText('#sim-timer', formatSeconds(elapsed));
    setText('#sim-log-time', formatSeconds(elapsed));
  }

  function renderBoard() {
    const board = $('#sim-board');
    if (!board) return;

    const cells = [];
    for (let row = 0; row < ROWS; row += 1) {
      for (let col = 0; col < COLS; col += 1) {
        const unit = unitAt(col, row);
        const selected = unit && state.selected && state.selected.unitId === unit.id;
        const target = !unit && state.selected;
        const classes = [
          'board-cell',
          unit ? 'has-unit' : '',
          selected ? 'is-selected' : '',
          target ? 'is-target' : '',
        ].filter(Boolean).join(' ');
        const editable = canEdit();
        const attrs = [
          `class="${classes}"`,
          'type="button"',
          'role="gridcell"',
          `data-col="${col}"`,
          `data-row="${row}"`,
          `aria-label="${escapeHtml(cellAria(col, row, unit))}"`,
          unit ? `title="${escapeHtml(unitAria(unit))}"` : '',
          unit ? `aria-selected="${Boolean(selected)}"` : '',
          unit ? `data-unit-id="${escapeHtml(unit.id)}"` : '',
          unit && editable ? 'draggable="true"' : '',
          editable ? '' : 'disabled',
        ].filter(Boolean).join(' ');

        cells.push(`<button ${attrs}>${unit ? tokenMarkup(unit) : ''}</button>`);
      }
    }

    board.innerHTML = cells.join('');
    board.dataset.phase = state.phase;
    board.setAttribute('aria-busy', String(state.phase === 'running'));

    const empty = $('#board-empty');
    if (empty) empty.hidden = state.units.length > 0;
  }

  function renderTray() {
    const root = $('#sim-tray');
    if (!root) return;

    const editable = canEdit();
    const groups = [
      { label: 'FRIENDLY', kinds: ['defender', 'cache'] },
      { label: 'HOSTILE', kinds: ['raider', 'drone', 'armor'] },
    ];

    root.innerHTML = groups.map((group) => {
      const tokens = group.kinds.map((kind) => {
        const def = UNIT_DEFS[kind];
        const count = available(kind);
        const selected = state.selected && state.selected.kind === kind;
        const disabled = !editable || count <= 0;
        const attrs = [
          'type="button"',
          `class="tray-token${selected ? ' is-selected' : ''}"`,
          `data-kind="${kind}"`,
          `draggable="${!disabled}"`,
          `aria-label="${escapeHtml(`${def.name}, ${def.sub}, ${count} available`)}"`,
          `aria-pressed="${Boolean(selected)}"`,
          disabled ? 'disabled' : '',
        ].filter(Boolean).join(' ');

        return `
          <button ${attrs}>
            <span class="tray-art" data-kind="${kind}">${GLYPHS[kind]}</span>
            <span class="tray-name"><strong>${escapeHtml(def.name)}</strong><small>${escapeHtml(def.sub)}</small></span>
            <span class="tray-qty">×${count}</span>
          </button>`;
      }).join('');

      return `<div class="tray-group"><span class="tray-group-label">${group.label}</span>${tokens}</div>`;
    }).join('');

    const total = Object.keys(DEFAULT_LOADOUT).reduce((sum, kind) => sum + available(kind), 0);
    setText('#tray-count', `${total} in tray`);
  }

  function renderLoadout() {
    Object.keys(DEFAULT_LOADOUT).forEach((kind) => {
      setText(`#count-${kind}`, String(state.loadout[kind]));
      document.querySelectorAll(`[data-count="${kind}"]`).forEach((button) => {
        const next = state.loadout[kind] + Number(button.dataset.delta);
        button.disabled = state.phase === 'running' || next < LIMITS[kind].min || next > LIMITS[kind].max;
      });
    });

    const defenders = getDefenders();
    const enemies = getEnemies();
    const canRun = state.phase === 'debrief'
      ? Boolean(state.initialUnits)
      : defenders.length > 0 && enemies.length > 0;
    const start = $('#sim-start');
    if (start) start.disabled = state.phase === 'running' || !canRun;
    setText('#sim-start-label', state.phase === 'running' ? 'Sim running' : state.phase === 'debrief' ? 'Run again' : 'Run sim');

    const clear = $('#sim-clear');
    const reset = $('#sim-reset');
    if (clear) clear.disabled = state.phase === 'running';
    if (reset) reset.disabled = state.phase === 'running';
    setText('#sim-hint', state.hint || 'Drag a token onto the board, or tap a token then a cell.');
  }

  function renderStats() {
    const defenders = getDefenders();
    const enemies = getEnemies();
    const caches = getCaches();
    const rounds = defenders.reduce((sum, unit) => sum + unit.ammo, 0);
    const cacheRounds = caches.reduce((sum, unit) => sum + unit.ammo, 0);

    setText('#sim-defenders', pad(defenders.length));
    setText('#sim-rounds', String(rounds).padStart(3, '0'));
    setText('#sim-cache-rounds', String(cacheRounds).padStart(3, '0'));
    setText('#sim-threats', pad(enemies.length));
    setText('#hero-defenders', pad(defenders.length));
    setText('#hero-rounds', String(rounds).padStart(3, '0'));
    setText('#hero-hostiles', pad(enemies.length));
  }

  function renderLog() {
    const root = $('#sim-events');
    if (!root) return;

    if (!state.log.length) {
      root.innerHTML = '<p class="empty">No events yet.</p>';
      return;
    }

    root.innerHTML = state.log.slice(-40).reverse().map((entry) => `
      <div class="sim-log-entry tone-${entry.tone}">
        <span class="log-time">${escapeHtml(entry.time)}</span>
        <span class="log-dot" aria-hidden="true"></span>
        <span class="log-message">${escapeHtml(entry.message)}</span>
      </div>
    `).join('');
  }

  function renderResult() {
    const overlay = $('#sim-result');
    if (!overlay) return;

    if (state.phase !== 'debrief' || !state.result) {
      overlay.hidden = true;
      overlay.innerHTML = '';
      return;
    }

    const result = state.result;
    const titles = { victory: 'DEFENSE HOLDS', defeat: 'LINE BREACHED', limit: 'SIM LIMIT' };
    const title = titles[result.outcome] || 'SIM COMPLETE';
    const copy = result.outcome === 'victory'
      ? `${result.defenders} defenders standing · ${result.rounds} 100-pack rounds left · ${result.initialHostiles - result.hostiles} hostiles down.`
      : result.outcome === 'defeat'
        ? `${result.hostiles} hostiles still active · ${result.initialDefenders} defenders committed.`
        : `${result.hostiles} hostiles active · ${result.defenders} defenders standing at the tick limit.`;

    overlay.hidden = false;
    overlay.innerHTML = `
      <div class="result-card">
        <span class="result-kicker">SIM COMPLETE · ${result.ticks} TICKS</span>
        <strong class="result-title outcome-${result.outcome}">${title}</strong>
        <p class="result-copy">${copy}</p>
        <div class="result-actions">
          <button class="scan-btn" type="button" data-action="again">Run again <span aria-hidden="true">→</span></button>
          <button class="ghost-btn" type="button" data-action="new">New setup</button>
        </div>
      </div>`;
  }

  function renderAll() {
    renderPhase();
    renderBoard();
    renderTray();
    renderLoadout();
    renderStats();
    renderLog();
    renderResult();
  }

  function resetDemo() {
    stopSim();
    state.loadout = { ...DEFAULT_LOADOUT };
    state.idSeq = { defender: 0, cache: 0, raider: 0, drone: 0, armor: 0 };
    state.units = DEMO_PLACEMENTS.map(([kind, col, row]) => newUnit(kind, col, row));
    state.selected = null;
    state.dragPayload = null;
    state.phase = 'staged';
    state.result = null;
    state.initialUnits = null;
    state.initialHostiles = 0;
    state.initialDefenders = 0;
    state.tick = 0;
    state.startedAt = 0;
    state.log = [];
    state.hint = 'Drag a token onto the board, or tap a token then a cell.';
    addSimLog('info', 'Demo board staged. Five tokens remain in the tray.');
    renderAll();
  }

  function clearBoard() {
    stopSim();
    state.units = [];
    state.selected = null;
    state.dragPayload = null;
    state.phase = 'prep';
    state.result = null;
    state.initialUnits = null;
    state.initialHostiles = 0;
    state.initialDefenders = 0;
    state.tick = 0;
    state.startedAt = 0;
    state.log = [];
    state.hint = 'Board cleared. Drag defenders, 200 caches, or hostiles from the tray.';
    addSimLog('info', 'New setup ready. All loadout tokens are available.');
    renderAll();
  }

  function placeUnit(kind, col, row) {
    if (!canEdit()) return;
    if (!UNIT_DEFS[kind] || available(kind) <= 0) {
      setHint('No tokens of that type are left in the tray.');
      return;
    }
    if (!isFree(col, row)) {
      setHint('That cell is occupied. Choose an empty cell.');
      return;
    }

    const unit = newUnit(kind, col, row);
    state.units.push(unit);
    state.phase = 'staged';
    state.result = null;
    state.initialUnits = null;
    state.hint = `${UNIT_DEFS[kind].name} ${unit.id} placed. ${available(kind)} left in tray.`;
    if (available(kind) <= 0) state.selected = null;
    renderAll();
  }

  function moveUnit(unitId, col, row) {
    if (!canEdit()) return;
    const unit = state.units.find((candidate) => candidate.id === unitId);
    if (!unit) return;
    if (!isFree(col, row, unit.id)) {
      setHint('That cell is occupied. Choose an empty cell.');
      return;
    }

    unit.col = col;
    unit.row = row;
    state.phase = 'staged';
    state.result = null;
    state.initialUnits = null;
    state.selected = { unitId: unit.id };
    state.hint = `${unit.id} moved. Tap another cell to reposition it, or Delete to remove it.`;
    renderAll();
  }

  function removeUnit(unitId) {
    if (!canEdit()) return;
    const unit = state.units.find((candidate) => candidate.id === unitId);
    if (!unit) return;

    state.units = state.units.filter((candidate) => candidate.id !== unitId);
    if (state.selected && state.selected.unitId === unitId) state.selected = null;
    state.phase = state.units.length ? 'staged' : 'prep';
    state.result = null;
    state.initialUnits = null;
    state.hint = `${unit.id} returned to the tray.`;
    renderAll();
  }

  function adjustCount(kind, delta) {
    if (state.phase === 'running' || !LIMITS[kind]) return;

    const next = Math.max(LIMITS[kind].min, Math.min(LIMITS[kind].max, state.loadout[kind] + delta));
    if (next === state.loadout[kind]) return;

    state.loadout[kind] = next;
    const placed = getUnits(kind);
    if (placed.length > next) {
      const removeIds = new Set(placed.slice(next).map((unit) => unit.id));
      state.units = state.units.filter((unit) => !removeIds.has(unit.id));
    }

    if (state.phase === 'debrief') {
      state.phase = state.units.length ? 'staged' : 'prep';
      state.result = null;
      state.initialUnits = null;
      state.log = [];
      addSimLog('info', `Loadout updated. ${UNIT_DEFS[kind].name} count is ${next}.`);
    }

    state.selected = null;
    state.hint = `${UNIT_DEFS[kind].name} count: ${next}. ${available(kind)} available in tray.`;
    renderAll();
  }

  function startSim() {
    if (state.phase === 'running') return;

    if (state.phase === 'debrief' && state.initialUnits) {
      state.units = state.initialUnits.map(cloneUnit);
    }

    const defenders = getDefenders();
    const enemies = getEnemies();
    if (!defenders.length || !enemies.length) {
      setHint('Stage at least one defender and one hostile first.');
      renderAll();
      return;
    }

    stopSim();
    state.initialUnits = state.units.map(cloneUnit);
    state.initialHostiles = enemies.length;
    state.initialDefenders = defenders.length;
    state.phase = 'running';
    state.tick = 0;
    state.startedAt = Date.now();
    state.result = null;
    state.selected = null;
    state.log = [];
    state.hint = 'Simulation live. Defenders are spending their 100-packs.';
    addSimLog('info', `Sim started: ${defenders.length} defenders, ${getCaches().length} caches, ${enemies.length} hostiles.`);
    renderAll();
    state.timer = setInterval(simTick, 500);
  }

  function stopSim() {
    if (state.timer) clearInterval(state.timer);
    state.timer = null;
  }

  function resupply(defender) {
    const cache = getCaches()
      .filter((candidate) => candidate.ammo > 0 && distance(defender, candidate) <= 3)
      .sort((a, b) => distance(defender, a) - distance(defender, b))[0];
    if (!cache) return;

    const transfer = Math.min(100 - defender.ammo, cache.ammo);
    if (transfer <= 0) return;

    defender.ammo += transfer;
    cache.ammo -= transfer;
    addSimLog('good', `${defender.id} draws ${transfer} rounds from ${cache.id}.`);
  }

  function moveEnemy(enemy, target) {
    const dx = Math.sign(target.col - enemy.col);
    const dy = Math.sign(target.row - enemy.row);
    const options = [];

    if (Math.abs(target.col - enemy.col) >= Math.abs(target.row - enemy.row)) {
      if (dx) options.push([enemy.col + dx, enemy.row]);
      if (dy) options.push([enemy.col, enemy.row + dy]);
    } else {
      if (dy) options.push([enemy.col, enemy.row + dy]);
      if (dx) options.push([enemy.col + dx, enemy.row]);
    }

    for (const [col, row] of options) {
      if (isFree(col, row, enemy.id)) {
        enemy.col = col;
        enemy.row = row;
        return;
      }
    }
  }

  function finishSim(outcome) {
    stopSim();
    const defenders = getDefenders();
    const enemies = getEnemies();
    const rounds = defenders.reduce((sum, unit) => sum + unit.ammo, 0);
    const cacheRounds = getCaches().reduce((sum, unit) => sum + unit.ammo, 0);
    state.phase = 'debrief';
    state.result = {
      outcome,
      ticks: state.tick,
      defenders: defenders.length,
      hostiles: enemies.length,
      initialHostiles: state.initialHostiles,
      initialDefenders: state.initialDefenders,
      rounds,
      cacheRounds,
      seconds: Math.max(1, Math.round((Date.now() - state.startedAt) / 1000)),
    };

    const title = outcome === 'victory' ? 'DEFENSE HOLDS' : outcome === 'defeat' ? 'LINE BREACHED' : 'SIM LIMIT';
    const tone = outcome === 'victory' ? 'good' : outcome === 'defeat' ? 'bad' : 'warn';
    addSimLog(tone, `${title}. ${defenders.length} defenders standing; ${enemies.length} hostiles active.`);
    state.hint = 'Sim complete. Run it again with the same setup, or start a new board.';
    renderAll();
  }

  function simTick() {
    if (state.phase !== 'running') return;
    state.tick += 1;

    for (const defender of getDefenders()) {
      if (!state.units.includes(defender)) continue;
      if (defender.ammo < 80) resupply(defender);
      if (defender.ammo < UNIT_DEFS.defender.ammoCost) continue;

      const target = getEnemies()
        .filter((enemy) => distance(defender, enemy) <= UNIT_DEFS.defender.range)
        .sort((a, b) => distance(defender, a) - distance(defender, b) || a.hp - b.hp)[0];
      if (!target) continue;

      defender.ammo -= UNIT_DEFS.defender.ammoCost;
      target.hp -= UNIT_DEFS.defender.damage;

      if (target.hp <= 0) {
        state.units = state.units.filter((unit) => unit.id !== target.id);
        addSimLog('good', `${defender.id} drops ${target.id}. ${defender.ammo} rounds left in the 100-pack.`);
      }
    }

    for (const enemy of getEnemies()) {
      if (!state.units.includes(enemy)) continue;
      const defenders = getDefenders();
      if (!defenders.length) break;

      const target = defenders.sort((a, b) => distance(enemy, a) - distance(enemy, b))[0];
      const enemyDef = UNIT_DEFS[enemy.kind];

      if (distance(enemy, target) <= enemyDef.range) {
        target.hp -= enemyDef.damage;
        addSimLog('bad', `${enemy.id} hits ${target.id} for ${enemyDef.damage}.`);
        if (target.hp <= 0) {
          state.units = state.units.filter((unit) => unit.id !== target.id);
          addSimLog('bad', `${target.id} is down.`);
        }
      } else if (state.tick % (enemyDef.moveEvery || 1) === 0) {
        moveEnemy(enemy, target);
      }
    }

    if (!getDefenders().length) {
      finishSim('defeat');
      return;
    }
    if (!getEnemies().length) {
      finishSim('victory');
      return;
    }
    if (state.tick >= MAX_TICKS) {
      finishSim('limit');
      return;
    }

    renderAll();
  }

  function handleBoardClick(event) {
    if (!canEdit()) return;
    const cell = event.target.closest('.board-cell');
    if (!cell) return;

    const col = Number(cell.dataset.col);
    const row = Number(cell.dataset.row);
    const unit = unitAt(col, row);

    if (unit) {
      if (state.selected && state.selected.unitId === unit.id) {
        state.selected = null;
        setHint('Selection cleared.');
      } else {
        state.selected = { unitId: unit.id };
        setHint(`Selected ${unit.id}. Tap an empty cell to move it, or press Delete to remove it.`);
      }
      renderAll();
      return;
    }

    if (!state.selected) return;
    if (state.selected.unitId) {
      moveUnit(state.selected.unitId, col, row);
    } else {
      placeUnit(state.selected.kind, col, row);
    }
  }

  function handleTrayClick(event) {
    const token = event.target.closest('.tray-token');
    if (!token || !canEdit()) return;

    const kind = token.dataset.kind;
    if (available(kind) <= 0) return;

    if (state.selected && state.selected.kind === kind) {
      state.selected = null;
      setHint('Selection cleared.');
    } else {
      state.selected = { kind };
      setHint(`Selected ${UNIT_DEFS[kind].name}. Tap an empty cell to place it.`);
    }
    renderAll();
  }

  function handleResultClick(event) {
    const action = event.target.closest('[data-action]');
    if (!action) return;
    if (action.dataset.action === 'again') startSim();
    if (action.dataset.action === 'new') clearBoard();
  }

  function readDragPayload(event) {
    if (state.dragPayload) return state.dragPayload;
    try {
      const raw = event.dataTransfer && event.dataTransfer.getData('application/x-sky-sentinel');
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  }

  function clearDragStyles() {
    document.querySelectorAll('.board-cell.is-drop').forEach((cell) => cell.classList.remove('is-drop'));
    document.body.classList.remove('is-dragging');
    state.dragPayload = null;
  }

  function onDragStart(event) {
    if (!canEdit()) return;
    const target = event.target instanceof Element ? event.target : null;
    if (!target) return;

    const trayToken = target.closest('.tray-token');
    const boardCell = target.closest('.board-cell.has-unit');
    let payload = null;

    if (trayToken) {
      const kind = trayToken.dataset.kind;
      if (available(kind) <= 0) {
        event.preventDefault();
        return;
      }
      payload = { kind };
    } else if (boardCell) {
      payload = { unitId: boardCell.dataset.unitId };
    }

    if (!payload) return;

    state.dragPayload = payload;
    if (event.dataTransfer) {
      event.dataTransfer.effectAllowed = payload.unitId ? 'move' : 'copy';
      event.dataTransfer.setData('application/x-sky-sentinel', JSON.stringify(payload));
      event.dataTransfer.setData('text/plain', payload.unitId || payload.kind);
    }
    document.body.classList.add('is-dragging');
  }

  function onBoardDragOver(event) {
    if (!canEdit() || !state.dragPayload) return;
    event.preventDefault();
    if (event.dataTransfer) {
      event.dataTransfer.dropEffect = state.dragPayload.unitId ? 'move' : 'copy';
    }
    const cell = event.target.closest('.board-cell');
    if (cell) cell.classList.add('is-drop');
  }

  function onBoardDrop(event) {
    if (!canEdit()) return;
    const cell = event.target.closest('.board-cell');
    if (!cell) return;

    event.preventDefault();
    const payload = readDragPayload(event);
    clearDragStyles();
    if (!payload) return;

    const col = Number(cell.dataset.col);
    const row = Number(cell.dataset.row);
    if (payload.unitId) {
      moveUnit(payload.unitId, col, row);
    } else {
      placeUnit(payload.kind, col, row);
    }
  }

  function onTrayDragOver(event) {
    if (!canEdit() || !state.dragPayload || !state.dragPayload.unitId) return;
    event.preventDefault();
    if (event.dataTransfer) event.dataTransfer.dropEffect = 'move';
  }

  function onTrayDrop(event) {
    if (!state.dragPayload || !state.dragPayload.unitId) return;
    event.preventDefault();
    const unitId = state.dragPayload.unitId;
    clearDragStyles();
    removeUnit(unitId);
  }

  function onKeyDown(event) {
    if (event.key === 'Escape' && state.selected) {
      state.selected = null;
      setHint('Selection cleared.');
      renderAll();
      return;
    }

    if ((event.key === 'Delete' || event.key === 'Backspace') && state.selected && state.selected.unitId) {
      const tag = document.activeElement && document.activeElement.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA') return;
      event.preventDefault();
      removeUnit(state.selected.unitId);
    }
  }

  function init() {
    if (!$('#sim-board')) return;

    document.querySelectorAll('[data-icon]').forEach((element) => {
      element.innerHTML = GLYPHS[element.dataset.icon] || '';
    });

    $('#sim-board').addEventListener('click', handleBoardClick);
    $('#sim-tray').addEventListener('click', handleTrayClick);
    $('#sim-start').addEventListener('click', startSim);
    $('#sim-clear').addEventListener('click', clearBoard);
    $('#sim-reset').addEventListener('click', resetDemo);
    $('#sim-result').addEventListener('click', handleResultClick);

    document.querySelectorAll('[data-count]').forEach((button) => {
      button.addEventListener('click', () => adjustCount(button.dataset.count, Number(button.dataset.delta)));
    });

    document.addEventListener('dragstart', onDragStart);
    document.addEventListener('dragend', clearDragStyles);

    const board = $('#sim-board');
    board.addEventListener('dragover', onBoardDragOver);
    board.addEventListener('dragleave', clearDragStyles);
    board.addEventListener('drop', onBoardDrop);

    const tray = $('#sim-tray');
    tray.addEventListener('dragover', onTrayDragOver);
    tray.addEventListener('drop', onTrayDrop);

    document.addEventListener('keydown', onKeyDown);
    resetDemo();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
