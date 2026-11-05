# ENGINE_DECISION — executed

**Status: EXECUTED, 2026-11-05. The smoke test prints a settled box.**

Muse delegated the engine call to Freebuff ("do whatever is best and easiest"), with the
rule that this document is written as an executed decision only once the smoke test
prints a settled box. It does.

## The blocker, as measured

Genesis World 1.4.5 and torch 2.15.0+cpu installed cleanly. `quadrants`, the engine's
compiler backend, writes its kernel cache to a hardcoded literal
`C:/quadrants_cache/qdcache/` inside `quadrants_python.cp312-win_amd64.pyd`. The Python
layer exposes no `cache_dir`, and `QD_CACHE_PATH`, `QD_CACHE_DIR`, `QD_LIB_DIR`,
`TI_CACHE_DIR` and `TI_CACHE_PATH` all leave the path unchanged. `gs.init` therefore
died with `PermissionError: [WinError 5] Access is denied`.

## What was done

1. One-time elevated `mkdir C:\quadrants_cache`, approved by the machine's user.
2. That folder was owned by the elevated token, so the normal account still could not
   create `qdcache` inside it (the engine failed again at
   `C:/quadrants_cache/qdcache`). Granted modify rights on that one folder and its
   children: `icacls C:\quadrants_cache /grant Sentinel:(OI)(CI)M`.
3. No override, no engine patch, no vendored copy: the engine writes where it always
   expected to, with permissions that let it.

## Proof

Run from `gensis/tools/` with the engine venv, so the repo's `genesis/` package cannot
shadow the engine:

```
.venv-engine/Scripts/python.exe engine_smoke.py
engine=cpu steps=200 seconds=4.073 fps=49.1 rest_z=0.2499 expected=0.2500
settled=True
```

A body dropped onto the floor settles at 0.2499 m against the analytic 0.2500 m after
200 steps. This is the first engine-stepped scene in the project.

## What this establishes, and what it does not

- **Establishes:** the engine runs headless on this host, steps a scene, and matches the
  analytic rest height to 0.1 mm at 49.1 steps/s on CPU.
- **Does not establish:** the photoreal rendering standard (plan task 721), GPU
  throughput, or engine-versus-kernel equivalence on the 128 m town. None of those is
  claimed here; each needs its own measurement.
- The stdlib kernel remains the source of truth for every number in
  `docs/GENESIS_TESTING_REPORT.md` until an engine scene reproduces one.

## Cost

One elevated folder and one ACL grant. No money, no account, no dependency change.
