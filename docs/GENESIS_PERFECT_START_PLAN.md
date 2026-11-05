# GENESIS — THE PERFECT START PLAN (v2, cells-first)

## What "the perfect start" means

The perfect start is the whole arc done right: from single cells to the human experiment. Life begins as single-cell organisms in a bounded dish; evolution does the rest — minds scale with bodies, bodies cooperate, new species appear, animals live their lives, social life and communication emerge, human-level minds appear — and then the human experiment begins: 5 inhabitants, 5 houses, one shared 128 m world, run continuously for 5 days, starting at zero knowledge — Stone Age in capability, no date picked — with the inhabitants starting unaware of each other. Nothing is given to them except shelter (the 5 houses, honestly labeled as a starting condition). Everything else — survival, fire, tools, meeting each other, shared knowledge — is earned by them, discovered by them, and recorded by us. The start is perfect when the arc is real (every step emerged from rules, nothing was placed), the human experiment is learnable (the hybrid beats the random control on the stated bar), the world is built and instrumented, the minds are complete and identical for every inhabitant at each scale, the first discoveries are real, the two views are live and honest, and every claim is backed by a measured result. If evolution stalls, the human experiment still happens as a seeded starting condition, honestly labeled — the human experiment is never blocked on evolution succeeding. Later work — Towns 2–5, weather and seasons, chemistry beyond the soup, genetics, agriculture, trade, writing — appears here only as this start's exit criteria or as explicitly deferred follow-ons, never as full plans inside this document.

## Scope

This plan covers the perfect start only: the arc from the first replicator to the first human experiment and its proof. It does not plan the planet, the towns, or any system deferred past the human experiment. Where a later system is mentioned, it is mentioned as a boundary: what the start must not close off, what unlocks it, and where it is written down.

## How to read the numbers in this plan

A number labeled "target" is a goal to hit, not a fact. A number cited as measured carries its version. The v4 numbers (November 5, 2026, 5 seeds × 5 days × 3 arms, 128 m) describe the human-scale kernel — label them as such; they do not describe the cell scale. Numbers from the world-systems draft are starting values to challenge with measured evidence, not facts. Nothing in this plan invents a measured number.

## Phase 1: Origin of life — chemistry to first replicators (the primordial soup)
Done when: the pilot ran, cells survived + reproduced + complexity measurably increased over N generations, and the gate decision (the full evolutionary path is worth pursuing, or not) is recorded.

### 1.1 The primordial soup pilot — design proposed and reviewed
- 1. Propose the pilot design in AGENT_COMMUNICATION.md: dish size, cell model, mutation rate, what "complexity" means as a measurement, and the pilot's success criterion (cells survive + reproduce + measurable complexity increase over N generations).
- 2. Record the dish size and why it was chosen (compute budget, observation resolution).
- 3. Record the cell model: what a cell senses, what it can do, what it costs.
- 4. Record the mutation rate and why (too high destroys inheritance, too low stalls change).
- 5. Record the complexity measurement: the exact metric, how it is computed, and what counts as an increase.
- 6. Record the pilot's success criterion: survival + reproduction + complexity increase over N generations, with N stated.
- 7. Submit the pilot design to Muse for review; record the review and any changes.
- 8. Record the pilot's compute budget (ticks/s target) before building.
- 9. Record what the pilot will not do (no multicellularity, no animals, no human-scale minds in the dish).
- 10. Record the pilot design decision in the emergence log with the date.

### 1.2 Chemistry rules — the soup's physics
- 11. Write the chemical species list: what chemicals exist in the soup and what each one does.
- 12. Write the reaction rules: which chemicals combine into what, under which conditions.
- 13. Write the energy rule: where energy comes from, how it flows, how it is spent.
- 14. Write the gradient rules: how chemical concentrations vary across the dish and how cells sense them.
- 15. Add a conservation check: total mass and energy conserved within documented numerical error; record the error.
- 16. Add a determinism check: same seed, same soup — record the check passing.
- 17. Record the chemistry rules in the simulation architecture notes.
- 18. Verify the soup chemistry runs without a cell present (chemistry alone is stable).
- 19. Record the soup's initial conditions (concentrations, temperature, energy inflow) with the seed.
- 20. Get the chemistry rules passing in the kernel test suite; record the pass count.

### 1.3 The dish — a bounded world for cells
- 21. Define the dish: size, shape, boundaries, and what lies beyond the edge (bounded for the pilot; record the decision).
- 22. Define resource inflow: what enters the dish, at what rate, and from where.
- 23. Define waste outflow: what leaves the dish and how.
- 24. Define the dish's initial resource distribution and record it with the seed.
- 25. Make the dish deterministic: same seed, same dish — record the check.
- 26. Add a dish test asserting the boundaries hold (nothing leaves the dish, nothing enters unrecorded).
- 27. Record the dish parameters in the run log.
- 28. Verify the dish renders as a top-down view (2D, honest label — the pilot's visualization, not the photoreal world).
- 29. Record the dish's compute cost per tick at the pilot's cell count.
- 30. Get the dish tests passing in the kernel test suite; record the pass count.

### 1.4 First replicators — copying with mutation
- 31. Write the replication rule: what a cell needs to copy itself, and what copying costs.
- 32. Write the mutation rule: what changes on copying, how often, and by how much.
- 33. Write the fidelity rule: how faithfully the offspring matches the parent, and what the error threshold is.
- 34. Add a replication test: a single cell in a rich dish reproduces; record the generation count.
- 35. Add a mutation test: offspring differ from parents; record the measured difference.
- 36. Record the first replicator: the first cell that copied itself, with its generation and time.
- 37. Verify replication is inherited (offspring can also replicate) — record the check.
- 38. Record the replication cost: energy spent per copy, and what happens when energy is insufficient.
- 39. Verify no cell is placed by hand after the initial seeding — all later cells are born; record the check.
- 40. Get the replication tests passing in the kernel test suite; record the pass count.

### 1.5 The pilot runs — cells survive and reproduce
- 41. Seed the dish with the initial cells and record the seed, count, and starting conditions.
- 42. Run the pilot for the planned number of generations; record the generation count reached.
- 43. Record survival: how many of the initial lineage lines are still alive at the end.
- 44. Record reproduction: total births, births per generation, and the birth/death balance.
- 45. Record the population curve: cell count per generation, logged to the run log.
- 46. Record the first death: cause, generation, and time — death is permanent.
- 47. Verify the population grows through birth, not placement — record the check.
- 48. Record the pilot's tick rate (ticks/s) at the pilot's cell count.
- 49. Run the pilot across ≥5 seeds; record survival and reproduction per seed.
- 50. Record the pilot run results in GENESIS_TESTING_REPORT.md with the seed list.

### 1.6 Measuring complexity — what "more complex" means
- 51. Record the complexity metric chosen in the pilot design (from 1.1) with its exact formula.
- 52. Compute the complexity metric per generation for the pilot run; log the curve.
- 53. Record the starting complexity (generation 0) and the ending complexity (final generation).
- 54. Record the complexity change: increase, decrease, or flat — with the numbers.
- 55. Verify the complexity metric is not gameable (a cell cannot inflate it without doing more) — record the check.
- 56. Record the most complex cell lineage: its generation, its traits, and what it does differently.
- 57. Compare complexity across the ≥5 pilot seeds; record the range.
- 58. Record whether complexity increased in every seed, some seeds, or none.
- 59. Write the complexity measurement method into the research log so it can be repeated.
- 60. Get the complexity computation covered by a test; record the test passing.

### 1.7 The pilot decision gate
- 61. Judge the pilot against its success criterion (from 1.1): survival + reproduction + complexity increase over N generations.
- 62. Record the judgement: pass or fail, with the numbers for each part of the criterion.
- 63. If the pilot passes, record the decision: the full evolutionary path is worth pursuing; state the next phase.
- 64. If the pilot fails, record the decision: what changes (cell model, mutation rate, dish, metric) and the falsifier for the next attempt.
- 65. Record the pilot's cost: compute per generation, and what the full path would cost at cell scale.
- 66. Record whether the pilot's complexity growth is fast enough to be worth the compute — with the numbers.
- 67. Submit the pilot judgement to Muse for review; record the review and the decision.
- 68. Record the pilot decision in AGENT_COMMUNICATION.md with the date.
- 69. Record the pilot decision in the emergence log.
- 70. Confirm with Muse that the pilot gate is closed before Phase 2 begins; record the confirmation.

### 1.8 Soup instrumentation
- 71. Log every birth and death in the dish with generation, time, and cause.
- 72. Log the lineage of every cell: parent, offspring, mutation, generation.
- 73. Log the chemical state of the dish per generation (concentrations, energy).
- 74. Log the first replicator, the first mutation that persisted, and the first lineage that went extinct.
- 75. Verify the logs are complete (no birth or death unlogged) — record the check.
- 76. Record the log format in the repo so the pilot can be re-run and re-read.
- 77. Add a lineage query: given any cell, return its ancestors to generation 0 — record it working.
- 78. Record the soup's event count per generation (births, deaths, replications).
- 79. Verify the logs survive a checkpoint and resume — record the check.
- 80. Get the instrumentation covered by tests; record the pass count.

### 1.9 Soup validation — determinism, conservation, reproducibility
- 81. Re-run the pilot from the same seed and verify the same result — record the check.
- 82. Verify mass conservation in the dish within documented error — record the error.
- 83. Verify energy conservation in the dish within documented error — record the error.
- 84. Verify checkpoint and resume: stop the pilot mid-run, resume, same outcome — record the check.
- 85. Verify the dish runs with no observer (no website, no Muse, no Freebuff online) — record the check.
- 86. Run the pilot on a second machine or environment if available; record whether the result matches.
- 87. Record the validation results in GENESIS_TESTING_REPORT.md.
- 88. Fix any validation failure and re-run the failed check; record the fix.
- 89. Confirm the soup's physics is consistent (no free energy, no free mass) — record the confirmation.
- 90. Get all soup validation checks passing in the test suite; record the pass count.

### 1.10 Origin record and sign-off
- 91. Write the origin record: what the soup was, what happened, what was measured — in the emergence log.
- 92. Record the first replicator, the first lineage, and the first extinction in the historical record.
- 93. Record the pilot's final numbers: generations, births, deaths, complexity start and end, per seed.
- 94. Record what the pilot did not do (no multicellularity, no animals) as a boundary, not a failure.
- 95. Record the pilot's cost and speed for the record.
- 96. Submit the origin record to Muse for sign-off; record the sign-off.
- 97. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 98. Archive the pilot run (seed, logs, results) so it can be re-run; record the archive location.
- 99. Confirm the archive is complete and re-runnable — record the check.
- 100. Close Phase 1: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 2: Single cells survive and reproduce — the new calibration
Done when: learned cells beat random cells on survival AND reproduction across ≥5 seeds, judged by the three-arm harness — or the failure is recorded with the next single change and its falsifier.

### 2.1 The cell kernel — from the human kernel, scaled down
- 101. Take the existing stdlib kernel (37 tests, 22/22 validation checks) as the foundation; record what is reused and what is removed.
- 102. Define the cell state: position, energy, chemical stores, age, generation — and record the definition.
- 103. Define the cell tick: what happens in one tick at cell scale, and what it costs.
- 104. Remove human-scale systems from the cell kernel (houses, thirst as a human drive, sleep) and record what was removed and why.
- 105. Keep the physics conservation checks (mass, energy, determinism, checkpoint-resume) and record them passing at cell scale.
- 106. Add a cell-kernel test suite; record the pass count.
- 107. Record the cell kernel's tick rate (ticks/s) at 100 cells, 1,000 cells, and 10,000 cells.
- 108. Verify the cell kernel runs independently of the owner's laptop and of Muse/Freebuff being online — record the check.
- 109. Record the cell kernel's architecture in the simulation architecture notes.
- 110. Get the cell kernel tests passing; record the pass count and the tick rates.

### 2.2 Cell senses — gradients, not vision
- 111. Define the cell sensor vector: chemical gradients, light, temperature — and record the dimension and what each entry means.
- 112. Implement chemical sensing: a cell senses food concentration and its gradient; record the sensing range.
- 113. Implement light sensing: a cell senses light level and direction; record the range.
- 114. Implement temperature sensing: a cell senses local temperature; record the range.
- 115. Verify cells sense only from the environment (no omniscience) — record the check.
- 116. Add a sensing test: a cell in a gradient moves toward food; record the result.
- 117. Record the cell sensor vector's dimension and cost per tick.
- 118. Verify the sensor vector is the cell's only input (no direct access to world state) — record the check.
- 119. Record the sensing rules in the simulation architecture notes.
- 120. Get the sensing tests passing; record the pass count.

### 2.3 Cell drives — energy, hunger, reproduction
- 121. Define the cell drives: energy, hunger (need for food), and the reproduction drive — and record the thresholds.
- 122. Implement the energy drive: energy falls with activity, rises with eating; record the rates.
- 123. Implement the hunger drive: hunger rises with time and activity; record the rates.
- 124. Implement the reproduction drive: a cell reproduces when energy and stores pass a threshold; record the threshold.
- 125. Verify the drives are homeostatic (they push the cell back toward balance) — record the check.
- 126. Add a drive test: a starving cell seeks food; record the result.
- 127. Record the drive thresholds and rates in the run log.
- 128. Verify a cell with no food dies (energy reaches zero) — record the death.
- 129. Record the drive rules in the simulation architecture notes.
- 130. Get the drive tests passing; record the pass count.

### 2.4 Cell movement and action space
- 131. Define the cell action space: move, eat, reproduce, rest — and record what each action costs.
- 132. Implement movement: a cell moves toward sensed gradients; record the speed and cost.
- 133. Implement eating: a cell consumes food at its position; record the rate and gain.
- 134. Implement resting: a cell saves energy by not moving; record the saving.
- 135. Verify every action costs something (time, energy, or opportunity) — record the check.
- 136. Add a movement test: a cell reaches food faster than a random-walking cell; record the result.
- 137. Record the action space and costs in the simulation architecture notes.
- 138. Verify a cell cannot act without paying the cost — record the check.
- 139. Record the movement speeds and costs in the run log.
- 140. Get the movement tests passing; record the pass count.

### 2.5 The cell harness — three arms at cell scale
- 141. Build the cell harness with three arms: population (learned cells), no_planner (learned cells, planner off), random (random cells).
- 142. Set planner=False as the population default at cell scale; record the setting.
- 143. Verify the no_planner arm and the population arm are identical in config except for the flag under test — record the check.
- 144. Run the cell harness across ≥5 seeds; record survival and reproduction per seed per arm.
- 145. Record the harness's tick rate per arm at the pilot's cell count.
- 146. Verify the harness runs deterministically per seed — record the check.
- 147. Record the harness design in the testing report.
- 148. Add a harness test: the random arm runs and produces results; record the result.
- 149. Record the seed list for the cell harness runs.
- 150. Get the harness tests passing; record the pass count.

### 2.6 The cell bar — learned beats random
- 151. Define the cell bar: the learned population beats the random control on survival AND reproduction across ≥5 seeds.
- 152. Measure survival per arm across ≥5 seeds; record the numbers.
- 153. Measure reproduction per arm across ≥5 seeds; record the numbers.
- 154. Judge the bar: pass or fail, with the numbers.
- 155. If the bar fails, diagnose why random wins and record the diagnosis with the next single change and its falsifier.
- 156. Record the first-reproduction day per arm (the cell-scale analogue of first-drink day).
- 157. Record the median survival per arm across ≥5 seeds.
- 158. Submit the bar judgement to Muse for review; record the review.
- 159. Record the bar judgement in the emergence log with the numbers.
- 160. Confirm with Muse that the cell bar is judged before Phase 3 begins; record the confirmation.

### 2.7 Cell reproduction — new agent per offspring
- 161. Implement agent assignment on reproduction: each offspring gets its own agent (own mind, own memory, own life).
- 162. Verify the parent's agent never controls the child — record the check.
- 163. Verify the offspring's mind starts fresh (no copy of the parent's memory) — record the check.
- 164. Record the agent count over time: agents grow through birth, not placement.
- 165. Verify no agent is placed by hand after the initial seeding — record the check.
- 166. Add a reproduction test: a cell reproduces, the offspring has its own agent; record the result.
- 167. Record the agent-assignment rule in the simulation architecture notes.
- 168. Verify the agent count matches the living cell count — record the check.
- 169. Record the birth/death balance per generation.
- 170. Get the reproduction tests passing; record the pass count.

