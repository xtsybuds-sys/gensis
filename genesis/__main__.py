"""Genesis command line.

    python -m genesis run --days 5 --db runs/five-inhabitants.sqlite
    python -m genesis verify
    python -m genesis status --db runs/five-inhabitants.sqlite
"""

from __future__ import annotations

import argparse
import json
import pickle
import sys
import time

from . import verify
from .config import Config
from .sim import Simulation
from .store import Store


def cmd_run(args):
    cfg = Config(
        seed=args.seed,
        days=args.days,
        grid=args.grid,
        population=args.population,
        tick_seconds=args.tick_seconds,
        checkpoint_every=args.checkpoint_every,
        log_every=args.log_every,
    )
    store = Store(args.db)
    sim = Simulation(cfg, store)
    if args.resume:
        row = store.latest_checkpoint()
        if row is None:
            print("no checkpoint found; starting a fresh world")
        else:
            sim.load_state(pickle.loads(row[1]))
            print(f"resumed at tick {sim.tick} ({sim.world.clock()})")
    started = time.time()
    print(f"Genesis: {cfg.population} inhabitants, {cfg.world_days:.2f} world days")
    report = sim.run(progress=args.progress or None)
    elapsed = time.time() - started
    report["elapsed_s"] = round(elapsed, 2)
    report["ticks_per_s"] = round(sim.tick / max(elapsed, 1e-9), 1)
    store.meta("last_report", report)
    store.close()
    text = json.dumps(report, indent=2)
    print(text)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
        print(f"wrote {args.out}")
    return 0


def cmd_verify(args):
    results = verify.run_all()
    width = max(len(r["check"]) for r in results)
    failures = 0
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"  [{status}] {result['check']:<{width}}  {verify.brief(result)}")
        if not result["passed"]:
            failures += 1
    print(f"\n{len(results) - failures}/{len(results)} checks passed")
    return 0 if failures == 0 else 1


def cmd_status(args):
    store = Store(args.db)
    row = store.latest_checkpoint()
    if row is None:
        print(f"no checkpoints in {args.db}")
        return 1
    state = pickle.loads(row[1])
    sim = Simulation(Config(**state["cfg"]), None)
    sim.load_state(state)
    print(json.dumps(sim.report(), indent=2))
    print(json.dumps({"counts": store.counts()}, indent=2))
    return 0


def cmd_calibrate(args):
    from .experiments import calibrate, format_table

    seeds = [args.seed + i for i in range(args.seeds)]
    arms = tuple(part.strip() for part in args.arms.split(",") if part.strip())
    results = calibrate(
        seeds,
        days=args.days,
        arms=arms,
        grid=args.grid,
        population=args.population,
        world=args.world,
    )
    print(format_table(results))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            json.dump(results, handle, indent=2)
        print(f"wrote {args.out}")
    return 0


