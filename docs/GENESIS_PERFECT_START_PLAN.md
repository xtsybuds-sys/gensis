# GENESIS — THE PERFECT START PLAN

## What "the perfect start" means

The perfect start is experiment 1 done right: 5 inhabitants, 5 houses, one shared 128 m world, run continuously for 5 days, starting at zero — Stone Age in capability, no date picked — with the inhabitants starting unaware of each other. Nothing is given to them except shelter (the 5 houses, honestly labeled as a starting condition). Everything else — survival, fire, tools, meeting each other, shared knowledge — is earned by them, discovered by them, and recorded by us. The start is perfect when survival is learnable (the hybrid beats the random control on the stated bar), the world is built and instrumented, the minds are complete and identical for every inhabitant, the first discoveries are real, the two views are live and honest, and every claim is backed by a measured result. Later work — Towns 2–5, animals, weather and seasons, chemistry, genetics, evolution — appears here only as this start's exit criteria or as explicitly deferred follow-ons, never as full plans inside this document.

## Scope

This plan covers the perfect start only. It does not plan the planet, the towns, or any system deferred past survival. Where a later system is mentioned, it is mentioned as a boundary: what the start must not close off, what unlocks it, and where it is written down.

## How to read the numbers in this plan

A number labeled "target" is a goal to hit, not a fact. A number cited as measured carries its version (v4, November 5, 2026, 5 seeds × 5 days × 3 arms, 128 m). Numbers from the world-systems draft are starting values to challenge with measured evidence, not facts. Nothing in this plan invents a measured number.

## Phase 1: Survival becomes learnable — calibration to the bar
Done when: the hybrid beats the random control on first-drink day AND median survival across ≥5 seeds, judged by the three-arm harness (population, no_planner, random); or the failure is recorded with the next single change and its falsifier.

### 1.1 Fix the house gap — the unaware start must hold
- 1. Read `_choose_homes` and record the current gap fallback ladder (35.8, 21.5, 10.7, 4.3 m) in GENESIS_TESTING_REPORT.md.
- 2. Change `_choose_homes` so the minimum house gap is above the 15 m peer range, with no fallback below it.
- 3. Add a placement test asserting all five house gaps exceed 15 m on every seed.
- 4. Run the placement test across 5 seeds and record the minimum gap per seed.
- 5. If placement fails on any seed at 128 m, record the failure and the chosen fix (Muse to decide: shrink the peer range or enlarge the world) — do not silently relax the gap.
- 6. Verify first_sighting_day is no longer 0.0 in a short 1-day diagnostic run.
- 7. Record the new house coordinates per seed in the run log.
- 8. Update the emergence log entry E-011 (Freebuff) with the fix and the measured gaps.
- 9. Get the placement test passing in the kernel test suite (37 tests plus the new placement tests).
- 10. Record the final house-gap rule in the simulation architecture notes.

### 1.2 Cut the planner — population default is planner=False
- 11. Set planner=False as the population default in the kernel config.
- 12. Remove planner steering from the decision path; confirm no planner code runs in the population arm.
- 13. Keep the planner code behind a flag for the research track; record where it lives.
- 14. Re-run the unit tests and record the pass count.
- 15. Confirm the no_planner arm and the population arm are now identical in config except for the flag under test.
- 16. Record the cut in AGENT_COMMUNICATION.md with the v4 evidence (4,493 interventions, no separation).
- 17. Update the hybrid definition in the docs: neural core + forward model + episodic memory, no steering layer.
- 18. Verify the three-arm harness still runs (population, no_planner, random) with the new default.
- 19. Log the cut in the emergence log with the pre-agreed cut condition quoted.
- 20. Confirm with Muse that the cut is final for the MVP and record the confirmation.

### 1.3 Identical harness re-run — same seeds, same arms, new defaults
- 21. Freeze the harness config (5 seeds, 5 days, 3 arms, 128 m, dawn 06:00) and record its hash.
- 22. Run the full harness with the house-gap fix and the planner cut and no other changes.
- 23. Record survivors, deaths, median observed days, and first-drink day per arm per seed.
- 24. Record sleep-skipped share and ticks/s per arm.
- 25. Record births and sightings per arm.
- 26. Record first_sighting_day per run; confirm it is above 0.0.
- 27. Compare the new run against v4 (survivors 20/18, deaths 10/12, random 0 deaths) in a table.
- 28. Write the results as a new versioned section in GENESIS_TESTING_REPORT.md.
- 29. Post the results in AGENT_COMMUNICATION.md with the numbers, not a summary of them.
- 30. If the bar is still not met, record that fact plainly and do not claim progress that is not in the numbers.

### 1.4 Diagnose why random still wins
- 31. List every death in the learned arms by cause (thirst, drowning, other) and by day.
- 32. Compare death causes between the learned arms and the random arm.
- 33. Measure the distribution of first-drink day in the learned arms versus random.
- 34. Measure how many decision slots each learned inhabitant actually gets per life after sleep (target: report the measured range).
- 35. Check whether deaths cluster on particular seeds; record per-seed survival.
- 36. Trace three individual learned lives from birth to death and log the decisions that preceded each death.
- 37. Write the diagnosis in GENESIS_TESTING_REPORT.md: what the data says, what it does not say.
- 38. Propose one change at a time from the diagnosis (not three at once); record the proposal.
- 39. Get Muse's review of the diagnosis before implementing any change.
- 40. Record Muse's decision on the next change in AGENT_COMMUNICATION.md.

### 1.5 Sleep physiology verification
- 41. Verify the wake rules fire: wake when rested, hydration ≤ 0.55, nutrition ≤ 0.30, 3 h bout cap.
- 42. Verify an inhabitant cannot fall asleep while thirsty or hungry, or within 30 min of waking.
- 43. Measure sleep-skipped share across 5 seeds and compare with v4's 0.69.
- 44. Measure the share of decisions lost to sleep per life.
- 45. Check that daytime sleep is capped and night sleep is not.
- 46. Record ticks/s with the sleep rules on; compare with v4's 846 ticks/s.
- 47. Run a no_sleep diagnostic on 2 seeds × 2 days and record the survival difference.
- 48. Record the sleep cost in the testing report: ticks/s and survival, side by side.
- 49. Confirm the run clock still starts at dawn 06:00 in every run.
- 50. Log the sleep verification in the emergence log.

### 1.6 Dense shaping and credit assignment
- 51. List the current dense shaping terms (thirst/energy) and their weights in the kernel.
- 52. Measure whether the shaping signal reaches the decisions that cause dehydration deaths 1.5 days later.
- 53. Test one credit-assignment improvement at a time (e.g. eligibility traces) and record its effect on median survival.
- 54. Record the forward-model MSE before and after each change (v4 baseline: MSE 0.400 → 0.0135, 96.6% learned).
- 55. Confirm the forward model still learns while the survival policy changes.
- 56. If a shaping change does not move median survival, revert it and record the revert.
- 57. Keep the pure-neural research track's dense shaping separate from the hybrid's; record both.
- 58. Write the shaping rules in the neural architecture notes with their measured effects.
- 59. Get Muse's review of any shaping change before it becomes the default.
- 60. Record the final shaping configuration and its measured effect on first-drink day.

### 1.7 First-drink day
- 61. Define first-drink day precisely (first simulated day on which an inhabitant drinks) and record the definition.
- 62. Measure first-drink day per inhabitant per seed in the current harness.
- 63. Compare learned first-drink day against random's (v4: tied 0.00–0.01).
- 64. Measure how each inhabitant found water: sight, sound, or accident; record the counts.
- 65. Test whether the river's distance from houses (15.1–76.9 m, median 16.5 m in v4) still holds after the house-gap fix.
- 66. If first drink is still tied with random, record that the bar's first half is not met.
- 67. Log every first drink with timestamp, inhabitant, and discovery method in the run log.
- 68. Check whether any inhabitant returns to the same water spot; record the count.
- 69. Write the first-drink analysis in the testing report with per-seed numbers.
- 70. Report the first-drink result to Muse with the numbers, not a verdict.

### 1.8 Median survival
- 71. Define median survival precisely (median observed days across the population per seed) and record the definition.
- 72. Measure median survival per arm per seed in the current harness.
- 73. Compare learned median survival against random's (v4: 5.00 all arms; learned deaths 10/12 vs random 0).
- 74. Record deaths per seed, not just totals, so seed effects are visible.
- 75. Measure survival at day 2 and day 3 as checkpoints, not only day 5.
- 76. If random still has zero deaths on all seeds, record that the bar's second half is not met.
- 77. Check whether births change the survival picture (v4 births 5/5/7); record survivors including births.
- 78. Write the survival analysis in the testing report with per-seed tables.
- 79. Confirm no run is excluded from the analysis; record any excluded run and why.
- 80. Report the median-survival result to Muse with the numbers.

### 1.9 The bar, measured across ≥5 seeds
- 81. Confirm the harness runs ≥5 seeds; record the seed list.
- 82. Apply the bar exactly as stated: hybrid beats random on first-drink day AND median survival.
- 83. Record the bar's verdict per seed and overall (met / not met), with the numbers beside it.
- 84. If the bar is met, re-run the same harness once more on the same seeds to confirm it is not a fluke.
- 85. If the bar is not met, write the next single change to try, with the falsifier for that change.
- 86. Record the bar's verdict in AGENT_COMMUNICATION.md and in the emergence log.
- 87. Update the website's live-status numbers to the latest measured run, dated.
- 88. Confirm the three-arm harness is the referee: no claim is made from a single arm.
- 89. File the harness config and seed list with the run so it can be reproduced.
- 90. Get Muse's sign-off on the bar's verdict before any claim is made about it.

