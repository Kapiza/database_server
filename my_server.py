from http.server import HTTPServer

from connection import connection
from handlers.main_handler import make_handler_class

hostName = "0.0.0.0"
serverPort = 8080

HandlerClass = make_handler_class(connection)
webServer = HTTPServer((hostName, serverPort), HandlerClass)  # instantiate webserver

print("Listening on: http://%s:%s" % (hostName, serverPort))

# Run webserver until stopped by keyboard interrupt
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

# properly close webserver and db connection
webServer.server_close()
connection.close()
print("\nServer stopped.")