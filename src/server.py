from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import sys


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b'Running smoothly')
            return

        elif parsed_path.path == '/test':
            try:
                cat = json.loads(parsed_qs['category'][0])
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Try another time')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Pased Qs worked')
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile(b'Not Found')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.send_response_only()

def create_server():
    return HTTPServer(('127.0.0.1', 3000), HTTPRequestHandler)

def run_forever():
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()

if __name__ == '__main__':
    run_forever()