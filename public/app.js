const $ = (selector) => document.querySelector(selector);

const state = {
  telemetry: null,
  scanBusy: false,
};

let radar;

const escapeHtml = (value) => String(value ?? '').replace(/[&<>"']/g, (char) => ({
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#39;',
}[char]));

function setText(selector, value) {
  const element = $(selector);
  if (element) element.textContent = value;
}

function tickClock() {
  setText('#clock', `${new Date().toISOString().slice(11, 19)} UTC`);
}

async function getJson(path, options = {}) {
  const response = await fetch(path, { cache: 'no-store', ...options });
  if (!response.ok) throw new Error(`${path} returned ${response.status}`);
  return response.json();
}

function renderHealth(health) {
  setText('#api-status', health.ok ? 'ONLINE' : 'DEGRADED');
  setText('#api-version', `v${health.version}`);
}

function renderTracks(tracks = []) {
  const root = $('#tracks');
  if (!root) return;
  setText('#track-count', String(tracks.length).padStart(2, '0'));

  if (!tracks.length) {
    root.innerHTML = '<p class="empty">No tracks in the current sweep.</p>';
    return;
  }

  root.innerHTML = tracks.map((track) => `
    <article class="track">
      <div class="track-top">
        <span class="track-id">${escapeHtml(track.id)}</span>
        <span class="track-class">${escapeHtml(track.kind)}</span>
      </div>
      <div class="track-meta">
        <span>${Number(track.bearing).toFixed(0)}°</span>
        <span>${Number(track.range).toFixed(1)} km</span>
        <span>${Number(track.altitude).toLocaleString('en-US')} ft</span>
      </div>
      <div class="meter" title="Confidence ${Math.round(track.confidence * 100)}%"><span style="width:${Math.round(track.confidence * 100)}%"></span></div>
    </article>
  `).join('');
}

function renderSectors(sectors = []) {
  const root = $('#sectors');
  if (!root) return;

  root.innerHTML = sectors.map((sector) => `
    <div class="sector-row">
      <span class="status-dot ${escapeHtml(sector.status)}"></span>
      <div class="sector-name">
        <strong>${escapeHtml(sector.name)}</strong>
        <span>${escapeHtml(sector.id)} · ${sector.contacts} contact${sector.contacts === 1 ? '' : 's'}</span>
      </div>
      <span class="sector-vis">${Math.round(sector.visibility * 100)}%</span>
    </div>
  `).join('');
}

function renderEvents(events = []) {
  const root = $('#events');
  if (!root) return;

  if (!events.length) {
    root.innerHTML = '<p class="empty">No events recorded.</p>';
    return;
  }

  root.innerHTML = events.map((event) => `
    <div class="event">
      <span class="event-time">${escapeHtml(event.time)}</span>
      <span class="event-level ${escapeHtml(event.level)}">${escapeHtml(event.level)}</span>
      <span class="event-message">${escapeHtml(event.message)}</span>
    </div>
  `).join('');
}

function renderTelemetry(data) {
  state.telemetry = data;
  setText('#posture', data.posture);
  setText('#confidence', `${Math.round(data.confidence * 100)}%`);
  setText('#active-tracks', String(data.activeTracks).padStart(2, '0'));
  setText('#feed-mode', data.mode === 'simulation' ? 'SIMULATED FEED' : 'LIVE FEED');
  setText('#updated-at', `${new Date(data.generatedAt).toISOString().slice(11, 19)} UTC`);
  setText('#radar-state', 'SYNCED');
  renderTracks(data.tracks);
  renderSectors(data.sectors);
  renderEvents(data.events);
  if (radar) radar.setTracks(data.tracks || []);
}

function addEvent(level, message) {
  if (!state.telemetry) state.telemetry = { events: [] };
  const time = new Date().toISOString().slice(11, 19);
  state.telemetry.events = [
    { time, level, message },
    ...(state.telemetry.events || []),
  ].slice(0, 8);
  renderEvents(state.telemetry.events);
}

async function refresh() {
  try {
    const [health, telemetry] = await Promise.all([
      getJson('/api/health'),
      getJson('/api/telemetry'),
    ]);
    renderHealth(health);
    renderTelemetry(telemetry);
  } catch (error) {
    setText('#api-status', 'OFFLINE');
    setText('#radar-state', 'OFFLINE');
    addEvent('alert', `Telemetry unavailable: ${error.message}`);
  }
}

