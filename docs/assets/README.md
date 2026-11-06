# Render assets

These are **renderer tests**, not pictures of the world.

- `town1_eye_level.png`, `town1_eye_level_half.png` — a test of what the engine can draw
  (terrain, water, a fire, timber-framed huts, figures) for a **future** town. No town,
  hut, fire or person exists in the simulation today. These images must not be presented
  as the world, on the site or anywhere else. The photoreal bar is not met: this is a
  rasterizer frame with flat-shaded primitives (report §21).

The world that exists is cells in water. Its live, first-person view is served by the
Gateway at `http://127.0.0.1:8787/` (see `docs/implementation/GATEWAY_CONTRACT.md`) and
is generated from the running pilot, not from an image.

- `world_live_frame.png` — a frame captured from the live viewer at 20:22, showing 63 real
  cells in the dish. It is evidence of the live render, not an illustration; the live
  render itself is the deliverable at `http://127.0.0.1:8787/`.

## Cosmogony frames

- `cosmos_disk.png`, `cosmos_life.png` — frames captured headlessly from the live cosmogony
  viewer (`/`, model in `genesis/cosmos/cosmogony.py`) at tau 0.55 and 0.95. They show the
  reduced model's own output: the disk, its planets, and the water-rich world at 0.3206 that
  first enters the habitable zone. The surface texture on the focus world is procedural
  (renderer-side); the model has water fraction, not geography. These are evidence of the
  live render, not illustrations, and they make no claim about the actual universe.
