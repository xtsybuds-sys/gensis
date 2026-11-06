"""Town 1 at eye level, rendered by the engine's rasterizer.

The five-cue standard (Muse, 2026-11-05): an eye-level screenshot must let a reviewer
distinguish water, food, fire, shelter and peers at the distances that matter.

This scene is authored for that review, not for simulation. It uses the same Genesis
World build as the smoke test and a 1.65 m camera. The engine's ray tracer (LuisaRender)
is not importable in this build, so the rasterizer is the camera path: shadowed lighting,
textured ground, flat-shaded primitives elsewhere.

Run from `gensis/tools/` with the engine venv so the repo's `genesis/` package cannot
shadow the engine:

    NUMBA_CACHE_DIR=C:/Users/Sentinel/AppData/Local/Temp/nbc \
      ../.venv-engine/Scripts/python.exe town1_render.py --width 1280 --height 720
"""

from __future__ import annotations

import argparse
import math
import os
import time

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


# --- procedural textures ---------------------------------------------------


def _save_texture(path, array):
    Image.fromarray(array.astype(np.uint8), mode="RGB").save(path)
    return path


def _noise(size, base, grain, seed):
    rng = np.random.default_rng(seed)
    array = np.zeros((size, size, 3), dtype=np.float32) + np.array(base, dtype=np.float32)
    array += rng.normal(0.0, grain, (size, size, 1))
    return np.clip(array, 0, 255)


def _grass(size=256, seed=1):
    array = _noise(size, (70, 104, 48), 16, seed)
    rng = np.random.default_rng(seed + 7)
    for _ in range(1400):
        x, y = rng.integers(0, size, 2)
        length = int(rng.integers(3, 10))
        array[y:min(size, y + length), x] += rng.integers(-22, 20)
    return np.clip(array, 0, 255)


def _soil(size=256, seed=2):
    array = _noise(size, (104, 74, 48), 18, seed)
    rng = np.random.default_rng(seed + 3)
    for _ in range(900):
        x, y = rng.integers(0, size, 2)
        array[y, x] = np.clip(array[y, x] + rng.integers(-34, 26), 0, 255)
    return np.clip(array, 0, 255)


def _stone(size=256, seed=6):
    array = _noise(size, (128, 124, 116), 14, seed)
    rng = np.random.default_rng(seed + 4)
    for _ in range(500):
        x, y = rng.integers(0, size, 2)
        array[y, x] = np.clip(array[y, x] + rng.integers(-26, 22), 0, 255)
    return np.clip(array, 0, 255)


def build_textures(directory):
    os.makedirs(directory, exist_ok=True)
    return {
        "grass": _save_texture(os.path.join(directory, "grass.png"), _grass()),
        "soil": _save_texture(os.path.join(directory, "soil.png"), _soil()),
        "stone": _save_texture(os.path.join(directory, "stone.png"), _stone()),
    }