async function runScan() {
  if (state.scanBusy) return;

  const button = $('#scan-btn');
  state.scanBusy = true;
  button.disabled = true;
  button.classList.add('loading');
  setText('#radar-state', 'SWEEPING');
  addEvent('info', 'Manual sweep requested.');

  try {
    const result = await getJson('/api/scan', { method: 'POST' });
    addEvent('info', `Sweep ${result.scan.id}: ${result.scan.summary}`);
    await refresh();
  } catch (error) {
    addEvent('alert', `Sweep failed: ${error.message}`);
    setText('#radar-state', 'OFFLINE');
  } finally {
    state.scanBusy = false;
    button.disabled = false;
    button.classList.remove('loading');
  }
}

class Radar {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.tracks = [];
    this.width = 0;
    this.height = 0;
    this.resize = this.resize.bind(this);
    window.addEventListener('resize', this.resize, { passive: true });
    this.resize();
  }

  setTracks(tracks) {
    this.tracks = tracks;
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    this.canvas.height = Math.max(1, Math.floor(rect.height * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  start() {
    const frame = (time) => {
      this.draw(time);
      requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  }

  draw(time) {
    const { ctx, width: w, height: h } = this;
    if (!w || !h) return;

    ctx.clearRect(0, 0, w, h);
    const cx = w / 2;
    const cy = h / 2;
    const radius = Math.min(w, h) * 0.42;

    const bg = ctx.createRadialGradient(cx, cy, 0, cx, cy, radius);
    bg.addColorStop(0, 'rgba(14, 40, 48, .35)');
    bg.addColorStop(1, 'rgba(4, 10, 16, .05)');
    ctx.fillStyle = bg;
    ctx.beginPath();
    ctx.arc(cx, cy, radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = 'rgba(114, 241, 208, .12)';
    ctx.lineWidth = 1;
    for (let i = 1; i <= 4; i += 1) {
      ctx.beginPath();
      ctx.arc(cx, cy, (radius * i) / 4, 0, Math.PI * 2);
      ctx.stroke();
    }

    ctx.strokeStyle = 'rgba(114, 241, 208, .08)';
    ctx.beginPath();
    ctx.moveTo(cx - radius, cy);
    ctx.lineTo(cx + radius, cy);
    ctx.moveTo(cx, cy - radius);
    ctx.lineTo(cx, cy + radius);
    ctx.stroke();

    const sweep = ((time || 0) / 3800) % (Math.PI * 2) - Math.PI / 2;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.arc(cx, cy, radius, sweep, sweep + 0.65);
    ctx.closePath();
    ctx.fillStyle = 'rgba(114, 241, 208, .07)';
    ctx.fill();
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + Math.cos(sweep) * radius, cy + Math.sin(sweep) * radius);
    ctx.strokeStyle = 'rgba(114, 241, 208, .35)';
    ctx.stroke();

    for (const track of this.tracks) {
      const angle = ((Number(track.bearing) || 0) * Math.PI) / 180 - Math.PI / 2;
      const range = Math.min(Math.max(Number(track.range) || 0, 0), 30) / 30;
      const x = cx + Math.cos(angle) * radius * range;
      const y = cy + Math.sin(angle) * radius * range;
      const pulse = 1 + Math.sin((time || 0) / 430 + range * 8) * 0.18;

      ctx.beginPath();
      ctx.arc(x, y, 4.5 * pulse, 0, Math.PI * 2);
      ctx.fillStyle = '#72f1d0';
      ctx.fill();
      ctx.beginPath();
      ctx.arc(x, y, 10 * pulse, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(114, 241, 208, .22)';
      ctx.stroke();
      ctx.font = '9px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
      ctx.fillStyle = 'rgba(230, 242, 246, .82)';
      ctx.fillText(String(track.id), x + 10, y + 3);
    }

    ctx.beginPath();
    ctx.arc(cx, cy, 2.5, 0, Math.PI * 2);
    ctx.fillStyle = '#f6bd63';
    ctx.fill();
    ctx.font = '8px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
    ctx.fillStyle = 'rgba(142, 166, 178, .7)';
    ctx.fillText('SENTINEL', cx + 8, cy - 8);

    if (!this.tracks.length) {
      ctx.font = '9px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
      ctx.fillStyle = 'rgba(142, 166, 178, .65)';
      ctx.textAlign = 'center';
      ctx.fillText('AWAITING TELEMETRY', cx, cy + radius * 0.58);
      ctx.textAlign = 'start';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  tickClock();
  setInterval(tickClock, 1000);

  const canvas = $('#radar');
  if (canvas) {
    radar = new Radar(canvas);
    radar.start();
  }

  $('#scan-btn').addEventListener('click', runScan);
  refresh();
  setInterval(refresh, 12000);
});
