# GENESIS_TESTING_REPORT

**Status: Implemented and tested for the simulation kernel (v0.5, house floor +
planner cut + one mind). Everything downstream of the kernel - HTTP API, dashboard,
engine backend - is Planned or Blocked, and is not claimed here. The unaware start
now holds at spawn (33.7 m minimum house separation against a 15 m peer range) and
every inhabitant runs the same hybrid, but the pre-stated bar is still not met: the
random control had zero deaths in all five seeds (section 15).**

**Human-scale numbers, parked:** the cells-first decision (Muse, 2026-11-05) pauses
this calibration. Sections 13-15 describe the human-scale kernel and resume in Phase 9;
the immediate next step is the primordial-soup pilot design, awaiting Muse's review.

Maintained by Freebuff. Every number below came from a command run on 2026-11-05.
Nothing is marked complete because code was written; each row names the check that
exercises it.

## 1. Environment

| Item | Value |
| --- | --- |
| OS | Windows 11 Education, build 26200 |
| CPU / RAM | 4 logical cores / 15.7 GB |
| GPU | Intel Iris Xe, 2 GB VRAM, no CUDA (no NVIDIA driver present) |
| Python | 3.12.10 (kernel is stdlib only, no third-party packages) |
| Engine | **not installed, not used** - `genesis-world` was still installing into `.venv-engine` when this report was written, and nothing in it comes from the engine |

## 2. Commands (run from the repo root)

```
python -m unittest discover -s tests -t . -v     -> 37 tests, OK
python -m genesis verify                         -> 22/22 checks passed
python -m genesis run --days 5 --db runs/five-days.sqlite
python -m genesis status --db runs/five-days.sqlite
python -m genesis calibrate --seeds 3 --days 5 --arms population,no_planner,random \
    --out runs/calibration-5day.json
python -m genesis calibrate --seeds 5 --days 5 --arms population,no_planner,random \
    --grid 32 --population 5 --world 128 --out runs/calibration-128m-5seed.json
python -m genesis calibrate --seeds 2 --days 2 --arms population,no_sleep \
    --grid 32 --population 5 --world 128 --out runs/diagnostic-sleep.json
python -m genesis calibrate --seeds 5 --days 5 --arms population,no_planner,random \
    --grid 32 --population 5 --world 128 --out runs/calibration-v4-sleep15m.json
python -m genesis calibrate --seeds 5 --days 5 --arms population,planner,random \
    --grid 32 --population 5 --world 128 --out runs/calibration-v5-town.json
PYTHONPATH=. python tools/repro_diagnostic.py    -> reproduction gate diagnosis
.venv-engine/Scripts/python.exe tools/engine_smoke.py   -> engine probe (see 8)
```

## 3. Validation suite

| Check | Result | Measured |
| --- | --- | --- |
| architecture/two-inhabitant-architectures | PASS | neural + hybrid only |
| physics/water-mass-conservation | PASS | drift 0 m^3 over 60 sweeps |
| physics/shallow-water-mass-and-flow | PASS | 32 -> 32 m^3; peak 2.0 -> 0.259 m; corner wetted 0.172 m |
| physics/thermal-diffusion-conservation | PASS | drift 9.09e-13; heat reached the centre |
| physics/thermal-energy-ledger | PASS | residual 0; radiated 243; capacity change 1150 booked |
| physics/free-fall-analytic | PASS | error 1.42e-14 m after 2 s |
| physics/ballistic-energy-drift | PASS | 2.31e-16 relative over 1.5 s |
| physics/restitution-apex | PASS | apex 1.80 m vs 1.80 m, 0.07% error |
| integration/determinism | PASS | two worlds, same seed, identical digest at 60 ticks |
| integration/checkpoint-resume-identity | PASS | identical digest after resume at tick 40 |
| integration/five-separate-houses | PASS | 5 distinct sites on land, min separation 33.7 m at a 128 m world (>= 10% of world) |
| intelligence/forward-model-learning | PASS | MSE 0.401 -> 0.0631 (84.3%) with the 28-dim input |
| intelligence/architectures-comparable | PASS | same 28-dim input, both 6 bounded outputs |
| intelligence/sensory-firewall | PASS | 136 m cell change invisible; 40 m ray cap |
| biology/permanent-death-recorded | PASS | dies once, stays dead, event logged |
| social/knowledge-transfer | PASS | token + place copied between hybrid brains |
| intelligence/conspecific-channel | PASS | peer at 10 m: proximity 0.917, bearing sin 1.0 / cos 0.0; alone 0.0 |
| biology/social-drive-homeostatic | PASS | isolation 0.312 after 10 h alone, 0.0 after 4 h with a peer |
| intelligence/dense-shaping-attribution | PASS | drink reward 1.03, no-change reward -0.17 |
| environment/lives-start-at-dawn | PASS | clock `day 1 06:00`, light 0.091 |
| environment/reachability-measured-per-world | PASS | 128 m world, 7 wadeable cells, 15.1-76.9 m per house |

