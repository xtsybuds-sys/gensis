# Genesis - Neural Architecture (pure neural inhabitant)

## 1. Interface

Both architectures use exactly this interface, which is what makes them
comparable rather than merely coexisting.

| Vector | Dimension | Contents |
| --- | --- | --- |
| input | 24 | 8 ray proximities, 8 surface codes (none/water/plant/rock), light, local slope, thirst, hunger, fatigue, warmth, health, day phase |
| output | 6 | forward, turn, drink, eat, rest, signal |

Sensors are produced only by sampling the world from the agent's position; a
validation check confirms that a water cell 724 m away does not alter the vector.

## 2. Core

```
h_t   = tanh(W_in x_t + W_rec h_{t-1} + b)          # 24 -> 24 -> 24, tanh
o_t   = tanh(W_out h_t)                             # 24 -> 6
```

No backpropagation through the world, no batch training, no pretraining. All
learning is online and local, as the specification requires of a neural inhabitant.

## 3. Plasticity

Three-factor, reward-modulated Hebbian learning with eligibility traces:

```
E_in  += h_t (x)ᵀ            E_rec += h_t (h_{t-1})ᵀ        E_out += o_t (h)ᵀ
E     *= 0.9                 (decay each decision)
mod    = clamp(r + 0.35 * novelty, -3, 3)
W     += lr * mod * E  -  decay * W                          (clamped to ±4)
```

`lr_out = 0.02`, `lr_in = 0.0016` (slower feature learning), weight decay
`2e-6`/`6e-6`. Traces are used as the eligibility bridge between an action and the
outcome observed one window later.

## 4. Forward model and curiosity

A sensor-only linear predictor, trained by normalised LMS:

```
x̂_{t+1} = W_pred x_t
e = x̂_{t+1} - x_{t+1},   mse = mean(e²)
W_pred[i][j] -= (lr / (||x||² + eps)) * e_i * x_j * keep
novelty = min(1, mse)                 # intrinsic reward for surprise
```

`lr_pred = 0.03`, ridge `keep = 1 - 1e-4`. Normalisation keeps the step contractive
for any sensor magnitude.

Two design decisions were forced by measurement, not taste (see the research log):

1. Plain LMS diverged - the update was written with the wrong sign, so error grew
   geometrically. Fixed; now contracts as predicted.
2. Action-conditioned prediction was abandoned: feeding the network's own drifting
   motor output into the regressor makes the target non-stationary and the error
   grows (measured MSE 0.66 -> 19.3). Sensor-only prediction is stationary.

Result on the rotation task: **MSE 0.400 -> 0.0135, a 96.6% reduction** over 240
decisions (`intelligence/forward-model-learning`).

## 5. Reward

Extrinsic reward is only the change in the agent's own wellbeing:

```
wellbeing = 0.30*energy + 0.28*hydration + 0.22*nutrition + 0.20*health
reward    = 40 * (wellbeing_after - wellbeing_before)
```

There is no task reward, no external score, and no reward channel an inhabitant can
game without actually drinking, eating, resting, and staying alive.

## 6. What this architecture is not

- Not spiking. No spike timing, no STDP window, no membrane dynamics.
- No hierarchy, no attention, no separate neuromodulator channels (dopamine-like
  modulation is a single scalar).
- No episodic memory and therefore no sleep replay (`consolidate()` returns 0).
- No developmental curriculum; capability growth is whatever plasticity yields.

These are candidate upgrades, each with an experiment, in `GENESIS_RESEARCH_PLAN.md`.

## 7. Falsifiable first question

Does a purely plastic network with only drive-based reward and prediction-error
curiosity learn directed water-seeking better than a random motor policy, within
five days and across >= 5 seeds? Metric: mean distance to water at first drink,
against a random-policy baseline. If it does not beat random, the claim "the neural
inhabitant learns" must be withdrawn for this version.