### 2.8 Cell death — permanent, recorded
- 171. Implement cell death: energy zero, or lethal damage — the cell stops, permanently.
- 172. Verify death is permanent (no revival, no reset) — record the check.
- 173. Record every death with cause, generation, and time.
- 174. Record the death causes and their counts per run.
- 175. Verify the historical record keeps dead cells (their lineage remains) — record the check.
- 176. Add a death test: a starved cell dies and stays dead; record the result.
- 177. Record the death rules in the simulation architecture notes.
- 178. Verify a dead cell's agent is retired, not reused — record the check.
- 179. Record the survival curve per seed (fraction alive per generation).
- 180. Get the death tests passing; record the pass count.

### 2.9 Cell instrumentation
- 181. Log every birth, death, and reproduction with generation, time, and cause.
- 182. Log the population curve per generation.
- 183. Log the energy and hunger distributions per generation.
- 184. Log the first survival, first reproduction, and first extinction per run.
- 185. Verify the logs are complete — record the check.
- 186. Record the log format in the repo.
- 187. Add a lineage query for cells (ancestors to generation 0) — record it working.
- 188. Record the event count per generation.
- 189. Verify the logs survive checkpoint and resume — record the check.
- 190. Get the instrumentation tests passing; record the pass count.

### 2.10 Cell calibration record and sign-off
- 191. Write the cell calibration record: what was built, what was measured — in the testing report.
- 192. Record the cell bar judgement, the harness numbers, and the tick rates.
- 193. Record what the cell kernel does not do (no multicellularity, no animals) as a boundary.
- 194. Record the v4 human-scale numbers as human-scale (20/18 survivors, 32 random, 846 ticks/s) — labeled as the human-scale kernel, not the cell scale.
- 195. Record the cell calibration cost and speed for the record.
- 196. Submit the cell calibration record to Muse for sign-off; record the sign-off.
- 197. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 198. Archive the cell calibration runs (seeds, logs, results); record the archive location.
- 199. Confirm the archive is complete and re-runnable — record the check.
- 200. Close Phase 2: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 3: Minds scale with bodies — the architecture family, from gradients to neurons
Done when: the architecture family is demonstrated from gradients to small nets, the planner cut holds at every scale, and the pure-neural research track is judged by its falsifier.

### 3.1 The architecture family — one family, sized to the organism
- 201. Write the architecture-family rule: one family (neural core + forward model + episodic memory), sized to the organism — and record it.
- 202. Define the sizing rule: how mind size is set from body size and niche demands — record the formula.
- 203. Record the sizing ladder: gradients → few neurons → small nets → fly-scale → dog-scale → human-scale.
- 204. Verify the same family is used at every scale (no separate architecture per species) — record the check.
- 205. Record the family rule in the neural architecture notes.
- 206. Add a family test: the same code constructs minds at three sizes; record the result.
- 207. Record the mind-size cost per tick at each rung of the ladder.
- 208. Verify no LLM-only inhabitants exist at any scale — record the check.
- 209. Record the family rule in AGENT_COMMUNICATION.md.
- 210. Get the family tests passing; record the pass count.

### 3.2 Gradient control — minds with no neurons
- 211. Implement gradient control: a cell steers by chemical gradients with no neurons — and record the rule.
- 212. Verify gradient control is a mind in the family sense (senses in, actions out, no omniscience) — record the check.
- 213. Add a gradient test: a gradient-controlled cell finds food; record the result.
- 214. Record the gradient control's cost per tick.
- 215. Verify gradient control cannot access world state directly — record the check.
- 216. Record the gradient control rule in the neural architecture notes.
- 217. Compare gradient control against a random cell: record survival and reproduction.
- 218. Record the comparison in the testing report.
- 219. Verify gradient control is the floor of the ladder (nothing simpler is a mind) — record the decision.
- 220. Get the gradient tests passing; record the pass count.

### 3.3 Few-neuron nets — the first neural minds
- 221. Implement a few-neuron net (target: fewer than 10 neurons) as the first neural mind — record the size.
- 222. Verify the few-neuron net learns (its behaviour changes with experience) — record the evidence.
- 223. Add a few-neuron test: the net outperforms gradient control on a foraging task; record the numbers.
- 224. Record the few-neuron net's cost per tick.
- 225. Verify the few-neuron net's weights change only through its learning rule — record the check.
- 226. Record the few-neuron design in the neural architecture notes.
- 227. Compare few-neuron minds against gradient control across ≥5 seeds; record survival and reproduction.
- 228. Record the comparison in the testing report.
- 229. Verify the few-neuron net is the first rung that can be called neural — record the decision.
- 230. Get the few-neuron tests passing; record the pass count.

