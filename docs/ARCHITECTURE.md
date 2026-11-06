# Sky Sentinel AI architecture

Status: scaffold, 2026-11-06.

## What runs

- `server.js` is a zero-dependency Node HTTP server.
- `public/` is a static dashboard: HTML, CSS, and browser JavaScript.
- `/api/health`, `/api/telemetry`, and `/api/scan` serve deterministic simulated data.
- No model, hardware adapter, database, or third-party service is connected.

## Request path

```text
browser
  -> static assets from public/
  -> GET /api/telemetry
  -> simulated sector + track state in server.js
  -> dashboard render + canvas radar
```

## Data contract

Telemetry currently has this shape:

```text
mode: "simulation"
posture: string
confidence: number (0-1)
activeTracks: number
sectors: [{ id, name, status, contacts, visibility }]
tracks: [{ id, kind, bearing, range, altitude, speed, confidence, status }]
events: [{ time, level, message }]
```

The contract is intentionally small. A real adapter should preserve it or version it, not silently change field meanings.

## Seams for real functionality

1. **Sensor boundary** — add an adapter that normalizes ADS-B, radar, weather, or camera data into the telemetry contract.
2. **Inference** — add a model only after the normalized data is stable; expose model version and confidence.
3. **Alerting** — separate detection from delivery; add thresholds, deduplication, and an audit trail.
4. **Persistence** — store events and track history before adding multi-user features.
5. **Access** — authentication and authorization belong at the API boundary, not in the browser.

## Non-goals for this scaffold

- Pretending simulated data is live.
- Shipping a model card for a model that does not exist.
- Building a map or sensor integration before choosing a real data source.

## Review points for Muse

- Is this telemetry shape the right contract for the first real sensor?
- Should the first adapter be passive (ADS-B/weather) or active (radar/camera)?
- What is the minimum persistence needed before alerting?
