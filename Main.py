from http.server import BaseHTTPRequestHandler, HTTPServer
# import time
from TestServer import TestServer

hostName = "localhost"
port = 8080

if __name__ == "__main__":
    webServer = HTTPServer((hostName, port), TestServer)
    print("Server startet at http://%s:%s" % (hostName, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server Stopped")
