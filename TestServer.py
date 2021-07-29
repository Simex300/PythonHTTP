import json
from Route import Route
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

class TestServer(BaseHTTPRequestHandler):
    route = Route()

    def do_GET(self):
        try: 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""

            actualRoute = self.route.getRoute("GET", self.path)
            if len(actualRoute) == 2:
                endPath, executableMethod = actualRoute
                res = executableMethod()
                message = res
            elif len(actualRoute) == 3: 
                endPath, executableMethod, parameter = actualRoute
                res = executableMethod("", parameter)
                message = res
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
        if len(actualRoute) == 3:
            endPath, executableMethod, parameter = actualRoute
            if body.decode("utf-8") != "":
                request = json.loads(body.decode("utf-8"))
                res = executableMethod(request, parameter)
            else:
                res = executableMethod("", parameter)
        elif len(actualRoute) == 2:
            endPath, executableMethod = actualRoute
            request = json.loads(body.decode("utf-8"))
            res = executableMethod(request)

        self.wfile.write(res.encode("utf-8"))

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


        # self.send_response(200)
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))