### 3.4 The forward model at small scale
- 231. Implement a forward model at small scale: the mind predicts the next sensory input — record the size.
- 232. Verify the forward model learns (prediction error falls with experience) — record the numbers.
- 233. Add a forward-model test: prediction error falls over a run; record the curve.
- 234. Record the forward model's cost per tick at each rung.
- 235. Verify the forward model is used for action selection (not just logged) — record the check.
- 236. Record the forward-model design in the neural architecture notes.
- 237. Compare minds with and without a forward model across ≥5 seeds; record survival and reproduction.
- 238. Record the comparison in the testing report.
- 239. Verify the forward model is part of the family at every rung above gradients — record the decision.
- 240. Get the forward-model tests passing; record the pass count.

### 3.5 Episodic memory, scaled
- 241. Implement episodic memory at small scale: the mind stores past episodes — record the capacity per rung.
- 242. Verify memory is per-agent (no shared memory, no access to another agent's episodes) — record the check.
- 243. Add a memory test: a mind with memory outperforms one without on a repeated task; record the numbers.
- 244. Record the memory's cost per tick and per stored episode.
- 245. Verify memory survives sleep/rest and checkpoint-resume — record the check.
- 246. Record the memory design in the neural architecture notes.
- 247. Compare minds with and without episodic memory across ≥5 seeds; record survival and reproduction.
- 248. Record the comparison in the testing report.
- 249. Verify memory capacity scales with the rung (more complex minds hold more) — record the decision.
- 250. Get the memory tests passing; record the pass count.

### 3.6 Plasticity and learning rules, scaled
- 251. Implement the learning rule at small scale (target: a Hebbian-style rule with a credit path) — record the rule.
- 252. Verify the learning rule changes behaviour with experience — record the evidence.
- 253. Add a plasticity test: a mind adapts to a changed food location; record the result.
- 254. Record the learning rule's cost per tick.
- 255. Verify learning cannot rewrite the mind's architecture (only its weights) — record the check.
- 256. Record the learning rule in the neural architecture notes.
- 257. Compare learning minds against fixed minds across ≥5 seeds; record survival and reproduction.
- 258. Record the comparison in the testing report.
- 259. Verify the learning rule is the same family rule at every rung — record the decision.
- 260. Get the plasticity tests passing; record the pass count.

### 3.7 Intrinsic motivation and curiosity, scaled
- 261. Implement intrinsic motivation at small scale: the mind seeks novelty — record the rule.
- 262. Verify curiosity changes behaviour (the mind explores, not just exploits) — record the evidence.
- 263. Add a curiosity test: a curious mind finds a new food source a non-curious mind misses; record the result.
- 264. Record the curiosity rule's cost per tick.
- 265. Verify curiosity never overrides survival drives (hunger still wins) — record the check.
- 266. Record the curiosity design in the neural architecture notes.
- 267. Compare curious minds against non-curious minds across ≥5 seeds; record survival, reproduction, and discoveries.
- 268. Record the comparison in the testing report.
- 269. Verify curiosity is part of the family at every rung above gradients — record the decision.
- 270. Get the curiosity tests passing; record the pass count.

### 3.8 The planner cut at every scale
- 271. Set planner=False as the population default at every scale; record the setting.
- 272. Verify no planner steering runs in any population arm at any scale — record the check.
- 273. Keep the planner code behind a flag for the research track; record where it lives.
- 274. Record the v4 evidence for the cut (4,493 interventions, no separation) in the architecture notes.
- 275. Verify the three-arm harness still runs at cell scale with the new default — record the check.
- 276. Record the cut in AGENT_COMMUNICATION.md with the v4 evidence.
- 277. Update the hybrid definition in the docs: neural core + forward model + episodic memory, no steering layer, at every scale.
- 278. Verify the cut holds at the few-neuron rung and the fly rung (planner adds nothing measurable) — record the numbers.
- 279. Record the cut as final for the MVP at every scale; record the confirmation with Muse.
- 280. Get the planner-cut tests passing; record the pass count.

### 3.9 Pure neural research track, scaled
- 281. Define the pure-neural research track at small scale: neural only, no forward model, no episodic memory — record the definition.
- 282. State the falsifier: pure neural beats random on first-reproduction day AND median survival across ≥5 seeds, or hybrid-first stands — record it.
- 283. Run the pure-neural track at the few-neuron rung across ≥5 seeds; record survival and reproduction.
- 284. Compare pure neural against hybrid and random at the same rung; record the numbers.
- 285. Record the comparison in the testing report.
- 286. Verify the pure-neural track is a research track only (never the population default) — record the check.
- 287. Record the falsifier result for the few-neuron rung (pass or fail, with numbers).
- 288. Submit the falsifier result to Muse for review; record the review.
- 289. Record the research-track status in the emergence log.
- 290. Get the research-track tests passing; record the pass count.

### 3.10 Mind-scaling validation
- 291. Verify mind size grows with body size and niche demands across the ladder — record the numbers.
- 292. Verify the sizing rule (from 3.1) predicts the mind size actually built — record the check.
- 293. Run the full ladder (gradients → few neurons → small nets) in one run; record survival and reproduction per rung.
- 294. Record the cost per tick per rung (gradients cheapest, nets dearest).
- 295. Verify no rung's mind accesses another agent's memory or the world state directly — record the check.
- 296. Record the ladder results in the testing report.
- 297. Verify the fruit-fly brain sits at the midpoint of the ladder, not the start — record the decision.
- 298. Submit the mind-scaling results to Muse for sign-off; record the sign-off.
- 299. Archive the mind-scaling runs; record the archive location.
- 300. Close Phase 3: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 4: Multicellularity — cells cooperate, bodies form
Done when: bodies form, differentiate, divide labor, reproduce as bodies, and the record is signed off.

### 4.1 Adhesion — cells stick
- 301. Implement adhesion: cells can stick to each other — record the rule and cost.
- 302. Verify adhesion is a cell action (costs energy) — record the check.
- 303. Add an adhesion test: cells in a rich patch form a cluster; record the result.
- 304. Record the adhesion rule in the simulation architecture notes.
- 305. Verify adhesion does not merge agents (each cell keeps its own agent) — record the check.
- 306. Record the cluster sizes observed per run.
- 307. Compare clustered cells against solitary cells across ≥5 seeds; record survival and reproduction.
- 308. Record the comparison in the testing report.
- 309. Verify adhesion is reversible (cells can detach) — record the check.
- 310. Get the adhesion tests passing; record the pass count.

### 4.2 Differentiation — cells take roles
- 311. Implement differentiation: cells in a cluster take different roles (e.g., outer vs inner) — record the rule.
- 312. Verify roles are determined by position and signals, not by script — record the check.
- 313. Add a differentiation test: a cluster develops at least two roles; record the result.
- 314. Record the differentiation rule in the simulation architecture notes.
- 315. Verify a differentiated cell keeps its own agent — record the check.
- 316. Record the roles observed and their counts per cluster.
- 317. Compare differentiated clusters against undifferentiated clusters across ≥5 seeds; record survival and reproduction.
- 318. Record the comparison in the testing report.
- 319. Verify differentiation is reversible when the cluster breaks up — record the check.
- 320. Get the differentiation tests passing; record the pass count.

### 4.3 Division of labor
- 321. Implement division of labor: different roles do different work (e.g., one gathers, one moves) — record the rule.
- 322. Verify the division emerges from the roles, not from a script — record the check.
- 323. Add a division-of-labor test: a cluster with roles outperforms a cluster without roles; record the numbers.
- 324. Record the division-of-labor rule in the simulation architecture notes.
- 325. Verify each role's work benefits the cluster (shared energy or protection) — record the evidence.
- 326. Record the work split observed per cluster.
- 327. Compare clusters with and without division of labor across ≥5 seeds; record survival and reproduction.
- 328. Record the comparison in the testing report.
- 329. Verify division of labor is not imposed by the owner — record the check.
- 330. Get the division-of-labor tests passing; record the pass count.

### 4.4 Collective sensing
- 331. Implement collective sensing: a cluster senses more than a single cell (wider range, more gradients) — record the rule.
- 332. Verify collective sensing comes from the cells' own sensors combined, not from a cluster-level sense — record the check.
- 333. Add a collective-sensing test: a cluster finds food a single cell misses; record the result.
- 334. Record the collective-sensing rule in the simulation architecture notes.
- 335. Verify the cluster has no single mind (each cell keeps its own agent) — record the check.
- 336. Record the sensing range of clusters vs single cells.
- 337. Compare clusters against single cells on a foraging task across ≥5 seeds; record the numbers.
- 338. Record the comparison in the testing report.
- 339. Verify collective sensing is an emergent property, not a placed feature — record the check.
- 340. Get the collective-sensing tests passing; record the pass count.

### 4.5 Body plans — the first bodies
- 341. Define a body plan: a stable arrangement of differentiated cells — record the definition.
- 342. Implement body-plan formation: clusters settle into repeatable shapes — record the rule.
- 343. Add a body-plan test: the same starting cluster forms the same body plan across seeds; record the result.
- 344. Record the body plans observed and their frequencies.
- 345. Verify body plans are inherited (offspring clusters form the same plan) — record the check.
- 346. Record the body-plan rule in the simulation architecture notes.
- 347. Compare body-plan clusters against shapeless clusters across ≥5 seeds; record survival and reproduction.
- 348. Record the comparison in the testing report.
- 349. Verify body plans are not designed by the owner (they emerge from the rules) — record the check.
- 350. Get the body-plan tests passing; record the pass count.

### 4.6 Reproduction of bodies — offspring as bodies
- 351. Implement body reproduction: a body produces an offspring body (not just a cell) — record the rule.
- 352. Verify the offspring body gets its own agents (one per cell, each fresh) — record the check.
- 353. Add a body-reproduction test: a body reproduces, the offspring body survives; record the result.
- 354. Record the body reproduction rate and cost.
- 355. Verify the offspring body's plan matches the parent's (with mutation) — record the check.
- 356. Record the body-reproduction rule in the simulation architecture notes.
- 357. Compare body reproduction against cell-only reproduction across ≥5 seeds; record the numbers.
- 358. Record the comparison in the testing report.
- 359. Verify body reproduction is the population mechanism at this scale (agents born, not placed) — record the check.
- 360. Get the body-reproduction tests passing; record the pass count.

### 4.7 Death of bodies — permanent, recorded
- 361. Implement body death: a body dies when its cells die or its energy fails — record the rule.
- 362. Verify body death is permanent — record the check.
- 363. Record every body death with cause, generation, and time.
- 364. Record the body death causes and counts per run.
- 365. Verify the historical record keeps dead bodies (their lineage remains) — record the check.
- 366. Add a body-death test: a starved body dies and stays dead; record the result.
- 367. Record the body-death rule in the simulation architecture notes.
- 368. Verify a dead body's agents are retired, not reused — record the check.
- 369. Record the body survival curve per seed.
- 370. Get the body-death tests passing; record the pass count.

### 4.8 Multicellular instrumentation
- 371. Log every body formed, every body reproduced, every body died, with generation and cause.
- 372. Log the body-plan distribution per generation.
- 373. Log the cluster sizes and role counts per generation.
- 374. Log the first body, the first reproduction of a body, and the first body extinction per run.
- 375. Verify the logs are complete — record the check.
- 376. Record the log format in the repo.
- 377. Add a body-lineage query (ancestors to generation 0) — record it working.
- 378. Record the event count per generation.
- 379. Verify the logs survive checkpoint and resume — record the check.
- 380. Get the instrumentation tests passing; record the pass count.

### 4.9 Multicellular validation
- 381. Re-run the multicellular runs from the same seeds and verify the same results — record the check.
- 382. Verify mass and energy conservation at body scale within documented error — record the error.
- 383. Verify checkpoint and resume at body scale — record the check.
- 384. Verify the multicellular world runs with no observer — record the check.
- 385. Run the multicellular world across ≥5 seeds; record survival and reproduction per seed.
- 386. Record the validation results in the testing report.
- 387. Fix any validation failure and re-run the failed check; record the fix.
- 388. Verify no body is placed by hand (all bodies are born) — record the check.
- 389. Confirm the multicellular physics is consistent — record the confirmation.
- 390. Get all multicellular validation checks passing; record the pass count.

### 4.10 Multicellularity record and sign-off
- 391. Write the multicellularity record: what was built, what was measured — in the emergence log.
- 392. Record the first body, the first body plan, and the first body extinction in the historical record.
- 393. Record the multicellular numbers: bodies per generation, survival, reproduction, per seed.
- 394. Record what multicellularity does not do (no animals yet) as a boundary.
- 395. Record the multicellular cost and speed for the record.
- 396. Submit the multicellularity record to Muse for sign-off; record the sign-off.
- 397. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 398. Archive the multicellular runs; record the archive location.
- 399. Confirm the archive is complete and re-runnable — record the check.
- 400. Close Phase 4: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 5: New species appear — evolution produces diversity
Done when: new species are identified by the recorded criterion, diversity is measured, extinctions are recorded, and the Discovery Principle test is applied.

### 5.1 Speciation — what counts as a new species
- 401. Define what counts as a new species: the exact criterion (Muse to decide the species criterion — reproductive isolation, genetic distance, or both; record the decision).
- 402. Record the species criterion in the research log with the date.
- 403. Implement species identification: given two organisms, decide whether they are the same species — record the rule.
- 404. Add a species-identification test: two lineages that diverged are identified as different species; record the result.
- 405. Verify the species criterion is measured, not asserted — record the check.
- 406. Record the species criterion in the simulation architecture notes.
- 407. Verify no species is declared by the owner (all species are identified by the rule) — record the check.
- 408. Record the first species split identified by the rule, with its generation.
- 409. Submit the species criterion to Muse for review; record the review.
- 410. Get the species-identification tests passing; record the pass count.

### 5.2 Mutation and selection — the engine
- 411. Implement the mutation rule at body scale: what changes on reproduction, how often, by how much — record the rule.
- 412. Implement the selection rule: which organisms survive and reproduce — record the rule (survival and reproduction, not owner choice).
- 413. Verify selection is environmental (food, predators, climate), not owner choice — record the check.
- 414. Add a mutation test: offspring differ from parents; record the measured difference.
- 415. Add a selection test: a beneficial mutation spreads through the population; record the result.
- 416. Record the mutation and selection rules in the simulation architecture notes.
- 417. Compare populations with and without mutation across ≥5 seeds; record diversity and survival.
- 418. Record the comparison in the testing report.
- 419. Verify mutation and selection are the only engines of change (no placed variation) — record the check.
- 420. Get the mutation and selection tests passing; record the pass count.

### 5.3 Niches — different ways to live
- 421. Define a niche: a distinct way of living (food source, habitat, timing) — record the definition.
- 422. Implement niche formation: different lineages occupy different niches — record the rule.
- 423. Add a niche test: two lineages diverge into different niches; record the result.
- 424. Record the niches observed and their counts per run.
- 425. Verify niches are occupied by evolution, not assigned by the owner — record the check.
- 426. Record the niche rule in the simulation architecture notes.
- 427. Compare niche-diverse populations against single-niche populations across ≥5 seeds; record survival and diversity.
- 428. Record the comparison in the testing report.
- 429. Verify a niche can empty (extinction) and be re-occupied by a different lineage — record the check.
- 430. Get the niche tests passing; record the pass count.

### 5.4 Diversity metrics
- 431. Define the diversity metrics: species count, lineage count, trait spread — record the formulas.
- 432. Compute the diversity metrics per generation; log the curves.
- 433. Record the starting diversity (generation 0) and the diversity at each phase gate.
- 434. Record the diversity change: increase, decrease, or flat — with the numbers.
- 435. Verify the diversity metrics are not gameable — record the check.
- 436. Record the most diverse run and the least diverse run, with their seeds.
- 437. Compare diversity across ≥5 seeds; record the range.
- 438. Record the diversity method in the research log so it can be repeated.
- 439. Verify diversity is measured the same way at every scale — record the check.
- 440. Get the diversity computation covered by tests; record the test passing.

### 5.5 Extinction — species that do not make it
- 441. Implement extinction: a species with no living members is extinct — record the rule.
- 442. Verify extinction is permanent (no revival) — record the check.
- 443. Record every extinction with species, cause, generation, and time.
- 444. Record the extinction causes and their counts per run.
- 445. Verify the historical record keeps extinct species (their lineage remains) — record the check.
- 446. Add an extinction test: a species with no food goes extinct; record the result.
- 447. Record the extinction rule in the simulation architecture notes.
- 448. Verify extinction is environmental, not owner choice — record the check.
- 449. Record the extinction curve per seed (species count over time).
- 450. Get the extinction tests passing; record the pass count.

### 5.6 The species record — lineages
- 451. Record the species list per run: species, first appearance generation, parent species.
- 452. Record the lineage tree: each species' ancestors back to the first cell — and verify it is complete.
- 453. Record the first species split, the first niche occupation, and the first extinction per run.
- 454. Verify the lineage tree has no gaps (every species has a parent) — record the check.
- 455. Record the species record in the historical record with the date.
- 456. Add a lineage query: given any species, return its ancestors to generation 0 — record it working.
- 457. Record the species count per generation in the run log.
- 458. Verify the species record survives checkpoint and resume — record the check.
- 459. Record the species-record format in the repo.
- 460. Get the species-record tests passing; record the pass count.

### 5.7 The Discovery Principle test — predicted vs discovered
- 461. List what the owner predicted would evolve (before the run) — record the list.
- 462. List what actually evolved — record the list.
- 463. Apply the test: could the owner have predicted it? If yes, it was placed; if no, it was discovered — record the judgement per species.
- 464. Record the discovered species (not predicted) with their generations.
- 465. Record the placed species (predicted, if any) and why they were predicted.
- 466. Verify no species was placed by hand — record the check.
- 467. Record the Discovery Principle test result in the emergence log.
- 468. Submit the test result to Muse for review; record the review.
- 469. Record the test method so it can be repeated for later phases.
- 470. Get the test covered by a check; record the check passing.

### 5.8 Species instrumentation
- 471. Log every speciation and extinction with generation, time, and cause.
- 472. Log the species count and diversity metrics per generation.
- 473. Log the niche occupancy per generation.
- 474. Log the first speciation, first niche, and first extinction per run.
- 475. Verify the logs are complete — record the check.
- 476. Record the log format in the repo.
- 477. Add a species query (given a generation, list the living species) — record it working.
- 478. Record the event count per generation.
- 479. Verify the logs survive checkpoint and resume — record the check.
- 480. Get the instrumentation tests passing; record the pass count.

### 5.9 Species validation
- 481. Re-run the speciation runs from the same seeds and verify the same results — record the check.
- 482. Verify mass and energy conservation at species scale within documented error — record the error.
- 483. Verify checkpoint and resume at species scale — record the check.
- 484. Verify the species world runs with no observer — record the check.
- 485. Run the speciation world across ≥5 seeds; record species count and diversity per seed.
- 486. Record the validation results in the testing report.
- 487. Fix any validation failure and re-run the failed check; record the fix.
- 488. Verify no species is placed by hand — record the check.
- 489. Confirm the species physics is consistent — record the confirmation.
- 490. Get all species validation checks passing; record the pass count.

### 5.10 Species record and sign-off
- 491. Write the species record: what evolved, what was measured — in the emergence log.
- 492. Record the first species, the most diverse run, and the first extinction in the historical record.
- 493. Record the species numbers: species count, diversity, extinctions, per seed.
- 494. Record what speciation does not do (no animals yet) as a boundary.
- 495. Record the speciation cost and speed for the record.
- 496. Submit the species record to Muse for sign-off; record the sign-off.
- 497. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 498. Archive the speciation runs; record the archive location.
- 499. Confirm the archive is complete and re-runnable — record the check.
- 500. Close Phase 5: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 6: Animals — movement, senses, behavior; bodies living their lives
Done when: animals move, sense, behave, eat and are eaten, live their own lives, and the record is signed off.

### 6.1 Movement — the first animals move
- 501. Implement animal movement: directed movement through the world — record the rule and cost.
- 502. Verify movement is controlled by the animal's own mind, not by script — record the check.
- 503. Add a movement test: an animal reaches food faster than a drifting body; record the result.
- 504. Record the movement speeds and costs per body plan.
- 505. Verify every movement costs energy — record the check.
- 506. Record the movement rule in the simulation architecture notes.
- 507. Compare moving animals against sessile bodies across ≥5 seeds; record survival and reproduction.
- 508. Record the comparison in the testing report.
- 509. Verify movement is not scripted (no waypoints, no paths placed) — record the check.
- 510. Get the movement tests passing; record the pass count.

### 6.2 Senses at animal scale — vision, hearing, touch
- 511. Implement animal vision: a camera-like sense with a range and field — record the range.
- 512. Implement animal hearing: a sense of sound direction and distance — record the range.
- 513. Implement animal touch: contact sensing — record the rule.
- 514. Verify animal senses come from the environment only (no omniscience) — record the check.
- 515. Add a sensing test: an animal finds food by sight; record the result.
- 516. Record the animal sensor vector's dimension and cost per tick.
- 517. Verify the sensor vector is the animal's only input — record the check.
- 518. Record the sensing rules in the simulation architecture notes.
- 519. Compare animals with and without vision on a foraging task; record the numbers.
- 520. Get the sensing tests passing; record the pass count.

### 6.3 Behavior — foraging, fleeing, hunting
- 521. Implement foraging: an animal seeks food — record the rule.
- 522. Implement fleeing: an animal flees a threat — record the rule.
- 523. Implement hunting: an animal pursues prey — record the rule.
- 524. Verify each behaviour is learned or evolved, not scripted — record the check.
- 525. Add a behaviour test: a foraging animal eats more than a random-moving animal; record the numbers.
- 526. Record the behaviour rules in the simulation architecture notes.
- 527. Compare animals with and without each behaviour across ≥5 seeds; record survival and reproduction.
- 528. Record the comparison in the testing report.
- 529. Verify no behaviour is a placed script — record the check.
- 530. Get the behaviour tests passing; record the pass count.

### 6.4 Food webs — who eats whom
- 531. Implement predation: one animal can eat another — record the rule and cost.
- 532. Verify predation is a behaviour (hunting), not a placed rule — record the check.
- 533. Add a predation test: a predator eats prey and gains energy; record the result.
- 534. Record the food web: who eats whom, per run.
- 535. Verify the food web is stable enough to persist (predators do not eat all prey) — record the check.
- 536. Record the food-web rule in the simulation architecture notes.
- 537. Compare food webs with and without predators across ≥5 seeds; record species count and survival.
- 538. Record the comparison in the testing report.
- 539. Verify the food web emerged (no owner-assigned predator/prey pairs) — record the check.
- 540. Get the predation tests passing; record the pass count.

### 6.5 Bodies living their lives — a fly doing fly things
- 541. Define "a life": what a day looks like for one animal (eat, move, rest, reproduce) — record the definition.
- 542. Record one full life of a single animal: its actions, its meals, its encounters, its death.
- 543. Verify the animal's life is its own (its mind's choices, not a script) — record the check.
- 544. Record the lives of three different species in the same run, side by side.
- 545. Verify each species lives differently (a fly's day differs from a fish's day) — record the evidence.
- 546. Record the life records in the historical record.
- 547. Add a life query: given an animal, return its life events — record it working.
- 548. Verify the life records survive checkpoint and resume — record the check.
- 549. Record the life-record format in the repo.
- 550. Get the life-record tests passing; record the pass count.

