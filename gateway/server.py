"""The Agent Gateway: the HTTP surface the world viewer and agents read.

Run with ``python -m gateway`` (or ``python gateway/server.py`` from the repo root).
It serves the local viewer in ``world/`` and a live, read-only feed of the real
soup pilot. Nothing here simulates in the browser.
"""

from __future__ import annotations

import json
import mimetypes
import os
import posixpath
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .solar import solar_position
from genesis.soup.live import LiveFeed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORLD_DIR = os.path.join(ROOT, "world")
CONTRACT_VERSION = 1
VIEWER_LATITUDE = 35.0
VIEWER_LONGITUDE = 0.0

FEED = LiveFeed()
FEED.start()


def world_payload():
    frame = FEED.snapshot()
    now = time.time()
    sun = solar_position(now, VIEWER_LATITUDE, VIEWER_LONGITUDE)
    return {
        "contract": CONTRACT_VERSION,
        "source": "genesis.soup.pilot.run_pilot on_tick (live)",
        "server_time": now,
        "sim": frame,
        "sun": sun,
        "patches": [
            {"id": 0, "x": 4.0, "y": 4.0, "radius": 3.0},
            {"id": 1, "x": 12.0, "y": 4.0, "radius": 3.0},
            {"id": 2, "x": 8.0, "y": 12.0, "radius": 3.0},
        ],
        "viewer": {
            "latitude_deg": VIEWER_LATITUDE,
            "longitude_deg": VIEWER_LONGITUDE,
            "units": "metres",
            "scale_note": "cells drawn enlarged; positions and counts are the simulation's",
        },
        "error": FEED.error,
    }


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    # Without this, Windows delayed-ACK adds ~40 ms to every small response.
    disable_nagle_algorithm = True

    def log_message(self, fmt, *args):
        pass

    def _send(self, status, body, content_type="application/json; charset=utf-8",
              cache="no-store"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", cache)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path == "/api/world":
            self._send(200, json.dumps(world_payload()))
            return
        if path == "/api/health":
            self._send(200, json.dumps({"ok": True, "tick": FEED.snapshot()["tick"]}))
            return
        if path == "/api/stream":
            self._stream()
            return
        self._static(path)

    def _stream(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        try:
            while True:
                payload = json.dumps(world_payload())
                self.wfile.write(f"data: {payload}\n\n".encode("utf-8"))
                self.wfile.flush()
                time.sleep(0.05)
        except (BrokenPipeError, ConnectionResetError, OSError):
            return

    def _static(self, path):
        if path in ("", "/"):
            path = "/index.html"
        clean = posixpath.normpath(path).lstrip("/")
        if clean.startswith("..") or os.path.isabs(clean):
            self._send(403, "forbidden", "text/plain")
            return
        target = os.path.join(WORLD_DIR, *clean.split("/"))
        if not os.path.isfile(target):
            self._send(404, "not found", "text/plain")
            return
        ctype = mimetypes.guess_type(target)[0] or "application/octet-stream"
        with open(target, "rb") as handle:
            body = handle.read()
        self._send(200, body, ctype, cache="no-cache")


def serve(host="127.0.0.1", port=8787):
    server = ThreadingHTTPServer((host, port), Handler)
    server.daemon_threads = True
    print(f"genesis gateway on http://{host}:{port} (contract v{CONTRACT_VERSION})", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        FEED.stop()
        server.server_close()


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
    serve(port=port)
