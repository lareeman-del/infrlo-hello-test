import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"hello from infrlo"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

port = int(os.environ.get("PORT", "8080"))
print(f"HELLO_READY port={port}", flush=True)
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