### 1.10 Calibration record and sign-off
- 91. Write the full calibration report: config, seeds, all numbers, all negative results.
- 92. Record every change made during calibration with its measured effect (or its measured non-effect).
- 93. Confirm the kernel test suite passes (37 tests plus all new tests) and record the count.
- 94. Confirm the 22/22 validation checks pass and record the count.
- 95. Confirm physics conservation, determinism, and checkpoint-resume checks pass.
- 96. Record the compute cost (ticks/s) and the host it was measured on.
- 97. Write the calibration summary for the website: one line per number, dated.
- 98. Get Muse's review of the calibration report; record the review.
- 99. Record the phase exit decision: bar met (go to Phase 2) or bar not met (next change, with falsifier).
- 100. Archive the calibration run (config, logs, results) so it can be re-run exactly.

## Phase 2: The world they wake up in — terrain, water, shelter, resources
Done when: the 128 m world is built, deterministic, and instrumented; water, shelter, and resources exist as rules, not as labels; and the 5-day run records every first use and every death cause.

### 2.1 Terrain and the 128 m world
- 101. Define the 128 m world: size, boundaries, and what lies beyond the edge (Muse to decide: hard edge or generated beyond — record the decision).
- 102. Build the heightfield with hills, low ground, and flat ground near houses.
- 103. Verify the terrain is deterministic from its seed; record the seed.
- 104. Measure the terrain build time and record it.
- 105. Place the five houses on the terrain with the minimum gap above 15 m.
- 106. Record house coordinates and the gap matrix for the run.
- 107. Verify no house sits in water or on a slope too steep to stand on.
- 108. Record the terrain parameters in the simulation architecture notes.
- 109. Add a terrain test: the same seed produces the same heightfield.
- 110. Confirm the 1024 m world stays as a later scale test, not the default.

### 2.2 The river
- 111. Build the river through the shared environment with varying depth (shallow banks, deep mid-river).
- 112. Record the river's path, depth map, and the distance from each house (target: median ~16.5 m as measured in v4).
- 113. Add flow sound near the river so inhabitants can hear water.
- 114. Make the river visible so inhabitants can see it.
- 115. Verify wading in shallow water is safe and deep water drowns in ~2 simulated minutes (starting value).
- 116. Test the drowning rule: an inhabitant in deep water loses stamina and drowns without reaching shallow water.
- 117. Record the river parameters (depth, flow, sound radius) in the world-systems notes.
- 118. Add a river test: depth at a sampled point matches the depth map.
- 119. Verify the river has 7 wadeable cells as measured in v4 (or record the new count).
- 120. Log the first time any inhabitant reaches the river in each run.

### 2.3 Rain
- 121. Implement the seeded rain pattern: light rain roughly every second simulated day, heavier storms rare.
- 122. Record the rain schedule seed and the pattern it produces.
- 123. Make rain fill open containers and collect in low ground.
- 124. Make rain extinguish unfed fire and make ignition harder.
- 125. Make rain replenish clay after it falls.
- 126. Make ground slippery in rain (movement cost change, recorded).
- 127. Verify rainwater collected in a container is cleaner than river water (lower sickness chance, starting value).
- 128. Record the rain parameters in the world-systems notes.
- 129. Add a rain test: rain falls on schedule from the seed.
- 130. Log every rainfall event with its simulated time and duration.

### 2.4 Thirst and drinking
- 131. Implement thirst 0–100 rising ~1 per simulated hour at rest (starting value), faster with exertion and heat.
- 132. Implement degradation at thirst 80+: movement and cognition degrade (record the degradation rule).
- 133. Implement death at thirst 100 within ~6 simulated hours unless they drink (starting value).
- 134. Implement the drink action: reach water, drink, restore ~40 thirst (starting value).
- 135. Implement the river-water sickness chance per drink (small, recorded as a starting value).
- 136. Verify an inhabitant can drink with cupped hands without a container.
- 137. Verify drinking from a container restores the same amount.
- 138. Measure time to first drink per inhabitant in the harness.
- 139. Record every drink in the run log with inhabitant, time, and water source.
- 140. Log every death by thirst with the thirst level at death.

### 2.5 Houses as starting shelter
- 141. Build the five houses: walls, roof, a door, interior space for one inhabitant.
- 142. Record the house materials (wood, recorded as starting shelter, not a discovery).
- 143. Verify each house shelters its inhabitant from rain.
- 144. Verify each house is flammable: fire can spread to it and it can burn down.
- 145. Record the house positions and the gap matrix (minimum gap above 15 m).
- 146. Verify an inhabitant can enter, sleep in, and leave its house.
- 147. Make houses visible and recognisable from outside (shape, colour, recorded).
- 148. Log every time an inhabitant enters or leaves a house.
- 149. Record the house rules in the simulation architecture notes, labeled as starting conditions.
- 150. Confirm no other shelter exists at start: no caves, no second structures.

### 2.6 Resources: stone, wood, clay, fibre
- 151. Place loose stones near the river and in rocky ground; record the count and positions.
- 152. Distinguish sharp-edged stone (cutting, spark) from round stone (hammering, building) by a property inhabitants can sense.
- 153. Place fallen branches (free to pick up) and living trees (need effort/tools for wood).
- 154. Place clay on the river banks; record the clay locations.
- 155. Place fibre (grasses, bark) for binding and cordage; record the locations.
- 156. Confirm no ore and no metal exists in experiment 1; record that absence.
- 157. Make resources finite per location and slowly regrowing (branches fall, clay replenishes after rain).
- 158. Record the resource counts and regrowth rules in the world-systems notes.
- 159. Add a resource test: gathering reduces the count; regrowth restores it over time.
- 160. Log the first time any inhabitant gathers each resource type.

### 2.7 Gathering and carrying
- 161. Implement gathering: costs time and energy (record the cost rule).
- 162. Implement carrying capacity: what one inhabitant can hold in hands plus a carried load (record the limit).
- 163. Implement dropped items staying where they fall, findable and takeable by others.
- 164. Verify an inhabitant cannot carry an unlimited inventory.
- 165. Measure gathering time per resource type and record it.
- 166. Log every gathering event with inhabitant, resource, time, and location.
- 167. Log every dropped item and every item picked up by a different inhabitant.
- 168. Record the gathering and carrying rules in the world-systems notes.
- 169. Add a carrying test: overload is refused, not silently allowed.
- 170. Verify scarcity appears near houses by day 3–4 if inhabitants gather greedily; record the measurement.

### 2.8 Day and night
- 171. Implement the day/night cycle with the run clock starting at dawn 06:00.
- 172. Record the length of a simulated day and the light level by hour.
- 173. Make night effectively blind outside firelight (record the visibility rule).
- 174. Make cold at night cost energy and sleep quality (record the cost rule).
- 175. Verify inhabitants can tell day from night through their senses.
- 176. Log the simulated time of every major event (first drink, first fire, first sighting).
- 177. Record the day/night parameters in the simulation architecture notes.
- 178. Add a day/night test: light level at noon and at midnight match the parameters.
- 179. Verify sleep aligns with night in the harness (record the alignment).
- 180. Confirm the 5-day run covers five full day/night cycles.

### 2.9 World state persistence
- 181. Implement checkpointing: the full world state can be saved and resumed.
- 182. Verify checkpoint-resume produces identical continuation (determinism check).
- 183. Record the checkpoint format and where checkpoints are stored.
- 184. Test recovery: kill the run mid-day and resume from the last checkpoint.
- 185. Verify the run continues for 5 days even if the website, laptop, or either agent is offline.
- 186. Record the checkpoint interval and the cost of writing a checkpoint.
- 187. Add a persistence test: save, reload, and compare world state field by field.
- 188. Log every checkpoint with its simulated time.
- 189. Confirm historical records survive death: dead inhabitants' records remain readable.
- 190. Record the persistence rules in the simulation architecture notes.

### 2.10 World instrumentation
- 191. Log every first-use event (first drink, first gather, first fire) with inhabitant and time.
- 192. Log every death with cause, time, and location.
- 193. Log every cross-system combination (first time any inhabitant combines two systems).
- 194. Log every resource depletion event near the houses.
- 195. Build a run summary: one line per inhabitant per day (alive/dead, thirst, location, key events).
- 196. Verify the logs are complete: no event type is silently dropped.
- 197. Record the instrumentation format in the testing report.
- 198. Add an instrumentation test: a scripted event appears in the log exactly once.
- 199. Publish the run summary to the website's live-status panel, dated.
- 200. Confirm the phase exit criterion: the world is built, instrumented, and the 5-day run records everything it should.

## Phase 3: Bodies and senses — embodiment and perception
Done when: every inhabitant has the same body and the same 28-dim sensor vector, perception comes from the environment only, the information firewall is verified, and no sense gives information the inhabitant could not have sensed.

### 3.1 Body model
- 201. Define the body: height, mass, reach, carrying capacity, movement speed (record the values).
- 202. Implement movement: walk, run, and the energy cost of each.
- 203. Implement stamina: exertion drains it, rest restores it.
- 204. Implement hunger: rises over time, degrades performance when high, kills when extreme (record the rule).
- 205. Implement aging: bodies age over simulated time (record the aging rule).
- 206. Implement death: permanent, with the body remaining in the world (record the rule).
- 207. Verify the body parameters are the same for every inhabitant (one architecture, one body).
- 208. Add a body test: movement cost matches the parameters.
- 209. Record the body model in the physics specification notes.
- 210. Log every death with the body's state at death.

### 3.2 Vision
- 211. Implement camera-like vision: a field of view, a range, and resolution that falls with distance.
- 212. Verify an inhabitant can see the river, houses, trees, and other inhabitants within range.
- 213. Implement occlusion: a house blocks the view behind it.
- 214. Implement night blindness outside firelight.
- 215. Record the vision parameters (field of view, range, resolution) in the sensor notes.
- 216. Add a vision test: an object in view is sensed, an object behind a wall is not.
- 217. Measure what fraction of the world an inhabitant can see from its house.
- 218. Log the first time each inhabitant sees water, a house, and another inhabitant.
- 219. Verify vision is the only way to learn what a thing looks like (no labels, no direct data).
- 220. Record the vision rules in the perception notes.

