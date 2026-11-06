# Abiotic chemistry baseline

Purpose: a baseline in which no life is placed. At `t = 0` the reactor contains four monomer
species, energy and nothing else. Life has to originate as chemical replication, or the run
records that it did not.

## Rules (fixed before the runs)

- Geochemistry adds energy and, from it, monomers.
- Monomers ligate into strands; strands join while they fit under `MAX_LEN = 10`.
- A strand of at least `MIN_TEMPLATE_LEN = 4` template-copies when the complementary monomers
  and energy exist. The copy inherits the complement with a 2% per-base mutation rate.
- Strands hydrolyse back to monomers. The strand population is capped at 500.
- Template replication **disabled** is the control arm.

## Pre-registered criterion

A lineage is "established" if, counting only samples at or after the first template-copy
event, it reaches 4 copies, holds at least 2 copies for 10 consecutive samples (2,000 ticks),
and has at least one one-base mutant neighbour. This is chemical self-replication with
heredity and variation. It is **not** a claim of life, consciousness or civilization.

## Results, 2026-11-06

Command: `python -m genesis abiotic --seeds 3 --ticks 60000 --out runs/abiotic/seed.json`

| seed | ticks | strands | births | first strand | first replication | max copies | persistence | mutants | established |
|---|---|---|---|---|---|---|---|---|---|
| 20261105 | 60000 | 493 | 79297 | 0 | 2 | 55 | 60000 | 3 | yes |
| 20261106 | 60000 | 499 | 79419 | 0 | 0 | 53 | 60000 | 3 | yes |
| 20261107 | 60000 | 495 | 79797 | 0 | 5 | 52 | 60000 | 3 | yes |

Control: `python -m genesis abiotic --seeds 2 --ticks 20000 --control`

| seed | ticks | strands | births | max copies | established |
|---|---|---|---|---|---|
| 20261105 | 20000 | 14 | 0 | 0 | no |
| 20261106 | 20000 | 17 | 0 | 0 | no |

## What this does and does not show

It shows that, under permissive template copying, a self-replicating lineage appears from
monomers and persists for the full window, with mutants, while the control never replicates.
It does **not** show that catalysis, protocells, life or civilization emerge. Any strand of
length 4 or more can copy, so this is the weakest form of the origin test. The next falsifier
is a catalytic requirement: replication only when a catalyst motif is present, so a
self-sustaining set has to arise rather than any template being able to copy.
