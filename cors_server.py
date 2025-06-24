import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()

def main():
    parser = argparse.ArgumentParser(description="Simple CORS-enabled HTTP server")
    parser.add_argument('--port', type=int, default=8000, help='Port to run the server on')
    args = parser.parse_args()

    server_address = ('', args.port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"Serving at http://localhost:{args.port}")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