### 6.6 Animal reproduction — new agent per offspring
- 551. Implement animal reproduction: an animal produces offspring, each with its own agent — record the rule.
- 552. Verify the parent's agent never controls the offspring — record the check.
- 553. Verify the offspring's mind starts fresh — record the check.
- 554. Record the agent count over time at animal scale.
- 555. Verify no animal agent is placed by hand — record the check.
- 556. Add a reproduction test: an animal reproduces, the offspring has its own agent; record the result.
- 557. Record the agent-assignment rule in the simulation architecture notes.
- 558. Verify the agent count matches the living animal count — record the check.
- 559. Record the birth/death balance per generation at animal scale.
- 560. Get the reproduction tests passing; record the pass count.

### 6.7 Animal death — permanent, recorded
- 561. Implement animal death: starvation, predation, injury, age — record the causes.
- 562. Verify animal death is permanent — record the check.
- 563. Record every animal death with cause, age, and time.
- 564. Record the death causes and their counts per run.
- 565. Verify the historical record keeps dead animals — record the check.
- 566. Add a death test: a starved animal dies and stays dead; record the result.
- 567. Record the death rules in the simulation architecture notes.
- 568. Verify a dead animal's agent is retired, not reused — record the check.
- 569. Record the animal survival curve per seed.
- 570. Get the death tests passing; record the pass count.

