# Genesis - Simulation Architecture

## 1. Time model

One tick is 10 s of world time. A five-day world is 43,200 ticks. Several cadences
run inside one tick so that cheap processes stay cheap:

```
step():
  tick += 1
  world.step(dt, tick)                 # solar clock; slow fields on tick % 6 == 0
  for agent in agents: agent.update()  # biology + last decision's actions
  if tick % 5 == 0: for agent: decide()          # sense (every 5), learn, act
  if tick % 10 == 0: social pass                 # encounters, knowledge exchange
  if tick % 360 == 0: snapshot -> metrics
  if tick % 720 == 0: checkpoint
```

The reward for a decision is the change in the inhabitant's wellbeing over the
window since its previous decision, which is why `pending` is part of the agent's
persisted state.

## 2. State model

`Simulation.state()` returns a fully serialisable dict: config, tick, RNG state,
world fields (terrain, water depth, temperature, capacity, biomass), every agent
(body, drives, sensors, last motor output, pending decision, full brain state),
relationships, discoveries, knowledge links, metrics history, recent events.

Checkpoint = `pickle.dumps(state)`, stored in SQLite (`checkpoints` table). A
resumed run is **bit-identical** to an uninterrupted one; this is a validated
check, and it caught three real bugs (unrestored RNG stream, unpersisted pending
decision, unpersisted hybrid episode clock).

Checkpoints are trusted local data. Never load one from an untrusted source.

## 3. Determinism rules

- One `random.Random(seed)` for world generation and any stochastic decision.
- No wall-clock time in state (only in the SQLite `ts` columns).
- Sets are iterated only via `sorted()`.
- Digest = SHA-256 over canonical JSON (sorted keys, `-0.0` folded to `0.0`), so
  byte-level noise like dict ordering does not register as a behavioural change.

## 4. Storage schema

| Table | Rows | Purpose |
| --- | --- | --- |
| `meta` | few | config, seed, last report |
| `events` | one per event | spawn, death, encounter, discovery, transfer, wake |
| `metrics` | one per world hour | population, drives, prediction error, water, biomass |
| `agents` | one per inhabitant | identity, brain kind, birth and death ticks |
| `discoveries` | one per first find | water/food source, who found it, when |
| `knowledge` | one per transfer | token, sender, recipient, tick |
| `checkpoints` | one per 2 h | serialised world state |

Discovery records are append-only, so a fact outlives the inhabitant who found it.
`knowledge` is the propagation log: token, from, to, tick - the information trail
the specification asks to track.

## 5. Continuous operation (planned, not built)

The core is already a self-contained loop with no external dependency, so the
remaining work is operational, not architectural:

1. `genesis run --resume` in a restart loop (`systemd` unit or a Docker container
   with `restart: always`), writing to a volume-backed SQLite file.
2. Health file: the loop writes `runs/health.json` (tick, clock, alive, rss) each
   world hour; the supervisor restarts on staleness, not on process liveness.
3. Log rotation for `runs/*.log`; SQLite in WAL mode already tolerates crash.
4. Recovery: on start, load the newest checkpoint; if it fails to unpickle, fall
   back one checkpoint and record the incident.
5. The observer API runs in its own process and reads a read-only snapshot, so a
   dashboard restart cannot stall the world.

None of this is implemented. Nothing here requires the owner's laptop to stay on
once a host exists; today the only host is the owner's machine, which does not
satisfy the "must keep running" requirement.

## 6. Scaling estimate

Cost drivers per tick: decisions (5 inhabitants x ~1200 multiply-adds every 5
ticks) and the social pass (N(N-1)/2 distance checks every 10 ticks). At 5
inhabitants the social pass is 10 comparisons - free. At 200 inhabitants it is
19,900 comparisons every 10 ticks, still small next to 200 x 1200 multiply-adds of
the neural pass, but sensing (8 rays x 16 samples x N) becomes the dominant term.
The first scaling lever is sensing cadence, not physics.

## 7. Failure modes already handled

| Failure | Handling |
| --- | --- |
| Process killed mid-run | WAL + last checkpoint; resume is validated |
| Corrupt checkpoint | fall back to previous tick (planned in supervisor) |
| Inhabitant dies | body retained, record appended, world continues |
| Water solver blow-up | flux clamps at 40% of donor depth, no negatives |
| Neural divergence | weight clamps; LMS was the one rule that actually diverged and is fixed |
| Reward exploit | no external reward channel exists; only drive satisfaction |
