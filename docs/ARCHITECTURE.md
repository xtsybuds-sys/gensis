# Sky Sentinel AI architecture

Status: scaffold, 2026-11-07.

## What runs

- `server.js` is a zero-dependency Node HTTP server.
- `public/` is a static dashboard: HTML, CSS, and browser JavaScript.
- `/api/health`, `/api/telemetry`, and `/api/scan` serve deterministic simulated air data.
- No model, hardware adapter, database, or third-party service is connected.

## Ground-defense sim

The Sim Prep surface is entirely client-side in `public/sim.js`.

```text
loadout steppers
  -> tray counts
  -> drag or tap placement on a 10x7 grid
  -> prep / staged
  -> run: defenders fire, hostiles move and attack
  -> debrief
```

The unit model is intentionally small:

```text
defender: 100-pack, 100 rounds, range 4, spends 8 rounds per burst
200 cache: 200 rounds; tops up a nearby defender below 80 rounds
raider: ground hostile
drone: fast hostile, range 2
armor: heavy hostile, moves every other tick
```

Combat resolution runs in the browser on a 500 ms tick and stops on victory, defeat, or the 24-tick limit. Ammo, health, positions, the current phase, and the event log are in-memory only; reloading the page resets the board to the demo.

This is a sandbox, not a server-authoritative game. If runs become shared, persistent, or competitive, move resolution behind an authenticated server boundary and keep the client as a renderer.

## Request path

```text
browser
  -> static assets from public/
  -> GET /api/telemetry
  -> simulated sector + track state in server.js
  -> dashboard render + canvas radar
```

## Air data contract

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

1. **Sensor boundary** — normalize ADS-B, radar, weather, or camera data into the telemetry contract.
2. **Inference** — add a model only after the normalized data is stable; expose model version and confidence.
3. **Sim authority** — keep the board client-side for previews, or move tick resolution to an authenticated server for shared runs.
4. **Persistence** — store run snapshots and event history before adding shared or replayable simulations.
5. **Access** — authentication and authorization belong at the API boundary, not in the browser.

## Non-goals for this scaffold

- Pretending simulated data is live.
- Shipping a model card for a model that does not exist.
- Treating the browser-side combat result as an authoritative record.
- Building a map or sensor integration before choosing a real data source.

## Review points for Muse

- Is the 100-pack / 200-cache economy readable enough to test different boards?
- Should the next iteration add scenario presets, or keep placement fully manual?
- Does the sim need a server-authoritative tick before any shared use?
