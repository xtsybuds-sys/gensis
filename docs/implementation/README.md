# Implementation docs (Freebuff)

The repository has two documentation sets on purpose:

| Location | Owner | Meaning |
| --- | --- | --- |
| `docs/GENESIS_*.md` | Muse (architect) | normative specification. Outlines today; status markers are authoritative. |
| `docs/implementation/*` | Freebuff (engineer) | **as-built** description of what actually runs, what was measured, and what is missing. |

If a spec and an as-built document disagree, the code and the test report win, and
the disagreement is a bug to raise with the architect - not something to paper over.

## Contents

| File | Contents |
| --- | --- |
| `ENGINE_DECISION.md` | Engine recommendation with measured hardware evidence, and the options that were rejected |
| `GENESIS_PHYSICS_SPECIFICATION.md` | Solvers as implemented, conservation results, every approximation named |
| `GENESIS_NEURAL_ARCHITECTURE.md` | Pure neural brain: dimensions, plasticity rule, forward model, measured learning |
| `GENESIS_HYBRID_ARCHITECTURE.md` | Hybrid brain: memory, replay, planner, symbol layer, and the declared confound |
| `GENESIS_SIMULATION_ARCHITECTURE.md` | Tick pipeline, state model, checkpointing, determinism, storage, scaling |
| `GENESIS_API_SPECIFICATION.md` | Observer API contract for the future dashboard (not running) |
| `GENESIS_RESEARCH_PLAN.md` | Falsifiable experiments R1-R9, including FlyWire feasibility |
| `GENESIS_DEVELOPMENT_ROADMAP.md` | Phase-by-phase status |

The authoritative record of test results is `docs/GENESIS_TESTING_REPORT.md`; the
research record is `docs/GENESIS_EMERGENCE_RESEARCH_LOG.md`.

## Two naming facts that will trip people up

1. The **repository** is `gensis` (as spelled by the owner). The **Python package**
   is `genesis/`. Both are intentional; do not "fix" either.
2. Paths inside these as-built documents are written relative to the package root,
   e.g. `physics/fields.py` means `genesis/physics/fields.py` in this repo.

## Running it

```bash
python -m unittest discover -s tests -t . -v
python -m genesis verify
python -m genesis run --days 5 --db runs/five-days.sqlite --progress 7200
```

`runs/` is git-ignored: checkpoints are large and regenerable.
