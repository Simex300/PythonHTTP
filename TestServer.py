import json
from Route import Route
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import os

class TestServer(BaseHTTPRequestHandler):
    route = Route()

    def do_GET(self):
        try: 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""

            actualRoute = self.route.getRoute("GET", self.path)
            # if self.path.endswith("/getuser"):
            #     fobj = open("user/data.txt")
            #     for line in fobj:
            #         message += line + "\n"
            # elif self.path.endswith("/route"):
            #     routes = self.route.getRoute(0)
            #     print(routes)
            if len(actualRoute) > 0:
                endPath, executableMethod = actualRoute[0]
                res = executableMethod()
                print(res)
            else:
                message += "<html><body>404 not found!</body></html>"
            self.wfile.write(message.encode('utf-8'))
            return
        except IOError:
            print("Get Received: but with 404")
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        contentLength = int(self.headers['Content-Length'])
        body = self.rfile.read(contentLength)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'POST Received.')
        response.write(b'Received: ')
        response.write(body)

        actualRoute = self.route.getRoute("POST", self.path)
        if len(actualRoute) > 0:
            endPath, executableMethod = actualRoute[0]
            request = json.loads(body.decode("utf-8"))
            res = executableMethod(request)

        # if not os.path.exists("user"):
        #     os.mkdir("user")
        # fobj = open("user/data.txt", "a")
        # obj = body.decode('utf-8')
        # obj = obj.strip()
        # obj = obj.split("\n")
        # obj = "".join(obj)
        # obj = obj.split("\r")
        # obj = "".join(obj)
        # obj = obj.split(" ")
        # obj = "".join(obj)
        # print(obj)
        # fobj.write(obj + "\n")
        # fobj.close()

        self.wfile.write(response.getvalue())

        # self.send_response(200)
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))