## 4. Unit / integration tests

31 tests, all passing. The original 18 cover every check above plus SQLite
persistence (events, metrics, checkpoints written and re-readable) and a 900-tick
five-inhabitant run. The 13 added tests cover genomes (bounded mutation over 300
generations, dict round-trip, brain built from genome), reproduction (birth creates
generation 1, population cap blocks it, range gate blocks it, an exhausted parent
cannot breed), dream mode (a sleeping inhabitant takes zero decisions and accrues
replays; an awake one decides), the ablation switches (`planner=False` persists on
the hybrid brain; `BRAIN_KINDS` stays at two and `RandomPolicy` is not one of them),
and the calibration harness output fields.

## 5. Five-day experiment, single seed - NEGATIVE RESULT (seed 20261105, v0.1 kernel)

| Metric | Value |
| --- | --- |
| World | 1.024 km^2 heightfield, 32x32 cells, 5.0 world days = 43,200 ticks |
| Wall clock | 46.0 s, 938.9 ticks/s, 60 checkpoints |
| Survivors | **0 of 5** - all died at tick 16,792 (day 1.94), hydration 0.0 |
| Drinks | **0** |
| Meals | 577 / 100 / 173 / 157 / 176 |
| Distance walked | 12,996 / 27,343 / 1,063 / 17,012 / 10,540 m |
| Food sources | 81 distinct cells |
| Water sources | 0 |
| Encounters | 43 pair-ticks, 3 first contacts, first at day 2 06:23 (21.5 m) |
| Proto-symbols | 42 accumulated, 0 transferred |
| Water conservation | 993,060.69 -> 993,060.69 m^3 (drift 0.0) |
| Thermal ledger | residual 0.0 |

Reachability check (the obvious objection): nearest wadeable water was 71.6 / 163.2
/ 160.0 / 315.2 / 96.0 m from the five houses; 47 wadeable cells, 229 deep cells, max
depth 9.21 m. Water was reachable. The inhabitants never found a shore inside the
~1.9 days their hydration budget allowed.

**Do not read this as a result about intelligence, learning quality, or the two
architectures.** It is a calibration failure, diagnosed in
`GENESIS_EMERGENCE_RESEARCH_LOG.md` E-004.

## 6. Multi-seed calibration - 5 world days, 3 seeds x 3 arms

`python -m genesis calibrate --seeds 3 --days 5 --arms population,no_planner,random
--grid 32 --population 5 --out runs/calibration-5day.json` (artefact checked in as
`runs/calibration-5day.json`, ignored by git; the table is the record).

| arm | seed | survivors | observed days | first death (day) | first drink (day) | births | sleep-skipped |
| --- | --- | --- | --- | --- | --- | --- | --- |
| population | 20261105 | 0 | 2.60 | 1.59 | 0.00 | 0 | 0.936 |
| population | 20261106 | 1 | 5.00 | 1.85 | 0.66 | 0 | 0.512 |
| population | 20261107 | 0 | 2.77 | 1.66 | 1.47 | 0 | 0.977 |
| no_planner | 20261105 | 0 | 2.60 | 1.59 | 0.00 | 0 | 0.936 |
| no_planner | 20261106 | 1 | 5.00 | 1.85 | 0.66 | 0 | 0.512 |
| no_planner | 20261107 | 0 | 2.77 | 1.66 | 1.47 | 0 | 0.935 |
| random | 20261105 | 0 | 4.00 | 1.94 | 0.43 | 0 | 0.986 |
| random | 20261106 | 0 | 4.16 | 1.94 | 0.00 | 0 | 0.984 |
| random | 20261107 | 1 | 5.00 | 1.94 | 0.01 | 0 | 0.983 |

What this actually says:

- Drinking now happens in 7 of 9 runs, first at day 0.00-1.47 (v0.1 recorded 0
  drinks). The change is the genome-driven brain scale and initialisation, not a
  new water-seeking rule; no water-seeking rule was added.
