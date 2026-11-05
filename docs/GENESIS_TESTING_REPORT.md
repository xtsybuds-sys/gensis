# GENESIS_TESTING_REPORT

**Status: Implemented and tested for the simulation kernel (v0.1). Everything
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
| Python | 3.12.10 (stdlib only, no third-party packages) |
| Engine | **none installed** - engine decision pending, see `implementation/ENGINE_DECISION.md` |

## 2. Commands (run from the repo root)

```
python -m unittest discover -s tests -t . -v     -> 18 tests, OK
python -m genesis verify                         -> 16/16 checks passed
python -m genesis run --days 5 --db runs/five-days.sqlite
python -m genesis status --db runs/five-days.sqlite
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

18 tests, all passing. They cover every check above plus SQLite persistence (events,
metrics, checkpoints written and re-readable) and a 900-tick five-inhabitant run.

## 5. Five-day experiment - NEGATIVE RESULT (seed 20261105)

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
`GENESIS_EMERGENCE_RESEARCH_LOG.md` E-004. The world is currently unsurvivable
without water-finding in under two days, so no learning comparison is measurable yet.

## 6. Bugs found by testing (all fixed)

1. `brain.state` list shadowed the `brain.state()` method - crashed on first checkpoint.
2. Health recovered from exactly 0.0, so an inhabitant at zero health could not die.
3. Forward-model LMS update had the wrong sign - prediction MSE grew 0.51 -> 19.3.
4. Action-conditioned prediction was non-stationary - MSE 0.66 -> 13.9; dropped.
5. Resume was not identical: unrestored RNG stream, unpersisted pending decision,
   unpersisted hybrid episode clock.
6. Raw-pickle digest flagged behaviourally irrelevant dict ordering; replaced with a
   canonical JSON digest.

Each was caught by a check with a numeric criterion. None was found by reading code.

## 7. Not tested - do not claim

- No CI, no multi-version or multi-OS matrix.
- No soak test past 5 world days; no memory-growth measurement over 120 h.
- No run above 5 inhabitants; scaling statements are estimates.
- No engine backend, no HTTP API, no dashboard - those layers do not exist yet.
- No generalisation test for the world model (in-distribution only).
- No security testing of an API that has not been built.
- No evidence that learning improves survival, because nothing survived long enough
  for the measurement to mean anything.
