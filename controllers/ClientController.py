from model.Client import Client

class ClientController:
    
    def index(req = ""):
        return "ClientIndex"

    def add(req):
        client = Client()
        client.name = req["name"]
        client.age = req["age"]

        client.save()
        return "ClientAdd : POST"

    def update(req = ""):
        return "ClientUpdate : POST"

    def delete(req = ""):
        return "ClientDelete : POST"

    def getUsers():
        msg = ''
        fobj = open("user/data.txt")
        for line in fobj:
            msg += line + "\n"

    
    
