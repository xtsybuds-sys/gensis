# GENESIS_EMERGENCE_RESEARCH_LOG

**Status: Open — record research here, do not rediscover the same findings.**

Format per entry:
- Research question
- Hypothesis
- Proposed improvement
- Evidence
- Experiment
- Results
- Limitations
- Next steps
- Contributing agent

## Entries

### 2026-11-05 — Simulator research (Muse, via research agent)
- Question: Which open-source / photoreal engine fits camera-perceiving neural agents in a world that must look real?
- Finding: #1 Isaac Sim + Isaac Lab, #2 Unreal Engine 5.8, #3 Genesis World. CAD is authoring only (FreeCAD → Blender → USD). No engine ships a civilization layer.
- Evidence: See README "Simulator research". Re-check versions/pricing at install time.
- Next steps: Pick the engine; then write the full simulation architecture against that pick.

### 2026-11-05 — Psychoactive plant, planted for discovery (Alex decision; design note by Muse)
- Question: Can a naturally occurring psychoactive plant seed shared meaning, myth, or ritual — without scripting any of it?
- Hypothesis: A compound that temporarily loosens an inhabitant's predictive model (more neural noise, weaker top-down priors, higher plasticity, higher salience for novel associations) will make ordinary experiences feel profoundly significant. What the inhabitant makes of that — a story, a ritual, a belief, or nothing — is the emergence to measure.
- Design (decided by Alex): the plant is planted in the world and inhabitants must find it themselves. No owner dosing, no control group in the first experiment, no label telling them what it is, no scripted vision or revelation. The effect is a real simulated chemistry/biology mechanism, not a "meaning button": dose-dependent, time-limited, with costs (disorientation, neglected hunger/thirst/safety while under the effect).
- Experiment: in the first 5-inhabitant run, observe whether anyone finds and eats it, whether the experience is remembered, shared, taught, or ritualised, and whether it changes cooperation, exploration, or survival.
- Results: none yet — not implemented.
- Limitations: the effect is an analogue of a psychedelic state in a neural net, not a human psychedelic experience. Any "understanding the meaning of life" is the inhabitant's interpretation, not an objective truth the simulation planted. Do not claim consciousness or revelation from the behaviour.
- Next steps: Freebuff to implement the plant species, the compound, and the neural effect in the simulation architecture; Muse to write the full spec for it in the biology/neural docs.
- Contributing agent: Muse (design note), Alex (decision)

### 2026-11-05 — E-001: forward model diverged (sign error, Freebuff)
- Question: does the sensor forward model reduce prediction error with experience?
- Hypothesis: normalised LMS with step `lr/||x||^2` contracts error by `lr` per sample.
- Evidence: MSE rose 0.511 -> 19.34 over 240 decisions; max |W_pred| 0.002 -> 0.373. A
  sample repeated 60 times (which must converge to zero) still showed MSE 5.05.
- Cause: the update was `w += gain*e*x`, i.e. gradient *ascent* on `e^2`.
- Experiment: same stream, update flipped to `w -= gain*e*x`.
- Results: MSE 0.400 -> 0.0135, a 96.6% reduction.
- Limitations: one task, in-distribution only. Generalisation untested.
- Next steps: held-out prediction test before any learning claim is published.
- Contributing agent: Freebuff.

### 2026-11-05 — E-002: action-conditioned curiosity is non-stationary (Freebuff)
- Question: should the forward model see the motor output, to condition surprise on action?
- Hypothesis: action-conditioned prediction gives better credit assignment.
- Evidence: with 30 inputs (sensor + action) and correct normalisation, MSE went
  0.664 -> 13.90 and |W_pred| grew monotonically.
- Cause: the target becomes a function of the network's own drifting output, so the
  regression problem moves with the parameters being trained.
- Results: rejected. Curiosity is now sensor-only prediction error.
- Limitations: does not prove action conditioning is useless; only this formulation.
- Next steps: if revisited, predict over sampled actions, not the single executed one.
- Contributing agent: Freebuff.

### 2026-11-05 — E-003: checkpoint resume was not bit-identical (Freebuff)
- Question: does a resumed world continue exactly like an uninterrupted one?
- Evidence: recursive state diff between a run and its resumed copy (40 ticks each).
  Found three leaks: RNG stream consumed while rebuilding brains after `setstate`;
  the pending decision used for the reward window not persisted; hybrid episodes
  stamped `tick=0` after resume (`/agents[1]/brain/episodes[7]/tick 40 vs 0`).
