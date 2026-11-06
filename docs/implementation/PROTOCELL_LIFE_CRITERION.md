# Protocell life criterion



Status: pre-registered 2026-11-06, before the 8,000-tick validation runs; validated 2026-11-06. The pilot runs

used to tune rates are not validation runs. The validation seeds are 20261105, 20261106

and 20261107.



## What is being tested



A coarse-grained chemistry that starts with monomers, energy and no strands, membranes or

cells. Amphiphiles self-assemble into empty vesicles. Inside a vesicle, strands ligate and

hydrolyse. A strand is a catalyst when it starts with GG and has at least four bases. A

catalyst copies itself with a 2% per-base mutation probability, and it synthesises membrane

lipid from monomers. A vesicle grows only from its own catalyst-made lipid and divides at

twice its assembly lipid content, splitting its strands between two daughters. Daughters

inherit catalysts; an empty daughter can acquire one later by ligation, but that is not

inheritance. Vesicles can lyse. Nothing is placed or steered after t = 0.



The heritable catalytic trait is GC fraction: efficiency is `1 + 2 * GC` in the main arm.

The neutral control has efficiency 1 regardless of GC, so its GC changes are mutation and

drift, not selection. The no-catalysis control disables replication but leaves ligation,

membranes and division intact.



## The six criteria



A run counts as **operational life in this model** only if all six hold:



1. **Origin without placement.** At t = 0 there are no strands and no vesicles. The first

   catalyst appears by ligation, and the first catalysed copy follows it. Placed replicators

   disqualify the run.

2. **Self-sustaining replication.** The best lineage has at least 10 consecutive generations

   in which a daughter inherited at least one catalyst, reaches generation 10, has more than

   zero catalysed births, and persists for at least 5,000 ticks after its first catalyst.

3. **Compartmentalised individuality.** The lineage reproduces by vesicle division (at least

   10 divisions), and the inherited-catalyst streak is carried through those divisions.

4. **Metabolism.** The lineage produces catalyst-made membrane lipid, and the no-catalysis

   control cannot establish: it must have zero catalysed births and fail criterion 2.

5. **Heritable variation.** Mutation is enabled, at least one mutation event occurs, and at

   least one mutant catalyst sequence persists for 1,000 ticks (10 consecutive samples).

6. **Selection.** The main arm's final mean GC fraction exceeds the neutral control's final

   mean by at least 0.10, using the same seed and horizon, in at least 2 of 3 validation

   seeds. A within-run rise alone is not enough because the GG catalyst motif biases the

   mutation equilibrium upward; the neutral control is the null.



If a run fails a criterion it is reported as a negative result. Criteria are not changed

after seeing the validation numbers.



## What this would and would not establish



Passing all six would establish a self-sustaining, compartmentalised chemical system with

heredity, variation and measurable selection under a fixed set of coarse-grained rules -

the NASA working definition of life, operationalised. It would **not** establish wet-lab

chemistry, consciousness, intelligence, multicellularity or civilisation. The model has no

spatial structure, no explicit molecular structure, no translation, and its catalyst rule is

a designed genotype-phenotype map. Those limits go in the report with the result.



## Validation results (2026-11-06)

8,000 ticks, seeds 20261105-07, sample every 100 ticks.

| seed | first catalyst | first replication | births | divisions | generation | inherited streak | final GC | mutant persistence | established |
|---|---|---|---|---|---|---|---|---|---|
| 20261105 | 265 | 353 | 137511 | 5025 | 67 | 67 | 0.864 | 7700 | yes |
| 20261106 | 289 | 330 | 138081 | 5043 | 67 | 67 | 0.875 | 7600 | yes |
| 20261107 | 282 | 285 | 140663 | 5173 | 69 | 69 | 0.883 | 7800 | yes |

Neutral control final GC: 0.713 / 0.732 / 0.702. Main-minus-neutral differences:
+0.1511 / +0.1435 / +0.1812; criterion 6 passes in 3/3.

No-catalysis control: 0 births, 0 mutations, not established in 3/3, despite 1,580 / 1,531 /
1,676 divisions and inherited catalyst streaks of 25 / 24 / 27. This is the negative control:
membranes, ligation and division alone do not satisfy life.

Verdict: all six criteria pass in 3/3 main seeds, with all controls behaving as required.
Limits remain as stated above.
