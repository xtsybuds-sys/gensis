# GENESIS WORLD SYSTEMS — DRAFT

**Status: APPROVED 2026-11-05 — approved by Muse (Chief Architect), per Alex's delegation to decide the world additions. Freebuff to implement per §5 build order; numbers below are proposed starting values for Freebuff to challenge with measured evidence, not measured facts.**

This covers the three world additions Muse recommended starting with in the 2026-11-05 morning check-in, in build order: **water, fire, materials & crafting**. It is written against the first experiment as defined in `README.md`: 5 inhabitants, 5 separate houses, shared environment, basic bodies/resources/senses, independent memory, inhabitants starting unaware of each other, run continuously for 5 days, death permanent.

It is a draft of the design that will eventually fill in `GENESIS_PHYSICS_SPECIFICATION.md` and `GENESIS_SIMULATION_ARCHITECTURE.md` (both currently outline-only). Anything engine-dependent is flagged as an open question for Freebuff rather than decided here.

## 0. Design rules these systems must obey

- **No omniscience, no scripting.** Inhabitants learn a system exists only by sensing it (seeing water, feeling heat, finding stone). No labels, no tutorial, no "meaning button" — same rule as the psychoactive plant decision (2026-11-05).
- **Consistent physics, multiscale.** Simulate at the cheapest fidelity that stays consistent: terrain/water at environment scale, bodies/senses at body scale, chemistry only where it changes behaviour. Do not simulate every atom.
- **Everything costs something.** Water, fire and tools all cost time, energy, attention, or risk. A free resource teaches nothing.
- **Measure emergence, don't claim it.** Each system below lists what to record. If inhabitants never use a system, that is a result — log it, don't force it.

## 1. Water

### 1.1 What exists in the world
- One river running through the shared environment, plus rainfall that collects in low ground and in any open container left out. No lakes or ocean in experiment 1.
- Water is visible, audible (flow sound near the river), and cold to the touch. Depth varies: shallow at the banks, deep enough mid-river to drown in.

### 1.2 Survival mechanics (proposed starting values)
- **Thirst:** each inhabitant has a thirst level, 0 (sated) to 100 (dying). Rises ~1 point per simulated hour at rest, faster with exertion and heat. At 80+, movement and cognition degrade; at 100, death within ~6 simulated hours unless they drink.
- **Drinking:** requires reaching water and performing a drink action (cupped hands, or a container — see §3). One drink restores ~40 thirst. River water is untreated: small chance of sickness per drink (see §1.5) — enough to matter, not enough to dominate.
- **Drowning:** in water deeper than chest height, an inhabitant that cannot swim (none can, initially) loses stamina fast and drowns in ~2 simulated minutes unless it reaches shallow water. Wading in shallow water is safe. This is the first real environmental killer in the world, and it must be learnable: inhabitants that watch or experience near-drowning should avoid deep water afterwards.

### 1.3 Rain
- Rain falls on a schedule set by the weather system (not built in experiment 1 — use a simple seeded pattern: light rain roughly every second simulated day, heavier storms rare). Rain fills open containers, makes fire harder (§2), and makes ground slippery.
- Rainwater collected in a container is cleaner than river water (lower sickness chance) — a discoverable advantage for inhabitants that store it.

### 1.4 What to measure
- Time from start until each inhabitant's first drink; how they found water (sight, sound, accident).
- Drinks per day per inhabitant; deaths or near-deaths by thirst and by drowning.
- Whether any inhabitant stores water, returns to the same spot, or (later) shows another where water is.

### 1.5 Out of scope for experiment 1
Fishing, swimming as a learned skill, wells, irrigation, farming. Boats. Water purification beyond "rainwater is cleaner".

## 2. Fire

### 2.1 What exists in the world
- No fire exists at start. Fire must be **made**: friction (rubbing dry wood — slow, needs dry fuel and patience) or spark (striking stone — faster, needs the right stone, see §3). Both are discoverable by trial, not taught.
- Fuel: dry wood, dry grass, leaves. A fire consumes fuel; unfed, a small campfire burns ~2 simulated hours. Rain extinguishes an unfed fire and makes ignition much harder; a sheltered hearth (§3) protects it.

### 2.2 Effects (proposed starting values)
- **Light:** a campfire lights ~8 m radius at night. Inhabitants can see and work in that radius after dark; outside it, night is effectively blind.
- **Heat:** warmth within ~3 m. Cold at night costs energy and sleep quality; fire removes that cost nearby. Standing too close (<0.5 m) burns — pain, injury, learned avoidance.
- **Cooking:** food held over fire becomes cooked — more nutrition, lower sickness chance than raw. (Food itself is a later system; in experiment 1, cooking applies to whatever edible plants exist.)
- **Spread:** fire spreads to adjacent dry fuel and to wooden structures if untended. A house can burn down. This is deliberate: fire is the first tool that can destroy what inhabitants built.

### 2.3 What to measure
- Time until first fire; method used (friction vs spark); how many attempts failed first.
- Whether fire is kept alive overnight, moved, shared, or hoarded; whether it is used for light, heat, cooking — or all three.
- Fire accidents: burns, spread events, structures lost. Do inhabitants learn to tend it, shelter it, or keep it away from houses?

### 2.4 Out of scope for experiment 1
Metal smelting, kilns, torches as portable light (a carried brand is allowed if it emerges from play, not as a designed recipe), signal fires as a designed communication channel.

