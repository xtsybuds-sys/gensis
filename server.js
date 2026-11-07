import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { dirname, extname, join, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PUBLIC_DIR = resolve(__dirname, 'public');
const PORT = Number(process.env.PORT || 3000);
const HOST = process.env.HOST || '127.0.0.1';
const STARTED_AT = Date.now();

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
};

const SECURITY_HEADERS = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
  'Content-Security-Policy': "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'self'",
};

const SECTORS = [
  { id: 'N-01', name: 'North Ridge', status: 'clear', contacts: 0, visibility: 0.96 },
  { id: 'NE-02', name: 'Harbor Approach', status: 'watch', contacts: 2, visibility: 0.88 },
  { id: 'E-03', name: 'East Corridor', status: 'clear', contacts: 0, visibility: 0.93 },
  { id: 'S-04', name: 'South Basin', status: 'attention', contacts: 1, visibility: 0.71 },
  { id: 'W-05', name: 'West Shelf', status: 'clear', contacts: 0, visibility: 0.9 },
  { id: 'C-06', name: 'Central Field', status: 'watch', contacts: 1, visibility: 0.84 },
];

const TRACKS = [
  { id: 'TRK-042', kind: 'aircraft', bearing: 42, range: 18.4, altitude: 10400, speed: 212, confidence: 0.93, status: 'tracking' },
  { id: 'TRK-118', kind: 'drone', bearing: 118, range: 9.6, altitude: 420, speed: 38, confidence: 0.81, status: 'tracking' },
  { id: 'TRK-271', kind: 'unknown', bearing: 271, range: 24.2, altitude: 3100, speed: 96, confidence: 0.64, status: 'watch' },
];

const EVENTS = [
  { time: '12:04:18', level: 'info', message: 'Sector sweep completed; 3 tracks correlated.' },
  { time: '12:03:51', level: 'watch', message: 'Track TRK-271 entered the western boundary.' },
  { time: '12:02:07', level: 'info', message: 'Weather ceiling stable at 4,800 m.' },
  { time: '12:00:00', level: 'info', message: 'Sentinel simulation resumed from checkpoint.' },
];

function sendJson(res, status, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(status, {
    ...SECURITY_HEADERS,
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(body),
    'Cache-Control': 'no-store',
  });
  res.end(body);
}

function buildTelemetry() {
  return {
    mode: 'simulation',
    generatedAt: new Date().toISOString(),
    posture: 'WATCH',
    confidence: 0.87,
    activeTracks: TRACKS.length,
    sectors: SECTORS,
    tracks: TRACKS,
    events: EVENTS,
  };
}

function runScan() {
  return {
    id: `SCAN-${Date.now().toString(36).toUpperCase()}`,
    mode: 'simulation',
    startedAt: new Date().toISOString(),
    durationMs: 900,
    summary: 'Simulated sweep complete. No live sensor feed is connected.',
    findings: TRACKS.map((track) => ({
      trackId: track.id,
      kind: track.kind,
      confidence: track.confidence,
    })),
  };
}

async function serveStatic(res, pathname) {
  let decoded;
  try {
    decoded = decodeURIComponent(pathname);
  } catch {
    res.writeHead(400, SECURITY_HEADERS);
    res.end('Bad request');
    return;
  }

  const requested = decoded === '/' ? '/index.html' : decoded;
  const filePath = resolve(PUBLIC_DIR, `.${requested}`);
  if (!filePath.startsWith(`${PUBLIC_DIR}${sep}`)) {
    res.writeHead(403, SECURITY_HEADERS);
    res.end('Forbidden');
    return;
  }

  try {
    const info = await stat(filePath);
    if (!info.isFile()) throw new Error('Not a file');
    const body = await readFile(filePath);
    res.writeHead(200, {
      ...SECURITY_HEADERS,
      'Content-Type': MIME[extname(filePath).toLowerCase()] || 'application/octet-stream',
      'Content-Length': body.length,
      'Cache-Control': 'no-cache',
    });
    res.end(body);
  } catch {
    const fallback = await readFile(join(PUBLIC_DIR, 'index.html'));
    res.writeHead(200, {
      ...SECURITY_HEADERS,
      'Content-Type': MIME['.html'],
      'Content-Length': fallback.length,
      'Cache-Control': 'no-cache',
    });
    res.end(fallback);
  }
}

const server = createServer(async (req, res) => {
  if (!req.url) {
    sendJson(res, 400, { error: 'Missing URL' });
    return;
  }

  let url;
  try {
    url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  } catch {
    sendJson(res, 400, { error: 'Invalid URL' });
    return;
  }

  if (url.pathname === '/api/health') {
    if (req.method !== 'GET') return sendJson(res, 405, { error: 'Method not allowed' });
    return sendJson(res, 200, {
      ok: true,
      service: 'sky-sentinel-ai',
      version: '0.2.0',
      mode: 'simulation',
      uptimeSeconds: Math.round((Date.now() - STARTED_AT) / 1000),
    });
  }

  if (url.pathname === '/api/telemetry') {
    if (req.method !== 'GET') return sendJson(res, 405, { error: 'Method not allowed' });
    return sendJson(res, 200, buildTelemetry());
  }

  if (url.pathname === '/api/scan') {
    if (req.method !== 'POST') return sendJson(res, 405, { error: 'Method not allowed' });
    return sendJson(res, 200, { ok: true, scan: runScan() });
  }

  if (url.pathname.startsWith('/api/')) {
    return sendJson(res, 404, { error: 'Unknown API route' });
  }

  if (req.method !== 'GET') {
    return sendJson(res, 405, { error: 'Method not allowed' });
  }

  try {
    return await serveStatic(res, url.pathname);
  } catch (error) {
    console.error(error);
    return sendJson(res, 500, { error: 'Internal server error' });
  }
});

server.listen(PORT, HOST, () => {
  console.log(`Sky Sentinel AI listening on http://${HOST}:${PORT} (simulation mode)`);
});