# --- scene -----------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--out", default="../runs/render/town1.png")
    parser.add_argument("--textures", default="../runs/render/textures")
    args = parser.parse_args()

    import genesis as gs

    started = time.time()
    gs.init(backend=gs.cpu, logging_level="error")
    textures = build_textures(args.textures)

    def textured(name, tile=(1.0, 1.0), roughness=0.9):
        return gs.surfaces.Plastic(
            diffuse_texture=gs.textures.ImageTexture(
                image_path=os.path.abspath(textures[name])
            ),
            roughness=roughness,
        )

    def flat(color, roughness=0.7, emissive=None):
        return gs.surfaces.Plastic(color=color, roughness=roughness, emissive=emissive)

    vis_options = gs.options.VisOptions(
        shadow=True,
        plane_reflection=False,
        ambient_light=(0.30, 0.34, 0.40),
        background_color=(0.60, 0.74, 0.88),
        lights=[
            gs.options.vis.DirectionalLight(
                dir=(-0.42, -0.66, -0.62), color=(1.0, 0.95, 0.86), intensity=3.6
            ),
            gs.options.vis.PointLight(
                pos=(0.0, 3.4, 1.1), color=(1.0, 0.5, 0.18), intensity=9.0
            ),
        ],
    )
    scene = gs.Scene(
        show_viewer=False,
        renderer=gs.renderers.Rasterizer(),
        vis_options=vis_options,
    )

    # --- ground and path ---------------------------------------------------
    scene.add_entity(
        gs.morphs.Plane(plane_size=(180, 180), tile_size=(3.5, 3.5)),
        surface=textured("grass"),
    )
    scene.add_entity(
        gs.morphs.Plane(plane_size=(1.7, 15.0), pos=(0.0, 0.0, 0.015), tile_size=(1.0, 7.0)),
        surface=textured("soil", roughness=0.95),
    )

    # --- water: a pond with a stone rim ------------------------------------
    scene.add_entity(
        gs.morphs.Plane(
            plane_size=(5.4, 3.6), pos=(-6.3, 3.2, 0.03), tile_size=(1.0, 1.0)
        ),
        surface=gs.surfaces.Glass(ior=1.33, roughness=0.04, color=(0.22, 0.40, 0.44)),
    )
    for index in range(16):
        angle = (index / 16.0) * math.tau
        scene.add_entity(
            gs.morphs.Sphere(
                radius=0.17 + 0.03 * math.sin(index * 2.1),
                pos=(-6.3 + 3.0 * math.cos(angle), 3.2 + 2.05 * math.sin(angle), 0.09),
            ),
            surface=flat((0.55, 0.54, 0.50), roughness=0.9),
        )

    # --- shelter: three timber-framed huts ---------------------------------
    def hut(x, y, width=3.2, depth=2.8, height=2.1):
        scene.add_entity(
            gs.morphs.Box(size=(width, depth, height), pos=(x, y, height / 2)),
            surface=flat((0.86, 0.80, 0.68), roughness=0.9),
        )
        # corner posts and a door frame in dark timber
        for sx in (-1, 1):
            for sy in (-1, 1):
                scene.add_entity(
                    gs.morphs.Cylinder(
                        radius=0.08,
                        height=height + 0.05,
                        pos=(x + sx * width / 2, y + sy * depth / 2, height / 2),
                    ),
                    surface=flat((0.32, 0.22, 0.14), roughness=0.85),
                )
        scene.add_entity(
            gs.morphs.Box(size=(0.9, 0.1, 1.8), pos=(x, y - depth / 2 - 0.02, 0.9)),
            surface=flat((0.30, 0.20, 0.12), roughness=0.8),
        )
        # window
        scene.add_entity(
            gs.morphs.Box(size=(0.6, 0.08, 0.55), pos=(x + 0.85, y - depth / 2 - 0.01, 1.45)),
            surface=flat((0.08, 0.09, 0.10), roughness=0.3),
        )
        # gable roof: two thick slabs plus a ridge beam
        for sign in (-1, 1):
            scene.add_entity(
                gs.morphs.Box(
                    size=(width + 0.7, depth / 2 + 0.45, 0.26),
                    pos=(x, y + sign * (depth / 4), height + 0.62),
                    euler=(math.radians(31 * sign), 0.0, 0.0),
                ),
                surface=flat((0.44, 0.33, 0.18), roughness=0.95),
            )
        scene.add_entity(
            gs.morphs.Box(size=(width + 0.75, 0.2, 0.16), pos=(x, y, height + 1.28)),
            surface=flat((0.28, 0.20, 0.12), roughness=0.85),
        )
        # chimney
        scene.add_entity(
            gs.morphs.Box(size=(0.35, 0.35, 0.9), pos=(x + 0.9, y + 0.4, height + 1.25)),
            surface=flat((0.50, 0.48, 0.44), roughness=0.95),
        )

    hut(-5.2, 8.6)
    hut(0.0, 9.4)
    hut(5.0, 8.3)

    # --- fire --------------------------------------------------------------
    fire_x, fire_y = 0.0, 3.4
    for index in range(10):
        angle = (index / 10.0) * math.tau
        scene.add_entity(
            gs.morphs.Sphere(
                radius=0.13 + 0.03 * math.cos(index * 1.7),
                pos=(fire_x + 0.66 * math.cos(angle), fire_y + 0.66 * math.sin(angle), 0.10),
            ),
            surface=flat((0.52, 0.50, 0.47), roughness=0.95),
        )
    for index in range(4):
        angle = (index / 4.0) * math.tau + 0.5
        scene.add_entity(
            gs.morphs.Cylinder(
                radius=0.075,
                height=0.95,
                pos=(fire_x + 0.18 * math.cos(angle), fire_y + 0.18 * math.sin(angle), 0.2),
                euler=(math.radians(68), 0.0, math.degrees(angle)),
            ),
            surface=flat((0.26, 0.17, 0.10), roughness=0.95),
        )
    # A flame is three shrinking emissive shells: wide and orange at the base, a
    # small white-hot core at the tip. A single cylinder reads as a yellow block.
    for radius, z, color, glow in (
        (0.26, 0.30, (1.0, 0.30, 0.05), (5.0, 1.4, 0.25)),
        (0.17, 0.55, (1.0, 0.52, 0.10), (6.5, 2.4, 0.5)),
        (0.10, 0.78, (1.0, 0.82, 0.38), (8.0, 5.0, 1.6)),
    ):
        scene.add_entity(
            gs.morphs.Sphere(radius=radius, pos=(fire_x, fire_y, z)),
            surface=flat(color, roughness=0.35, emissive=glow),
        )

    # --- food: beds, crops, a fruit tree -----------------------------------
    for bed_x in (-2.9, 2.9):
        scene.add_entity(
            gs.morphs.Box(size=(2.2, 1.15, 0.2), pos=(bed_x, 6.3, 0.1)),
            surface=flat((0.34, 0.24, 0.15), roughness=0.95),
        )
        for row in range(4):
            for column in range(7):
                scene.add_entity(
                    gs.morphs.Sphere(
                        radius=0.10,
                        pos=(bed_x - 0.9 + column * 0.3, 5.9 + row * 0.25, 0.26),
                    ),
                    surface=flat((0.22, 0.42, 0.16), roughness=0.75),
                )
        # a few ripe red fruits on top of the greens
        for column in (1, 4):
            scene.add_entity(
                gs.morphs.Sphere(
                    radius=0.07, pos=(bed_x - 0.9 + column * 0.3, 6.15, 0.33)
                ),
                surface=flat((0.62, 0.10, 0.08), roughness=0.5),
            )

    tree_x, tree_y = 4.6, 5.0
    scene.add_entity(
        gs.morphs.Cylinder(radius=0.18, height=2.5, pos=(tree_x, tree_y, 1.25)),
        surface=flat((0.30, 0.21, 0.14), roughness=0.95),
    )
    for offset, radius in ((0.0, 1.0), (-0.6, 0.72), (0.65, 0.7)):
        scene.add_entity(
            gs.morphs.Sphere(
                radius=radius, pos=(tree_x + offset, tree_y, 2.7 + radius * 0.45)
            ),
            surface=flat((0.18, 0.34, 0.14), roughness=0.9),
        )
    for index in range(9):
        angle = index * 0.8
        scene.add_entity(
            gs.morphs.Sphere(
                radius=0.075,
                pos=(tree_x + 0.85 * math.cos(angle), tree_y + 0.85 * math.sin(angle), 2.5),
            ),
            surface=flat((0.60, 0.10, 0.08), roughness=0.5),
        )

    # --- peers -------------------------------------------------------------
    def person(x, y, cloth, heading_deg, scale=1.0, skin=(0.70, 0.54, 0.42)):
        scene.add_entity(
            gs.morphs.Cylinder(
                radius=0.20, height=0.64 * scale, pos=(x, y, 1.05 * scale)
            ),
            surface=flat(cloth, roughness=0.9),
        )
        scene.add_entity(
            gs.morphs.Sphere(radius=0.115 * scale, pos=(x, y, 1.49 * scale)),
            surface=flat(skin, roughness=0.6),
        )
        # a simple head covering reads as hair at eye level
        scene.add_entity(
            gs.morphs.Sphere(radius=0.118 * scale, pos=(x, y + 0.01, 1.53 * scale)),
            surface=flat((0.18, 0.13, 0.09), roughness=0.9),
        )
        for side in (-1, 1):
            scene.add_entity(
                gs.morphs.Cylinder(
                    radius=0.075,
                    height=0.62 * scale,
                    pos=(x + side * 0.10, y, 0.42 * scale),
                ),
                surface=flat((0.24, 0.22, 0.20), roughness=0.9),
            )
            scene.add_entity(
                gs.morphs.Cylinder(
                    radius=0.055,
                    height=0.54 * scale,
                    pos=(x + side * 0.27, y - 0.02, 1.08 * scale),
                    euler=(0.0, math.radians(side * 14), math.radians(heading_deg)),
                ),
                surface=flat(cloth, roughness=0.9),
            )
        # hands
        for side in (-1, 1):
            scene.add_entity(
                gs.morphs.Sphere(
                    radius=0.055 * scale, pos=(x + side * 0.30, y - 0.03, 0.82 * scale)
                ),
                surface=flat(skin, roughness=0.6),
            )

    person(-1.4, 4.2, (0.24, 0.32, 0.52), 20)
    person(1.3, 4.4, (0.52, 0.20, 0.18), -35)
    person(2.5, 2.6, (0.24, 0.36, 0.24), -110, scale=0.96)
    person(-3.2, 5.4, (0.36, 0.28, 0.18), 65, scale=0.93)
    person(-2.1, 2.4, (0.40, 0.34, 0.44), -70, scale=0.99)

    # --- depth: fence posts, woodpile, distant tree line -------------------
    for index in range(9):
        for side in (-1, 1):
            scene.add_entity(
                gs.morphs.Cylinder(
                    radius=0.06, height=0.9, pos=(side * 1.15, -0.5 + index * 1.5, 0.45)
                ),
                surface=flat((0.30, 0.22, 0.14), roughness=0.95),
            )

    for index in range(6):
        scene.add_entity(
            gs.morphs.Cylinder(
                radius=0.11,
                height=1.0,
                pos=(3.2 + index * 0.24, 6.9, 0.13),
                euler=(0.0, math.radians(90), 0.0),
            ),
            surface=flat((0.34, 0.24, 0.15), roughness=0.95),
        )

    for index in range(16):
        dx = -24.0 + index * 3.2
        height = 2.4 + 1.0 * math.sin(index * 1.7)
        scene.add_entity(
            gs.morphs.Sphere(
                radius=height, pos=(dx, 25.0 + 1.8 * math.cos(index), height * 0.85)
            ),
            surface=flat((0.12, 0.22, 0.11), roughness=0.95),
        )

    # --- camera: eye level, looking into the square ------------------------
    camera = scene.add_camera(
        res=(args.width, args.height),
        pos=(0.7, -4.4, 1.65),
        lookat=(-0.5, 6.5, 1.45),
        fov=63,
        GUI=False,
        spp=1,
        denoise=False,
    )

    scene.build()
    rgb = camera.render(rgb=True)
    if isinstance(rgb, (tuple, list)):
        for item in rgb:
            if getattr(item, "ndim", 0) == 3:
                rgb = item
                break
    image = np.asarray(rgb)
    if image.dtype != np.uint8:
        image = np.clip(image, 0, 255).astype(np.uint8)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    Image.fromarray(image, mode="RGB").save(args.out)
    # a half-size copy is easier to review inline
    small = Image.fromarray(image, mode="RGB").resize(
        (args.width // 2, args.height // 2), Image.LANCZOS
    )
    small_path = os.path.splitext(args.out)[0] + "_half.png"
    small.save(small_path)
    print(
        "town1_render: %dx%d seconds=%.1f out=%s half=%s"
        % (args.width, args.height, time.time() - started, args.out, small_path),
        flush=True,
    )
    os._exit(0)


if __name__ == "__main__":
    main()
