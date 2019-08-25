from http.server import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(201)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(201)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"hello world")
        return

try:
    httpd = HTTPServer(("localhost", PORT_NUMBER), SimpleHTTPRequestHandler)
    print("* Simple HTTP server")
    print("* Serving at port", PORT_NUMBER)
    print("* Running on http://127.0.0.1:"+str(PORT_NUMBER)+"/ (Press CTRL+C to quit)")
    httpd.serve_forever()

except KeyboardInterrupt:
    print(" received, shutting down the web server")
    httpd.socket.close()