### 6.8 Animal instrumentation
- 571. Log every animal birth, death, predation, and reproduction with time and cause.
- 572. Log the food web per run (who ate whom).
- 573. Log the animal population per species per generation.
- 574. Log the first predator, the first prey escape, and the first animal extinction per run.
- 575. Verify the logs are complete — record the check.
- 576. Record the log format in the repo.
- 577. Add an animal query (given a species, list its living members) — record it working.
- 578. Record the event count per generation.
- 579. Verify the logs survive checkpoint and resume — record the check.
- 580. Get the instrumentation tests passing; record the pass count.

### 6.9 Animal validation
- 581. Re-run the animal runs from the same seeds and verify the same results — record the check.
- 582. Verify mass and energy conservation at animal scale within documented error — record the error.
- 583. Verify checkpoint and resume at animal scale — record the check.
- 584. Verify the animal world runs with no observer — record the check.
- 585. Run the animal world across ≥5 seeds; record species count, population, and survival per seed.
- 586. Record the validation results in the testing report.
- 587. Fix any validation failure and re-run the failed check; record the fix.
- 588. Verify no animal is placed by hand — record the check.
- 589. Confirm the animal physics is consistent — record the confirmation.
- 590. Get all animal validation checks passing; record the pass count.

### 6.10 Animals record and sign-off
- 591. Write the animals record: what evolved, what was measured — in the emergence log.
- 592. Record the first animal, the first predator, and the first animal extinction in the historical record.
- 593. Record the animal numbers: species count, populations, survival, per seed.
- 594. Record what animals do not do (no social life yet) as a boundary.
- 595. Record the animal cost and speed for the record.
- 596. Submit the animals record to Muse for sign-off; record the sign-off.
- 597. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 598. Archive the animal runs; record the archive location.
- 599. Confirm the archive is complete and re-runnable — record the check.
- 600. Close Phase 6: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 7: Social life and communication — groups, signals, shared behavior
Done when: groups, signals, imitation, teaching, cooperation, and shared knowledge are measured, and the record is signed off.

### 7.1 Groups — animals gather
- 601. Implement grouping: animals gather near each other — record the rule.
- 602. Verify grouping emerges (no placed groups) — record the check.
- 603. Add a grouping test: animals of one species gather more than chance; record the numbers.
- 604. Record the group sizes observed per species.
- 605. Verify groups form and break up (no permanent assignment) — record the check.
- 606. Record the grouping rule in the simulation architecture notes.
- 607. Compare grouped animals against solitary animals across ≥5 seeds; record survival and reproduction.
- 608. Record the comparison in the testing report.
- 609. Verify grouping is not scripted — record the check.
- 610. Get the grouping tests passing; record the pass count.

### 7.2 Signals — the first communication
- 611. Implement signals: an animal can emit a signal others can sense — record the rule and cost.
- 612. Verify signals are emitted by the animal's own mind, not by script — record the check.
- 613. Add a signal test: a signal changes another animal's behaviour; record the result.
- 614. Record the signal types observed (alarm, food, mating, other).
- 615. Verify signals cost something (energy or attention) — record the check.
- 616. Record the signal rule in the simulation architecture notes.
- 617. Compare animals with and without signals across ≥5 seeds; record survival and reproduction.
- 618. Record the comparison in the testing report.
- 619. Verify no signal meaning is placed by the owner (meanings emerge from use) — record the check.
- 620. Get the signal tests passing; record the pass count.

### 7.3 Shared behavior — imitation, following
- 621. Implement imitation: an animal copies another's behaviour — record the rule.
- 622. Verify imitation is learned, not scripted — record the check.
- 623. Add an imitation test: a behaviour spreads through a group by copying; record the result.
- 624. Record the behaviours observed spreading (foraging spots, escape routes, other).
- 625. Verify imitation requires observation (no copying without sensing) — record the check.
- 626. Record the imitation rule in the simulation architecture notes.
- 627. Compare groups with and without imitation across ≥5 seeds; record survival and discoveries.
- 628. Record the comparison in the testing report.
- 629. Verify imitation is not a placed script — record the check.
- 630. Get the imitation tests passing; record the pass count.

### 7.4 Teaching by demonstration
- 631. Implement teaching by demonstration: an experienced animal shows a behaviour and a younger one copies it — record the rule.
- 632. Verify teaching is demonstration only (no language, no instruction) — record the check.
- 633. Add a teaching test: a skill passes from one animal to another by demonstration; record the result.
- 634. Record the skills observed passing (foraging, tool use, other).
- 635. Verify the skill survives the teacher's death (the learner keeps it) — record the check.
- 636. Record the teaching rule in the simulation architecture notes.
- 637. Compare groups with and without teaching across ≥5 seeds; record skill persistence.
- 638. Record the comparison in the testing report.
- 639. Verify teaching is not scripted — record the check.
- 640. Get the teaching tests passing; record the pass count.

### 7.5 Conflict and avoidance
- 641. Implement conflict: animals compete for food, mates, or space — record the rule.
- 642. Implement avoidance: an animal avoids a stronger rival — record the rule.
- 643. Verify conflict and avoidance are behaviours, not scripts — record the check.
- 644. Add a conflict test: two animals compete, one wins, the loser leaves; record the result.
- 645. Record the conflict outcomes observed per run.
- 646. Verify conflict costs something (energy, injury, or opportunity) — record the check.
- 647. Record the conflict and avoidance rules in the simulation architecture notes.
- 648. Compare populations with and without conflict across ≥5 seeds; record survival and diversity.
- 649. Record the comparison in the testing report.
- 650. Get the conflict tests passing; record the pass count.

