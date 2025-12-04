#!/usr/bin/env python3
"""
Simple API server using Python's http.server
Endpoints:
  GET /         -> plain text greeting
  GET /status   -> plain text "OK"
  GET /data     -> JSON {"name": "John", "age": 30, "city": "New York"}
  GET /info     -> JSON {"version": "1.0", "description": "..."}
  POST /echo    -> echoes back JSON payload (Content-Type: application/json)
Any other path -> 404 Not Found with JSON message
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
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, text, status=200):
        body = text.encode("utf-8")
        self.send_response(status)
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

        # Unknown endpoint
        self._send_json({"error": "Endpoint not found", "path": path}, status=404)

    def do_POST(self):
        # Example: small echo endpoint for JSON body POSTs to /echo
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        content_type = self.headers.get("Content-Type", "")

        body_bytes = self.rfile.read(content_length) if content_length > 0 else b""

        # Only accept JSON for this demo
        if path == "/echo":
            if "application/json" in content_type:
                try:
                    data = json.loads(body_bytes.decode("utf-8") or "{}")
                    # echo back with an acknowledgement
                    resp = {"received": data, "message": "Echo successful"}
                    self._send_json(resp, status=200)
                except json.JSONDecodeError:
                    self._send_json({"error": "Invalid JSON"}, status=400)
            else:
                self._send_json({"error": "Content-Type must be application/json"}, status=415)
            return

        # POST to unknown path
        self._send_json({"error": "Endpoint not found", "path": path}, status=404)

    # Suppress default logging to keep output clean; remove if you want logs
    def log_message(self, format, *args):
        # Uncomment next line to enable basic logging
        # super().log_message(format, *args)
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