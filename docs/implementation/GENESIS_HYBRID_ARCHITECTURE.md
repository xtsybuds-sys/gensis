# Genesis - Hybrid Architecture

A hybrid inhabitant is the same neural core plus non-neural components, as the
specification permits. The neural core is unchanged and receives the identical
24-float vector, so any behavioural difference is attributable to the added
components - provided the confound in section 6 is controlled.

## 1. Components

| Component | Implementation | Learns? |
| --- | --- | --- |
| Neural core | `NeuralBrain` (verbatim) | yes, online |
| Episodic memory | last 200 transitions (x, motor, next x, reward) | no (stored) |
| Sleep replay | on wake, re-fit the world model on up to 50 recent episodes | yes |
| Bearing memory | 8 water and 8 food vote channels, decay 0.97 / 0.85 | yes, decayed |
| Planner | drive-gated steering toward the strongest remembered bearing | no (fixed rule) |
| Symbol layer | discrete tokens, `water:i,j` / `food:i,j`, shared on contact | no (assigned) |

## 2. Behaviour

Motor output is a blend, not a replacement:

```
o[0] = 0.65 * plan.forward + 0.35 * neural[0]
o[1] = 0.75 * plan.turn    + 0.25 * neural[1]
```

The planner only engages when a drive is above 0.5 and a remembered bearing vote
is above 0.15, so an unthreatened inhabitant is driven mostly by its neural core.

## 3. Memory and sleep

Consolidation happens at wake: up to 50 recent episodes are replayed through the
world model, which lowers prediction error without new sensory input. This is the
minimum viable form of the memory-consolidation requirement; it is not a
biologically grounded replay mechanism, and it does not yet reorganise memory.

## 4. Knowledge as an object

A discovery becomes a token when an inhabitant first drinks or eats at a cell. The
token carries the source coordinates, is stored in the finder's token set, and is
copied to other hybrid brains within 25 m during the social pass. Every copy is
logged as `(tick, token, sender, recipient)` in the `knowledge` table.

Consequence: a fact can outlive its discoverer, and its spread is auditable. This
is the infrastructure the emergence questions need; it is not evidence that
culture emerged.

## 5. What "language" does not mean here

There is no grammar, no composition, no reference negotiation, and no symbol
invention - tokens are assigned by a naming scheme. Calling this "language" would
be false. It is a shared-label layer whose only job is to make knowledge transfer
observable and measurable.

## 6. Known confound (must be fixed before any comparative claim)

The planner is a **hand-designed prior**. It gives hybrid inhabitants an advantage
at water and food seeking that has nothing to do with learning. Any claim of the
form "hybrids outperform neural inhabitants" is therefore unsupported until the
planner is ablated. Planned control: a `planner=False` flag on the hybrid brain,
giving three arms (neural, hybrid-with-planner, hybrid-without-planner) evaluated
on identical seeds and identical worlds. Until that experiment exists, this
document makes no comparative performance claim.

## 7. Next experiments

1. Planner ablation (above) at n=5 seeds, measure first-drink distance and deaths.
2. Token utility: does receiving a `water:` token reduce time-to-next-drink?
   Falsifiable: no reduction within 3 days means the token layer is decorative.
3. Replay value: with and without consolidation, compare post-wake prediction error.
