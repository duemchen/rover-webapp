import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

os.chdir("/home/pi/rover_app")

class NoCacheHandler(SimpleHTTPRequestHandler):
    # Protokoll auf HTTP/1.1 setzen, damit Connection: close sauber greift
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Connection", "close")
        super().end_headers()

if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 80), NoCacheHandler)
    server.daemon_threads = True
    print("Server läuft in:", os.getcwd())
    server.serve_forever()
