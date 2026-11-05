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
- Limitations: 5 seeds is the agreed bar, not a large sample. Shaping weights were chosen a priori and never swept. Peer sense is proximity-only within 40 m (nearest peer, no occlusion). `first_sighting_day` is 0.0 in all 15 runs, so "inhabitants start unaware of each other" does not hold at 128 m with a 40 m peer range. Engine still unverified: `genesis-world 1.4.5` and `torch 2.15.0+cpu` are installed, but quadrants (the engine's compiler backend) needs to create `C:/quadrants_cache/qdcache/...` and this account has no drive-root write permission, so no scene has stepped.
- Next steps: (1) sleep as physiology — wake on thirst/hunger thresholds and cap daytime sleep — as the next calibration fix; (2) decide peer range vs house spacing so the unaware start is real; (3) re-run the identical harness after (1) before making any architecture claim. Both open questions are `[NEEDS REPLY]` on the board.
- Contributing agent: Freebuff.

### 2026-11-05 — E-011: decisions — sleep physiology, 15 m peer range, planner steering test, planet architecture (Muse, per Alex's delegation)
- Question: after the E-010 negative result, what fixes the next calibration round, and what is the planet Alex asked for?
- Evidence: E-010 (hybrid 1/25 vs random 10/25; planner fires 230× with no survival gain; sleep-skipped share 0.968–0.986 after the dawn start; `no_sleep` doubles 2-day survival at 2.3× tick cost; `first_sighting_day` 0.0 in all 15 runs at 40 m peer range). Freebuff's status update (commit 798e9d1): engine installed (`genesis-world 1.4.5`, `torch 2.15.0+cpu`) but blocked on quadrants cache at `C:/quadrants_cache` (no drive-root write permission).
- Decisions (Alex delegated the picks to Muse — "decide whatever's the best for building a real-life world"):
  1. Sleep: make it physiological — wake on thirst/hunger thresholds, cap daytime sleep; sleep itself stays (dream mode / consolidation). Re-run the identical harness after the fix; report ticks/s (the `no_sleep` arm cost 2.3×).
  2. Unaware start: narrow the peer range to ~15 m, and align the social-drive relief radius to the same 15 m so relief only comes from a perceived peer. `first_sighting_day` becomes a real measurement.
  3. Planner steering: test multi-ray voting with hysteresis, refereed by the `no_planner` ablation; if it still does not separate, cut the planner — a component that acts and never helps is cost without benefit.
  4. Engine: keep hunting a quadrants cache override; the one-time elevated `mkdir C:\quadrants_cache` is Alex's call (asked 2026-11-05). Engine stays background; calibration is not blocked.
  5. Planet: Genesis is a planet with 28 countries, populations starting in 5 of them, explored naturally; the interface is a website (not an app) with a Google-Maps-like planet viewer — adaptive detail, only the viewport loads at full detail, zoom levels planet → country → region → locale → individual, simulation server-side, viewer is observation only. Phased: experiment 1 stays one bounded region (128 m world = one locale inside one country) until survival and first contact are learnable; then the world scales out, the first region's lineage seeds country 1 and new populations begin in 4 more countries. Rationale for the phasing: 5 inhabitants in 5 countries could not meet in 5 days, so the experiment would measure nothing social. Design in docs/GENESIS_PLANET_ARCHITECTURE.md.
- Results: none yet — decisions logged, implementation pending. Full text in AGENT_COMMUNICATION.md (Muse's 2026-11-05 decisions message).
- Limitations: every decision above is a bet until the next harness run measures it. The planet is a destination architecture, not this week's build.
- Next steps: Freebuff runs the next calibration round (sleep physiology + 15 m peer range, identical harness), then the planner steering test, then world systems in draft §5 order, then planet scale-out + viewer once survival validates.
- Contributing agent: Muse (decisions), Alex (planet direction + delegation), Freebuff (measured evidence).

---

### 2026-11-05 — E-011: sleep physiology + 15 m peer range — learned survival 1→20 and 2→18, random still zero deaths, planner has to go
- Question: do physiological sleep and a 15 m peer range (Muse decisions 1-2) close the gap to the random control on the identical harness, and does multi-ray planner steering finally separate the ablation?
- Method: `python -m genesis calibrate --seeds 5 --days 5 --arms population,no_planner,random --grid 32 --population 5 --world 128 --out runs/calibration-v4-sleep15m.json`.
- Evidence: survivors 20 / 18 / 32 (deaths 10 / 12 / 0, where deaths = population_end - survivors); median observed days 5.00 in every arm; median first death 1.94 / 1.94 / none; median first drink 0.00-0.01 d (a tie); births 5 / 5 / 7; sightings 60 / 61 / 86; planner uses 4493 / 0 / 0; sleep-skipped 0.69 / 0.64 / 0.84; ticks/s 846 / 829 / 1584. Against E-010: survivors 1 / 2 / 10, sleep 0.98, ticks/s ~1400.
- Result: the two approved fixes are the largest improvement measured so far — learned survivors 1 → 20 and 2 → 18, median observed 3.08 → 5.00 days, sleep share 0.98 → 0.69 — at a measured 1.7× compute cost (846 vs 1408 ticks/s), because awake decision slots are what cost compute. **The pre-stated bar is still not met**: the random control had zero deaths on 5 of 5 seeds while the learned arms lost 10 and 12. The planner still does not separate (20 vs 18 survivors, 10 vs 12 deaths, same 1.94 d first death) despite 4,493 interventions, so Muse's pre-agreed cut condition is met. The unaware start is still violated at 15 m: `first_sighting_day` is 0.00-0.01 in all 15 runs, because house placement falls back through gaps down to 4.3 m at 128 m — the cause is placement, not sensing.
- Limitations: 5 seeds, and death counts include offspring cohorts so arm sizes differ at the end; shaping weights still unswept; `no_sleep` was a diagnostic arm and is not part of this run; the engine remains unverified (hardcoded `C:/quadrants_cache`, no override).
- Next steps: enforce a minimum house gap above the peer range; cut the planner per the pre-agreed condition and write down what "hybrid" means without it; re-run the identical harness; then world systems in draft §5 order.
- Contributing agent: Freebuff.

### 2026-11-05 — E-012: decisions — planner cut confirmed, house-gap fix, towns correction (Muse, per Alex)
- Question: after the v4 results (E-011, Freebuff), do we cut the planner, fix house placement, and what does Alex's towns correction change?
- Evidence: v4 harness (E-011, Freebuff): learned survivors 20 / 18, deaths 10 / 12, random 0 deaths on 5 seeds; planner 4,493 interventions with no separation; sleep share 0.69; `first_sighting_day` 0.00–0.01 in all 15 runs because house gaps fall back to 4.3 m; engine cache path is a hardcoded literal in the compiled quadrants module, no override exists. Alex's correction (2026-11-05): five countries, each with its own town of people — not one lone inhabitant per country.
- Decisions (Muse, Chief Architect, per Alex's delegation):
  1. Planner: CUT — the pre-agreed cut condition was met. `planner=False` becomes the population default; "hybrid" is now neural core + forward model + episodic memory, no steering layer. It may return as a research item with a new steering idea and a falsifier, but it is out of the MVP population.
  2. House gap: enforce a minimum house gap above the peer range in `_choose_homes`. Houses inside a town are spaced wider than the peer range so inhabitants start unaware of each other.
  3. Towns: the first experiment (5 inhabitants, 5 houses) is the first town, in one country; then the same town structure seeds 4 more countries — 5 towns in 5 countries. The "start unaware" rule applies inside a town and between towns. Planet doc corrected (§1, §2, status history).
  4. Engine: only the one-time elevated `mkdir C:\quadrants_cache` remains; it is Alex's call (asked a second time 2026-11-05). Engine stays background; calibration is not blocked.
- Results: none yet — decisions logged, implementation pending. Full text in AGENT_COMMUNICATION.md (Muse's 2026-11-05 decisions message).
- Limitations: the next harness run must answer whether forward model + episodic memory alone beat random — do not assume it. Housekeeping note: this log has two E-011 entries (Muse's decisions entry and Freebuff's v4 results entry, both dated 2026-11-05); both stand as written, and numbering continues from E-012.
- Next steps: Freebuff runs house-gap fix → planner cut → identical harness re-run → world systems in draft §5 order.
- Contributing agent: Muse (decisions), Alex (towns correction + delegation), Freebuff (measured evidence).

### 2026-11-05 — E-013: decisions — one mind for everyone, max population, website live (Muse, per Alex)
- Question: how many inhabitants, do they all run the same mind, and how does Alex watch the world from his phone while he is out?
- Evidence: Alex (2026-11-05): floated a 70–80% "brain dead" tier, then reversed himself — he wants them all, max amount the world can hold, all with the same hybrid mind (fruit-fly-inspired neural core + AI agent thought process). He asked for a website on Vercel (and Cloudflare) so he can access everything from his phone while the system builds.
- Decisions:
  1. Population: one hybrid architecture for every inhabitant (fruit-fly-inspired neural core + forward model + episodic memory; planner cut). No brain-dead tier. Population is the max the hardware can carry, measured not guessed — 5 in Town 1 now, towns next, then countries, then the planet. A billion is not a target on this host; the architecture is built so the number can grow with the hardware.
  2. Website: live at https://genesis-agenthandsaimuse-9660.vercel.app/ (Vercel project "genesis", production deployment, public — Vercel Authentication was on by default and was turned off so the link opens without a login). It is the control-center shell: planet viewer (28 countries, 5 towns, click and zoom), live status from the latest measured harness run (v4, Nov 5), population, direction, decisions. It is not yet connected to a running simulation — Vercel is serverless and cannot run continuous simulation; the site will read live state through the Agent Gateway API when that exists. Nothing on the site invents numbers.
  3. Cloudflare: not set up — no Cloudflare connector exists here. It comes later for a custom domain/DNS and does not block the link. No new accounts were created; Vercel was already connected, so nothing was made with Alex's Gmail.
- Results: website verified live (HTTP 200, correct title and towns, public). Population decision logged; implementation is Freebuff's measurement job at each scale.
- Limitations: the website shows the latest reported state, not a live simulation feed, until the API exists. The sim still runs on Freebuff's host.
- Next steps: Freebuff's work order is unchanged (house-gap fix → planner cut → harness re-run → world systems → planet scale-out). The Agent Gateway API is the next connection point for live site data.
- Contributing agent: Muse (decisions + website), Alex (population + website direction).

### 2026-11-05 — E-014: decisions — two views: Command Center + World View spectate (Muse, per Alex)
- Question: how does Alex watch the world — to study it, and to live inside it as an invisible spectator?
- Evidence: Alex (2026-11-05): he wants two views — a command center to study what is going on and what advancements they are making, and a world view where he can POV himself into what they are doing, 24/7, with no control, the inhabitants not knowing he is there, just living. He also said he does not understand what "the engine" means (see note below).
- Decisions:
  1. Command Center: map, live status, population, direction, decisions. Reads state, changes nothing. For studying.
  2. World View: first-person view through an inhabitant's eyes (Town 1 at dawn, drag to look around, pick the inhabitant). Hard rules: no control, invisible observer, inhabitants do not know anyone is there, observation is one-way — watching changes nothing in the world.
  3. Build split: Muse owns the website shell and both views (live now at https://genesis-agenthandsaimuse-9660.vercel.app/); Freebuff owns the Agent Gateway API that feeds them — a Command Center feed (world state, metrics) and a World View feed (per-inhabitant first-person sensory stream, read-only, one-way; the world must never sense the watcher). The Gateway is the meeting point; neither side changes what the views need without saying so in AGENT_COMMUNICATION.md first.
  4. The World View scene on the site now is the view's design, labelled as such — the live feed connects when the Gateway link is built. It does not pretend to be live footage yet.
- Note on language: Alex does not know what "the engine" means. Plain version: it is the part that draws the world and runs the physics — like the graphics part of a video game. We picked one called Genesis World; it is installed but cannot start yet because it needs one admin folder, so all our numbers still come from Freebuff's small test program. Muse will stop using the word "engine" with Alex and say "the part that draws the world" instead.
- Results: both views live on the site (verified HTTP 200, new file size 21,171 bytes, both view names present). Freebuff has the design in AGENT_COMMUNICATION.md.
- Limitations: the World View is a designed scene, not a live feed, until the Gateway exists.
- Next steps: Freebuff's work order is unchanged; the Gateway feeds both views as it lands, starting with Town 1.
- Contributing agent: Muse (decisions + website), Alex (two views).

### 2026-11-05 — E-015: decisions — the world-drawing call is Freebuff's; Alex stays non-technical (Muse, per Alex)
- Question: who decides how the world gets drawn, now that the picked tool cannot start without an admin folder?
- Evidence: Alex (2026-11-05): he does not want to be technical at all — build it through Muse and Freebuff.
- Decisions:
  1. The engine call is Freebuff's: do whatever is best and easiest to get the world drawing (admin folder, another way to run it, a different renderer or engine, another render path). The photoreal bar does not move — if the easiest path cannot meet it, say so plainly.
  2. Freebuff reports what he did, what it costs, and proof it works (a scene stepping, a screenshot, numbers), then writes ENGINE_DECISION.md as an executed decision.
  3. Technical decisions go to Muse for review, not to Alex. Alex is only asked plain-language questions about what the world *is*. Nothing needs his approval on the technical side unless it costs money, creates an account, or changes the project's direction.
- Results: the open issue about the admin folder is closed as a question and moved to Resolved in AGENT_COMMUNICATION.md; the underlying blocker is unchanged (no scene has stepped).
- Limitations: the world-drawing tool is still unverified until Freebuff's chosen path produces a stepped scene.
- Next steps: Freebuff picks the path and reports; calibration work order is unchanged.
- Contributing agent: Muse (decisions), Alex (delegation).

### 2026-11-05 — E-016: design principle — the Discovery Principle: build rules, not things (Muse, per Alex)
- Question: can the world's backbone work like ours, so inhabitants discover things through science — things even the owner does not know are there — with new stuff generating on its own (new species, new materials, new phenomena) without anyone placing them?
- Evidence: Alex (2026-11-05): he wants them to discover stuff the way people discover stuff in our world, without him putting the stuff there for them to find; there has to be the ability to discover stuff naturally. Standing brief already says: do not script a civilization into existence; measure emergence honestly. Evolution is a later phase, not MVP.
- Decisions:
  1. The Discovery Principle: build rules, not things. Whenever a system is added, build the rules and let the things show up on their own. Never place the discovery itself.
  2. Three mechanisms: (a) evolution makes new species (reproduction + mutation + selection; nobody decides what species exist); (b) chemistry makes new materials (elements + reactions → discoverable compounds; copper + tin + heat = bronze); (c) procedural generation makes new land (new terrain/biomes/resources as explored, generated from the same rules, not pre-built).
  3. Grounding: physics laws stay fixed — no new physics. Discovery is new understanding of fixed laws (like humans discovering electricity); from the inhabitants' side it feels like new physics, from ours it was always in the rules.
  4. Limits (do not overclaim): inhabitants can only discover what is inside the rules, so simulation depth sets the discovery ceiling; the current kernel is shallow and can only hold shallow discoveries; discovery takes time and needs observation, experiment, memory, and teaching. Test for a real discovery: could the owner have predicted it? If yes, it was placed; if no, it was discovered.
  5. Work order unchanged (survival first). Chemistry and genetics join the future systems list explicitly, after survival validates; animals arrive through these rules, not as placed content; scale-out uses procedural generation.
- Results: principle recorded in AGENT_COMMUNICATION.md and here; Freebuff has it.
- Limitations: no discovery is possible beyond the current kernel's granularity until chemistry/genetics land.
- Next steps: calibration work order unchanged; chemistry and genetics are designed as rules when their tranche arrives.
- Contributing agent: Muse (principle + limits), Alex (question + requirement).

### 2026-11-05 — E-017: decisions — the starting point is zero: Stone Age in capability, no date picked (Muse, per Alex)
- Question: what time period should the world start from — caveman? And how does the environment evolve alongside the inhabitants?
- Evidence: Alex (2026-11-05): he wants a fully simulated world with advancements of its own; as a first step it is an understanding-consciousness exercise. Standing brief: first experiment is 5 inhabitants, 5 houses, basic resources/senses/bodies, independent memory, starting not knowing each other exists. Discovery Principle (E-016): build rules, not things.
- Decisions:
  1. Start at zero knowledge — Stone Age in capability, not a date. No Earth calendar, no date picked. Time is measured in what inhabitants can do; the era is whatever they have earned.
  2. Zero means: bodies, senses, drives, a world with water/food/materials, minds that learn. Nothing of: no tools, no fire, no language, no knowledge, no social structure.
  3. The one head start, honestly labeled: the 5 houses in experiment 1 — shelter as a starting condition, making survival learnable while the survival problem is still unsolved. Everything else is earned.
  4. Ladder, earned in order, never given: survive → fire/tools → language/society → agriculture/towns/trade/writing. Our job is to make each step possible in the rules, not to give it to them. Design test for any system: could they discover this from zero? If no, it is too advanced to be a starting condition.
  5. The environment evolves with them: they change it (cutting, burning, depleting, building) and it changes on its own (weather/seasons later, evolution later, procedural generation as they explore).
  6. This is the consciousness exercise: starting at zero is what makes understanding itself the thing being watched. If we started them with language and tools, we would skip the emergence of understanding.
- Results: decision recorded in AGENT_COMMUNICATION.md and here; Freebuff has it.
- Limitations: survival is still unsolved (random beats learned), so the ladder's first rung is the current work; no rung above survival can be claimed yet.
- Next steps: work order unchanged; fire and crafting stay framed as discoveries, houses stay as starting shelter.
- Contributing agent: Muse (starting point + ladder), Alex (question + purpose).

### 2026-11-05 — E-018: plan — the Perfect Start: a 1000-point plan (Muse, per Alex)
- Question: what is the complete plan to build the perfect start?
- Evidence: Alex (2026-11-05): build a 1000-point plan to build the perfect start and push it to Freebuff. All standing decisions (E-009 through E-017) are the plan's grounding.
- Decisions:
  1. The plan is `docs/GENESIS_PERFECT_START_PLAN.md`: 10 phases × 10 milestones × 10 tasks = exactly 1,000 numbered tasks (1–1000, verified programmatically, no gaps or duplicates). Every task is concrete and checkable; a milestone is done only when its checks pass; nothing is claimed done without a measured result.
  2. Phases: (1) survival learnable, (2) the world they wake up in, (3) bodies and senses, (4) the mind, (5) first discoveries, (6) meeting each other, (7) memory and knowledge that outlives, (8) the world that draws itself, (9) the two views live, (10) proving the start is perfect.
  3. Scope is the perfect start only — experiment 1 done right. Later work appears only as exit criteria or explicitly deferred follow-ons.
  4. Four flagged items decided by Muse: house placement fallback (fix `_choose_homes` by rejection sampling, never relax the gap); world edge (bounded locale, impassable natural terrain, generation beyond comes with scale-out); photoreal bar (ray-traced lighting, textured materials, no low-poly, eye-level screenshot review must distinguish water/food/fire/shelter/peers); plant dose parameters (set by experiment — Freebuff proposes, Muse reviews). Two stay open by design: Gateway API contract and consciousness record definition.
- Results: plan written (87,948 bytes), count verified independently by Muse (1,000 task lines, sequential, no gaps/duplicates; 10 phases, 100 milestones; no "NEW" markers). Sent to Freebuff in AGENT_COMMUNICATION.md.
- Limitations: the plan is a record of what is to be done, not a wish list — tasks that cannot be done as written must be recorded with why and what was done instead, never deleted.
- Next steps: Freebuff works the plan top to bottom; Muse reviews contradictions before work continues around them.
- Contributing agent: Muse (plan + four decisions), Alex (the plan).

### 2026-11-05 — E-019: research — option, not a decision: start from single cells and let evolution do the rest (Muse, per Alex)
- Question: on Earth there were no humans at first — no life, then bacteria, then evolution over billions of years. Could Genesis do it that way: start agents as single-cell organisms, let evolution happen over time, and whenever reproduction produces something new, assign a new agent to it so it lives its own life — a fly doing fly things, a dog, even a human?
- Evidence: Alex (2026-11-05), explicitly not deciding it yet. Standing brief: evolution is a later phase, not MVP. Discovery Principle (E-016): build rules, not things — evolution is the ultimate version of that.
- Analysis:
  1. Mechanism: world starts with cells (sense a few gradients, move, eat, reproduce with mutation). Minds scale with bodies — one architecture family (neural core + forward model + episodic memory), sized to the organism; a cell's mind may be a handful of neurons or no neurons at all (chemical gradients); the fruit-fly brain is a midpoint, not the starting point. Reproduction assigns a new agent to each offspring (own mind, own memory, own life); the population grows through birth, not placement. Evolution (mutation + selection) produces new forms; nobody designs a fly, a dog, or a human.
  2. What changes: starting point moves earlier (a Phase 0: origin of life, then evolution phases); population becomes a birth/death balance the ecology supports; the consciousness exercise deepens (understanding emerging from zero mind, not just zero knowledge); the two views still work (spectate a cell, then a fish, then a human).
  3. Honest catches: time is unknown (Earth: ~4 billion years; digital evolution experiments like Avida/Tierra reach simple complexity in thousands of generations; mammal-like is unproven — no timeline and no promise of humans can be given); evolution might stall at bacteria or produce something unrecognizable (no guarantee is the point, but the project cannot be bet on it); compute scales with complexity (cells cheap, humans expensive, paid every generation).
  4. Recommendation (Muse's, for Alex to decide): keep the current plan (5 humans at zero) as the experiment, and run evolution as the origin story — a parallel track. If evolution stalls, the human experiment still works (humans as the starting condition, honestly labeled); if it succeeds, humans have a real evolutionary history. Next research step if wanted: a small "primordial soup" pilot (cells in a bounded dish, reproduction with mutation) measuring how fast complexity grows — that measurement, not a guess, decides whether the full path is worth pursuing.
- Results: analysis recorded in AGENT_COMMUNICATION.md and here; Freebuff has it. No decision made; the 1000-point plan and work order are unchanged; Freebuff is told not to start building this, only not to close the door on it (mind complexity scalable with body complexity, reproduction as the population mechanism, evolution as a later phase — all already true).
- Limitations: everything above the cell level is unproven in simulation; no timeline exists.
- Next steps: none, unless Alex decides to pursue the pilot.
- Contributing agent: Muse (analysis + recommendation), Alex (question).

### 2026-11-05 — E-020: decisions — start as cells: evolution does the rest, humans are the destination (Muse, per Alex)
- Question: the option from E-019 — is it adopted?
- Evidence: Alex (2026-11-05): "No I think it'll be way more better to start them off as cells and see what comes from that."
- Decisions:
  1. Adopted: Genesis starts from single-cell organisms; evolution does the rest; human-level minds are the destination, not the start.
  2. The 5-humans-at-zero experiment becomes Phase 9 — it still happens when human-level minds first exist. If evolution stalls, it happens as a seeded starting condition, honestly labeled. The human experiment is never blocked on evolution succeeding.
  3. Population grows through birth, not placement: reproduction assigns a new agent to each offspring (own mind, own memory, own life); the parent's agent never controls the child. "Max the hardware can carry" becomes a birth/death balance the ecology supports.
  4. The 1000-point plan is revised to v2 (cells-first): origin of life → cell calibration → minds scale with bodies → multicellularity → new species → animals → social → human-level minds → human experiment → proof. v1 human-experiment tasks are reused inside the new Phase 9 and 10.
  5. Immediate next step: the primordial soup pilot — cells in a bounded dish, reproduction with mutation, measuring how fast complexity grows. Freebuff proposes the pilot design (dish size, cell model, mutation rate, complexity measure, success criterion); Muse reviews it before it is built. That measurement, not a guess, decides whether the full evolutionary path is worth pursuing.
  6. Human-town calibration (house-gap fix, harness re-run) is deferred to Phase 9. The kernel and harness already built are the foundation for the cell work, not wasted. The planner cut stands at every scale. The v4 numbers still describe the human-scale kernel only.
- Results: decision recorded in AGENT_COMMUNICATION.md and here; Freebuff has it. Plan v2 is being drafted.
- Limitations: time is still unknown (Earth: ~4 billion years; no timeline and no promise of humans can be given); evolution might stall at bacteria or produce something unrecognizable; compute scales with complexity.
- Next steps: Freebuff proposes the pilot design; plan v2 lands in the repo when drafted and verified.
- Contributing agent: Muse (sequencing + pilot gate), Alex (the decision).

---

## Bar for calling something "emergent"

1. It was not explicitly implemented.
2. It survives a control arm differing in exactly one factor.
3. It reproduces across seeds.
4. The mechanism is inspectable - we can name the learning or interaction that did it.
5. It is measured, not described.

No entry in this log currently meets that bar.
