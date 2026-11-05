# Genesis - Observer API Specification

Status: **specified, not built.** Nothing in this document is running today. It
exists so the dashboard work can start against a fixed contract once the
HireHumans.si stack is available, and so the simulation and the site stay decoupled.

## 1. Principles

- Read-only. The dashboard can never influence the world; there is no control
  endpoint that mutates simulation state.
- Authenticated. Observer data is private to the owner until deliberately published.
- `Cache-Control: no-store` on every response; no personal data in URLs.
- Snapshot-based: the API serialises the last committed snapshot, never a live
  object, so a slow dashboard cannot stall the tick loop.
- No inhabitant can reach this API; the firewall is structural, not a permission.

## 2. Endpoints

### `GET /api/genesis/status`

```json
{
  "tick": 43200,
  "clock": "day 5 00:00",
  "alive": 5,
  "population": 5,
  "deaths": 0,
  "sleeping": 2,
  "mean_energy": 0.91,
  "mean_hydration": 0.94,
  "mean_nutrition": 0.88,
  "mean_health": 1.0,
  "mean_prediction_error": 0.012,
  "mean_distance_m": 4120.5,
  "encounters": 3,
  "discoveries": 12,
  "water_sources": 8,
  "food_sources": 4,
  "knowledge_links": 5,
  "tokens": 12,
  "water_m3": 8360.0,
  "biomass": 731.4,
  "light": 0.02
}
```

### `GET /api/genesis/population`

Array of `agent.stats()`:
`id, name, alive, brain{kind,label,hidden,synapses,prediction_error,novelty,weight_norm,mean_reward,decisions,...}, pos, heading, energy, hydration, nutrition, health, body_temp, sleeping, age_days, distance_m, drinks, meals, sleep_hours, blocked_ticks, home_cell, died_tick`.

Hybrid brains additionally expose `episodes, tokens, known_places, signals, transfers, replays`.

### `GET /api/genesis/world`

Terrain summary (cells, cell size, min/mean/max height), water volume, biomass,
temperature bounds and mean, light, sun elevation, clock, slow-field update count.
Plus the low-resolution heightfield array for the 3D mesh and the water depth
array. Both are static-size (32 x 32) and cacheable per tick.

### `GET /api/genesis/conservation`

```json
{
  "water_start_m3": 8360.2, "water_now_m3": 8360.2, "water_drift_m3": 0.0,
  "thermal_energy_start": 12288.0, "thermal_energy_now": 12310.4,
  "thermal_energy_expected": 12310.4, "thermal_residual": 0.0
}
```

This is deliberately public to the observer: physics honesty should be visible, not
asserted in a document.

### `GET /api/genesis/events?limit=50`

`[{tick, kind, agent, detail}]`, newest first. Kinds: `spawn, death, encounter,
knowledge_transfer, concept, wake`.

### `GET /api/genesis/discoveries?limit=40`

`[{tick, kind, cell, agent, detail}]` - `water_source` / `food_source` with depth or
biomass at discovery.

### `GET /api/genesis/metrics?limit=120`

The hourly metric series for charts.

### `GET /api/genesis/relationships`

`[{a, b, encounters}]` where `a` and `b` are inhabitant ids.

## 3. Dashboard mapping (once the stack is known)

| Route | Contents |
| --- | --- |
| `/genesis` | status, clock, population strip, conservation banner |
| `/genesis/world` | 3D terrain mesh from heightfield + water plane, agent markers |
| `/genesis/control` | readonly overview + system health (tick rate, checkpoint age) |
| `/genesis/population` | per-inhabitant body gauges, brain panel, memory/token list |
| `/genesis/experiments` | run ledger, seed, config, report JSON |
| `/genesis/research` | this document set and the emergence log, rendered |

## 4. Auth

Reuse whatever HireHumans.si already uses; do not add a second identity system. The
owner is the only observer role for now. The API must reject unauthenticated
requests with 401 and cross-origin mutations do not exist (read-only), so CSRF is
not applicable beyond denying non-GET methods entirely.

## 5. Open questions for the architect

1. Should `/genesis` be public (spectator) or owner-only? That decides whether
   inhabitant names and histories are treated as personal data.
2. Polling at 1 Hz or server-sent events? SSE is a better fit for a persistent
   world and avoids client timers, but adds an endpoint the site must hold open.
3. Where does the heightfield mesh get built - server-side (three.js on the client,
   raw arrays) or precomputed? Raw arrays at 32 x 32 are tiny; send them raw.