def cmd_soup(args):
    """Primordial soup pilot: cells in a bounded dish, mutation, selection."""
    from .soup.pilot import evaluate, format_table, run_pilot

    seeds = [args.seed + i for i in range(args.seeds)]
    results = []
    for seed in seeds:
        row = run_pilot(
            seed,
            target_turnovers=args.turnovers,
            minutes=args.minutes,
            initial=args.population,
            cap=args.cap,
            floor_turnovers=args.floor,
            verbose=True,
            checkpoint_path=f"{args.out}.partial.json" if args.out else None,
        )
        results.append(row)
        print(
            f"seed {seed}: turnovers {row['turnovers']:.0f} gen {row['max_gen']} "
            f"pop {row['final']['population']} ticks {row['ticks']} "
            f"{row['ticks_per_s']} t/s target={'yes' if row['reached_target'] else 'no'}"
        )
        if args.probe:
            break
    print()
    print(format_table(results))
    verdict = evaluate(results, target=args.turnovers)
    print()
    print(json.dumps(verdict, indent=2, sort_keys=True))
    if args.probe:
        row = results[0]
        projected = row["elapsed_s"] * (args.target / max(row["turnovers"], 1e-9))
        print(
            f"probe: {row['turnovers']:.0f} turnovers in {row['elapsed_s']}s; "
            f"projected {args.target} turnovers = {projected:.0f}s per seed"
        )
    if args.out:
        payload = {"rows": results, "verdict": verdict}
        with open(args.out, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
        print(f"wrote {args.out}")
    return 0 if args.probe or verdict["passed"] else 1


def cmd_abiotic(args):
    """Abiotic chemistry baseline: no cells, no placed life; measure replication."""
    from .abiotic.reactor import format_table, run_abiotic

    seeds = [args.seed + i for i in range(args.seeds)]
    rows = []
    for seed in seeds:
        row = run_abiotic(seed, ticks=args.ticks, replication=not args.control)
        rows.append(row)
        print(
            f"seed {seed}: strands {row['strands']} births {row['births']} "
            f"copies {row['max_copies']} persist {row['persistence_ticks']}t "
            f"mutants {row['mutant_neighbours']} established={row['established']}"
        )
    if args.control:
        print()
        print("control: template replication disabled")
    print()
    print(format_table(rows))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            json.dump({"rows": rows, "control": bool(args.control)}, handle, indent=2)
        print(f"wrote {args.out}")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="genesis", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run an experiment")
    run.add_argument("--days", type=float, default=5.0)
    run.add_argument("--seed", type=int, default=20261105)
    run.add_argument("--grid", type=int, default=32)
    run.add_argument("--population", type=int, default=5)
    run.add_argument("--tick-seconds", type=float, default=10.0)
    run.add_argument("--checkpoint-every", type=int, default=720)
    run.add_argument("--log-every", type=int, default=360)
    run.add_argument("--db", default="runs/genesis.sqlite")
    run.add_argument("--out", default=None)
    run.add_argument("--progress", type=int, default=0)
    run.add_argument("--resume", action="store_true")
    run.set_defaults(func=cmd_run)

    check = sub.add_parser("verify", help="run the validation suite")
    check.set_defaults(func=cmd_verify)

    status = sub.add_parser("status", help="print the latest checkpoint report")
    status.add_argument("--db", default="runs/genesis.sqlite")
    status.set_defaults(func=cmd_status)

    cal = sub.add_parser("calibrate", help="multi-seed calibration and ablations")
    cal.add_argument("--seeds", type=int, default=3)
    cal.add_argument("--days", type=float, default=5.0)
    cal.add_argument("--arms", default="population,planner,random")
    cal.add_argument("--grid", type=int, default=32)
    cal.add_argument("--population", type=int, default=5)
    cal.add_argument("--world", type=int, default=1024)
    cal.add_argument("--seed", type=int, default=20261105)
    cal.add_argument("--out", default=None)
    cal.set_defaults(func=cmd_calibrate)

    soup = sub.add_parser(
        "soup", help="primordial soup pilot (cells, mutation, nutrient dish)"
    )
    soup.add_argument("--seeds", type=int, default=5)
    soup.add_argument("--turnovers", type=int, default=2000)
    soup.add_argument("--floor", type=int, default=1000)
    soup.add_argument("--target", type=int, default=2000)
    soup.add_argument("--minutes", type=float, default=45.0)
    soup.add_argument("--population", type=int, default=200)
    soup.add_argument("--cap", type=int, default=600)
    soup.add_argument("--seed", type=int, default=20261105)
    soup.add_argument("--out", default=None)
    soup.add_argument("--probe", action="store_true")
    soup.set_defaults(func=cmd_soup)
    abiotic = sub.add_parser(
        "abiotic", help="abiotic chemistry baseline (no cells; measure replication)"
    )
    abiotic.add_argument("--seeds", type=int, default=3)
    abiotic.add_argument("--seed", type=int, default=20261105)
    abiotic.add_argument("--ticks", type=int, default=60000)
    abiotic.add_argument("--control", action="store_true", help="disable template replication")
    abiotic.add_argument("--out", default=None)
    abiotic.set_defaults(func=cmd_abiotic)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