- Survival is still poor: 2 of 9 runs had a survivor at day 5, median first death
  between 1.59 and 1.94 days.
- **The random-policy control outlives the learning arms on two of three seeds**
  (observed 4.00 / 4.16 days vs 2.60 / 2.77). At 5 days and 5 inhabitants, learned
  behaviour is not measurably better than random. This is a negative result and is
  the current calibration blocker.
- `no_planner` is indistinguishable from `population` on seeds 1-2 and differs only
  in the sleep-skip fraction on seed 3. The planner ablation therefore does not yet
  separate anything; E-005 stays open.
- Zero births in every arm at default density - see section 7.

## 7. Reproduction, dream mode, and the density finding

**Gates are reachable.** Diagnostic on seed 20261105, 5 days
(`tools/repro_diagnostic.py`, sampled every 900 ticks): energy gate satisfied in
61.5% of sampled agent-instances, nutrition gate in 53.1%, both together in 38.5%.
So the thresholds are not the blocker.

**Proximity is the blocker.** Zero births occurred because the closest any two
inhabitants ever came was **342.8 m**, against a 12 m reproduction range and a 25 m
encounter range. The 24-dim sensor vector has no channel for other inhabitants, so
agents cannot perceive, and therefore cannot approach, each other. Reproduction is
implemented and exercised by tests, but it is inert at the default world scale.

Density sweep (seed 20261105, 2 days, population 5, 32x32 cells):

| World | Births | Encounters | Closest approach |
| --- | --- | --- | --- |
| 1024 m | 0 | 0 | 342.8 m |
| 512 m | 0 | 0 | 135.4 m |
| 256 m | 0 | 0 | 47.8 m |
| 128 m | 1 | 1802 | 0.5 m |

The 128 m arm reproduces through the CLI:
`python -m genesis calibrate --seeds 2 --days 2 --arms population --world 128`
gives generation 1 born on seed 20261105 (1 birth) and 0 births on 20261106. One
birth in one seed is not a viable population, and no selection claim is made.

**Dream mode.** While asleep an inhabitant takes no sensory sample and no motor
decision; every `dream_every` ticks a memory replay re-fits the forward model. The
measured share of decision slots skipped for sleep is 0.512-0.986 across the nine
runs (the world clock starts at night and night is most of the run). This saves the
decision path only - the physics step still advances at full rate, so wall-clock
savings are a fraction of total step cost, not a discount on the simulation.

## 8. Bugs found by testing (all fixed)

1. `brain.state` list shadowed the `brain.state()` method - crashed on first checkpoint.
2. Health recovered from exactly 0.0, so an inhabitant at zero health could not die.
3. Forward-model LMS update had the wrong sign - prediction MSE grew 0.51 -> 19.3.
4. Action-conditioned prediction was non-stationary - MSE 0.66 -> 13.9; dropped.
5. Resume was not identical: unrestored RNG stream, unpersisted pending decision,
   unpersisted hybrid episode clock.
6. Raw-pickle digest flagged behaviourally irrelevant dict ordering; replaced with a
   canonical JSON digest.
7. `_birth` used `clamp` without importing it - the first reproduction test raised
   `NameError`, so no birth could ever have completed in a real run.
8. Measurement error, not code: `import genesis` in the engine venv "succeeded"
   because the local `genesis/` package shadowed the installed engine. The probe was
   moved to `tools/` (where the repo root is not on `sys.path`) so it can only ever
   report the real engine.

Each was caught by a check with a numeric criterion. None was found by reading code.

## 9. Not tested - do not claim

