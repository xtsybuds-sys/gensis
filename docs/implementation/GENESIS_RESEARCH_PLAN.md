# Genesis - Research Plan

Each item states a question, a measurement, and what result would force us to
withdraw the claim. No item is satisfied by a demonstration that merely looks alive.

## R1. Does a plastic network learn directed behaviour?

- Question: can the pure neural brain find water faster than a random policy?
- Design: same 5 worlds, same seeds; arms = neural, hybrid-without-planner,
  hybrid-with-planner, random motor policy.
- Measure: metres travelled before first drink; deaths in 5 days; mean hydration.
- Falsified if: neural is not distinguishable from random at n=5 seeds.
- Status: infrastructure ready, experiment not yet run (planner ablation missing).

## R2. Is curiosity doing anything?

- Question: does the novelty term change exploration, or is it decoration?
- Design: `novelty_weight` in {0, 0.35}; measure spatial coverage (unique cells
  visited / reachable cells) and time-to-first-discovery.
- Falsified if: no difference in coverage beyond seed noise.

## R3. Do world models generalise?

- Question: does the forward model predict *unseen* transitions?
- Design: hold out 20% of the sensor stream; compare held-out MSE to training MSE.
- Current state: only in-distribution MSE is measured (96.6% reduction). Generalisation
  is untested, and must not be claimed.

## R4. Does receiving knowledge help?

- Question: does a `water:` token reduce time to the next drink?
- Design: transfer enabled vs disabled; measure time-to-drink for the receiver.
- Falsified if: no reduction within 3 days.

## R5. Does sleep replay improve anything measurable?

- Question: does wake-time consolidation reduce post-wake prediction error vs none?
- Design: replay on/off; measure prediction error before and after sleep.

## R6. Does communication become compositional?

- Question: do inhabitants invent distinctions not present in the naming scheme?
- Current state: impossible - tokens are assigned by us. This experiment requires a
  learned symbol layer first. Until then, any "language emerged" claim is false.

## R7. FlyWire / connectome feasibility

Findings, kept deliberately modest:

- FlyWire provides a largely complete synaptic connectome of adult *Drosophila*
  (≈130k neurons, millions of synapses) with cell-type annotations.
- A connectome is wiring, not a brain: it does not supply synaptic weights, time
  constants, neuromodulation, or dynamics. Any simulation built on it still has to
  choose a neuron model, and the choices dominate the dynamics.
- Realistic spiking simulation of ~130k neurons with realistic connectivity is far
  beyond a single Python process, and beyond what this project needs to test its
  current questions.
- Recommendation: do **not** block the MVP. If pursued, the tractable path is a
  reduced circuit (e.g. a few thousand neurons in the mushroom body or central
  complex) as an optional pure-neural brain variant, benchmarked against the
  current recurrent core on the same tasks. Cost: a spiking simulator dependency
  (Brian2 or NEST) and a large data pipeline; requires owner approval.

## R8. Developmental trajectory

- Question: does capability grow with experience within one lifetime?
- Design: freeze half the population's plasticity after day 1 and compare survival,
  distance-to-water, and prediction error at day 5.
- This is the cleanest test that "development" is real rather than a random walk.

## R9. Evolution (deferred)

- Design sketch: genome = init weight scale, plasticity rate, hidden size, curiosity
  weight, sensory ray count; selection = survival over 5 days in a fixed world;
  measure generational change in genome and behaviour.
- Guard: evolution does not imply improvement. Report trait drift and fitness, and
  keep a control line with no selection.

## Method rules

1. Fix seeds, report n, never report a single lucky run.
2. Report nulls. A failed arm is a result.
3. Any behavioural claim needs a control arm differing in exactly one thing.
4. Never call a difference "emergence" unless the behaviour was not explicitly
   implemented and survives a scripted-behaviour review.
