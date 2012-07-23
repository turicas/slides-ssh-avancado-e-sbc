#!/usr/bin/env python2
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        ip, port = self.client_address
        self.wfile.write("IP do cliente: {0}\n".format(ip))

if __name__ == "__main__":
    try:
        server = HTTPServer(('', 8000), Handler)
        print("HAI")
        print("CAN HAS PORT 8000?")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKTHXBYE")
        server.shutdown()
    finally:
        server.socket.close()