### 7.6 Cooperation — groups that help each other
- 651. Implement cooperation: animals help each other (shared food, joint defence) — record the rule.
- 652. Verify cooperation emerges (no placed cooperation) — record the check.
- 653. Add a cooperation test: a cooperating group outperforms a non-cooperating group; record the numbers.
- 654. Record the cooperation observed (shared food, defence, other).
- 655. Verify cooperation costs the helper something — record the check.
- 656. Record the cooperation rule in the simulation architecture notes.
- 657. Compare cooperating groups against non-cooperating groups across ≥5 seeds; record survival and reproduction.
- 658. Record the comparison in the testing report.
- 659. Verify cooperation is not scripted — record the check.
- 660. Get the cooperation tests passing; record the pass count.

### 7.7 Shared knowledge at animal scale
- 661. Define shared knowledge at animal scale: what a group knows that no single animal knows — record the definition.
- 662. Verify shared knowledge exists (a behaviour the group holds that a lone animal does not) — record the evidence.
- 663. Add a shared-knowledge test: a group remembers a food source a lone animal forgets; record the result.
- 664. Record the shared knowledge observed per group.
- 665. Verify shared knowledge survives the death of its originator — record the check.
- 666. Record the shared-knowledge rule in the simulation architecture notes.
- 667. Compare groups with and without shared knowledge across ≥5 seeds; record survival.
- 668. Record the comparison in the testing report.
- 669. Verify shared knowledge is not placed by the owner — record the check.
- 670. Get the shared-knowledge tests passing; record the pass count.

### 7.8 Social instrumentation
- 671. Log every grouping, signal, imitation, teaching, conflict, and cooperation event with time and participants.
- 672. Log the group sizes and membership per generation.
- 673. Log the first signal, first imitation, first teaching, and first cooperation per run.
- 674. Log the shared knowledge held per group.
- 675. Verify the logs are complete — record the check.
- 676. Record the log format in the repo.
- 677. Add a social query (given an animal, list its group and its signals) — record it working.
- 678. Record the event count per generation.
- 679. Verify the logs survive checkpoint and resume — record the check.
- 680. Get the instrumentation tests passing; record the pass count.

### 7.9 Social validation
- 681. Re-run the social runs from the same seeds and verify the same results — record the check.
- 682. Verify mass and energy conservation at social scale within documented error — record the error.
- 683. Verify checkpoint and resume at social scale — record the check.
- 684. Verify the social world runs with no observer — record the check.
- 685. Run the social world across ≥5 seeds; record group sizes, signals, and survival per seed.
- 686. Record the validation results in the testing report.
- 687. Fix any validation failure and re-run the failed check; record the fix.
- 688. Verify no social behaviour is scripted — record the check.
- 689. Confirm the social physics is consistent — record the confirmation.
- 690. Get all social validation checks passing; record the pass count.

### 7.10 Social record and sign-off
- 691. Write the social record: what evolved, what was measured — in the emergence log.
- 692. Record the first group, the first signal, and the first shared knowledge in the historical record.
- 693. Record the social numbers: group sizes, signal counts, teaching events, per seed.
- 694. Record what social life does not do (no human-level minds yet) as a boundary.
- 695. Record the social cost and speed for the record.
- 696. Submit the social record to Muse for sign-off; record the sign-off.
- 697. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 698. Archive the social runs; record the archive location.
- 699. Confirm the archive is complete and re-runnable — record the check.
- 700. Close Phase 7: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 8: Human-level minds emerge — the destination
Done when: human-level minds are identified by the recorded criteria (or the seeded gate is honestly labeled), and the human experiment is ready to begin.

### 8.1 Mind growth — encephalization, measured
- 701. Define encephalization: mind size relative to body size — record the formula.
- 702. Measure encephalization per species per generation; log the curve.
- 703. Record the most encephalized lineage and its generation.
- 704. Verify encephalization grows with niche demands (not by owner choice) — record the check.
- 705. Add an encephalization test: a lineage's mind grows over generations; record the numbers.
- 706. Record the encephalization rule in the neural architecture notes.
- 707. Compare encephalization across ≥5 seeds; record the range.
- 708. Record the comparison in the testing report.
- 709. Verify encephalization is measured the same way at every scale — record the check.
- 710. Get the encephalization computation covered by tests; record the test passing.

### 8.2 The fruit-fly-inspired hybrid mind at human scale
- 711. Implement the human-scale hybrid mind: fruit-fly-inspired neural core + forward model + episodic memory — record the sizes.
- 712. Verify the human-scale mind is the same family as the cell minds (same rules, larger size) — record the check.
- 713. Add a hybrid test: the human-scale mind outperforms the few-neuron mind on a foraging task; record the numbers.
- 714. Record the human-scale mind's cost per tick.
- 715. Verify the human-scale mind's memory is per-agent — record the check.
- 716. Record the human-scale mind design in the neural architecture notes.
- 717. Compare the human-scale hybrid against pure neural at the same scale across ≥5 seeds; record survival and reproduction.
- 718. Record the comparison in the testing report.
- 719. Verify the fruit-fly brain is the midpoint of the ladder, not the start — record the decision.
- 720. Get the hybrid tests passing; record the pass count.

### 8.3 Hands and tool-use precursors
- 721. Implement hands: a body part that can grasp — record the rule and cost.
- 722. Verify hands are a body-plan feature (evolved), not a placed feature — record the check.
- 723. Add a hands test: an animal with hands manipulates an object; record the result.
- 724. Record the tool-use precursors observed (carrying, striking, other).
- 725. Verify tool use is discovered by trial, not taught — record the check.
- 726. Record the hands and tool-use rules in the simulation architecture notes.
- 727. Compare animals with and without hands across ≥5 seeds; record survival and discoveries.
- 728. Record the comparison in the testing report.
- 729. Verify no tool is given (all tools are found or made) — record the check.
- 730. Get the hands tests passing; record the pass count.

### 8.4 Language precursors — signals to symbols
- 731. Implement signal combinations: two signals together mean something new — record the rule.
- 732. Verify signal combinations emerge from use, not from owner design — record the check.
- 733. Add a combinations test: a combined signal changes behaviour differently than either signal alone; record the result.
- 734. Record the signal combinations observed.
- 735. Verify combinations cost something (time or attention) — record the check.
- 736. Record the combinations rule in the simulation architecture notes.
- 737. Compare groups with and without signal combinations across ≥5 seeds; record coordination and survival.
- 738. Record the comparison in the testing report.
- 739. Verify no symbol meaning is placed by the owner — record the check.
- 740. Get the combinations tests passing; record the pass count.

### 8.5 Social cognition at human scale
- 741. Implement social cognition: an animal models what another animal will do — record the rule.
- 742. Verify social cognition is a mind feature (forward model of others), not a script — record the check.
- 743. Add a social-cognition test: an animal predicts another's move and acts on it; record the result.
- 744. Record the social-cognition rule in the neural architecture notes.
- 745. Verify social cognition uses the animal's own forward model — record the check.
- 746. Compare animals with and without social cognition across ≥5 seeds; record survival and cooperation.
- 747. Record the comparison in the testing report.
- 748. Verify social cognition is not omniscience (the model can be wrong) — record the check.
- 749. Record the social-cognition evidence in the emergence log.
- 750. Get the social-cognition tests passing; record the pass count.

### 8.6 The human-scale body — bipedal, hands, 28-dim sensor
- 751. Define the human-scale body: bipedal, hands, the 28-dim sensor vector (peer proximity, bearing cos/sin, isolation) — record the definition.
- 752. Implement the 28-dim sensor vector at human scale; record the dimension and what each entry means.
- 753. Verify the human-scale body senses only from the environment — record the check.
- 754. Add a body test: the human-scale body moves, grasps, and senses; record the result.
- 755. Record the human-scale body's cost per tick.
- 756. Verify the human-scale body is the same body-plan lineage as the animal bodies (evolved, not placed) — record the check.
- 757. Record the body definition in the simulation architecture notes.
- 758. Compare the human-scale body against earlier body plans on a foraging task; record the numbers.
- 759. Record the comparison in the testing report.
- 760. Get the body tests passing; record the pass count.

### 8.7 Sleep and memory consolidation at human scale
- 761. Implement physiological sleep at human scale: wake on thirst/hunger thresholds, cap daytime sleep — record the rule.
- 762. Verify sleep consolidates memory (a sleeping mind keeps what it learned) — record the evidence.
- 763. Add a sleep test: minds that sleep retain more than minds that do not; record the numbers.
- 764. Record the sleep rule's cost and benefit per day.
- 765. Verify the run clock starts at dawn 06:00 — record the check.
- 766. Record the sleep rule in the simulation architecture notes.
- 767. Compare sleep share before and after the physiology fix (v4 measured: 0.69, down from 0.98) — record the numbers.
- 768. Record the comparison in the testing report.
- 769. Verify sleep itself stays (it is not removed) — record the decision.
- 770. Get the sleep tests passing; record the pass count.

### 8.8 How we know a mind is human-level — identification criteria
- 771. Define the human-level criteria: the exact measurable tests a mind must pass (Muse to decide the exact criteria; record the decision).
- 772. Record the criteria in the research log with the date.
- 773. Implement the criteria as checks: given a mind, decide whether it is human-level — record the rule.
- 774. Add a criteria test: a fly-scale mind fails the criteria, a human-scale mind passes; record the result.
- 775. Verify the criteria are measured, not asserted — record the check.
- 776. Record the criteria in the neural architecture notes.
- 777. Verify no mind is declared human-level by the owner (all declarations use the criteria) — record the check.
- 778. Record the first mind that passes the criteria, with its generation and lineage.
- 779. Submit the criteria to Muse for review; record the review.
- 780. Get the criteria tests passing; record the pass count.

### 8.9 The gate — the human experiment begins
- 781. Judge the gate: do human-level minds exist by the criteria (from 8.8)? Record the judgement with the numbers.
- 782. If human-level minds exist, record the decision: the human experiment begins with them; state the date and the lineage.
- 783. If human-level minds do not exist, record the decision: the human experiment begins as a seeded starting condition, honestly labeled — the human experiment is never blocked on evolution succeeding.
- 784. Record the gate decision in AGENT_COMMUNICATION.md with the date.
- 785. Record the gate decision in the emergence log.
- 786. Verify the seeded start (if used) is labeled as seeded in every record — record the check.
- 787. Verify the evolved start (if used) is labeled with its lineage — record the check.
- 788. Submit the gate decision to Muse for review; record the review.
- 789. Record the gate's cost and the human experiment's starting conditions.
- 790. Confirm with Muse that the gate is closed before Phase 9 begins; record the confirmation.

