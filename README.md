# Sky Sentinel AI

Aerial awareness for a changing sky. A tactical ground-defense board for testing a defense.

Sky Sentinel AI is a runnable web app scaffold. It has two connected surfaces:

- **Sim Prep** — a 10 × 7 drag-and-drop board where you choose defenders, 200 caches, and hostile units, place them, then run a client-side defense simulation.
- **Air picture** — simulated tracks, sector health, a radar view, a signal log, and a small JSON API.

> **Scaffold status.** The board is a client-side simulation with fictional units. The air feed is simulated. No sensor adapter, trained model, alert delivery, authentication, or persistence is connected.

## Run

Requires Node.js 18+.

```bash
npm start
```

Open <http://127.0.0.1:3000>. There are no dependencies, so `npm install` is not required.

`npm run dev` uses Node's watch mode. Set `PORT` or `HOST` from `.env.example` if needed; the server reads the process environment directly.

## Sim Prep

Every **defender** carries a **100-pack**: a visible 100-round backpack. During a run, defenders spend 8 rounds per burst at hostiles in range. The token’s meter shows the remaining pack.

**200 caches** are 200-round resupply points. When a defender’s pack drops below 80 rounds, it draws the difference from a cache within three cells, topping the 100-pack back up. Caches are also physical obstacles on the board.

The **loadout steppers** set how many of each token are available. Use the tray to drag a token onto a cell, or tap a token and then tap a cell. A placed token can be dragged to another cell, dragged back to the tray, selected and moved by tapping a cell, or removed with `Delete`. `Escape` clears the selection.

The board phases are **SIM PREP**, **STAGED**, **SIM RUNNING**, and **DEBRIEF**. `Run sim` starts the defense; `Run again` restores the starting layout after a run; `New setup` clears the board; `Reset demo` restores the sample board.

## API

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Service state and uptime |
| `GET` | `/api/telemetry` | Sector health, tracks, and events |
| `POST` | `/api/scan` | Simulated sweep result |

Every response carries `mode: "simulation"`. The scan endpoint does not call a model or external service.

## Layout

```text
server.js              zero-dependency HTTP server
public/index.html      dashboard and Sim Prep markup
public/sim.css         tactical board, tokens, and controls
public/sim.js          drag/drop staging and defense simulation
public/app.js          air picture and radar
public/styles.css      shared shell and air picture styling
docs/ARCHITECTURE.md   boundaries and next seams
AGENT_COMMUNICATION.md async handoff for Muse
```

## Deliberately missing

- Real radar, ADS-B, weather, or camera adapters.
- A detection or tracking model.
- Server-authoritative simulation or durable run storage.
- Authentication and per-user access.
- Alert delivery.

Those are the next seams, not hidden claims.

## Direction

Keep the board’s unit contract stable while the interaction model is tested. If the sim graduates from a sandbox, move combat resolution behind an authenticated server boundary before adding persistence or shared runs.