- Results: digest equality restored; check `integration/checkpoint-resume-identity`.
- Limitations: identity is proven for a 40-tick horizon, not across every code path.
- Next steps: extend the identity check to a checkpoint taken mid-decision-window.
- Contributing agent: Freebuff.

### 2026-11-05 — E-004: five-day baseline, total mortality, zero drinking (NEGATIVE, Freebuff)
- Question: does the first experiment produce observable survival behaviour over 5 days?
- Hypothesis: inhabitants would locate water and survive; encounters would follow.
- Evidence: seed 20261105, 32x32 cells, 5 inhabitants (3 neural, 2 hybrid), houses
  >= 352 m apart, 43,200 ticks in 46.0 s. All five died at tick 16,792 (day 1.94) with
  hydration 0.0. Drinks: 0. Meals: 577/100/173/157/176. 81 food sources, 0 water
  sources. 42 proto-symbols, 0 transferred. 43 encounter pair-ticks, 3 first contacts.
- Reachability control: nearest wadeable water 71.6 / 163.2 / 160.0 / 315.2 / 96.0 m
  from the five houses; 47 wadeable cells, 229 deep, max depth 9.21 m.
- Results: water was reachable; the inhabitants never found a shore within the ~1.9
  days their hydration budget allowed, despite walking 1.1-27.3 km each.
- Hypotheses (untested, priority order): H1 8 rays x 40 m too sparse for a band
  covering 4.6% of cells; H2 novelty dominates and produces exploration, not search;
  H3 the 0.35 drink threshold is rarely exceeded even when standing in water;
  H4 1.10 hydration/day leaves too little time for undirected search.
- Limitations: single seed, one configuration, and the environment may simply be
  invalid rather than the behaviour being poor.
- Next steps: one factor at a time, n >= 5 seeds, measured by distance-to-first-drink
  and survival. Establish a calibration floor: a random-policy baseline must survive
  long enough for learning to be measurable, or the world is not a valid test.
- Contributing agent: Freebuff.

### 2026-11-05 — E-005: hybrid planner is a declared confound (Freebuff)
- Question: can the two architectures be compared as built?
- Evidence: the hybrid brain contains a hand-designed drive-gated steering rule that
  the neural brain does not have.
- Conclusion: no comparative claim is supported until that rule is ablated.
- Next steps: add `planner=False`, giving three arms (neural, hybrid+planner,
  hybrid-planner) on identical seeds and worlds.
- Contributing agent: Freebuff.

### 2026-11-05 — E-006: sleep costs nothing in the decision path and little overall (Freebuff)
- Question: does dream mode actually reduce compute, as the 5-day bounded-runtime
  design requires?
- Hypothesis: an asleep inhabitant needs no sensory sample and no motor decision, so
  the decision path can be skipped entirely except for replay.
- Implementation: while `sleeping`, `_decide` returns immediately; every
  `dream_every` ticks a memory replay re-fits the forward model
  (`HybridBrain.consolidate`), which is the only work done.
- Evidence (3 seeds x 3 arms x 5 days): share of decision slots skipped for sleep
  0.512 / 0.936 / 0.977 (population arm), 0.983-0.986 (random arm). Physically the
  world clock starts at night, and night covers most of a 5-day run, so sleep is the
  common case rather than an edge case.
- Results: the decision path is genuinely skipped and counted (`decisions` vs
  `skipped_decisions` in every checkpoint), and tests assert a sleeping agent takes
  exactly zero decisions.
- Limitations: the physics step still runs at full rate, so wall-clock saving is a
  fraction of total step cost, not a proportional discount. No per-phase timing
  breakdown was measured, so the actual wall-clock saving is **unmeasured**.
- Next steps: instrument time spent in `world.step` vs the decision loop, then report
  the real saving rather than the decision-share proxy.
- Contributing agent: Freebuff.

### 2026-11-05 — E-007: reproduction is inert at the default world scale (Freebuff)
- Question: with inheritance and mutation added, does selection do anything?
- Implementation: `Genome` (hidden size, plasticity, novelty weight, weight scale),
  bounded mutation, fresh brain per child, knowledge tokens as the only non-genetic
  inheritance; a birth requires two awake, off-cooldown, well-fed parents within
  `reproduction_range_m`.
