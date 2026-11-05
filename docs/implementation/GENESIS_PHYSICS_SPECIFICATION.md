# Genesis - Physics Specification

All quantities are SI. The world is a 1.024 km x 1.024 km heightfield of 32 x 32
cells (32 m cells). Time advances in 10 s ticks; slow fields update every 60 s.

## 1. Solvers

| Process | Model | Timestep | Conservation | Fidelity |
| --- | --- | --- | --- | --- |
| Terrain | fractal value noise heightfield, 4 octaves | static | n/a | 32 m horizontal |
| Water (global) | hydrostatic surface relaxation, pairwise | 60 s, 2 sweeps | mass exact | no momentum |
| Water (local) | explicit-flux shallow water, momentum | CFL <= 0.4 dx/sqrt(g h) | mass exact | waves, dam break |
| Heat | lumped capacity diffusion + solar + longwave | 60 s | energy via ledger | 2.5D column |
| Vegetation | logistic growth limited by light/moisture/temperature | 60 s | mass via harvest | per cell |
| Rigid bodies | velocity Verlet, quadratic drag, restitution | substepped | symplectic | spheres only |

### 1.1 Why two water solvers

A CFL-limited shallow-water solve over the whole world at 60 s would need hundreds
of substeps per cell and thousands of cells - unaffordable in pure Python. The
global world therefore uses a **diffusive** solver that is unconditionally stable,
exactly mass conserving, and produces lakes and level surfaces, but carries no
momentum. The momentum solver exists and is validated on small domains, and is the
intended high-fidelity path for local experiments (adaptive fidelity). This is a
documented approximation, not an accident.

### 1.2 Thermal model

Per-cell temperature with lumped capacity: land 1.0, water 4.0 (dimensionless
thermal mass). Solar input 5.5e-4 K/s scaled by illumination; longwave loss
2.2e-5 /s toward a 2 C sky; diffusion is a symmetric pairwise exchange with
conductance proportional to the smaller capacity, so internal exchange cannot
create energy. When water covers or uncovers a cell its capacity changes; that
energy change is booked as `capacity_adjustment` instead of hiding in the residual.

### 1.3 Rigid bodies

Velocity Verlet (symplectic, exact for constant acceleration), quadratic drag,
ground contact at the sampled heightfield, normal restitution and tangential
friction. Every inelastic loss is accumulated in `dissipated` so the ledger closes.

## 2. Measured validation

Command: `python -m genesis verify` (all 16 checks pass).

| Check | Measured | Tolerance |
| --- | --- | --- |
| Global water mass, 60 sweeps | drift 0 m^3 | <= 1e-6 relative |
| Shallow water volume, 300 steps | 32 -> 32 m^3, peak 2.0 -> 0.259 m, corner 0.172 m | <= 1e-9 relative |
| Thermal diffusion, 120 steps | drift 9.09e-13 | <= 1e-9 relative |
| Thermal ledger, 600 ticks | residual 0 (injected 0, radiated 243, capacity 1150) | <= 2% of forcing |
| Free fall, 2 s | 1.42e-14 m from analytic | <= 1e-6 relative |
| Ballistic energy, 1.5 s | 2.31e-16 relative drift | < 1e-9 |
| Restitution e=0.6 apex | 1.8 m vs 1.8 m (0.07% error) | < 12% |

## 3. Named limitations

Not implemented, and must not be claimed:

- No erosion, sediment transport, or landscape evolution.
- No wind field, clouds, precipitation, or pressure dynamics.
- No gas phase, no chemistry, no organic molecules.
- No electromagnetism beyond a placeholder constant.
- No sound propagation and no hearing; no smell. Senses are vision (8 rays, 40 m)
  plus local field samples. Hearing and chemosensing are planned, not present.
- No swimming: inhabitants cannot enter water deeper than 1.2 m.
- Global water has no momentum and cannot form rivers by itself; initial basins
  only. River channels must be authored or produced by a local high-fidelity study.
- Visibility is line-of-sight on the heightfield with a fixed eye height; there are
  no shadows, no scattering, no light transport.
- Terrain is 2.5D: overhangs, caves, and tunnels do not exist.

## 4. Multiscale schedule

| Cadence | Work |
| --- | --- |
| every tick (10 s) | biology, movement, action application |
| every 5 ticks (50 s) | sensing, decisions, learning |
| every 10 ticks (100 s) | social pass, knowledge exchange |
| every 6 ticks (60 s) | water, heat, vegetation |
| every 720 ticks (2 h) | checkpoint |

Adaptive fidelity today is a manual choice of solver (global vs local). Automatic
refinement around active regions is planned.

## 5. Planned upgrades, in cost order

1. Sound field with occlusion - cheap, closes a sensory gap.
2. Global coarse momentum solver (semi-implicit, 128 m cells) - medium.
3. Soil moisture as a state variable feeding vegetation and evaporation - medium.
4. Wind and precipitation driven by the thermal field - medium.
5. Local high-fidelity regions that step shallow water only near an experiment - larger.
6. Chemistry at the "reaction set" level, not molecular - larger, needs a spec.
