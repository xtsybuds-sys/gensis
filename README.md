# Sky Sentinel AI

Aerial awareness for a changing sky.

Sky Sentinel AI is a runnable web app scaffold for an aerial awareness dashboard. It renders simulated tracks, sector health, a radar view, a signal log, and a small JSON API.

> **Scaffold status.** The feed is simulated. No sensor adapter, trained model, alert delivery, authentication, or persistence is connected. The interface says so.

## Run

Requires Node.js 18+.

```bash
npm start
```

Open <http://127.0.0.1:3000>. There are no dependencies, so `npm install` is not required.

`npm run dev` uses Node's watch mode. Set `PORT` or `HOST` from `.env.example` if needed; the server reads the process environment directly.

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
public/                dashboard, styles, and browser logic
docs/ARCHITECTURE.md   boundaries and next seams
AGENT_COMMUNICATION.md async handoff for Muse
```

## Deliberately missing

- Real radar, ADS-B, weather, or camera adapters.
- A detection or tracking model.
- Durable event storage.
- Authentication and per-user access.
- Alert delivery.

Those are the next seams, not hidden claims.

## Direction

Start with one real data source, keep the telemetry contract stable, and add inference only after the data shape is understood. The current API is the contract to challenge.
