"""SQLite-backed persistence: event log, metrics, discoveries, checkpoints.

The simulation is the only writer. The observer API is read-only, which keeps
the information firewall intact: inhabitants can never reach this layer.
"""

from __future__ import annotations

import json
import os
import sqlite3
import time

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tick INTEGER NOT NULL,
    ts REAL NOT NULL,
    kind TEXT NOT NULL,
    agent TEXT,
    detail TEXT
);
CREATE INDEX IF NOT EXISTS idx_events_tick ON events(tick);
CREATE TABLE IF NOT EXISTS metrics (
    tick INTEGER PRIMARY KEY,
    ts REAL NOT NULL,
    data TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS agents (
    aid INTEGER PRIMARY KEY,
    name TEXT,
    brain TEXT,
    born_tick INTEGER,
    died_tick INTEGER,
    alive INTEGER
);
CREATE TABLE IF NOT EXISTS discoveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tick INTEGER,
    kind TEXT,
    cell TEXT,
    agent TEXT,
    detail TEXT
);
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tick INTEGER,
    token TEXT,
    sender TEXT,
    recipient TEXT
);
CREATE TABLE IF NOT EXISTS checkpoints (
    tick INTEGER PRIMARY KEY,
    ts REAL NOT NULL,
    bytes INTEGER NOT NULL,
    payload BLOB NOT NULL
);
"""


class Store:
    def __init__(self, path="genesis.sqlite"):
        directory = os.path.dirname(os.path.abspath(path))
        os.makedirs(directory, exist_ok=True)
        self.path = path
        self.conn = sqlite3.connect(path)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=NORMAL")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    # -- writes -----------------------------------------------------------
    def meta(self, key, value):
        payload = value if isinstance(value, str) else json.dumps(value)
        self.conn.execute(
            "INSERT INTO meta(key, value) VALUES(?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, payload),
        )
        self.conn.commit()

    def event(self, tick, kind, agent=None, detail=None):
        self.conn.execute(
            "INSERT INTO events(tick, ts, kind, agent, detail) VALUES(?,?,?,?,?)",
            (tick, time.time(), kind, agent, json.dumps(detail or {})),
        )

    def metric(self, tick, data):
        self.conn.execute(
            "INSERT OR REPLACE INTO metrics(tick, ts, data) VALUES(?,?,?)",
            (tick, time.time(), json.dumps(data)),
        )

    def agent(self, agent, tick):
        self.conn.execute(
            "INSERT OR REPLACE INTO agents(aid, name, brain, born_tick, died_tick, alive) "
            "VALUES(?,?,?,?,?,?)",
            (
                agent.aid,
                agent.name,
                agent.brain.kind,
                agent.born_tick,
                agent.died_tick,
                1 if agent.alive else 0,
            ),
        )

    def discovery(self, tick, kind, cell, agent, detail=None):
        self.conn.execute(
            "INSERT INTO discoveries(tick, kind, cell, agent, detail) VALUES(?,?,?,?,?)",
            (tick, kind, json.dumps(list(cell)), agent, json.dumps(detail or {})),
        )

    def knowledge(self, tick, token, sender, recipient):
        self.conn.execute(
            "INSERT INTO knowledge(tick, token, sender, recipient) VALUES(?,?,?,?)",
            (tick, token, sender, recipient),
        )

    def checkpoint(self, tick, payload):
        self.conn.execute(
            "INSERT OR REPLACE INTO checkpoints(tick, ts, bytes, payload) VALUES(?,?,?,?)",
            (tick, time.time(), len(payload), sqlite3.Binary(payload)),
        )
        self.conn.commit()

    def commit(self):
        self.conn.commit()

    # -- reads ------------------------------------------------------------
    def latest_checkpoint(self):
        row = self.conn.execute(
            "SELECT tick, payload FROM checkpoints ORDER BY tick DESC LIMIT 1"
        ).fetchone()
        return row

    def counts(self):
        result = {}
        for table in ("events", "metrics", "discoveries", "knowledge", "checkpoints"):
            row = self.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
            result[table] = row[0]
        return result

    def recent_events(self, limit=50):
        rows = self.conn.execute(
            "SELECT tick, kind, agent, detail FROM events ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [
            {
                "tick": r[0],
                "kind": r[1],
                "agent": r[2],
                "detail": json.loads(r[3] or "{}"),
            }
            for r in rows
        ]

    def close(self):
        self.commit()
        self.conn.close()