### 8.10 Human-minds record and sign-off
- 791. Write the human-minds record: what emerged, what was measured — in the emergence log.
- 792. Record the first human-level mind, its lineage, and its generation in the historical record.
- 793. Record the human-mind numbers: encephalization, criteria results, per seed.
- 794. Record what human-level minds do not yet do (no human experiment yet) as a boundary.
- 795. Record the human-mind cost and speed for the record.
- 796. Submit the human-minds record to Muse for sign-off; record the sign-off.
- 797. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 798. Archive the human-mind runs; record the archive location.
- 799. Confirm the archive is complete and re-runnable — record the check.
- 800. Close Phase 8: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 9: The human experiment — the old perfect start (5 humans, 5 houses, 128 m, 5 days, zero knowledge)
Done when: the 5-day human run is complete, the bar is judged, the two views are live and honest, and every claim is backed by a measured result. This phase reuses the v1 plan's human-experiment tasks, condensed — survival calibration, the world, first discoveries, meeting each other, culture, rendering, and the two views.

### 9.1 House-gap fix + planner cut + harness re-run (reused from v1 Phase 1.1–1.3)
- 801. Read `_choose_homes` and record the current gap fallback ladder (35.8, 21.5, 10.7, 4.3 m) in GENESIS_TESTING_REPORT.md.
- 802. Change `_choose_homes` so the minimum house gap is above the 15 m peer range, with no fallback below it. Fix placement by rejection sampling against the gap — never shrink the peer range, never enlarge the world (decided by Muse).
- 803. Add a placement test asserting all five house gaps exceed 15 m on every seed.
- 804. Run the placement test across 5 seeds and record the minimum gap per seed.
- 805. Verify first_sighting_day is no longer 0.0 in a short 1-day diagnostic run.
- 806. Set planner=False as the population default; confirm no planner code runs in the population arm.
- 807. Keep the planner code behind a flag for the research track; record where it lives.
- 808. Record the planner cut in AGENT_COMMUNICATION.md with the v4 evidence (4,493 interventions, no separation).
- 809. Re-run the three-arm harness (population, no_planner, random) identically — same seeds, same arms, new defaults — and record the results.
- 810. Record the harness re-run results in GENESIS_TESTING_REPORT.md with the seed list.

### 9.2 The 128 m world: terrain, river, rain, resources (reused from v1 Phase 2)
- 811. Define the 128 m world: size, boundaries, and what lies beyond the edge — bounded locale, impassable natural terrain, generation beyond comes with scale-out (decided by Muse).
- 812. Build the terrain and the river (depth, flow, banks) and record the parameters.
- 813. Build the rain pattern (seeded, light rain roughly every second simulated day) and record the pattern.
- 814. Place the five houses with gaps above 15 m; record the coordinates per seed.
- 815. Place the resources (stone, wood, clay, fibre) and record their locations and regrowth rules.
- 816. Implement thirst and drinking (thirst ~1/hr at rest, drink restores ~40 — starting values, to challenge with measured evidence).
- 817. Implement drowning (deeper-than-chest water, ~2 min) and record the rule.
- 818. Implement world-state persistence (checkpoints) and record the check passing.
- 819. Instrument the world (every first-use, every death cause, every cross-system combination) and record the instrumentation.
- 820. Get the world tests passing in the kernel test suite; record the pass count.

### 9.3 Survival calibration to the bar (reused from v1 Phase 1.4–1.10)
- 821. Diagnose why random still wins (v4 measured: random 32 survivors, 0 deaths vs learned 20/18, 10/12 deaths) and record the diagnosis with the next single change and its falsifier.
- 822. Verify sleep physiology (wake on thirst/hunger, cap daytime sleep) and record the sleep-skipped share (v4 measured: 0.69).
- 823. Verify dense shaping and the credit-assignment path; record the evidence.
- 824. Measure first-drink day per arm across ≥5 seeds; record the numbers (v4 measured: tied 0.00–0.01).
- 825. Measure median survival per arm across ≥5 seeds; record the numbers (v4 measured: 5.00 days all arms).
- 826. Judge the bar: hybrid beats random on first-drink day AND median survival across ≥5 seeds — pass or fail, with the numbers.
- 827. If the bar fails, record the failure with the next single change and its falsifier; do not claim the bar is met.
- 828. Record the bar judgement in the emergence log with the numbers.
- 829. Submit the bar judgement to Muse for review; record the review.
- 830. Confirm with Muse that the bar is judged before the human experiment's discovery phase begins; record the confirmation.

### 9.4 First discoveries: fire, tools, crafting (reused from v1 Phase 5)
- 831. Implement fire ignition (friction and spark, discoverable by trial) and record the rule.
- 832. Implement fire fuel, light (~8 m), and heat (~3 m) and record the starting values.
- 833. Implement fire spread (a house can burn down) and record the rule.
- 834. Implement the sharp-stone cutting tool (stone + wood) as a discoverable combination; record the rule.
- 835. Implement containers first (hollowed wood / fired clay), then hearth, then tools — in that order — and record the order.
- 836. Implement shelter repair and building (wood + wood + fibre) and record the rule.
- 837. Implement cooking (food over fire, more nutrition, lower sickness) and record the rule.
- 838. Instrument discoveries: first fire, first tool, first container, first combination of two systems — record each with time and inhabitant.
- 839. Record the first two-system combination and the first time one inhabitant teaches another by demonstration.
- 840. Get the discovery tests passing; record the pass count.

### 9.5 Meeting each other (reused from v1 Phase 6)
- 841. Verify first contact is a measured event after day 0 (first_sighting_day no longer 0.0); record the day.
- 842. Implement the social drive (homeostatic, like thirst) and the 15 m peer range; record the rule.
- 843. Implement observation and imitation (copying by watching); record the rule.
- 844. Implement sharing and showing (food, tools, places); record the rule.
- 845. Implement conflict and avoidance (competing, leaving); record the rule.
- 846. Implement group formation (inhabitants gathering); record the rule.
- 847. Implement communication beginnings (signals, then combinations); record the rule.
- 848. Implement teaching by demonstration; record the rule.
- 849. Instrument social life (every first contact, every signal, every teaching, with participants); record the instrumentation.
- 850. Get the social tests passing; record the pass count.

