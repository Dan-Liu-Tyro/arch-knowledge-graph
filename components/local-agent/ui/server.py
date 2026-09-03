#!/usr/bin/env python3
"""Local-only HTML relay for Arc Lite. Stdlib only, no deps, no deployment.

Serves index.html and relays POST /ask to a headless `claude -p --agent
arc-lite` invocation, mirroring exactly how a Claude Code session already
invokes the subagent (.claude/agents/arc-lite.md) -- this just automates
that same call instead of adding a second, parallel way to talk to it.
"""

import http.server
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
UI_DIR = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8765


def ask_arc_lite(question: str) -> str:
    """The one seam to change if this ever moves off a local subprocess call
    onto a deployed API -- everything else in this file is transport."""
    result = subprocess.run(
        [
            "claude", "-p", question,
            "--agent", "arc-lite",
            "--output-format", "json",
            "--permission-prompts", "none",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=180,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "claude CLI exited non-zero")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return result.stdout.strip()
    if payload.get("is_error"):
        raise RuntimeError(payload.get("result") or "Arc Lite returned an error")
    return payload.get("result", "").strip()


class Handler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, status: int, body: dict) -> None:
        data = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path != "/":
            self.send_response(404)
            self.end_headers()
            return
        html = (UI_DIR / "index.html").read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def do_POST(self):
        if self.path != "/ask":
            self.send_response(404)
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length))
            question = body["question"].strip()
            if not question:
                raise ValueError("empty question")
        except (json.JSONDecodeError, KeyError, ValueError):
            self._send_json(400, {"error": "expected JSON body {\"question\": \"...\"}"})
            return
        try:
            answer = ask_arc_lite(question)
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            self._send_json(502, {"error": str(exc)})
            return
        self._send_json(200, {"answer": answer})

    def log_message(self, fmt, *args):
        pass


def main():
    server = http.server.HTTPServer((HOST, PORT), Handler)
    print(f"Arc Lite UI: http://{HOST}:{PORT}  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    sys.exit(main())
