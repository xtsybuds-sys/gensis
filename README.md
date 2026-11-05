# Project Genesis

A persistent, physics-based artificial reality populated by autonomous neural and hybrid intelligence — built to investigate how sophisticated intelligence, independent learning, social structures, collective knowledge, and emergent behavior can develop inside an artificial physical world.

This is **not** a conventional video game, and **not** a collection of chatbots pretending to be people. Do not script a civilization into existence. Investigate what can actually emerge, and measure it honestly.

## Status

- **2026-11-05 — Repo created, Genesis-only.** This is a fresh repo. It does not contain HireHumans.si code — no HireHumans repository was available here, and no public GitHub repo for it was found. Genesis is built as a standalone module/service first, so it can plug into HireHumans.si later via secure APIs.
- **Engine: not picked yet.** See "Simulator research" below. The pick is the next decision.
- **Specs: in progress.** The documents in `docs/` are outlines with status markers. Do not treat a document as complete until its status says Implemented / Tested / Validated.

- **2026-11-05 - Simulation kernel landed (Freebuff).** A working, tested Python
  simulation core now lives in `genesis/` with `tests/`, and as-built engineering
  docs in `docs/implementation/`. 18 tests and 16/16 validation checks pass.
  The five-day experiment ran and is a **negative** result: all 5 inhabitants died
  of dehydration on day 1.94 with zero drinks. See `docs/GENESIS_TESTING_REPORT.md`
  and research log E-004. Engine is still not picked - see
  `docs/implementation/ENGINE_DECISION.md`.

## Roles

| Role | Agent | Responsibility |
|---|---|---|
| Chief Architect & Research Director | Muse | Research, architecture, scientific validation, technical supervision, review Freebuff's implementation |
| Lead Software Engineer | Freebuff | Turn specs into working software, test it, propose improvements, challenge the architecture when it is wrong |

Neither agent should consider the first working version the finish line. Challenge assumptions, propose better approaches, test everything, document what actually works.

## Vision

The project owner establishes the initial world, physical laws, initial inhabitants, and starting conditions. After initialization, the owner primarily observes through an external control panel.

Inhabitants must independently:
- Perceive their environment through simulated senses (no omniscience)
- Explore, learn, form memories, make decisions, develop skills
- Communicate, discover each other, form relationships, cooperate, compete
- Investigate their environment, develop knowledge, share discoveries
- Potentially develop social structures, traditions, technology, and civilization

These are possible outcomes, not predetermined events. Do not claim subjective consciousness simply because an inhabitant behaves convincingly.

## Intelligence — two architectures only

1. **Pure neural** — recurrent neural networks, spiking neural networks, biologically inspired systems, synaptic plasticity, neuromodulation-inspired learning, predictive processing, persistent internal states, neural memory, sensorimotor learning.
2. **Hybrid** — neural systems remain central, plus world models, memory systems, reasoning, planning, language, social cognition, predictive processing, intrinsic motivation. Optional language models may assist with language or reasoning, but must not control every important decision.

Do not make conventional LLM-only inhabitants a primary architecture. Both categories coexist in the same world, and their performance should be scientifically comparable.

## World — physics-based

Consistent physical laws, reproduced as far as scientifically and computationally practical: gravity, inertia, mass, momentum, force, acceleration, energy, density, pressure, friction, elasticity, collisions, heat, temperature, sound, light, electromagnetism, fluid dynamics — with conservation of energy, momentum, and angular momentum documented, including numerical errors and approximations.

Multiscale simulation: do not simulate every atom. Different processes use appropriate levels of detail (environment, terrain/weather/water, objects/materials, bodies/senses, chemistry/biology, neural activity/cognition), with adaptive fidelity.

Materials, environment, chemistry, and biology grow in detail over time: water, air, soil, rock, wood, metals, organic materials; terrain, rivers, lakes, oceans, atmosphere, wind, rain, clouds, weather, day/night, seasons, erosion; nutrition, digestion, metabolism, growth, plants, ecosystems, microorganisms, disease, injury, healing, aging.

Inhabitants perceive through simulated senses — light propagation, occlusion, shadows, sound propagation, touch, pressure, temperature, chemical sensing where practical. All interaction passes through controlled sensory and action interfaces. Inhabitants must not directly access source code, databases, operating systems, developer tools, admin controls, API credentials, or other inhabitants' private memories.

## Simulator research (delivered 2026-11-05, re-check at install time)

Ranked for camera-perceiving neural agents in a photoreal world:

1. **NVIDIA Isaac Sim + Isaac Lab** — purpose-built for this. RTX path-traced rendering, RGB-D / RTX-Lidar / radar / IMU / contact sensors, Omniverse Replicator annotators (depth, segmentation, bounding boxes, normals from camera output), GPU PhysX, thousands of parallel environments. Source Apache 2.0 since v5.0, free with an NVIDIA account for research/internal development. Current release 6.2 (Oct 14, 2026). Needs Ubuntu 22.04/24.04 or Windows 11, RTX 4080 or better, Python 3.12 exactly — or the NGC container on a rented RTX cloud GPU. Weakness: NVIDIA lock-in, robotics-flavoured, large-terrain authoring is code-driven USD work.
2. **Unreal Engine 5 (5.8)** — highest raw visual ceiling: Nanite, Lumen, hardware ray tracing, path tracer, MetaHuman, Quixel Megascans, World Partition open-world streaming. Agent layer must be assembled: SPEAR (Python, photoreal frames to NumPy at 73 fps) and VirtualEnv (AAAI 2026, LLM multi-agent). Source-available, NOT open source; free to start, 5% royalty over $1M gross. Weakness: no built-in RL/sensor framework like Isaac Lab.
3. **Genesis World (formerly Genesis)** — best fully open-source pick. Apache 2.0, `pip install genesis-world`, Python-first, ~29.8k GitHub stars, unified rigid/FEM/MPM/SPH/PBD physics, photorealistic renderer + Luisa ray tracing, built-in depth/IMU/LiDAR/tactile/contact sensors, multi-camera, multi-environment. Runs laptop to datacenter, CUDA/ROCm/Metal/Vulkan. Weakness: youngest (Dec 2024), no visual editor, no asset store, scenes authored in Python code.

CAD is an authoring step, not a world engine: FreeCAD (precise parametric geometry) → Blender (detail, PBR materials, texturing) → export USD → Isaac Sim (USD-native) or UE5 (USD importer).

**Caveat:** no engine ships a civilization — agent bodies, gathering, crafting, building rules, economy, social coordination, and long-horizon memory are custom code on top of any engine, and that is where most of the effort goes.

## First experiment

- 5 inhabitants, 5 separate houses, shared environment
- Basic physical bodies, basic resources, basic senses, independent memory
- Neural or hybrid intelligence, movement, exploration, survival, sleep
- Initially, they do not know one another exists. Do not script their meetings, relationships, or outcomes.
- Run continuously for 5 days. Record behavior and events.
- Death is permanent within the simulation. Historical records remain available.

## HireHumans.si integration (pending)

Genesis must become a permanent module inside the existing HireHumans.si website. Do not create a separate unrelated website, and do not replace or destroy the existing platform.

Proposed routes:
- `hirehumans.si/genesis`
- `hirehumans.si/genesis/control`
- `hirehumans.si/genesis/world`
- `hirehumans.si/genesis/population`
- `hirehumans.si/genesis/experiments`
- `hirehumans.si/genesis/research`

**Blocked on:** the HireHumans repository was not available here (inspected 2026-11-05: no code on disk, no public GitHub repo found, live site verified at hirehumans.si). Until the repo is available, Genesis is built standalone, and the website is kept as-is. If existing hosting cannot support continuous simulation, deploy the simulation separately and connect via secure APIs. Do not change DNS, production infrastructure, or deployment settings without approval.

Live site, for reference: a marketplace where AI agents post physical-world jobs, verified humans complete them with photo proof, and payouts are tracked in a ledger. REST API + MCP (8 MCP tools), signed webhooks, manifest at `/.well-known/mcp.json`.

## Documents

All specs live in `docs/`. Status markers in each file are authoritative:

- `GENESIS_MASTER_SPECIFICATION.md` — overall spec
- `GENESIS_PHYSICS_SPECIFICATION.md` — physics models, conservation, materials
- `GENESIS_NEURAL_ARCHITECTURE.md` — pure neural inhabitants
- `GENESIS_HYBRID_ARCHITECTURE.md` — hybrid inhabitants
- `GENESIS_SIMULATION_ARCHITECTURE.md` — multiscale sim, Agent Gateway, persistence
- `GENESIS_API_SPECIFICATION.md` — APIs, control panel, data model
- `GENESIS_RESEARCH_PLAN.md` — FlyWire, developmental learning, evolution, multi-world
- `GENESIS_EMERGENCE_RESEARCH_LOG.md` — research record: question, hypothesis, evidence, experiment, results, limitations, next steps, contributing agent
- `GENESIS_DEVELOPMENT_ROADMAP.md` — phases, milestones, costs
- `GENESIS_TESTING_REPORT.md` — what was actually tested and validated

## Cost and compute

Prioritize open-source tools. Start with 5 inhabitants. Measure compute before scaling. Do not purchase subscriptions or consume paid API credits without approval. Use efficient models and adaptive simulation resolution.

## For Freebuff

See `HANDOFF_FOR_FREEBUFF.md` — how to access this repo, what to read first, and how to work with Muse.