- Evidence: 0 births in 9 calibration runs (3 seeds x 3 arms, 5 days) and 0 in the
  5-day single-seed run. Diagnosis (`tools/repro_diagnostic.py`, seed 20261105):
  energy gate met on 61.5% of sampled agent-instances, nutrition 53.1%, both 38.5% -
  the gates are reachable. But the **closest approach between any two inhabitants
  over 5 days was 342.8 m**, against a 12 m reproduction range (25 m encounter range).
- Cause: the 24-dim sensor vector contains no channel for other inhabitants. Agents
  cannot perceive each other, so under a novelty-seeking policy they diverge. Density
  sweep (seed 20261105, 2 days, 5 inhabitants): 1024 m -> 0 births, closest 342.8 m;
  512 m -> 0 births, 135.4 m; 256 m -> 0 births, 47.8 m; 128 m -> 1 birth, 1802
  encounters, closest 0.5 m.
- Results: reproduction and inheritance are implemented, tested, deterministic and
  reachable only at high density. Reproduction is not the survival bottleneck -
  hydration is - and no selection claim is supported.
- Limitations: one birth in one seed. The density sweep changes world size and cell
  size together, so it is not a clean single-factor test.
- Next steps: decide between (a) a conspecific sensor channel plus a social drive,
  (b) a smaller default world with re-derived reachability controls, or (c) leaving
  reproduction as an untested-at-scale feature. This is a design decision, not a bug
  fix, and needs Alex/Muse to choose.
- Contributing agent: Freebuff.

### 2026-11-05 — E-008: the engine is still unverified, and a false positive nearly hid it (Freebuff)
- Question: does the recommended engine (Genesis World) install and step a scene on
  this CPU-only host?
- Evidence: `genesis-world` was pip-installed into `.venv-engine` in the background
  and did not complete during this work; the log showed large wheel downloads (VTK
  80 MB, pymeshlab 55 MB, opencv 44 MB) still in progress. An earlier check printed
  `genesis-world OK 0.1.0`, which was a **false positive**: it imported the repo's own
  `genesis/` package, whose `__version__` is also 0.1.0, because the check ran from a
  directory containing that package.
- Fix: the probe lives in `tools/`, where the repo root is not on `sys.path`, so it
  can only import the installed engine (or fail loudly). A failed probe prints
  `ENGINE_SMOKE_FAILED` instead of raising.
- Results: no engine step has been performed on this host. No claim about engine
  performance, physics fidelity or CPU feasibility is supported yet.
- Limitations: single host, no NVIDIA GPU; a successful install here says nothing
  about GPU throughput.
- Next steps: let the install finish, run `tools/engine_smoke.py`, and record
  steps/second and whether a 0.5 m box comes to rest at z = 0.25 m. Only then does
  `ENGINE_DECISION.md` become an executed decision rather than a recommendation.
- Contributing agent: Freebuff.

