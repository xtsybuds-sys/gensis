"""Feasibility probe: does Genesis World build and step a scene on this host?

Run with the engine venv:
    .venv-engine/Scripts/python.exe tools/engine_smoke.py

It is deliberately tiny: one plane, one falling box, 200 steps. If the box comes
to rest at half its height above the plane this reports a working rigid-body
step, which is the minimum bar for using the engine as the physics backend.
"""

from __future__ import annotations

import time


def main():
    import genesis as gs

    gs.init(backend=gs.cpu, logging_level="error")
    scene = gs.Scene(show_viewer=False)
    scene.add_entity(gs.morphs.Plane())
    box = scene.add_entity(gs.morphs.Box(size=(0.5, 0.5, 0.5), pos=(0.0, 0.0, 3.0)))
    scene.build()

    steps = 200
    started = time.time()
    for _ in range(steps):
        scene.step()
    elapsed = max(time.time() - started, 1e-9)
    height = float(box.get_pos()[2])
    print(
        "engine=cpu steps=%d seconds=%.3f fps=%.1f rest_z=%.4f expected=0.2500"
        % (steps, elapsed, steps / elapsed, height)
    )
    print("settled=%s" % (abs(height - 0.25) < 0.02))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - probe reports, never masks
        print("ENGINE_SMOKE_FAILED: %s: %s" % (type(exc).__name__, exc))