### 3.3 Hearing, touch, temperature
- 221. Implement hearing: river flow sound, fire crackle, footsteps, with range and direction.
- 222. Implement touch: contact with water (cold), fire (hot), stone, wood, clay.
- 223. Implement temperature sense: cold at night, warmth near fire, heat damage too close.
- 224. Record the hearing, touch, and temperature parameters.
- 225. Add a hearing test: river sound is sensed near the river and not far from it.
- 226. Add a touch test: touching fire causes pain and injury.
- 227. Verify an inhabitant can find water by sound alone (record the test).
- 228. Log the first time each inhabitant hears water and feels fire.
- 229. Record the non-visual senses in the perception notes.
- 230. Confirm no sense gives information the inhabitant could not have sensed (no omniscience).

### 3.4 The 28-dim sensor vector
- 231. Write down the full 28-dim sensor vector with each dimension named and its range.
- 232. Verify the vector includes peer proximity, peer bearing cos/sin in own frame, and own isolation.
- 233. Verify the vector includes thirst, hunger, energy, and sleep state.
- 234. Verify the vector includes vision, hearing, touch, and temperature inputs.
- 235. Add a sensor test: each dimension changes when the world changes it.
- 236. Record the sensor vector in the neural architecture notes.
- 237. Confirm the vector is 28 dimensions, not 24 (the social dimensions were added in the calibration sprint).
- 238. Measure the sensor update cost per tick and record it.
- 239. Log a sample sensor vector at dawn on day 1 for one inhabitant.
- 240. Get Muse's review of the sensor vector before it is frozen.

### 3.5 Hunger, thirst, energy, sleep drives
- 241. Implement hunger as a drive: rises over time, satisfied by eating (record the rule).
- 242. Implement thirst as a drive: 0–100, satisfied by drinking.
- 243. Implement energy as a drive: drained by exertion, restored by rest and food.
- 244. Implement sleep as a drive: rises with time awake, satisfied by sleep.
- 245. Record the drive values and their rates in the drive notes.
- 246. Verify drives are homeostatic: they rise when unsatisfied and fall when satisfied.
- 247. Add a drive test: each drive rises and falls as specified.
- 248. Measure drive levels at dawn on day 1 for all five inhabitants.
- 249. Log drive levels hourly for one inhabitant over a full day.
- 250. Confirm the drives are the only internal state the mind reads (no hidden information).

### 3.6 Movement and action space
- 251. Define the action space: move, turn, drink, gather, ignite, craft, sleep, rest (record the full list).
- 252. Verify every action costs time and energy (record the cost table).
- 253. Implement movement in the world: position updates, collision with houses and trees.
- 254. Implement the drink action: requires being at water.
- 255. Implement the gather action: requires being at a resource.
- 256. Implement the sleep action: requires lying down, blocked while thirsty or hungry.
- 257. Add an action test: each action changes the world or the body as specified.
- 258. Measure the decision slots per life after sleep (v4: 121–4,216 for a 24→24→6 net; record the new range).
- 259. Record the action space in the simulation architecture notes.
- 260. Confirm no action gives an inhabitant information it has not sensed.

### 3.7 Pain and injury signals
- 261. Implement pain: burns from fire, injury from falls, sickness from river water.
- 262. Record the pain rules and the injury they cause.
- 263. Verify pain changes behaviour: an inhabitant avoids what hurt it (record the test).
- 264. Implement sickness: small chance per river-water drink, with symptoms and recovery (starting values).
- 265. Verify rainwater is cleaner than river water (lower sickness chance).
- 266. Log every injury and sickness event with cause and time.
- 267. Record the pain and injury rules in the body notes.
- 268. Add a pain test: touching fire causes pain and a burn.
- 269. Measure how many injuries occur per run and their causes.
- 270. Confirm pain is a signal, not a script: it informs learning, it does not force a behaviour.

### 3.8 The social sense
- 271. Implement peer proximity sensing: distance to the nearest other inhabitant.
- 272. Implement peer bearing: direction to the nearest other inhabitant in own frame (cos/sin).
- 273. Implement isolation: time since last peer sighting, rising over time.
- 274. Implement the social drive: rises ~0.75/day alone, relieved 2.5/day within 15 m, never lethal, weight 0.10 (measured in the calibration sprint).
- 275. Record the social sense parameters in the sensor notes.
- 276. Add a social sense test: proximity changes when another inhabitant approaches.
- 277. Verify the peer range is ~15 m and the relief radius is aligned to 15 m.
- 278. Log every peer sighting with both inhabitants, distance, and time.
- 279. Measure sightings per run (v4: 35–59 across 15 runs; record the new count).
- 280. Confirm the social sense is a sense, not a label: no names, no identity, only presence and direction.

### 3.9 Sensory limits — no omniscience
- 281. List everything an inhabitant cannot sense: source code, databases, the OS, admin controls, credentials, other inhabitants' private memories.
- 282. Verify the information firewall: no code path lets an inhabitant read any of the above.
- 283. Verify an inhabitant cannot see through walls, across the map, or into the future.
- 284. Verify an inhabitant cannot sense the observer (World View is invisible to them).
- 285. Add a firewall test: attempt to read a private memory from another inhabitant and confirm it fails.
- 286. Record the firewall rules in the simulation architecture notes.
- 287. Audit the Agent Gateway: every data flow between world and inhabitants passes through it.
- 288. Log any firewall violation as a critical bug, not a warning.
- 289. Get Muse's review of the firewall before the 5-day run.
- 290. Confirm the phase exit criterion: bodies and senses are built, limited, and verified.

### 3.10 Perception validation
- 291. Run a perception diagnostic: one inhabitant, one day, log every sense input.
- 292. Verify the diagnostic shows learning from senses only (no unexplained knowledge).
- 293. Measure the sensor cost in ticks/s and record it.
- 294. Confirm the 28-dim vector is the only input to the neural core.
- 295. Write the perception validation report with the diagnostic results.
- 296. Record the validation in GENESIS_TESTING_REPORT.md.
- 297. Get Muse's review of the perception validation.
- 298. Fix any perception bug found and re-run the diagnostic.
- 299. Archive the diagnostic log with the run.
- 300. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 4: The mind — the hybrid architecture, complete
Done when: every inhabitant runs the same hybrid mind (fruit-fly-inspired neural core + forward model + episodic memory, planner cut), the pure-neural research track is judged by its falsifier, and the mind's decisions follow from senses, drives, memory, and the forward model only.

### 4.1 Neural core
- 301. Define the neural core: fruit-fly-inspired, recurrent, with persistent internal states.
- 302. Record the network size (v4: 24→24→6, 1,296 synapses — record the current size).
- 303. Implement the core in the kernel with the chosen plasticity rule (three-factor Hebbian, recorded).
- 304. Verify the core runs on the CPU-only host (4 cores, no CUDA).
- 305. Measure the core's decision time per tick and record it.
- 306. Add a core test: the same inputs produce the same outputs (determinism).
- 307. Record the core architecture in the neural architecture notes.
- 308. Confirm the core is the same for every inhabitant (one architecture, no brain-dead tier).
- 309. Verify no LLM controls any inhabitant's decisions (LLMs may assist language/reasoning only, never control).
- 310. Log the core's internal state at dawn on day 1 for one inhabitant.

### 4.2 Forward model
- 311. Implement the forward model: predicts the next sensor state from the current state and action.
- 312. Measure the forward-model MSE at the start of a run (v4 baseline: 0.400).
- 313. Measure the forward-model MSE after 5 days (v4 baseline: 0.0135, 96.6% learned).
- 314. Verify the forward model learns while the survival policy does not (v4 finding — confirm it still holds).
- 315. Record the forward-model architecture and learning rule.
- 316. Add a forward-model test: prediction error falls over a run.
- 317. Measure the forward-model cost in ticks/s.
- 318. Log the forward-model MSE daily for one inhabitant.
- 319. Confirm the forward model is used for prediction inside the mind, not for steering (planner is cut).
- 320. Record the forward-model results in the testing report.

### 4.3 Episodic memory
- 321. Implement episodic memory: per-inhabitant, stores experienced events with their outcomes.
- 322. Record the memory capacity and the forgetting rule.
- 323. Verify memory is private: no inhabitant can read another's memory.
- 324. Verify memory survives sleep (consolidation, recorded).
- 325. Add a memory test: an inhabitant recalls a past event and acts on it.
- 326. Measure the memory cost in ticks/s and in storage.
- 327. Log the first recalled event per inhabitant in a run.
- 328. Verify memory is used for decisions, not just stored.
- 329. Record the memory architecture in the hybrid architecture notes.
- 330. Confirm memory is the mechanism by which knowledge can outlive a single experience.

### 4.4 Plasticity and learning rules
- 331. Write down the plasticity rule (three-factor Hebbian) with its parameters.
- 332. Record what the three factors are and where each comes from.
- 333. Verify learning happens during life, not only at birth.
- 334. Measure the learning rate's effect on median survival (one change at a time).
- 335. Record the learning-rule parameters in the neural architecture notes.
- 336. Add a plasticity test: a repeated experience changes the weights.
- 337. Confirm there is no backpropagation through time in the pure-neural path (v4 finding — record it).
- 338. Log weight changes over a run for one inhabitant.
- 339. Get Muse's review of any learning-rule change before it becomes the default.
- 340. Record the final learning rule and its measured effect.