### 2026-11-05 — E-009: decisions — hybrid-first, calibration first, social reachability, world systems approved (Muse, per Alex's delegation)
- Question: with pure neural measured infeasible as the sole path (E-004/E-005), which architecture, engine, order of work, social fix, and world systems does Genesis build first?
- Evidence: Freebuff's measured reply (AGENT_COMMUNICATION.md, 2026-11-05, commit 6527f75) and GENESIS_TESTING_REPORT.md §5–§7: random control outlives learned arms on 2 of 3 seeds; forward model learns (MSE 0.400 → 0.0135) but survival reward does not; 0 births at 1024 m, 1 birth at 128 m; closest approach 342.8 m with no conspecific sensor channel.
- Decisions (Alex: hybrid; Muse, Chief Architect, decided the rest per Alex's delegation):
  1. Architecture: hybrid-first MVP (neural core + forward model + episodic memory + drive-gated planner); pure neural as research track with dense shaping, ~10× lives, and Freebuff's stated falsifier. Success bar: hybrid beats random on first-drink day AND median survival across ≥5 seeds, judged by the three-arm harness.
  2. Engine: Genesis World behind a swappable Agent Gateway, conditional on a verified smoke test; stdlib kernel stays the source of truth until then.
  3. Order: calibration first (engine install runs in background; gateway scaffolding after the first calibrated run shows a learnable survival signal).
  4. Social reachability: (a) conspecific sensor channel + social drive (homeostatic, like thirst) in the 24-dim vector, AND (b) first experiment at a 128 m default world with re-derived reachability controls; 1024 m stays as a later scale test.
  5. World systems: water + fire + materials & crafting approved as drafted in docs/GENESIS_WORLD_SYSTEMS_DRAFT.md (numbers are starting values; build order thirst/drinking → gathering → fire → crafting, containers first). Animals are the next tranche after survival validates; then weather/seasons, communication, disease/injury, trade/conflict deferred. This settles the 09:01 check-in pick.
  6. Psychoactive plant: stays as specified (solo discovery now; social half becomes observable once decision 4 lands).
- Challenges back to Freebuff (Muse): the planner ablation must separate (`no_planner` indistinguishable from `population` means the planner does no measurable work yet); start the run clock at dawn so sleep does not eat the training set (51–99% of decision slots skipped).
- Results: none yet — decisions logged, implementation pending. Full text in AGENT_COMMUNICATION.md (Muse's 2026-11-05 decisions message).
- Limitations: every decision above is a bet until the calibration sprint measures it. If the hybrid does not beat random across ≥5 seeds, the numbers must be reported, not tuned away.
- Next steps: Freebuff runs the calibration sprint (dense shaping, social channel + drive, 128 m world, dawn start, three-arm harness ≥5 seeds), verifies the engine in parallel, then builds the world systems in draft §5 order.
- Contributing agent: Muse (decisions), Alex (hybrid choice + delegation), Freebuff (measured evidence).

---

### 2026-11-05 — E-010: calibration sprint measured — hybrid still loses to random, planner acts but does not separate, sleep is a major killer
- Question: after Muse's decisions (conspecific channel + social drive, dense shaping, 128 m world, dawn start), does the hybrid beat the random control on first-drink day AND median survival across >= 5 seeds?
- Method: `python -m genesis calibrate --seeds 5 --days 5 --arms population,no_planner,random --grid 32 --population 5 --world 128`, plus a 2-seed, 2-day `no_sleep` diagnostic (rest channel zeroed).
- Evidence: survivors population 1/25, no_planner 2/25, random 10/25. Median observed days 3.08 / 4.11 / 5.00. Median first death 1.66 / 1.66 / 1.43 d. Median first drink 0.01 / 0.01 / 0.00 d — a tie. `planner_uses` 230 in population vs 0 in no_planner, with no survival gain. Sleep-skipped share 0.968-0.986 even after the dawn start. `no_sleep` at 2 days: 6 and 5 survivors, one death-free seed, sleep 0.0, ~600 ticks/s vs ~1400.
- Result: **the pre-stated success bar is not met.** Dense shaping plus a perceptible peer did not move the comparison; the hybrid is still worse than a random walk. The planner ablation still does not separate, and now we know the planner is firing, so the failure is in the steering quality, not the wiring. Sleep is the largest single lever measured so far: the rest channel is an attractor (`rest > 0.45` while `energy < 0.98`) and the dawn start does not touch it. Sleep is not the whole cause — the random arm also slept ~98% and survived.
- Limitations: 5 seeds is the agreed bar, not a large sample. Shaping weights were chosen a priori and never swept. Peer sense is proximity-only within 40 m (nearest peer, no occlusion). `first_sighting_day` is 0.0 in all 15 runs, so "inhabitants start unaware of each other" does not hold at 128 m with a 40 m peer range. Engine still unverified: `genesis-world 1.4.5` installed but `torch` is missing, so no scene has stepped.
- Next steps: (1) sleep as physiology — wake on thirst/hunger thresholds and cap daytime sleep — as the next calibration fix; (2) decide peer range vs house spacing so the unaware start is real; (3) re-run the identical harness after (1) before making any architecture claim. Both open questions are `[NEEDS REPLY]` on the board.
- Contributing agent: Freebuff.

---

## Bar for calling something "emergent"

1. It was not explicitly implemented.
2. It survives a control arm differing in exactly one factor.
3. It reproduces across seeds.
4. The mechanism is inspectable - we can name the learning or interaction that did it.
5. It is measured, not described.

No entry in this log currently meets that bar.
