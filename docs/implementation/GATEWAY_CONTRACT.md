# Genesis Gateway — API contract (v1)

**Status: implemented 2026-11-05.** Task 871 said the contract would be decided when the
Gateway is built; this is that decision. The site shell and its two views are Muse's; this
document covers the feed that fills them, and the local viewer used to verify it.

## 1. What the Gateway is

One read-only HTTP surface over the running world. It serves the local viewer and answers
agents. It never simulates in the browser, and it exposes no write path: observation is
one-way, per the planet design (§5), so nothing in the world can sense a watcher.

Base URL is the machine that runs the simulation (`http://127.0.0.1:8787` locally). No
auth in v1 because it binds to loopback; a public deployment must add auth before it
binds anything else. Do not expose v1 directly to the internet.

## 2. Endpoints

| Method | Path | Returns |
| --- | --- | --- |
| GET | `/api/world` | one complete snapshot (JSON) |
| GET | `/api/stream` | server-sent events, one snapshot per frame (~20 Hz) |
| GET | `/api/health` | `{"ok": true, "tick": <int>}` |
| GET | `/` | the local world viewer (`world/`) |

Every response is `Cache-Control: no-store`. `GET /api/world` is the stable contract;
`/api/stream` is a convenience transport carrying the same object.

## 3. Snapshot schema (v1)

```json
{
  "contract": 1,
  "source": "genesis.soup.pilot.run_pilot on_tick (live)",
  "server_time": 1793925209.12,
  "sim": {
    "tick": 13125,
    "births": 504,
    "turnovers": 14.52,
    "population": 66,
    "max_gen": 17,
    "mean_energy": 1.21,
    "mean_size": 0.967,
    "mean_speed": 0.0867,
    "lineages": 3,
    "cells": [[x, y, size, energy, lineage, speed], ...],
    "nutrient": [0..100, ...256 values, row-major 16x16],
    "size_m": 16.0,
    "wall_time": 1793925209.11
  },
  "sun": {
    "elevation_deg": -67.85,
    "azimuth_deg": 213.7,
    "direction": [-0.209, -0.926, 0.314],
    "is_day": false,
    "latitude_deg": 35.0,
    "longitude_deg": 0.0
  },
  "patches": [{"id": 0, "x": 4.0, "y": 4.0, "radius": 3.0}, ...],
  "viewer": {"latitude_deg": 35.0, "longitude_deg": 0.0, "units": "metres",
             "scale_note": "cells drawn enlarged; positions and counts are the simulation's"},
  "error": null
}
```

### Units and frames

- Positions are metres in the dish frame, `0..16` on both axes, matching
  `genesis.soup.pilot`. The viewer maps `x -> x - 8`, `y -> z - 8`.
- Direction is a unit vector with +y up, +x east, +z south.
- `sun` comes from real solar geometry (`gateway/solar.py`): declination and hour angle
  from the standard low-precision formulae. Latitude 35° and longitude 0° are viewer
  initial conditions, stated in the payload, not measurements of a simulated planet.
- `nutrient` is a coarse 16×16 sample of the real dish field, 0–100.
- `cells` is capped at 400 entries, in simulation order. `population` is the true count,
  so a client can detect the cap (`len(cells) < population`).

### Freshness and failure

- `sim.tick` strictly increases while the feed runs. A client must show the last good
  frame and mark it stale after 3 s without a new one.
- If the simulation thread throws, `error` holds `TypeName: message` and `sim` freezes.
  A frozen tick with an error is not live data.
- No fabricated metrics: every number above is read from the running pilot or computed
  from the clock. The viewer labels the cell-size magnification rather than pretending it
  is to scale.

## 4. What the viewer does with it

`world/` renders the dish as a shallow basin with three nutrient patches and the actual
cells as enlarged motes, first-person (`WASD`, mouse look, `M` for the top-down command
view). Day and night follow `sun.direction`: the directional light, sky gradient, water
specular and stars all use it. The viewer draws only what the payload contains; there are
no trees, huts, animals or towns, because none exist yet.

## 5. Non-goals in v1

- No write path, no control of inhabitants, no observation feedback.
- No per-inhabitant sensory stream yet: the town kernel (`genesis.sim`) is not the live
  subject; the dish is. World View for inhabitants arrives when a live town run exists.
- No authentication, multi-client rooms or history queries. History is the repo's logs and
  checkpoints, not this API.

## 6. Versioning

`contract` is an integer. Additive fields do not bump it; removing or changing the meaning
of a field does. Clients should ignore unknown keys and refuse an unknown major version.

## 7. Running it

```bash
python -m gateway.server 8787     # from the repo root
```

The feed starts one real pilot (seed 20261105, 200 founders, cap 600) and steps it
continuously. It costs roughly one core; the falsifier runs are separate processes and are
not modified by it.
