# Engine decision - recommendation from Freebuff

Status: **recommendation, not a decision.** No engine is installed and nothing has
been purchased. This document exists so the pick is made on evidence.

## 1. The machine we actually have

Measured 2026-11-05 on the only host available:

| Fact | Value | Why it matters |
| --- | --- | --- |
| OS | Windows 11 Education, build 26200 | Isaac Sim supports Windows 11, so OS is fine |
| CPU | 4 logical cores | parallel environments are CPU-bound at the wrapper level |
| RAM | 15.7 GB | below the comfortable line for a photoreal sim + agent stack |
| GPU | Intel Iris Xe Graphics, 2 GB VRAM, driver 32.0.101.7088 | **no CUDA, no RTX, no ray-tracing cores** |
| `nvidia-smi` | not found | confirms no NVIDIA driver/GPU |
| Disk free | 134.6 GB | enough for one engine, not several asset libraries |
| Python | 3.12.10, pip 25.0.1 | matches Isaac Sim's required 3.12 |

## 2. The requirement that decides it

The first experiment must run **continuously for five days**. That is not a
benchmark; it is an always-on service. So the engine must:

1. run on hardware we have, or on hardware we are approved to rent;
2. survive 120 hours unattended;
3. be free to use without per-hour spend, at least until the owner approves a budget;
4. expose sensors we can actually feed to neural inhabitants.

## 3. Scoring against those requirements

| Criterion | Isaac Sim + Lab | UE 5.8 | Genesis World |
| --- | --- | --- | --- |
| Runs on this host | **no** - needs RTX + CUDA | partially (Iris Xe, no Lumen-class perf) | **yes** - CPU/Metal/Vulkan/ROCm backends |
| 5-day unattended run | only on a rented RTX GPU | heavy editor/runtime, fragile headless on this class of GPU | designed as a Python library, headless by nature |
| Cost | rented RTX cloud GPU = recurring spend, needs approval | 5% royalty over $1M gross | Apache 2.0, no cost |
| Sensors | best in class (RGB-D, LiDAR, IMU, contact, annotators) | none built in; assemble SPEAR/VirtualEnv | good (depth, IMU, LiDAR, tactile, contact, multi-camera) |
| Physics | GPU PhysX, best rigid fidelity | Chaos, excellent visuals | unified rigid/FEM/MPM/SPH/PBD |
| Time to first inhabited run | days (USD authoring, RTX host) | weeks (agent layer from scratch) | hours (pip, Python scenes) |
| Project maturity | highest | highest visual ceiling | youngest spin-up risk |

## 4. Recommendation

**Pick Genesis World as the project's engine, and keep the engine behind the Agent
Gateway so it is replaceable.** Do not adopt Isaac Sim as the v1 path.

Reasons, in the order that drives the decision:

1. **Isaac Sim is not runnable here.** Recommending it means the first experiment
   waits on a rented RTX instance. That is a recurring cost and an owner approval,
   for a first experiment that does not need photoreal pixels: the inhabitants must
   find water and survive five days, not recognise textures.
2. **Genesis World runs on this exact machine**, is Apache 2.0, Python-native, and
   is specified by Muse as having the sensor suite the neural architecture needs.
   It is the only candidate that satisfies all four requirements today.
3. **UE 5.8 is a rendering target, not an agent simulation runtime.** Its visual
   ceiling is real, and I would revisit it for presentation later. As the physics
   and sensor host for five continuously running agents it costs the most effort
   (assemble SPEAR/VirtualEnv, author a world) for the least experimental value.
4. **The engine should not be able to trap the minds.** If physics, sensors and
   rendering sit behind one interface, the simulation kernel can be swapped without
   rewriting brains, memory, society or persistence. That is also what makes an
   Isaac Sim phase-2 possible later without a rewrite.

## 5. Where we are today, and what I will do

A zero-dependency Python kernel already exists in `genesis/` and runs the first
experiment at ~939 ticks/s for five inhabitants. It is **not** a photoreal engine and
does not claim to be: vision is 8 rays on a heightfield, no light transport, no
shadows. It is the reference backend that validates the intelligence stack, the
persistence layer, and the experiment protocol at zero cost and full determinism.

Proposed sequence:

1. **Now:** keep the kernel as the reference backend; fix the survival calibration
   (see research log E-004). Nothing here needs an engine.
2. **Next:** introduce an explicit `Backend` seam - physics step, sensor sample,
   action application - and implement the kernel as `ReferenceBackend`.
3. **Then:** a Genesis World spike (install, one inhabited cell, one day of runtime)
   measured against the same sensor contract, on this host. Re-check its version and
   CPU-backend behaviour at install time; Muse's research predates install.
4. **Deferred:** Isaac Sim, only if a photoreal/camera-learning experiment is funded
   and an RTX host is approved. UE 5.8 for presentation only.

## 6. What would change this recommendation

- An RTX 4090-class machine becoming available at no recurring cost: Isaac Sim
  becomes the strongest option for camera-based learning, and the backend seam makes
  it a swap rather than a rewrite.
- Genesis World failing the spike on this host (no CPU fallback, or dependency
  conflicts): fall back to the reference kernel, and treat the engine as a later
  presentation layer.
- A decision that inhabitants must learn from pixels rather than from a sensor
  vector: that raises the compute floor by orders of magnitude and must be costed
  before any engine is adopted.

## 7. Decision needed from Alex

Approve one of:

- **A (recommended):** Genesis World as engine, kernel as reference backend, no spend.
- **B:** rent an RTX GPU and go Isaac Sim first (recurring cost, needs a budget).
- **C:** stay engine-agnostic and keep building on the reference kernel until the
  survival baseline works, then re-decide.
