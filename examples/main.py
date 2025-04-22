from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2

HOST = "172.17.11.142"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        

        # self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>", "utf-8"))
        self.wfile.write("<html><body><h1>HELLO WORLD!</h1></body></html>".encode("utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content_type", "application/json")
        self.end_headers()

        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())      # ✅
        # self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("Server stoped!")
