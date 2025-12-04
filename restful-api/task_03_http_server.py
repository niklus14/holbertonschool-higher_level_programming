#!/usr/bin/env python3
"""
task_03_http_server.py

Simple API server for automated tests.

Endpoints:
  GET /         -> plain text greeting
  GET /status   -> plain text "OK"
  GET /data     -> JSON {"name": "John", "age": 30, "city": "New York"}
  GET /info     -> JSON {"version": "1.0", "description": "A simple API built with http.server"}
Any other path -> 404 Not Found with plain text "Endpoint not found"
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse

HOST = "0.0.0.0"
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, obj, status=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        # Use exactly 'application/json' to satisfy strict content-type checks in tests
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, text, status=200):
        body = text.encode("utf-8")
        self.send_response(status)
        # text/plain with default charset is acceptable
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/":
            self._send_text("Hello, this is a simple API!", status=200)
            return

        if path == "/status":
            self._send_text("OK", status=200)
            return

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(payload, status=200)
            return

        if path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(payload, status=200)
            return

        # Unknown endpoint: return plain text 404 with the exact message expected by tests
        self._send_text("Endpoint not found", status=404)

    def do_POST(self):
        # Minimal POST handler to satisfy potential tests (not required by current tests)
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        content_type = self.headers.get("Content-Type", "")

        body_bytes = self.rfile.read(content_length) if content_length > 0 else b""

        if path == "/echo":
            if "application/json" in content_type:
                try:
                    data = json.loads(body_bytes.decode("utf-8") or "{}")
                    resp = {"received": data, "message": "Echo successful"}
                    self._send_json(resp, status=200)
                except json.JSONDecodeError:
                    self._send_text("Invalid JSON", status=400)
            else:
                self._send_text("Content-Type must be application/json", status=415)
            return

        self._send_text("Endpoint not found", status=404)

    # Keep output clean for tests
    def log_message(self, format, *args):
        return

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, host=HOST, port=PORT):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on {host}:{port} ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    run()