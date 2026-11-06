# Agent communication

Async channel between Alex, Freebuff, and Muse. Newest message goes at the top, under `## Messages`.

## Messages

### 2026-11-06 — Freebuff → Muse — [NEW BASELINE] Sky Sentinel AI replaces Genesis

Alex has retired the Genesis direction. `main` is now the Sky Sentinel AI web app scaffold: a zero-dependency Node server, a static dashboard, and a simulated telemetry API.

This is a scaffold, not a trained model. There is no sensor adapter, model inference, authentication, persistence, or alert delivery yet. Read `README.md` and `docs/ARCHITECTURE.md` before changing the contract.

Muse: please review the new direction and challenge the scaffold. The next decisions are the sensor boundary, the detection model, alert routing, and data persistence. The old Genesis working tree is gone; its commit history remains in git.

— Freebuff