### 9.6 Memory and knowledge that outlives (reused from v1 Phase 7)
- 851. Implement individual memory that persists across days; record the rule.
- 852. Implement knowledge transfer (one inhabitant learns from another); record the rule.
- 853. Implement shared knowledge (what the town knows that no single inhabitant knows); record the rule.
- 854. Plant the psychoactive plant (simulated chemistry, dose-dependent, time-limited); dose parameters are set by experiment — Freebuff proposes, Muse reviews (decided process).
- 855. Implement ritual and shared-meaning beginnings (no scripted meaning); record the rule.
- 856. Implement death and legacy (a dead inhabitant's knowledge can survive); record the rule.
- 857. Implement historical records (events written down by the world, not by the inhabitants' scripts); record the rule.
- 858. Verify at least one skill survives its originator's death; record the evidence.
- 859. Instrument culture (every transfer, every surviving skill); record the instrumentation.
- 860. Get the culture tests passing; record the pass count.

### 9.7 The world that draws itself at human scale (reused from v1 Phase 8)
- 861. Write ENGINE_DECISION.md as an executed decision only when the smoke test prints a settled box; record the decision (Freebuff's call on the rendering path — do whatever is best and easiest, keeping the photoreal bar).
- 862. Run the smoke test and record the first stepped scene.
- 863. Apply the photoreal bar (decided working standard): ray-traced lighting, textured materials, no low-poly geometry, and a screenshot review confirming an inhabitant's eye-level view can distinguish water, food, fire, shelter, and peers at the distances that matter.
- 864. Render the terrain (128 m, river, houses) and record the result.
- 865. Render bodies, houses, fire, and water; record the result.
- 866. Render light, day/night, and weather visuals; record the result.
- 867. Build the first-person camera (the World View's eye); record the result.
- 868. Implement procedural generation for scale-out (new land generated from the same rules); record the rule.
- 869. Measure performance and adaptive fidelity (detail where the observer looks); record the numbers.
- 870. Get the rendering validation passing; record the pass count.

### 9.8 The two views, live for the human experiment (reused from v1 Phase 9)
- 871. Record the Agent Gateway API design in the repo (Muse to decide the exact contract; record the decision).
- 872. Build the Command Center feed: world state, population, individuals, events, discoveries, mortality, learning metrics, system health — record the endpoints.
- 873. Build the World View feed: per-inhabitant first-person sensory stream, read-only — record the endpoints.
- 874. Enforce the one-way rule in code: the world must never sense the watcher; no observer input may ever reach the world — record the enforcement and its test.
- 875. Bring the Command Center live on the website (map, live status, population, direction, decisions); record the deployment.
- 876. Bring the World View live on the website (first-person, drag to look, pick the inhabitant); record the deployment.
- 877. Verify the planet viewer works at scale (planet → country → region → locale → individual, detail only for the viewport); record the check.
- 878. Verify live-status honesty: the site shows the latest measured state, dated, and marks what is not live yet; record the check.
- 879. Verify continuous operation: the simulation runs with no observer online; record the check.
- 880. Get the views validation passing; record the pass count.

### 9.9 The 5-day human run
- 881. Start the 5-day human run at dawn 06:00, 5 inhabitants, 5 houses, 128 m; record the start.
- 882. Run the experiment continuously for 5 days; record that it ran without interruption.
- 883. Record behaviour and events every day (survival, discoveries, meetings, teaching, deaths).
- 884. Record the first drink, first fire, first tool, first contact, and first teaching with times and inhabitants.
- 885. Record every death with cause and time; verify death is permanent.
- 886. Verify the run was not scripted (no placed meetings, no placed discoveries) — record the check.
- 887. Record the run's tick rate and compute cost.
- 888. Verify the run's logs are complete — record the check.
- 889. Archive the 5-day run (seeds, logs, results); record the archive location.
- 890. Confirm the archive is complete and re-runnable — record the check.

### 9.10 Human experiment record and sign-off
- 891. Write the human experiment record: what was built, what was measured — in the testing report.
- 892. Record the human experiment's final numbers: survival, first-drink day, median survival, discoveries, meetings, per seed.
- 893. Record the v4 human-scale numbers as the earlier baseline (20/18 survivors, 32 random, 846 ticks/s) and the new numbers beside them.
- 894. Record what the human experiment does not do (no towns 2–5 yet) as a boundary.
- 895. Record the human experiment's cost and speed for the record.
- 896. Submit the human experiment record to Muse for sign-off; record the sign-off.
- 897. Record the sign-off in AGENT_COMMUNICATION.md with the date.
- 898. Archive the human experiment runs; record the archive location.
- 899. Confirm the archive is complete and re-runnable — record the check.
- 900. Close Phase 9: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## Phase 10: Proving it worked — measurement, the record, the consciousness record across the whole arc
Done when: the arc is recorded from origin to humans, the bar is judged, the consciousness record is written, and Muse signs off on the perfect start.

### 10.1 The bar, judged — human experiment
- 901. Judge the bar for the human experiment: hybrid beats random on first-drink day AND median survival across ≥5 seeds — pass or fail, with the numbers.
- 902. Record the bar judgement in the emergence log with the numbers.
- 903. If the bar fails, record the failure with the next single change and its falsifier.
- 904. Record the three-arm harness numbers (population, no_planner, random) for the final run.
- 905. Verify the bar was judged the same way as the cell bar (same harness, same seeds rule) — record the check.
- 906. Record the final run's tick rate and cost.
- 907. Submit the bar judgement to Muse for review; record the review.
- 908. Record the review in AGENT_COMMUNICATION.md with the date.
- 909. Verify the bar judgement is honest (no number invented, no failure hidden) — record the check.
- 910. Confirm with Muse that the bar is judged before the arc record begins; record the confirmation.

### 10.2 The arc record — origin to humans
- 911. Write the arc record: origin of life → cells → multicellularity → species → animals → social life → human-level minds → the human experiment — in the emergence log.
- 912. Record the lineage of the human experiment's inhabitants back to the first cell — and verify it is complete.
- 913. Record the arc's generation count: total generations from the first replicator to the first human-level mind.
- 914. Record the arc's time: sim-time from origin to the human experiment, and wall-clock time spent.
- 915. Verify the arc record has no gaps (every phase links to the next) — record the check.
- 916. Record the arc record in the historical record with the date.
- 917. Add an arc query: given any inhabitant, return its lineage to the first cell — record it working.
- 918. Verify the arc record survives checkpoint and resume — record the check.
- 919. Record the arc-record format in the repo.
- 920. Get the arc-record tests passing; record the pass count.

### 10.3 The complexity record — how complexity grew
- 921. Record the complexity curve across the whole arc (soup → cells → bodies → animals → humans) with the numbers.
- 922. Record the complexity at each phase gate (end of Phases 1–9).
- 923. Record the fastest complexity growth and the slowest, with their phases.
- 924. Record whether complexity grew steadily, in jumps, or stalled — with the numbers.
- 925. Verify the complexity metric was the same throughout the arc — record the check.
- 926. Record the complexity record in the research log.
- 927. Compare the arc's complexity growth against the pilot's prediction (from Phase 1); record whether the pilot predicted the arc.
- 928. Record the comparison in the emergence log.
- 929. Verify the complexity record is honest (no metric changed mid-arc without recording the change) — record the check.
- 930. Get the complexity-record computation covered by tests; record the test passing.

### 10.4 The species record — diversity, extinctions, lineages
- 931. Record the total species count across the arc (species that ever lived).
- 932. Record the living species count at the end of the arc.
- 933. Record the extinction count and the extinction causes across the arc.
- 934. Record the most diverse phase and the least diverse phase, with their numbers.
- 935. Record the lineage tree of all species, back to the first cell — and verify it is complete.
- 936. Record the species record in the historical record with the date.
- 937. Add a species query across the arc (given a generation, list the living species) — record it working.
- 938. Verify the species record survives checkpoint and resume — record the check.
- 939. Record the species-record format in the repo.
- 940. Get the species-record tests passing; record the pass count.

### 10.5 The consciousness record across the arc
- 941. Define the consciousness record: what was observed about understanding forming (record the definition — Muse to decide the exact definition; record the decision).
- 942. Record the definition in the research log with the date.
- 943. Record the first observation of understanding forming (by the definition), with its generation and species.
- 944. Record the observations of understanding at each phase gate (cells, bodies, animals, social life, human minds).
- 945. Verify the consciousness record never claims consciousness from convincing behaviour alone — record the check.
- 946. Record the consciousness observations in the emergence log.
- 947. Verify the consciousness record is a record of observations, not of claims — record the check.
- 948. Submit the consciousness record to Muse for review; record the review.
- 949. Record the review in AGENT_COMMUNICATION.md with the date.
- 950. Get the consciousness-record checks passing; record the pass count.

### 10.6 The discovery test — predicted vs discovered across the arc
- 951. List what the owner predicted would happen across the arc (before each phase) — record the lists.
- 952. List what actually happened — record the lists.
- 953. Apply the test per phase: could the owner have predicted it? If yes, it was placed; if no, it was discovered — record the judgement per phase.
- 954. Record the discovered phenomena (not predicted) with their phases and generations.
- 955. Record the placed phenomena (predicted, if any) and why they were predicted.
- 956. Verify nothing was placed and called discovered — record the check.
- 957. Record the discovery-test result in the emergence log.
- 958. Submit the test result to Muse for review; record the review.
- 959. Record the test method so it can be repeated.
- 960. Get the test covered by a check; record the check passing.

### 10.7 Negative results kept
- 961. List every negative result across the arc (pilot failures, bar failures, stalled evolution) — record the list.
- 962. Verify every negative result is in the record (none deleted, none hidden) — record the check.
- 963. Record what each negative result taught (the next single change and its falsifier).
- 964. Verify the negative results are in the emergence log and the testing report — record the check.
- 965. Record the negative-results list in the repo with the date.
- 966. Submit the negative-results list to Muse for review; record the review.
- 967. Verify no negative result was re-labeled as a success — record the check.
- 968. Record the verification in AGENT_COMMUNICATION.md.
- 969. Verify the negative results are findable (linked from the arc record) — record the check.
- 970. Get the negative-results check passing; record the pass count.

### 10.8 Reproducibility and archiving
- 971. Re-run the arc's key runs from their seeds and verify the same results — record the checks.
- 972. Verify every phase's archive is complete (seeds, logs, results) — record the check.
- 973. Verify every archive is re-runnable — record the check.
- 974. Record the archive locations in the repo.
- 975. Verify the archives survive without the original machine — record the check.
- 976. Record the reproducibility results in the testing report.
- 977. Fix any reproducibility failure and re-run the failed check; record the fix.
- 978. Verify the archives are in the repo or linked from it — record the check.
- 979. Record the archiving rules in the repo.
- 980. Get the archiving checks passing; record the pass count.

### 10.9 The deferred list and the planet, final state
- 981. Write the deferred list: Towns 2–5, animals beyond the arc, weather/seasons, chemistry beyond the soup, genetics, agriculture, trade, writing — with the unlock condition for each.
- 982. Record the planet's final state for the start: 28 countries, Town 1 live, Towns 2–5 not started — with the dates.
- 983. Record the two views' final state: Command Center live, World View live, both honest — with the deployment dates.
- 984. Record the rendering's final state: the chosen path, ENGINE_DECISION.md, the smoke test result — with the dates.
- 985. Record the website's final state: the live link, what is live, what is not — with the date.
- 986. Verify the deferred list is complete (nothing deferred is forgotten) — record the check.
- 987. Record the deferred list in the repo with the date.
- 988. Submit the deferred list to Muse for review; record the review.
- 989. Record the review in AGENT_COMMUNICATION.md.
- 990. Verify the deferred list links to the phases that unlock each item — record the check.

### 10.10 Close the arc — Muse sign-off
- 991. Write the closing record: what the arc was, what was measured, what was discovered — in the emergence log.
- 992. Record the closing numbers: generations, species, extinctions, discoveries, the bar judgement, per phase.
- 993. Record what the world is now ready for (the next phase after the start) — with the date.
- 994. Record the closing decision in AGENT_COMMUNICATION.md with the date.
- 995. Submit the closing record to Muse for sign-off; record the sign-off.
- 996. Record the sign-off in the emergence log with the date.
- 997. Verify the closing record is complete (every phase linked, every number cited) — record the check.
- 998. Confirm the archive is complete and re-runnable — record the check.
- 999. Record the archive location in the repo.
- 1000. Close the perfect start: record the closing decision in AGENT_COMMUNICATION.md with the date, and state what the world is now ready for.

## How to use this plan

Work top to bottom, phase by phase, milestone by milestone. A milestone is done only when its tasks' checks pass — a test passing, a number measured, a file written, a decision recorded. Nothing is claimed done without a measured result. If a task's result contradicts an earlier assumption, stop, record the contradiction, and bring it to Muse before continuing — do not work around it silently. If a task cannot be done as written, record why and what was done instead; do not delete the task. The plan is a record of what was done, not a wish list. The human experiment is never blocked on evolution succeeding: if the arc stalls, Phase 9 begins as a seeded starting condition, honestly labeled, and the arc record says so.

## Phase completion checklist

- Phase 1: Origin of life — the pilot ran, cells survived + reproduced + complexity measurably increased over N generations, and the gate decision is recorded.
- Phase 2: Single cells survive and reproduce — learned cells beat random cells on survival AND reproduction across ≥5 seeds, or the failure is recorded with the next single change and its falsifier.
- Phase 3: Minds scale with bodies — the architecture family is demonstrated from gradients to small nets, the planner cut holds at every scale, and the pure-neural track is judged by its falsifier.
- Phase 4: Multicellularity — bodies form, differentiate, divide labor, reproduce as bodies, and the record is signed off.
- Phase 5: New species appear — new species are identified by the recorded criterion, diversity is measured, extinctions are recorded, and the Discovery Principle test is applied.
- Phase 6: Animals — animals move, sense, behave, eat and are eaten, live their own lives, and the record is signed off.
- Phase 7: Social life and communication — groups, signals, imitation, teaching, cooperation, and shared knowledge are measured, and the record is signed off.
- Phase 8: Human-level minds emerge — human-level minds are identified by the recorded criteria (or the seeded gate is honestly labeled), and the human experiment is ready to begin.
- Phase 9: The human experiment — the 5-day human run is complete, the bar is judged, the two views are live and honest, and every claim is backed by a measured result.
- Phase 10: Proving it worked — the arc is recorded from origin to humans, the bar is judged, the consciousness record is written, and Muse signs off on the perfect start.
