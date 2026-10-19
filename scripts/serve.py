#!/usr/bin/env python3
"""Tiny local server that behaves like GitHub Pages / Cloudflare Pages:
extensionless URLs (/docs/cli) resolve to docs/cli.html, and missing
paths return 404.html with a 404 status. Use it to check that canonical
URLs (extensionless) and the files ARKlight emits (.html) agree.

Usage: python scripts/serve.py [DIR] [PORT]
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DIR = sys.argv[1] if len(sys.argv) > 1 else "ARK"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8000


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)

    def translate_path(self, path):
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        return p

    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.exists(os.path.join(DIR, "404.html")):
            body = open(os.path.join(DIR, "404.html"), "rb").read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    print(f"serving {DIR}/ at http://localhost:{PORT}")
    ThreadingHTTPServer(("", PORT), Handler).serve_forever()