- No CI, no multi-version or multi-OS matrix.
- No soak test past 5 world days; no memory-growth measurement over 120 h.
- No run above 12 inhabitants; scaling statements are estimates.
- No engine backend: `genesis-world 1.4.5` and `torch 2.15.0+cpu` are installed, but
  `tools/engine_smoke.py` cannot initialise: quadrants (the engine's compiler backend)
  creates its kernel cache at `C:/quadrants_cache/qdcache/kernel_compilation_manager`
  and this account has no write permission at the drive root (`RuntimeError:
  create_directories: Access is denied`). No scene has been built or stepped on this
  host, the Agent Gateway is unbuilt, and no physics number above comes from the engine
  - all of them come from the stdlib kernel.
- No HTTP API, no dashboard - those layers do not exist yet.
- No generalisation test for the world model (in-distribution only).
- No security testing of an API that has not been built.
- No evidence that learning improves survival: a random policy outlives both
  architectures on two of three seeds.
- No evidence of selection: one birth in one seed at a non-default world size.

## 10. Calibration sprint v0.3 - 5 world days, 5 seeds x 3 arms, 128 m world

Changes from Muse's 2026-11-05 decisions (commit `9f67dd0`), all exercised by the
checks above:

- sensor vector 24 -> 28 dims: nearest-peer proximity, peer bearing as cos/sin in the
  inhabitant's own frame, and its own isolation level
- social drive in physiology and wellbeing (rises alone, relieved by a peer, never lethal)
- dense shaping: 12 x d(hydration) + 6 x d(energy) + 4 x d(nutrition)
  + 2.5 x d(sensed water/food proximity) + 1.5 x d(isolation relief)
  - 0.35 x thirst - 0.20 x hunger, clamped to +/-3
- default world 128 m; lives start at 06:00 (dawn); reachability re-derived per world
- `no_sleep` diagnostic arm; harness label fix (ablation rows used to report `population`)

`python -m genesis calibrate --seeds 5 --days 5 --arms population,no_planner,random
--grid 32 --population 5 --world 128 --out runs/calibration-128m-5seed.json`

| arm | seed | survivors | observed days | first death | first drink | births | sightings | planner uses | sleep-skipped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| population | 20261105 | 0 | 2.51 | 1.78 | 0.01 | 0 | 4 | 88 | 0.981 |
| population | 20261106 | 1 | 5.00 | 1.66 | 0.31 | 1 | 13 | 11 | 0.967 |
| population | 20261107 | 0 | 3.08 | 1.66 | 0.01 | 0 | 6 | 80 | 0.985 |
| population | 20261108 | 0 | 2.09 | 1.70 | 0.01 | 0 | 7 | 15 | 0.978 |
| population | 20261109 | 0 | 4.11 | 1.47 | 0.00 | 1 | 6 | 36 | 0.986 |
| no_planner | 20261105 | 1 | 5.00 | 1.78 | 0.01 | 0 | 4 | 0 | 0.985 |
| no_planner | 20261106 | 0 | 3.72 | 1.66 | 0.31 | 1 | 11 | 0 | 0.974 |
| no_planner | 20261107 | 0 | 3.57 | 1.66 | 0.01 | 0 | 6 | 0 | 0.985 |
| no_planner | 20261108 | 1 | 5.00 | 1.70 | 0.01 | 0 | 8 | 0 | 0.719 |
| no_planner | 20261109 | 0 | 4.11 | 1.47 | 0.00 | 1 | 6 | 0 | 0.981 |
| random | 20261105 | 4 | 5.00 | 1.43 | 0.00 | 2 | 14 | 0 | 0.981 |
| random | 20261106 | 2 | 5.00 | 2.41 | 0.00 | 0 | 9 | 0 | 0.976 |
| random | 20261107 | 1 | 5.00 | 1.30 | 0.00 | 1 | 13 | 0 | 0.981 |
| random | 20261108 | 1 | 5.00 | 1.30 | 0.22 | 1 | 14 | 0 | 0.982 |
| random | 20261109 | 2 | 5.00 | 2.98 | 0.00 | 0 | 9 | 0 | 0.976 |

| arm | survivors / 25 | median observed days | median first death | births | sightings | planner uses |
| --- | --- | --- | --- | --- | --- | --- |
| population | 1 | 3.08 | 1.66 | 2 | 36 | 230 |
| no_planner | 2 | 4.11 | 1.66 | 2 | 35 | 0 |
| random | 10 | 5.00 | 1.43 | 4 | 59 | 0 |

What this actually says:

- **The success bar is not met.** Hybrid was to beat random on first-drink day AND
  median survival across >= 5 seeds. First drink is a tie (median 0.01 vs 0.00 day);
  median survival is 3.08 vs 5.00 days; survivors 1/25 vs 10/25. Dense shaping plus a
  perceptible peer did not move the comparison. This stands as measured.
- **The planner acts and still does not separate.** `planner_uses` 230 vs 0 proves the
  ablation is wired and firing, yet survival is 1 vs 2 of 25 - inside 5-seed noise and,
  if anything, backwards. Muse's challenge is unresolved; the planner's steering is not
  earning its place.
- **First sightings happen at spawn.** `first_sighting_day` is 0.0 in every run: at
  128 m the five houses start inside the 40 m peer range, so "inhabitants start unaware
  of each other" is violated at this density. Reproducible social measurement now
  exists, but the start condition needs a decision (section 12).
- **Reproduction works and is not yet self-sustaining:** 8 births across 15 runs, with
  deaths still dominating every arm.
- Reachability at 128 m is real: 7 wadeable cells in the verification world, nearest
  15.1 m from a house, worst 76.9 m; median over the five calibration seeds 16.5 m.

## 11. Sleep diagnostic - 2 world days, 2 seeds (NEGATIVE for the learned arms)

Dawn start did not reduce sleep. The skipped share is still 0.968-0.986, because the
attractor is the rest channel (`rest > 0.45` while `energy < 0.98`), not the clock.
`no_sleep` zeroes action[4] - diagnostic only, no architecture change:

| arm | seed | survivors | first death | sleep-skipped | ticks/s |
| --- | --- | --- | --- | --- | --- |
| population | 20261105 | 3 | 1.78 | 0.981 | 1404 |
| population | 20261106 | 3 | 1.66 | 0.968 | 1450 |
| no_sleep | 20261105 | 6 (1 birth) | none | 0.0 | 652 |
| no_sleep | 20261106 | 5 (1 birth) | 1.78 | 0.0 | 600 |

Zeroing the rest channel doubled 2-day survival and produced the only death-free run,
but at 2.3x the wall-clock cost per tick. Caveat before quoting it: 2 seeds, 2 days,
and the random arm also slept ~98% and still reached 10/25 at 5 days. Sleep is a large
contributor, not the whole cause.

## 12. Limitations added by the calibration sprint

- Peer perception is proximity-only within 40 m, nearest peer only, with no terrain
  occlusion test. It is not vision.
- The "starts unaware" property does not hold at 128 m with 40 m peer range.
- The sleep attractor is unresolved; `no_sleep` is a diagnostic arm, not a biology fix.
- Shaping weights were chosen a priori and were not swept; no claim that they are good,
  only that they are the ones measured.
- Reproduction is demonstrated, not sustained.
- The engine is installed but cannot initialise: its quadrants backend needs write
  access at `C:/quadrants_cache`, which this account lacks. Remains unverified.

## 13. Sleep physiology + 15 m peer range - 5 seeds x 5 days x 3 arms (v0.4)

Changes (Muse decisions 1-3, 2026-11-05): a sleeper now wakes when rested, thirsty
(`hydration <= 0.55`), hungry (`nutrition <= 0.30`) or after a 3 h bout cap, and cannot
start sleeping while thirsty, hungry, or within 30 min of waking; the conspecific range
is 15 m and the social-drive relief radius is aligned to it; the planner steers by a
vector sum of per-ray votes with 3-decision hysteresis instead of one best ray.

Same command as section 10, artefact `runs/calibration-v4-sleep15m.json`.

| arm | survivors | deaths | median observed days | median first death | births | sightings | planner uses | sleep-skipped | ticks/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| population | 20 | 10 | 5.00 | 1.94 | 5 | 60 | 4493 | 0.69 | 846 |
| no_planner | 18 | 12 | 5.00 | 1.94 | 5 | 61 | 0 | 0.64 | 829 |
| random | 32 | 0 | 5.00 | none | 7 | 86 | 0 | 0.84 | 1584 |

Deaths are `population_end - survivors`, because populations now grow through births
and raw survivor counts are not comparable across arms without it.

What changed from section 10:

- Learned arms now survive the run: 1 -> 20 and 2 -> 18 of the created population;
  median observed days 3.08 -> 5.00. This is the largest improvement measured so far,
  and it came from the two fixes Muse approved, not from tuning weights.
- Sleep share fell 0.98 -> 0.69 (population) and 0.64 (no_planner). It is not zero:
  the 3 h bout cap and the rest channel still put them under for most of the day.
- The cost is measured, not estimated: learned arms run 846 ticks/s against 1408 in
  section 10 (1.7x slower), random 1584 against 1929. Awake decision slots are what
  cost compute.
- Reproduction now fires in every arm: 5 / 5 / 7 births against 2 / 2 / 4.
- **The bar is still not met.** The random control had zero deaths in 5 of 5 seeds;
  the learned arms lost 10 and 12 inhabitants. First-drink day remains a tie
  (0.00-0.01 d). The hybrid is much better than it was and is still worse than a
  random walk.
- **The planner still does not separate:** 20 vs 18 survivors, 10 vs 12 deaths, and
  the same first-death median of 1.94 d, with 4493 interventions against 0. Per Muse's
  pre-agreed condition this is a cut, not a tune.
- **The unaware start is still violated, and 15 m did not fix it:** `first_sighting_day`
  is 0.00-0.01 in all 15 runs. The cause is house placement - `_choose_homes` falls back
  through gaps of 35.8, 21.5, 10.7 and 4.3 m at 128 m, so houses can start ~4 m apart.
  The fix belongs in placement (minimum gap above the peer range), not in the sensor.

## 14. Engine: no cache override exists on this install

The quadrants cache path is a hardcoded literal `C:/quadrants_cache/` inside
`quadrants_python.cp312-win_amd64.pyd` (confirmed by reading the binary). The Python
layer exposes no `cache_dir`, and `QD_CACHE_PATH`, `QD_CACHE_DIR`, `QD_LIB_DIR`,
`TI_CACHE_DIR` and `TI_CACHE_PATH` do not move it. `tools/engine_smoke.py` fails at
`gs.init` with `PermissionError: [WinError 5] Access is denied: 'C:/quadrants_cache'`
before any scene is built. The only remaining unblock is a one-time elevated
`mkdir C:\quadrants_cache`. The engine remains unverified and no engine number is
claimed anywhere in this report.

## 15. House floor + planner cut + one mind - 5 seeds x 5 days x 3 arms (v0.5)

Three approved changes: `_choose_homes` now refuses to seat houses below
`max(1.5 * social_range_m, 2 * cell_m)` (22.5 m at 128 m) and records a
`home_gap_shortfall` instead of silently shrinking the gap; `Config.planner` defaults
to `False`, with the `planner` arm retained as the research arm that keeps the cut
falsifiable; every inhabitant is hybrid, so there is no second-class neural tier.

`python -m genesis calibrate --seeds 5 --days 5 --arms population,planner,random --grid 32 --population 5 --world 128 --out runs/calibration-v5-town.json`

| arm | survivors | deaths | median observed | median first death | births | sightings | first sighting | planner uses | sleep-skipped | ticks/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| population (hybrid, planner cut) | 22 | 8 | 5.00 | 2.12 | 5 | 67 | 0.00 | 0 | 0.68 | 664 |
| planner (research arm) | 25 | 5 | 5.00 | 1.83 | 5 | 61 | 0.00 | 12191 | 0.74 | 661 |
| random | 32 | 0 | 5.00 | none | 7 | 86 | 0.00 | 0 | 0.84 | 1620 |

- **The house floor works and is verified:** the population check reports 33.7 m
  minimum separation against a 15 m peer range, with all five inhabitants hybrid. The
  unaware start is true at t=0 for the first time; the earlier 4.3 m fallback is gone.
- **First contact still lands inside day 1** (0.00 d in every run). With a 128 m town
  and walking at roughly 1 m/s the 18-34 m gap closes in seconds, so `first_sighting_day`
  at day resolution cannot distinguish the fixed spawn from the old bug. If first
  contact is meant to be a multi-day event, the town has to be larger; moving houses
  further apart inside 128 m cannot buy it.
- **The cut costs nothing measurable, and the retained research arm does not vindicate
  the planner either.** Without the planner: 22 survivors and 8 deaths, against v4's 20
  and 10 with it, at the same ~660 ticks/s. But in this run the `planner` arm scored 25
  survivors and 5 deaths against the cut population's 22 and 8 - the opposite direction,
  decided by two seeds (one of them 6/6 vs 6/6), and still inside five-seed noise. The
  cut stands on the original falsifier: separation was never demonstrated, in either
  direction. What would reopen it is a steering idea that separates across >=5 seeds,
  not this arm's three-survivor edge.
- **One mind costs compute:** 664 ticks/s against 846 in v4, because all five
  inhabitants now run the hybrid instead of three of five (1.27x slower, measured).
- **The bar remains unmet:** random lost nobody in 5 of 5 seeds while the learned
  population lost 8, and first-drink day is a tie at 0.00 in all three arms.

## 16. Engine: the one-time directory was requested and not granted

With the engine call delegated, the only remaining path still needs an OS permission
this account does not have. The elevated `mkdir C:\quadrants_cache` was submitted
through the desktop approval prompt, was not approved within the timeout, and the
directory does not exist afterwards - so the smoke test has not been re-run and no
engine frame exists. Nothing here claims the engine works. The standing decision is
the honest one: the stdlib kernel remains the source of truth, and the engine is
revisited the moment that folder exists.
