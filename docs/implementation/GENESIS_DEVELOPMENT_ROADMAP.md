# Genesis - Development Roadmap

Status: **done**, **partial**, **blocked**, **planned**. Nothing is "done" unless a
check in `GENESIS_TESTING_REPORT.md` exercises it.

## Phase 1 - Inspect HireHumans.si - BLOCKED

No source, no git history, no Node in this workspace. Nothing about the existing
site has been asserted or guessed. Unblock by providing a clone URL plus branch or a
project copy.

## Phase 2 - Genesis modular application - BLOCKED (same cause)

The route map (`/genesis`, `/control`, `/world`, `/population`, `/experiments`,
`/research`) is specified in `GENESIS_API_SPECIFICATION.md`, not built. Nothing in
the existing site was modified, so nothing can have been broken.

## Phase 3 - Backend, database, API - PARTIAL

- Simulation side: **done** (SQLite schema, event/metric/discovery/knowledge log,
  checkpointing with validated identity).
- Observer HTTP API: **planned**, contract written.
- Wiring into the site: **blocked**.

## Phase 4 - Control panel - PARTIAL

Data model that the panel needs (`status`, `population`, `world`, `conservation`,
`events`, `discoveries`, `metrics`, `relationships`) is **done and real** - every
field comes from the running simulation, no placeholders. UI: **blocked**.

## Phase 5 - Physical simulation foundation - DONE for v0.1

Terrain, hydrostatic water, shallow water (local), thermodynamics, vegetation,
rigid bodies, solar clock. 7 physics checks pass with numeric tolerances.

## Phase 6 - 3D world - PLANNED

Needs the site stack. The heightfield (32x32) and water depth arrays are already
exposed in the observer contract; rendering is a client concern.

## Phase 7 - Agent Gateway / information firewall - DONE

Senses and actions are the only channel; a validation check proves a distant water
cell cannot influence perception.

## Phase 8 - Two inhabitant architectures - DONE (v0.1)

Pure recurrent neural and hybrid (neural core + memory + planner + tokens), identical
interface, plus the comparability check. Spiking and connectome-inspired variants are
**planned**.

## Phase 9 - Memory, learning, movement, survival - PARTIAL

Learning, plasticity, forward model, drive-based reward, movement, metabolism, sleep,
death: **done**. Swimming: **not implemented**. Hearing and smell: **not implemented**.
Episodic memory and replay: **hybrid only**.

## Phase 10 - Five-inhabitant experiment - DONE, NEGATIVE

Ran 5 world days in 46 s. All five died of dehydration at day 1.94 with zero drinks,
although wadeable water was 72-315 m away. Recorded in full in
`GENESIS_EMERGENCE_RESEARCH_LOG.md` (E-004). The next run must change one factor at a
time and report distance-to-first-drink, not just survival.

## Phase 11 - Advanced research modules - PLANNED

Bearing-and-beacon alternatives, developmental freezing (R8), curiosity ablation (R2),
knowledge-transfer ablation (R4), symbol learning (R6), connectome-reduced brain (R7).

## Phase 12 - Continuous cloud operation - PLANNED

Design in `GENESIS_SIMULATION_ARCHITECTURE.md` section 5: restart loop, health file,
checkpoint fallback, log rotation, observer process isolation. Requires a host and the
owner's approval; nothing currently runs without the owner's machine.

## Phase 13 - Performance and expansion - MEASURED at n=5

938.9 ticks/s single process, 43,200 ticks in 46.0 s, DB 28.0 MB per 5-day run
(60 checkpoints). No profiling beyond this; no claim of scaling to >5 inhabitants.

## Immediate next actions (in order)

1. Fix the survival baseline: one factor at a time, n>=5 seeds, measured by
   distance-to-first-drink (E-004 hypotheses H1-H4).
2. Add the `planner=False` hybrid ablation so no comparative claim stays ambiguous.
3. Unblock Phase 1 with the repository, then build Phase 3's HTTP layer and Phase 4's
   panel against the existing contract.
4. Add held-out prediction generalisation (R3) before any learning claim is published.
