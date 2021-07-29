from app.Controller import Controller
from controllers.ClientController import ClientController
import re

class Route:
    routes = {
        "GET": [
            ('/', ClientController.index),
            ('/[id]', ClientController.get)
        ],
        "POST": [
            ('/', ClientController.add),
            ('/[id]', ClientController.update),
            ('/client', ClientController.update),
            ('/client/[id]', ClientController.update)
        ],
        "404": [
            ("/", Controller.notFound)
        ]
    }
    
    def getRoute(self, method, path):
        if re.search(".+/[A-Za-z0-9]", path):
            key = re.findall(".+/([A-Za-z])", path)
            print(key)
            return [endList for endList in self.routes[method] if re.search(".+/\[[A-Za-z]\]", endList[0])]
        else:
            print("here")
            for routes in self.routes[method]:
                if routes[0] == path:
                    return routes
                elif re.search(".*\/(\[[a-zA-Z]+\])", routes[0]):
                    print("Checked:", routes)
                    route, routeMethod = routes
                    routearr = route.split("/")
                    patharr = path.split("/")
                    if len(routearr) == len(patharr):
                        same = True
                        length = len(routearr)
                        print("Routes: ", routearr, patharr, length)
                        for i in range(0, length-1):
                            if routearr[i] != patharr[i]:
                                same = False
                                break
                        if same:
                            routes = routes + tuple([patharr[length-1]])
                            return routes
                    pass
                
            return self.routes["404"][0]
            # return [endList for endList in self.routes[method] if endList[0] == path]