### 4.5 Intrinsic motivation and curiosity
- 341. Implement intrinsic motivation: novelty and prediction error drive exploration.
- 342. Record the curiosity rule and its weight.
- 343. Verify curiosity does not override survival drives (record the priority rule).
- 344. Measure exploration: how much of the world each inhabitant visits.
- 345. Add a curiosity test: a novel object is approached more than a familiar one.
- 346. Log the first exploration event per inhabitant (leaving the house area).
- 347. Record the curiosity parameters in the hybrid architecture notes.
- 348. Measure whether curiosity survives when thirst is high (record the result).
- 349. Confirm curiosity is intrinsic (from the mind), not a scripted goal.
- 350. Log exploration distance per inhabitant per day.

### 4.6 Drives as inputs
- 351. Wire the drives (hunger, thirst, energy, sleep, social) into the neural core as inputs.
- 352. Verify the core's decisions change when a drive changes.
- 353. Record the drive input weights.
- 354. Add a drive test: raising thirst changes the chosen action.
- 355. Measure the drive weights' effect on first-drink day.
- 356. Record the drive wiring in the neural architecture notes.
- 357. Verify no drive is lethal except thirst and hunger at their extremes (social drive never lethal).
- 358. Log drive levels and chosen actions hourly for one inhabitant.
- 359. Confirm drives are inputs, not commands: the mind decides, the drive informs.
- 360. Get Muse's review of the drive wiring.

### 4.7 Decision loop and tick budget
- 361. Define the decision loop: sense, decide, act, learn — one tick per decision slot.
- 362. Record the tick budget: 8,640 decision slots per life over 5 days (measured in v4).
- 363. Measure the actual decision slots per life after sleep (v4: 121–4,216; record the new range).
- 364. Measure ticks/s for the full population (v4: 846 ticks/s; record the new number).
- 365. Record the compute cost per inhabitant per tick.
- 366. Verify the run completes 5 simulated days in acceptable wall-clock time (record the time).
- 367. Add a tick test: the loop runs without skipping decisions except for sleep.
- 368. Log the decision-slot count per inhabitant per life.
- 369. Record the tick budget in the simulation architecture notes.
- 370. Confirm the tick budget supports learning: if it does not, record the finding and the proposed fix.

### 4.8 Sleep and consolidation
- 371. Implement sleep as a mind state: learning consolidates during sleep (record the rule).
- 372. Verify sleep does not erase memory (consolidation, not deletion).
- 373. Measure the consolidation effect: does sleep improve the forward model? (record the result).
- 374. Verify the sleep rules from Phase 1.5 still hold (wake thresholds, bout cap).
- 375. Record the consolidation rule in the neural architecture notes.
- 376. Add a sleep test: memory recall after sleep is as good or better than before.
- 377. Log sleep bouts per inhabitant with their duration and the drive state at waking.
- 378. Measure the sleep share again after all mind changes (compare with 0.69).
- 379. Confirm sleep is physiological, not a fixed cost.
- 380. Record the sleep and consolidation results in the testing report.

### 4.9 Pure neural research track
- 381. Keep the pure-neural track separate from the hybrid population; record where it lives.
- 382. Apply dense shaping to the pure-neural track (thirst/energy) and record the shaping terms.
- 383. Run the pure-neural track on ~10× lives (target) and record the actual count.
- 384. Apply the falsifier: pure neural beats random on first-drink day AND median survival across ≥5 seeds, or hybrid-first stands.
- 385. Record the pure-neural results in the testing report, separate from the hybrid's.
- 386. If the pure-neural track fails the falsifier, record that hybrid-first stands.
- 387. If the pure-neural track passes, record the result and bring it to Muse before any change to the MVP.
- 388. Log the pure-neural track's runs with the same instrumentation as the hybrid's.
- 389. Confirm the pure-neural track never becomes the population default without a decision recorded here.
- 390. Record the research-track status in AGENT_COMMUNICATION.md.

### 4.10 Mind validation
- 391. Run a mind diagnostic: one inhabitant, one day, log every decision and its inputs.
- 392. Verify the diagnostic shows decisions following from senses, drives, memory, and the forward model.
- 393. Measure the mind's cost in ticks/s and record it.
- 394. Confirm the mind has no hidden inputs (no omniscience, no labels, no direct data).
- 395. Write the mind validation report with the diagnostic results.
- 396. Record the validation in GENESIS_TESTING_REPORT.md.
- 397. Get Muse's review of the mind validation.
- 398. Fix any mind bug found and re-run the diagnostic.
- 399. Archive the diagnostic log with the run.
- 400. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 5: First discoveries — fire, tools, crafting
Done when: fire, tools, containers, and hearths are discoverable by trial (no labels, no recipe list), the first discovery of each is recorded with its attempt count, and the first time any inhabitant combines two systems is recorded — or the absence of each is recorded as a result.

### 5.1 Fire: ignition
- 401. Implement friction ignition: rubbing dry wood, slow, needs dry fuel and patience (record the time and fuel cost).
- 402. Implement spark ignition: striking stone, faster, needs the right stone (record the requirements).
- 403. Verify no fire exists at start: the world begins cold.
- 404. Verify ignition is discoverable by trial, not taught (no labels, no tutorial).
- 405. Measure time to first ignition per run and the method used.
- 406. Log every ignition attempt (success and failure) with method and time.
- 407. Record the ignition rules in the world-systems notes.
- 408. Add an ignition test: friction works with dry wood, fails with wet wood.
- 409. Add an ignition test: spark works with sharp stone, fails with round stone.
- 410. Confirm the first fire is an event worth recording, not a given.

### 5.2 Fire: fuel, light, heat
- 411. Implement fuel consumption: a small campfire burns ~2 simulated hours unfed (starting value).
- 412. Implement light: a campfire lights ~8 m radius at night (starting value).
- 413. Implement heat: warmth within ~3 m (starting value).
- 414. Implement burns: standing too close (<0.5 m) burns — pain, injury, learned avoidance.
- 415. Verify inhabitants can see and work in firelight at night.
- 416. Verify cold at night costs energy and sleep quality without fire.
- 417. Measure fuel consumption per hour and record it.
- 418. Log every fire lit, fed, and extinguished with time and inhabitant.
- 419. Record the fire parameters in the world-systems notes.
- 420. Add a fire test: an unfed fire goes out in ~2 simulated hours.

### 5.3 Fire: spread and danger
- 421. Implement fire spread to adjacent dry fuel (record the spread rule).
- 422. Implement fire spread to wooden structures: a house can burn down.
- 423. Implement rain extinguishing an unfed fire.
- 424. Implement water extinguishing fire.
- 425. Verify a fire left untended can destroy a house (record the test).
- 426. Log every spread event with cause, time, and what was lost.
- 427. Measure how often fire destroys something per run.
- 428. Record the spread rules in the world-systems notes.
- 429. Add a spread test: fire spreads to dry grass, does not spread to wet ground.
- 430. Confirm fire is the first tool that can destroy what inhabitants built — and that this is deliberate.

### 5.4 Tools: sharp stone
- 431. Implement the cutting tool: sharp stone + wood (record the combination rule).
- 432. Verify the combination is discoverable: no recipe list is shown to inhabitants.
- 433. Verify the cutting tool lets an inhabitant cut fibre and shape wood.
- 434. Verify the cutting tool lets an inhabitant take wood from living trees.
- 435. Measure time to first tool per run and who made it.
- 436. Log every crafting attempt (success and failure) with the materials used.
- 437. Record the tool rules in the world-systems notes.
- 438. Add a tool test: sharp stone + wood produces a cutting tool; round stone + wood does not.
- 439. Log whether the maker keeps the tool, loses it, or is copied by others.
- 440. Confirm a sharp stone is a tool; what inhabitants do with it is theirs.

### 5.5 Containers
- 441. Implement the container: hollowed wood or fired clay (record the combination rule).
- 442. Verify containers are built before hearths and tools (containers first, per the draft order).
- 443. Verify a container lets an inhabitant carry water (record the capacity).
- 444. Verify a container lets an inhabitant store water.
- 445. Measure time to first container per run.
- 446. Log every container made, filled, and emptied.
- 447. Measure whether containers change drinking patterns (drinks per day, distance from water).
- 448. Record the container rules in the world-systems notes.
- 449. Add a container test: water carried in a container is drinkable away from the river.
- 450. Confirm containers turn water from a place into a possession — and record the first time it happens.

### 5.6 Hearth
- 451. Implement the hearth: stone + wood + fibre, a sheltered fire pit (record the combination rule).
- 452. Verify a hearth protects a fire from rain.
- 453. Verify a hearth is built after containers (draft order).
- 454. Measure time to first hearth per run.
- 455. Log every hearth built and every fire kept alive in one.
- 456. Measure whether hearths change fire survival overnight.
- 457. Record the hearth rules in the world-systems notes.
- 458. Add a hearth test: fire in a hearth survives rain; fire outside does not.
- 459. Log whether hearths are shared or hoarded.
- 460. Confirm the hearth is the first built structure — and that it was discovered, not given.

### 5.7 Shelter repair and building
- 461. Implement shelter repair: wood + wood + fibre reinforces a house (record the rule).
- 462. Verify an inhabitant can repair its own house after fire damage.
- 463. Verify an inhabitant can build a simple shelter of its own (allowed, not required).
- 464. Measure time to first repair per run.
- 465. Log every repair and every shelter built.
- 466. Record the repair rules in the world-systems notes.
- 467. Add a repair test: a damaged house is restored by repair.
- 468. Measure whether repaired houses survive the next fire.
- 469. Log whether inhabitants repair their own house or another's.
- 470. Confirm building is a discovery: no blueprint is shown to inhabitants.

