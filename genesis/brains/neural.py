"""Pure neural inhabitant: recurrent network, online plasticity, forward model.

Learning is three-factor and local: a reward/novelty modulatory signal gates
Hebbian eligibility traces (no global backpropagation through the world). A
linear forward model trained by LMS supplies the intrinsic curiosity signal,
which is the prediction error of the agent's own sensory stream.
"""

from __future__ import annotations

import math

from ..sensors import INPUT_DIM
from ..util import clamp, matvec, norm

OUTPUT_DIM = 6


class NeuralBrain:
    kind = "neural"

    def __init__(self, rng, hidden=24, plasticity=0.02, novelty_weight=0.35,
                 label="neural"):
        self.label = label
        self.input_dim = INPUT_DIM
        self.output_dim = OUTPUT_DIM
        self.hidden = int(hidden)
        self.plasticity = float(plasticity)
        self.novelty_weight = float(novelty_weight)
        self.trace_decay = 0.9
        self.lr_pred = 0.03
        self.decay_out = 2.0e-6
        self.decay_in = 6.0e-6

        h = self.hidden
        self.w_in = [[rng.gauss(0.0, 0.45) for _ in range(INPUT_DIM)] for _ in range(h)]
        rec_scale = 0.55 / math.sqrt(h)
        self.w_rec = [[rng.gauss(0.0, rec_scale) for _ in range(h)] for _ in range(h)]
        self.w_out = [[rng.gauss(0.0, 0.45) for _ in range(h)] for _ in range(OUTPUT_DIM)]
        self.bias = [rng.gauss(0.0, 0.05) for _ in range(h)]

        self.state = [0.0] * h
        self.e_in = [[0.0] * INPUT_DIM for _ in range(h)]
        self.e_rec = [[0.0] * h for _ in range(h)]
        self.e_out = [[0.0] * h for _ in range(OUTPUT_DIM)]
        self.w_pred = [[0.0] * INPUT_DIM for _ in range(INPUT_DIM)]

        self.prediction_error = 1.0
        self.last_mse = 1.0
        self.novelty = 1.0
        self.cumulative_reward = 0.0
        self.decisions = 0
        self._pending = None
        self._prev_state = [0.0] * h

    # -- forward pass -----------------------------------------------------
    def act(self, x, ctx=None):
        x = list(x)
        prev = self.state
        pre = matvec(self.w_in, x)
        rec = matvec(self.w_rec, prev)
        state = [
            math.tanh(pre[k] + rec[k] + self.bias[k]) for k in range(self.hidden)
        ]
        out = [math.tanh(v) for v in matvec(self.w_out, state)]
        self._prev_state = prev
        self.state = state
        self._pending = (x, prev, state, out)
        self.decisions += 1
        return out

    # -- learning ---------------------------------------------------------
    def _lms(self, x, next_x):
        """Train the sensor-only forward model; return MSE.

        The predictor deliberately does not consume the motor output. When the
        action vector is fed back in, the regression target becomes a function
        of the network's own drifting output, the problem turns non-stationary
        and the error grows instead of shrinking (measured: MSE 0.66 -> 19.3).
        Predicting the next sensor from the current sensor is stationary and
        learnable, which is what a curiosity signal needs.
        """
        inputs = list(x)
        prediction = matvec(self.w_pred, inputs)
        err = [prediction[i] - next_x[i] for i in range(INPUT_DIM)]
        mse = sum(e * e for e in err) / INPUT_DIM
        self.last_mse = mse
        # Normalised LMS. The step is divided by input energy, which keeps the
        # update contractive for any sensor magnitude; plain LMS diverges once
        # lr * ||x||^2 exceeds 2, and sensor vectors are large here.
        norm2 = sum(v * v for v in inputs) + 1e-6
        gain = self.lr_pred / norm2
        keep = 1.0 - 1.0e-4
        for i in range(INPUT_DIM):
            e = clamp(err[i], -1.0, 1.0)
            row = self.w_pred[i]
            for j in range(INPUT_DIM):
                value = row[j] * keep - gain * e * inputs[j]
                row[j] = -6.0 if value < -6.0 else 6.0 if value > 6.0 else value
        return mse

    def learn(self, reward, next_x):
        if self._pending is None:
            return self.stats()
        x, prev, state, out = self._pending
        self._pending = None
        next_x = list(next_x)

        mse = self._lms(x, next_x)
        self.prediction_error = 0.98 * self.prediction_error + 0.02 * mse
        self.novelty = min(1.0, mse)

        for k in range(self.hidden):
            s = state[k]
            er = self.e_in[k]
            rr = self.e_rec[k]
            for j in range(INPUT_DIM):
                er[j] += s * x[j]
            for j in range(self.hidden):
                rr[j] += s * prev[j]
        for o in range(self.output_dim):
            eo = self.e_out[o]
            so = out[o]
            for k in range(self.hidden):
                eo[k] += so * state[k]

        mod = clamp(reward + self.novelty_weight * self.novelty, -3.0, 3.0)
        lr_out = self.plasticity
        lr_in = self.plasticity * 0.08
        td = self.trace_decay

        for k in range(self.hidden):
            er = self.e_in[k]
            rr = self.e_rec[k]
            wi = self.w_in[k]
            wr = self.w_rec[k]
            for j in range(INPUT_DIM):
                er[j] *= td
                value = wi[j] * (1.0 - self.decay_in) + lr_in * mod * er[j]
                wi[j] = -4.0 if value < -4.0 else 4.0 if value > 4.0 else value
            for j in range(self.hidden):
                rr[j] *= td
                value = wr[j] * (1.0 - self.decay_in) + lr_in * mod * rr[j]
                wr[j] = -4.0 if value < -4.0 else 4.0 if value > 4.0 else value

        for o in range(self.output_dim):
            eo = self.e_out[o]
            wo = self.w_out[o]
            for k in range(self.hidden):
                eo[k] *= td
                value = wo[k] * (1.0 - self.decay_out) + lr_out * mod * eo[k]
                wo[k] = -4.0 if value < -4.0 else 4.0 if value > 4.0 else value

        self.cumulative_reward += reward
        return self.stats()

    def consolidate(self):
        """Sleep replay hook; the pure neural brain has no episodic store."""
        return 0

    # -- introspection ----------------------------------------------------
    def weight_norm(self):
        return norm([v for row in self.w_out for v in row])

    def synapse_count(self):
        return self.hidden * INPUT_DIM + self.hidden * self.hidden + OUTPUT_DIM * self.hidden

    def stats(self):
        return {
            "kind": self.kind,
            "label": self.label,
            "hidden": self.hidden,
            "synapses": self.synapse_count(),
            "prediction_error": round(self.prediction_error, 5),
            "novelty": round(self.novelty, 5),
            "weight_norm": round(self.weight_norm(), 4),
            "mean_reward": round(
                self.cumulative_reward / max(1, self.decisions), 5
            ),
            "decisions": self.decisions,
        }

    # -- persistence ------------------------------------------------------
    def state_dict(self):
        return {
            "kind": self.kind,
            "label": self.label,
            "hidden": self.hidden,
            "w_in": self.w_in,
            "w_rec": self.w_rec,
            "w_out": self.w_out,
            "bias": self.bias,
            "state": self.state,
            "e_in": self.e_in,
            "e_rec": self.e_rec,
            "e_out": self.e_out,
            "w_pred": self.w_pred,
            "prediction_error": self.prediction_error,
            "novelty": self.novelty,
            "cumulative_reward": self.cumulative_reward,
            "decisions": self.decisions,
            "prev_state": self._prev_state,
            "pending": self._pending,
        }

    def load(self, data):
        self.w_in = data["w_in"]
        self.w_rec = data["w_rec"]
        self.w_out = data["w_out"]
        self.bias = data["bias"]
        self.state = data["state"]
        self.e_in = data["e_in"]
        self.e_rec = data["e_rec"]
        self.e_out = data["e_out"]
        self.w_pred = data["w_pred"]
        self.prediction_error = data["prediction_error"]
        self.novelty = data["novelty"]
        self.cumulative_reward = data["cumulative_reward"]
        self.decisions = data["decisions"]
        self._prev_state = data["prev_state"]
        self._pending = data.get("pending")
