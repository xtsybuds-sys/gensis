# GENESIS_TESTING_REPORT

**Status: Implemented and tested for the simulation kernel (v0.2). Everything
downstream of the kernel - HTTP API, dashboard, engine backend - is Planned or
Blocked, and is not claimed here.**

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
python -m unittest discover -s tests -t . -v     -> 31 tests, OK
python -m genesis verify                         -> 16/16 checks passed
python -m genesis run --days 5 --db runs/five-days.sqlite
python -m genesis status --db runs/five-days.sqlite
python -m genesis calibrate --seeds 3 --days 5 --arms population,no_planner,random \
    --out runs/calibration-5day.json
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
| integration/five-separate-houses | PASS | 5 distinct sites on land, min separation 352 m |
| intelligence/forward-model-learning | PASS | MSE 0.400 -> 0.0135 (96.6%) |
| intelligence/architectures-comparable | PASS | same 24-dim input, both 6 bounded outputs |
| intelligence/sensory-firewall | PASS | 724 m cell change invisible; 40 m ray cap |
| biology/permanent-death-recorded | PASS | dies once, stays dead, event logged |
| social/knowledge-transfer | PASS | token + place copied between hybrid brains |

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
- No engine backend: `genesis-world` did not finish installing during this report,
  `tools/engine_smoke.py` has not yet built or stepped a real scene on this host, and
  the Agent Gateway is unbuilt. No physics number above comes from the engine - all
  of them come from the stdlib kernel.
- No HTTP API, no dashboard - those layers do not exist yet.
- No generalisation test for the world model (in-distribution only).
- No security testing of an API that has not been built.
- No evidence that learning improves survival: a random policy outlives both
  architectures on two of three seeds.
- No evidence of selection: one birth in one seed at a non-default world size.