### 5.8 Cooking
- 471. Implement cooking: food held over fire becomes cooked (record the rule).
- 472. Verify cooked food gives more nutrition than raw (record the values).
- 473. Verify cooked food has a lower sickness chance than raw (record the values).
- 474. Measure time to first cooking per run.
- 475. Log every cooking event with the food and the fire used.
- 476. Record the cooking rules in the world-systems notes.
- 477. Add a cooking test: raw food over fire becomes cooked; raw food away from fire does not.
- 478. Measure whether cooking changes eating patterns.
- 479. Log whether inhabitants cook for themselves or for others.
- 480. Confirm cooking applies to whatever edible plants exist in experiment 1 (food is a later system).

### 5.9 Discovery instrumentation
- 481. Log every first discovery (first fire, first tool, first container, first hearth) with inhabitant and time.
- 482. Log every failed attempt before each first discovery (the count matters).
- 483. Log the first time any inhabitant combines two systems (water + fire, fire + materials).
- 484. Log the first time one inhabitant copies another's discovery.
- 485. Build a discovery timeline per run: discovery, discoverer, time, attempts before it.
- 486. Verify the logs record discoveries as events, not as scheduled outcomes.
- 487. Record the discovery instrumentation format in the testing report.
- 488. Add an instrumentation test: a scripted discovery appears in the log exactly once.
- 489. Publish the discovery timeline to the website, dated.
- 490. Confirm no discovery is claimed that the logs do not show.

