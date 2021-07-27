from controllers.ClientController import ClientController

class Route:
    routes = {
        "GET": [
            ('/hi', ClientController.index)
        ],
        "POST": [
            ('/', ClientController.add)
        ]
    }
    
    def getRoute(self, method, path):
        return [endList for endList in self.routes[method] if endList[0] == path]