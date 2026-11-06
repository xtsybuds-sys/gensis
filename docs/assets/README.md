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