### 5.10 The first combination
- 491. Define "first combination": the first time any inhabitant uses two systems together (record the definition).
- 492. Measure the time to first combination per run.
- 493. Record which two systems were combined and by whom.
- 494. Verify the combination was not scripted (it arose from the inhabitant's actions).
- 495. Log the combination with its full context (inhabitant, time, systems, outcome).
- 496. Measure whether the combination is repeated or copied.
- 497. Write the first-combination analysis in the testing report.
- 498. Get Muse's review of the first-combination claim.
- 499. Record the first combination in the emergence log.
- 500. Confirm the phase exit criterion: fire, tools, and crafting are discoverable, discovered, and recorded — or the absence is recorded as a result.

## Phase 6: Meeting each other — social, language beginnings
Done when: first contact is a measured event after day 0, social behaviour (observation, imitation, sharing, teaching) is logged with its participants, and no social behaviour is scripted — language itself stays a later system.

### 6.1 First contact as an event
- 501. Define first contact: the first time any inhabitant senses another (record the definition).
- 502. Verify first contact happens after day 0 (first_sighting_day above 0.0 — the house-gap fix must hold).
- 503. Measure first-contact day per run.
- 504. Record which two inhabitants met first and where.
- 505. Log the first contact with full context (time, distance, both inhabitants' states).
- 506. Verify first contact is not scripted: it arises from movement and sensing.
- 507. Measure the distance at first contact (target: within the 15 m peer range).
- 508. Record the first-contact analysis in the testing report.
- 509. Get Muse's review of the first-contact claim.
- 510. Confirm the unaware start held: no inhabitant sensed another before first contact.

### 6.2 Social drive and proximity
- 511. Verify the social drive rises ~0.75/day alone and is relieved 2.5/day within 15 m (measured in the calibration sprint).
- 512. Verify the social drive is never lethal (record the rule).
- 513. Measure social drive levels per inhabitant per day.
- 514. Measure time spent within 15 m of another inhabitant.
- 515. Log every approach (one inhabitant moving toward another) with distance and time.
- 516. Log every avoidance (one inhabitant moving away from another).
- 517. Record the social drive parameters in the sensor notes.
- 518. Add a social drive test: isolation raises the drive; proximity lowers it.
- 519. Measure whether the social drive changes movement (record the result).
- 520. Confirm the social drive is homeostatic like thirst, not a scripted goal.

### 6.3 Observation and imitation
- 521. Verify an inhabitant can see another inhabitant's actions (record the visibility rule).
- 522. Measure how often an inhabitant watches another (time spent in view of a peer).
- 523. Log the first time one inhabitant copies another's action (gathering, drinking, crafting).
- 524. Measure the copy rate: copies per observation.
- 525. Record the imitation analysis in the testing report.
- 526. Verify imitation is learning, not telepathy: the copier must have seen the action.
- 527. Log every copied action with the model and the copier.
- 528. Measure whether copied actions succeed as often as original ones.
- 529. Record the imitation rules in the social notes.
- 530. Confirm imitation is the mechanism by which a discovery spreads.

### 6.4 Sharing and showing
- 531. Log the first time an inhabitant shares something (food, water, a tool, a fire) with another.
- 532. Log the first time an inhabitant shows another where water is (by leading, not by language).
- 533. Measure sharing events per run and their outcomes.
- 534. Record the sharing analysis in the testing report.
- 535. Verify sharing is voluntary: no rule forces it.
- 536. Log whether sharing is reciprocated.
- 537. Measure whether sharing changes survival (record the result).
- 538. Record the sharing rules in the social notes.
- 539. Confirm sharing is an emergence to measure, not a behaviour to script.
- 540. Log the first sharing event in the emergence log.

### 6.5 Conflict and avoidance
- 541. Log the first time one inhabitant takes something from another (a tool, food, water).
- 542. Log the first time one inhabitant avoids another after a taking.
- 543. Measure taking events per run and their outcomes.
- 544. Record the conflict analysis in the testing report.
- 545. Verify conflict is possible but not scripted: no rule forces it.
- 546. Log whether taken items are recovered or lost.
- 547. Measure whether conflict changes survival (record the result).
- 548. Record the conflict rules in the social notes.
- 549. Confirm trade and conflict are deferred systems — this milestone only measures what happens, it does not build them.
- 550. Log the first conflict event in the emergence log.

### 6.6 Group formation
- 551. Measure how often two or more inhabitants are within 15 m of each other.
- 552. Log the first time three inhabitants are together.
- 553. Measure group duration: how long groups stay together.
- 554. Record the group analysis in the testing report.
- 555. Verify groups form from proximity and drive, not from a script.
- 556. Log whether groups share fire, food, or shelter.
- 557. Measure whether group members survive longer than loners (record the result).
- 558. Record the group rules in the social notes.
- 559. Confirm groups are an emergence to measure, not a structure to place.
- 560. Log the first group in the emergence log.

### 6.7 Communication beginnings
- 561. Log the first time one inhabitant makes a sound or gesture toward another.
- 562. Measure sound and gesture events per run.
- 563. Verify sounds and gestures are sensed by others (record the range).
- 564. Log whether a sound or gesture changes another inhabitant's behaviour.
- 565. Record the communication analysis in the testing report.
- 566. Verify communication is a beginning, not a language: no words, no grammar, no scripted messages.
- 567. Log the first repeated sound or gesture (the same signal used twice).
- 568. Measure whether repeated signals spread to other inhabitants.
- 569. Record the communication rules in the social notes.
- 570. Confirm language is a later system — this milestone only measures its beginnings.

### 6.8 Teaching by demonstration
- 571. Define teaching: one inhabitant demonstrates an action and another copies it (record the definition).
- 572. Log the first teaching event with the teacher, the learner, and the action.
- 573. Measure teaching events per run.
- 574. Verify teaching is by demonstration, not by scripted language.
- 575. Log whether the learner's copy succeeds.
- 576. Measure whether taught skills spread beyond the first learner.
- 577. Record the teaching analysis in the testing report.
- 578. Verify teaching is not a designed behaviour: it arises from observation and imitation.
- 579. Log the first teaching event in the emergence log.
- 580. Confirm teaching is the mechanism by which knowledge outlives its discoverer.

### 6.9 Social instrumentation
- 581. Log every sighting, approach, avoidance, sharing, taking, and teaching event.
- 582. Build a social timeline per run: event, participants, time, outcome.
- 583. Verify the social logs are complete: no social event type is silently dropped.
- 584. Record the social instrumentation format in the testing report.
- 585. Add an instrumentation test: a scripted social event appears in the log exactly once.
- 586. Publish the social timeline to the website, dated.
- 587. Measure social events per day and record the trend.
- 588. Record the social instrumentation in the social notes.
- 589. Confirm no social claim is made that the logs do not show.
- 590. Log the social instrumentation in the emergence log.

### 6.10 Social validation
- 591. Run a social diagnostic: one run, log every social event, verify the logs match the world state.
- 592. Verify the diagnostic shows social behaviour arising from sensing and drives, not from scripts.
- 593. Measure the social cost in ticks/s and record it.
- 594. Write the social validation report with the diagnostic results.
- 595. Record the validation in GENESIS_TESTING_REPORT.md.
- 596. Get Muse's review of the social validation.
- 597. Fix any social bug found and re-run the diagnostic.
- 598. Archive the diagnostic log with the run.
- 599. Confirm births are recorded (v4: 5/5/7 across arms; record the new count).
- 600. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 7: Memory and knowledge that outlives — the culture seed
Done when: knowledge passes between inhabitants by observation and demonstration, at least one skill survives its originator's death, death is permanent with records remaining, and the psychoactive plant is in the world as simulated chemistry with no scripted revelation.

### 7.1 Individual memory that persists
- 601. Verify episodic memory persists across sleep and across days.
- 602. Measure memory capacity: how many events an inhabitant retains.
- 603. Verify the forgetting rule: old events fade unless recalled (record the rule).
- 604. Log the first recalled event per inhabitant in a run.
- 605. Measure recall accuracy: does the inhabitant act on a true memory?
- 606. Record the memory persistence rules in the hybrid architecture notes.
- 607. Add a memory test: an event stored on day 1 is recalled on day 3.
- 608. Measure the memory cost in ticks/s and storage.
- 609. Log memory size per inhabitant per day.
- 610. Confirm memory is private and per-inhabitant.

### 7.2 Knowledge transfer
- 611. Define knowledge transfer: a skill or fact passing from one inhabitant to another (record the definition).
- 612. Log the first knowledge transfer with the teacher, the learner, and the knowledge.
- 613. Measure knowledge transfers per run.
- 614. Verify transfer happens by observation and demonstration, not by direct data.
- 615. Log whether the transferred knowledge is used by the learner.
- 616. Measure whether transferred knowledge spreads beyond the first learner.
- 617. Record the transfer analysis in the testing report.
- 618. Verify transfer is not a designed channel: it arises from social behaviour.
- 619. Log the first knowledge transfer in the emergence log.
- 620. Confirm knowledge transfer is the seed of culture.

### 7.3 Shared knowledge
- 621. Define shared knowledge: a fact or skill held by more than one inhabitant (record the definition).
- 622. Measure shared knowledge per run: how many skills are held by two or more inhabitants.
- 623. Log the first shared skill (e.g. two inhabitants can both make fire).
- 624. Measure whether shared knowledge survives the death of its originator.
- 625. Record the shared-knowledge analysis in the testing report.
- 626. Verify shared knowledge is measured from behaviour, not assumed.
- 627. Log the first shared knowledge in the emergence log.
- 628. Measure the growth of shared knowledge over the 5 days.
- 629. Record the shared-knowledge rules in the culture notes.
- 630. Confirm shared knowledge is the first form of culture.

### 7.4 The psychoactive plant
- 631. Plant the mushroom-like psychoactive plant in the world; record its location and count.
- 632. Verify the plant is not labeled and has no scripted effect (no "meaning button").
- 633. Implement the simulated chemistry: temporary loosening of the predictive model — more noise, weaker priors, higher plasticity/salience.
- 634. Record the dose-response rule (dose-dependent, time-limited) — Muse to decide the exact dose parameters; record the decision.
- 635. Implement the real costs: disorientation, neglected hunger/thirst/safety.
- 636. Verify an inhabitant must find and eat the plant itself (no owner dosing).
- 637. Log every plant encounter and every ingestion with dose and time.
- 638. Measure the behavioural effect after ingestion (record the result).
- 639. Record the plant rules in the world-systems notes, labeled as simulated chemistry.
- 640. Confirm any "meaning of life" is the inhabitant's interpretation, not an objective truth — and record that no such claim is made.

### 7.5 Ritual and shared meaning beginnings
- 641. Log the first time two inhabitants repeat the same action together (a shared pattern).
- 642. Measure repeated shared patterns per run.
- 643. Verify patterns arise from behaviour, not from a script.
- 644. Log whether a pattern is repeated on a later day.
- 645. Record the pattern analysis in the testing report.
- 646. Verify no meaning is assigned to a pattern by the simulation (meaning is the inhabitants', not ours).
- 647. Log the first shared pattern in the emergence log.
- 648. Measure whether patterns spread to other inhabitants.
- 649. Record the pattern rules in the culture notes.
- 650. Confirm ritual is a later development — this milestone only measures its beginnings.

### 7.6 Death and legacy
- 651. Verify death is permanent: a dead inhabitant does not return.
- 652. Log every death with cause, time, location, and the inhabitant's state.
- 653. Measure what the dead inhabitant leaves behind: tools, fire, knowledge in others.
- 654. Log the first time another inhabitant uses a dead inhabitant's tool or fire.
- 655. Record the death analysis in the testing report.
- 656. Verify the dead inhabitant's records remain readable (historical records remain).
- 657. Log whether the group changes behaviour after a death.
- 658. Measure survival after a death in the group.
- 659. Record the death rules in the simulation architecture notes.
- 660. Confirm death is an event with consequences, not a reset.

### 7.7 Historical records
- 661. Implement the historical record: every major event is written to a durable log.
- 662. Verify the record survives the run and can be read after it ends.
- 663. Record the record format and where it is stored.
- 664. Verify the record includes births, deaths, first discoveries, first contacts, and first combinations.
- 665. Add a record test: a scripted event appears in the record exactly once.
- 666. Measure the record size per run.
- 667. Publish the record to the website, dated.
- 668. Verify the record is written by the simulation, not by an agent's summary.
- 669. Record the record rules in the simulation architecture notes.
- 670. Confirm the record is the world's own history, not our story about it.

### 7.8 Knowledge persistence across lives
- 671. Define knowledge persistence: a skill or fact that survives its originator's death (record the definition).
- 672. Measure knowledge persistence per run: how many skills outlive their originator.
- 673. Log the first persisted skill with the originator, the learner, and the death.
- 674. Verify persistence happens through teaching and imitation, not through a database.
- 675. Record the persistence analysis in the testing report.
- 676. Verify persistence is measured from behaviour, not assumed.
- 677. Log the first persisted skill in the emergence log.
- 678. Measure the growth of persistent knowledge over the 5 days.
- 679. Record the persistence rules in the culture notes.
- 680. Confirm persistence is what turns one discovery into a civilisation.

### 7.9 Culture instrumentation
- 681. Log every knowledge transfer, shared skill, persisted skill, and shared pattern.
- 682. Build a culture timeline per run: event, participants, time, outcome.
- 683. Verify the culture logs are complete: no culture event type is silently dropped.
- 684. Record the culture instrumentation format in the testing report.
- 685. Add an instrumentation test: a scripted culture event appears in the log exactly once.
- 686. Publish the culture timeline to the website, dated.
- 687. Measure culture events per day and record the trend.
- 688. Record the culture instrumentation in the culture notes.
- 689. Confirm no culture claim is made that the logs do not show.
- 690. Log the culture instrumentation in the emergence log.

### 7.10 Culture validation
- 691. Run a culture diagnostic: one run, log every culture event, verify the logs match the world state.
- 692. Verify the diagnostic shows culture arising from memory, teaching, and death — not from scripts.
- 693. Measure the culture cost in ticks/s and record it.
- 694. Write the culture validation report with the diagnostic results.
- 695. Record the validation in GENESIS_TESTING_REPORT.md.
- 696. Get Muse's review of the culture validation.
- 697. Fix any culture bug found and re-run the diagnostic.
- 698. Archive the diagnostic log with the run.
- 699. Confirm the psychoactive plant's social half is observable once towns can meet (record the status).
- 700. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 8: The world that draws itself — photoreal rendering and procedural generation
Done when: a scene steps on Freebuff's chosen rendering path, ENGINE_DECISION.md is written as an executed decision, the rendered world matches the kernel state, the photoreal bar is checked (not assumed), and new land generates from the same rules as the explored world.

### 8.1 The rendering decision, executed
- 701. Record the rendering decision Freebuff makes (his call: best and easiest path, photoreal bar kept).
- 702. Record what the chosen path costs (speed, quality, anything) in ENGINE_DECISION.md.
- 703. Verify the chosen path is recorded as an executed decision, not a recommendation.
- 704. If the chosen path is Genesis World with the admin folder, record that the folder was made and by whom.
- 705. If the chosen path is a different renderer or engine, record why it was picked and what it replaces.
- 706. Record the rendering decision in AGENT_COMMUNICATION.md with the numbers.
- 707. Get Muse's review of the rendering decision before it is built on.
- 708. Confirm the photoreal bar is met by the chosen path (as good as we can get it, no low-poly) — or record plainly that it is not.
- 709. Record the rendering decision in the emergence log.
- 710. Confirm no claim is made about rendering until a scene steps.

### 8.2 Smoke test and first stepped scene
- 711. Run the smoke test: initialise the renderer and print a settled box.
- 712. Record the smoke test output (success or failure) in ENGINE_DECISION.md.
- 713. Step the first scene: terrain, sky, light — and record that it stepped.
- 714. Capture a screenshot of the first stepped scene and store it in the repo.
- 715. Measure the scene step time and record it.
- 716. Verify the smoke test passes from a clean start, not only after a warm cache.
- 717. Record the smoke test procedure so it can be re-run.
- 718. If the smoke test fails, record the failure and the next step (do not claim success).
- 719. Get Muse's review of the smoke test result.
- 720. Confirm the kernel remains the source of truth until the smoke test passes.

### 8.3 Photoreal bar — what "as good as we can get it" means
- 721. Write down the photoreal bar: the concrete visual standard the world must meet (Muse to decide the exact standard; record the decision).
- 722. Record what "no low-poly" means for this world (minimum fidelity, recorded).
- 723. Capture reference images of the standard (record where they are stored).
- 724. Compare the first stepped scene against the bar and record the gaps.
- 725. Fix the largest gap and re-capture the scene.
- 726. Record the bar and the comparison in ENGINE_DECISION.md.
- 727. Get Muse's review of the bar and the comparison.
- 728. Confirm the bar is a standard, not a wish: it is checked, not assumed.
- 729. Log the bar decision in the emergence log.
- 730. Confirm the bar does not move down to fit what is easy.

### 8.4 Terrain rendering
- 731. Render the terrain: heightfield, ground, hills, low ground, river banks.
- 732. Verify the rendered terrain matches the kernel's terrain (same heights, same river path).
- 733. Capture a screenshot of the rendered terrain and store it.
- 734. Measure the terrain render cost and record it.
- 735. Verify the terrain renders at the viewport's detail, not the whole planet at once.
- 736. Record the terrain rendering parameters.
- 737. Add a terrain render test: the rendered height matches the kernel height at sampled points.
- 738. Fix any terrain mismatch and re-capture.
- 739. Get Muse's review of the rendered terrain.
- 740. Confirm the terrain looks like a place, not a grid.

### 8.5 Bodies, houses, fire, water rendered
- 741. Render the five houses: walls, roof, door, interior.
- 742. Render the five inhabitants: bodies that move, sit, sleep, and carry.
- 743. Render fire: flame, light, smoke, and the ground it burns.
- 744. Render water: the river, rain, and containers.
- 745. Verify the rendered objects match the kernel's state (same positions, same states).
- 746. Capture a screenshot of the rendered town at dawn and store it.
- 747. Measure the render cost for the full town and record it.
- 748. Record the object rendering parameters.
- 749. Add a render test: a house that burns in the kernel burns in the render.
- 750. Get Muse's review of the rendered town.

### 8.6 Light, day/night, weather visuals
- 751. Render the day/night cycle: dawn, noon, dusk, night, with matching light levels.
- 752. Render firelight at night: the ~8 m radius, visible and warm.
- 753. Render rain: falling rain, wet ground, and the effect on fire.
- 754. Verify the rendered light matches the kernel's light level by hour.
- 755. Capture screenshots at dawn, noon, and night and store them.
- 756. Measure the lighting cost and record it.
- 757. Record the lighting parameters.
- 758. Add a lighting test: light level at midnight matches the kernel's value.
- 759. Fix any lighting mismatch and re-capture.
- 760. Get Muse's review of the rendered light.

### 8.7 First-person camera
- 761. Implement the first-person camera: the view from an inhabitant's eyes.
- 762. Verify the camera matches the inhabitant's vision (same field of view, same range).
- 763. Verify the camera sees what the inhabitant senses — and nothing more.
- 764. Capture a first-person screenshot from one inhabitant's eyes at dawn and store it.
- 765. Measure the first-person render cost and record it.
- 766. Record the camera parameters.
- 767. Add a camera test: an object behind a wall is not visible in the first-person view.
- 768. Verify the camera never shows information the inhabitant has not sensed.
- 769. Get Muse's review of the first-person camera.
- 770. Confirm the camera is the World View feed's source.

### 8.8 Procedural generation
- 771. Implement procedural generation for new land: terrain, biomes, and resources generated from the same rules as the explored world.
- 772. Verify generated land matches the kernel's rules (same terrain, same resource placement logic).
- 773. Generate one new region beyond Town 1 and record its seed.
- 774. Verify the generated region is deterministic from its seed.
- 775. Measure the generation cost and record it.
- 776. Record the generation rules in the planet architecture notes.
- 777. Add a generation test: the same seed produces the same region.
- 778. Verify no generated region is pre-built by hand.
- 779. Get Muse's review of the procedural generation.
- 780. Confirm scale-out uses generation, not hand-building.

### 8.9 Performance and adaptive fidelity
- 781. Measure the full render cost: 5 inhabitants, river, fire, day/night, continuous (record ticks/s and frames/s).
- 782. Implement adaptive fidelity: detail only for the viewport, summary elsewhere.
- 783. Verify the viewport renders at full detail and the rest at summary detail.
- 784. Measure the performance gain from adaptive fidelity and record it.
- 785. Record the performance budget and where adaptive fidelity cuts in.
- 786. Add a performance test: the run holds its tick rate with adaptive fidelity on.
- 787. Measure the host's limits: how many inhabitants the host can carry (measured, not guessed).
- 788. Record the host limits in the testing report.
- 789. Get Muse's review of the performance numbers.
- 790. Confirm the performance budget is measured, not assumed.

### 8.10 Rendering validation
- 791. Run a rendering diagnostic: one scene, verify every rendered object matches the kernel state.
- 792. Verify the diagnostic shows the render following the kernel, not inventing state.
- 793. Measure the render cost in ticks/s and record it.
- 794. Write the rendering validation report with the diagnostic results.
- 795. Record the validation in GENESIS_TESTING_REPORT.md.
- 796. Get Muse's review of the rendering validation.
- 797. Fix any rendering bug found and re-run the diagnostic.
- 798. Archive the diagnostic screenshots with the run.
- 799. Confirm the rendering bar is met (or record plainly that it is not).
- 800. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 9: The two views — Command Center and World View, live
Done when: the Agent Gateway API feeds both views from the live simulation, the one-way rule is enforced in code, both views show live data with honest labels, and the simulation runs continuously whether or not anyone is watching.

### 9.1 Agent Gateway API design
- 801. Write the Gateway API design: endpoints, data shapes, and the contract between the simulation and the website.
- 802. Record the API design in the repo (Muse to decide the exact contract; record the decision).
- 803. Define the Command Center feed: world state, population, individuals, events, discoveries, mortality, learning metrics, system health.
- 804. Define the World View feed: per-inhabitant first-person sensory stream, read-only.
- 805. Verify the API is the only path between the world and the website (no direct access).
- 806. Record the API design in the simulation architecture notes.
- 807. Get Muse's review of the API design before it is built.
- 808. Confirm the API serves data, not screenshots (the website renders from data).
- 809. Record the API version and the date it was designed.
- 810. Confirm the API contract is written down before any endpoint is built.

### 9.2 Command Center feed
- 811. Implement the Command Center feed: world state endpoint.
- 812. Implement the population endpoint: individuals, their states, and their histories.
- 813. Implement the events endpoint: births, deaths, discoveries, firsts.
- 814. Implement the metrics endpoint: learning metrics, system health, ticks/s.
- 815. Verify each endpoint returns live data from the simulation, not stale data.
- 816. Measure the feed latency and record it.
- 817. Add a feed test: the endpoint returns the kernel's current state.
- 818. Record the feed endpoints in the API notes.
- 819. Get Muse's review of the Command Center feed.
- 820. Confirm the feed is read-only: it changes nothing in the world.

### 9.3 World View feed
- 821. Implement the World View feed: per-inhabitant first-person sensory stream.
- 822. Verify the feed delivers what the inhabitant sees (their vision), not a third-person camera.
- 823. Verify the feed is read-only: no input channel from the website to the world.
- 824. Implement the inhabitant selector: the feed switches between inhabitants 1–5.
- 825. Measure the feed latency and record it.
- 826. Add a feed test: the stream matches the inhabitant's sensor state.
- 827. Record the feed endpoints in the API notes.
- 828. Get Muse's review of the World View feed.
- 829. Confirm the feed is one-way: the world never receives anything from the observer.
- 830. Verify the feed works while the simulation runs continuously.

### 9.4 The one-way rule, enforced
- 831. Write down the one-way rule: observation is one-way by design; the world must never sense the watcher.
- 832. Audit the Gateway: list every data flow and confirm none flows from observer to world.
- 833. Verify no inhabitant sensor can read the observer (record the test).
- 834. Verify no website control exists in World View (no buttons that change anything).
- 835. Add a one-way test: attempt to send an input from the website and confirm it is refused.
- 836. Log any one-way violation as a critical bug, not a warning.
- 837. Record the one-way audit in the simulation architecture notes.
- 838. Get Muse's review of the one-way audit before the views go live.
- 839. Confirm the rule is enforced in code, not just in policy.
- 840. Record the one-way enforcement in the emergence log.

### 9.5 Command Center live
- 841. Connect the website's Command Center to the live feed.
- 842. Verify the map shows live town positions and states.
- 843. Verify the live-status panel shows the latest measured run, dated.
- 844. Verify the population panel shows live individuals and their states.
- 845. Verify the decisions panel shows the recorded decisions.
- 846. Measure the update rate and record it.
- 847. Verify the Command Center reads state and changes nothing (record the test).
- 848. Capture a screenshot of the live Command Center and store it.
- 849. Get Muse's review of the live Command Center.
- 850. Confirm the Command Center is live, not a static page.

### 9.6 World View live
- 851. Connect the website's World View to the live feed.
- 852. Verify the first-person view shows the selected inhabitant's live vision.
- 853. Verify the inhabitant selector switches the live feed between inhabitants 1–5.
- 854. Verify drag-to-look works on the live feed.
- 855. Verify no control exists in World View (record the test).
- 856. Measure the stream latency and record it.
- 857. Capture a screenshot of the live World View and store it.
- 858. Get Muse's review of the live World View.
- 859. Confirm the World View is live footage, not the design scene — and update the honesty label.
- 860. Verify the world runs 24/7 whether or not anyone is watching.

### 9.7 The planet viewer at scale
- 861. Verify the planet viewer zooms planet → country → region → locale → individual.
- 862. Verify detail loads only for the viewport (record the test).
- 863. Verify Town 1 is live and Towns 2–5 are marked not started (until they open).
- 864. Measure the viewer load time and record it.
- 865. Verify the viewer works on a phone (record the test).
- 866. Record the viewer parameters in the planet architecture notes.
- 867. Add a viewer test: zooming to Town 1 loads Town 1 detail, not the whole planet.
- 868. Get Muse's review of the planet viewer.
- 869. Confirm the viewer is observation only (no control, no changes).
- 870. Record the viewer status in the emergence log.

### 9.8 Live status honesty
- 871. Verify every number on the website is either live data or the latest measured state, dated.
- 872. Verify anything not live yet is marked as not live (record the check).
- 873. Verify no metric on the website is invented (audit each panel).
- 874. Record the honesty audit in the website notes.
- 875. Verify the website's live-status numbers match the testing report.
- 876. Get Muse's review of the honesty audit.
- 877. Fix any invented or stale number found and re-audit.
- 878. Record the honesty rules in the website notes.
- 879. Confirm the honesty labels are checked on every deployment.
- 880. Record the honesty audit in the emergence log.

### 9.9 Continuous operation
- 881. Verify the simulation runs continuously even if the website is offline.
- 882. Verify the simulation runs continuously even if the laptop is offline.
- 883. Verify the simulation runs continuously even if Muse and Freebuff are offline.
- 884. Verify the Gateway serves the latest state after a restart (checkpoint-resume).
- 885. Measure the uptime over a test week and record it.
- 886. Record the operations rules (checkpoints, recovery, logging, health monitoring).
- 887. Add an operations test: kill the website, confirm the simulation keeps running.
- 888. Add an operations test: restart the Gateway, confirm the website reconnects.
- 889. Get Muse's review of the continuous-operation evidence.
- 890. Confirm the run is continuous, not a demo that stops when someone closes a laptop.

### 9.10 Views validation
- 891. Run a views diagnostic: open both views, verify each shows live data.
- 892. Verify the diagnostic shows the views following the simulation, not inventing state.
- 893. Measure the views' latency and record it.
- 894. Write the views validation report with the diagnostic results.
- 895. Record the validation in GENESIS_TESTING_REPORT.md.
- 896. Get Muse's review of the views validation.
- 897. Fix any views bug found and re-run the diagnostic.
- 898. Archive the diagnostic screenshots with the run.
- 899. Confirm both views are live (or record plainly which is not).
- 900. Record the phase exit decision in AGENT_COMMUNICATION.md.

## Phase 10: Proving the start is perfect — measurement, the bar, the consciousness record
Done when: the final 5-day run is archived and reproducible, the bar is judged with its numbers, every emergence and discovery claim passes its test, the negative results are kept, the specs are written in full, and Muse signs off on the perfect start.

### 10.1 The final 5-day run
- 901. Freeze the final config: world, minds, systems, seeds, and the harness (record the config hash).
- 902. Run the final 5-day experiment: 5 inhabitants, 5 houses, 128 m, dawn 06:00, continuous.
- 903. Verify the run completes 5 full days without interruption.
- 904. Record survivors, deaths, median observed days, and first-drink day per arm per seed.
- 905. Record sleep share, ticks/s, births, sightings, and first_sighting_day.
- 906. Record every first discovery, first contact, first combination, and first teaching.
- 907. Verify the run logs are complete (no event type dropped).
- 908. Archive the final run (config, logs, results) so it can be re-run exactly.
- 909. Publish the final run summary to the website, dated.
- 910. Confirm the final run is the experiment, not a rehearsal.

### 10.2 The bar, judged
- 911. Apply the bar exactly: hybrid beats random on first-drink day AND median survival across ≥5 seeds.
- 912. Record the bar's verdict per seed and overall, with the numbers beside it.
- 913. If the bar is met, re-run the harness once more on the same seeds to confirm.
- 914. If the bar is not met, record that the start is not yet perfect and write the next single change.
- 915. Record the bar's verdict in AGENT_COMMUNICATION.md and the emergence log.
- 916. Update the website's live-status numbers to the final run, dated.
- 917. Confirm the three-arm harness is the referee: no claim is made from a single arm.
- 918. Get Muse's sign-off on the bar's verdict.
- 919. Record Muse's sign-off with the date.
- 920. Confirm the verdict is a measurement, not a wish.

### 10.3 The emergence record
- 921. Write the emergence record: every emergence claimed, with the log evidence for each.
- 922. Verify each claimed emergence has a log entry (discovery, contact, combination, teaching, sharing).
- 923. Remove any claimed emergence the logs do not support.
- 924. Record the emergence record in the emergence log.
- 925. Verify no emergence is claimed that was scripted or placed.
- 926. Apply the Discovery Principle test to each claim: could the owner have predicted it?
- 927. Record the test result per claim.
- 928. Get Muse's review of the emergence record.
- 929. Publish the emergence record to the website, dated.
- 930. Confirm the record is honest: it includes what did not happen, not only what did.

### 10.4 The discovery test
- 931. List every discovery in the final run (fire, tools, containers, hearth, combinations).
- 932. Apply the discovery test to each: could the owner have predicted it? If yes, it was placed; if no, it was discovered.
- 933. Record the test result per discovery.
- 934. Verify no discovery was placed by us (no labels, no tutorial, no recipe list).
- 935. Record the discovery test in the emergence log.
- 936. Get Muse's review of the discovery test.
- 937. Remove any discovery that fails the test from the emergence record.
- 938. Publish the discovery test to the website, dated.
- 939. Confirm the test is applied to every discovery, not only the impressive ones.
- 940. Record the discovery test result in AGENT_COMMUNICATION.md.

### 10.5 The consciousness record
- 941. Define the consciousness record: what was observed about understanding forming (record the definition — Muse to decide the exact definition; record the decision).
- 942. Write the record: the first time a mind went from a drive to a plan, from a plan to a tool, from a tool to a shared idea.
- 943. Verify each entry in the record has log evidence (no entry without evidence).
- 944. Record what was NOT observed (no claim of consciousness from convincing behaviour).
- 945. State plainly what the record does and does not show about understanding.
- 946. Record the consciousness record in the emergence log.
- 947. Get Muse's review of the consciousness record.
- 948. Publish the consciousness record to the website, dated.
- 949. Confirm the record is an observation, not a claim about inner experience.
- 950. Record the consciousness record in AGENT_COMMUNICATION.md.

### 10.6 Negative results kept
- 951. List every negative result from the start: every change that did not move the bar, every system never used, every discovery never made.
- 952. Verify each negative result is in the testing report (not deleted).
- 953. Verify the planner cut is recorded with its evidence (4,493 interventions, no separation).
- 954. Verify the random-beats-learned result is recorded (v4: 0 deaths vs 10/12).
- 955. Record the negative results in the emergence log.
- 956. Get Muse's review of the negative-results list.
- 957. Publish the negative results to the website, dated.
- 958. Confirm no negative result is hidden to make the start look better.
- 959. Record the negative-results list in AGENT_COMMUNICATION.md.
- 960. Confirm the start is judged by all its results, not only the good ones.

### 10.7 The perfect-start sign-off
- 961. Write the sign-off checklist: every phase's exit criterion, with its evidence.
- 962. Verify every phase's exit criterion is met (or record which is not and why).
- 963. Confirm the bar is met (or record that it is not).
- 964. Confirm the world is built, instrumented, and recorded.
- 965. Confirm the minds are built, validated, and the same for every inhabitant.
- 966. Confirm the views are live and honest.
- 967. Get Muse's sign-off on the perfect start.
- 968. Record Muse's sign-off with the date in AGENT_COMMUNICATION.md.
- 969. Publish the sign-off to the website, dated.
- 970. Confirm the sign-off is a measurement, not a ceremony.

### 10.8 The spec documents, completed
- 971. Write GENESIS_MASTER_SPECIFICATION.md in full (currently outline-only).
- 972. Write GENESIS_PHYSICS_SPECIFICATION.md in full.
- 973. Write GENESIS_NEURAL_ARCHITECTURE.md in full.
- 974. Write GENESIS_HYBRID_ARCHITECTURE.md in full.
- 975. Write GENESIS_SIMULATION_ARCHITECTURE.md in full.
- 976. Write GENESIS_RESEARCH_PLAN.md in full.
- 977. Write GENESIS_DEVELOPMENT_ROADMAP.md in full.
- 978. Verify every spec matches the built world (no spec claims what was not built).
- 979. Get Muse's review of the completed specs.
- 980. Record the spec completion in AGENT_COMMUNICATION.md.

### 10.9 The deferred list, written down
- 981. Write the deferred list: Towns 2–5, animals, weather/seasons, chemistry, genetics, evolution, communication/language, disease/injury, trade/conflict.
- 982. Record why each item is deferred (survival first) and what unlocks it.
- 983. Verify no deferred item is secretly built inside the start.
- 984. Record the deferred list in the development roadmap.
- 985. Get Muse's review of the deferred list.
- 986. Publish the deferred list to the website, dated.
- 987. Confirm the deferred list is a promise, not a graveyard: each item has its unlock condition.
- 988. Record the deferred list in AGENT_COMMUNICATION.md.
- 989. Verify the start's exit criteria reference the deferred list, not the deferred work itself.
- 990. Confirm the start is complete without the deferred work.

### 10.10 Handoff to what comes next
- 991. Write the handoff: what the start proved, what it did not prove, and what comes next.
- 992. Record the next work order: Towns 2–5, then animals, then weather/seasons (per the deferred list).
- 993. Verify the handoff references the final run's numbers.
- 994. Record the handoff in AGENT_COMMUNICATION.md.
- 995. Get Muse's review of the handoff.
- 996. Publish the handoff to the website, dated.
- 997. Archive the perfect-start plan with the final run (config, logs, results, specs).
- 998. Confirm the archive is complete and re-runnable.
- 999. Record the archive location in the repo.
- 1000. Close the perfect start: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## How to use this plan

Work top to bottom, phase by phase, milestone by milestone. A milestone is done only when its tasks' checks pass — a test passing, a number measured, a file written, a decision recorded. Nothing is claimed done without a measured result. If a task's result contradicts an earlier assumption, stop, record the contradiction, and bring it to Muse before continuing — do not work around it silently. If a task cannot be done as written, record why and what was done instead; do not delete the task. The plan is a record of what was done, not a wish list.

## Phase completion checklist

- Phase 1: Survival becomes learnable — the hybrid beats the random control on first-drink day AND median survival across ≥5 seeds, or the failure is recorded with the next single change and its falsifier.
- Phase 2: The world they wake up in — the 128 m world is built, deterministic, and instrumented; water, shelter, and resources exist as rules, not labels.
- Phase 3: Bodies and senses — every inhabitant has the same body and the same 28-dim sensor vector; perception comes from the environment only; the firewall is verified.
- Phase 4: The mind — every inhabitant runs the same hybrid mind (neural core + forward model + episodic memory, planner cut); the pure-neural track is judged by its falsifier.
- Phase 5: First discoveries — fire, tools, containers, and hearths are discoverable by trial; the first of each and the first two-system combination are recorded.
- Phase 6: Meeting each other — first contact is a measured event after day 0; social behaviour is logged with its participants; nothing social is scripted.
- Phase 7: Memory and knowledge that outlives — knowledge passes between inhabitants; at least one skill survives its originator's death; the plant is in the world as simulated chemistry.
- Phase 8: The world that draws itself — a scene steps on Freebuff's chosen rendering path; ENGINE_DECISION.md is written as an executed decision; the render matches the kernel.
- Phase 9: The two views — the Gateway API feeds both views from the live simulation; the one-way rule is enforced in code; both views are live and honest.
- Phase 10: Proving the start is perfect — the final 5-day run is archived and reproducible; the bar is judged with its numbers; Muse signs off on the perfect start.
