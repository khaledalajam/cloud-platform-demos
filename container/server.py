import http.server
import json
import time

start = time.time()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        if self.path == "/health":
            self.wfile.write(json.dumps({
                "status": "ok",
                "service": "platform-container",
                "role": "Platform Engineering",
                "uptime": round(time.time() - start, 1)
            }).encode())
        else:
            self.wfile.write(json.dumps({
                "message": "Platform Engineering — Container Deployment Service",
                "environment": "production",
                "version": "1.0.0"
            }).encode())

    def log_message(self, format, *args):
        pass  # suppress default access logs

http.server.HTTPServer(("", 3000), Handler).serve_forever()   