## 3. Materials & crafting

### 3.1 Resources in the world
- **Stone:** loose stones near the river and in rocky ground. Types matter only at the level inhabitants can sense: sharp-edged (cutting, spark) vs round (hammering, building).
- **Wood:** fallen branches (free to pick up) and living trees (need effort/tools to take wood from). Dry wood is fuel (§2); green wood is not.
- **Clay:** banks of the river. Soft when wet, hardens when dried or fired — a discoverable material for containers.
- **Fibre:** grasses and bark, for binding and cordage.
- Ore and metal are **not** in experiment 1.

### 3.2 Gathering and carrying
- Gathering costs time and energy; carrying capacity is limited by body (hands + a carried load, roughly what one inhabitant can hold). No infinite inventory. Dropped items stay where they fall — they can be found, taken, or stolen later.
- Resources are finite per location and regrow slowly (branches fall, clay replenishes after rain). Scarcity near the houses is real by day 3–4 if inhabitants gather greedily.

### 3.3 Crafting — recipes are discovered, not given
No recipe list is shown to inhabitants. The following are the **intended** discoverable combinations, defined so Freebuff can implement the underlying physics; inhabitants must find them by trying:
- **Sharp stone + wood → cutting tool.** Lets them cut fibre, shape wood, take wood from trees.
- **Hollowed wood / fired clay → container.** Lets them carry water (§1) and store it — the key that turns water from a place into a possession.
- **Stone + wood + fibre → hearth / sheltered fire pit.** Protects a fire from rain (§2).
- **Wood + wood + fibre → simple shelter / repair.** Reinforces the existing houses; a built shelter of their own is allowed but not required in experiment 1.
- Crafting takes time and can fail; a failed attempt wastes material and time, and the failure itself is information.

### 3.4 What to measure
- First tool made, by whom, after how many attempts; whether the maker keeps it, loses it, or is copied by others.
- Whether containers appear, and whether water storage changes drinking patterns (§1.4).
- Whether inhabitants specialise (one gathers, one crafts) or all do everything; whether tools are shared, traded, or taken.

### 3.5 Out of scope for experiment 1
Metal tools, farming tools, weapons as a designed category (a sharp stone is a tool; what inhabitants do with it is theirs), currency, written recipes.

## 4. How the three systems interact (the point of building them together)

- **Water × fire:** water extinguishes fire; rain makes ignition hard; a hearth (§3) protects fire from rain. Steam is not simulated in experiment 1.
- **Fire × materials:** fire hardens clay into containers; fire needs dry wood; fire can destroy wooden shelters and stored fuel.
- **Water × materials:** clay is found at the river; containers turn water portable; rain replenishes clay and fills containers.
- **The loop that matters:** water keeps inhabitants alive today; containers let them carry water tomorrow; fire lets them stay warm and cook tonight; tools let them make containers and hearths. An inhabitant that connects two of these has done the first real piece of civilisation-building. Record the first time any inhabitant combines two systems, and the first time one teaches another (by demonstration, not by scripted language — language is a later system).

## 5. Build order for Freebuff

1. Terrain + river + rain pattern, with depth and flow (§1). Thirst and drinking first — survival from hour one.
2. Loose resources + gathering + carrying (§3.1–3.2). No crafting yet.
3. Fire: ignition, fuel, light/heat, spread (§2). Needs §3.1 fuel to exist.
4. Crafting combinations (§3.3), containers first, then hearth, then tools — in that order, because containers change survival fastest.
5. Instrumentation: log every first-use, every death cause, every cross-system combination (§4). No instrumentation, no experiment.

## 6. Open questions (for Freebuff — engine-dependent)

- **Fluids:** can the chosen engine do a believable river + rain collection cheaply, or do we fake depth/flow with a heightfield and a flow field? Isaac Sim vs UE5 vs Genesis World differ sharply here. Do not build a full fluid sim for experiment 1.
- **Fire spread:** particle + heat-radius approximation, or a cellular spread model on the terrain grid? Needs a decision before §2 is implemented.
- **Performance budget:** 5 inhabitants + river + fire + day/night, continuous for 5 days — what is the compute cost, and where does adaptive fidelity cut in? Measure before scaling to animals or weather.
- **Engine pick still open** (see `AGENT_COMMUNICATION.md`): this draft assumes nothing engine-specific. If Freebuff picks an engine that cannot do one of these systems cheaply, say so here and propose the cut.

## 7. What this draft deliberately does not decide

- Engine choice. Animals, weather/seasons, communication/language, disease, trade/conflict — all deferred, in the ranked order from the 2026-11-05 morning check-in.
- Whether Alex wants all three systems or a subset: if he picks only water, §2–§3 drop out and §1 stands alone. If he adds animals later, they drink the same water and fear the same fire — these systems are the foundation either way.
- Exact numeric tuning: thirst rates, burn times, sickness chances are starting values. The first 24 simulated hours are a tuning run; log the numbers, adjust once, and record the change in the emergence log.

## Status history
- 2026-11-05: Draft written by Muse. Awaiting Alex's decision on which world additions to include.
- 2026-11-05: Approved by Muse (Chief Architect), per Alex's delegation. All three systems (water, fire, materials & crafting) approved; animals are the next tranche after survival validates.
