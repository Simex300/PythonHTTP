from app.Controller import Controller
from model.Client import Client

class ClientController(Controller):
    
    def index(req = ""):
        return "ClientIndex"

    def add(req):
        client = Client()
        client.name = req["name"]
        client.age = req["age"]

        res = client.save()
        return res

    def update(req):
        return "ClientUpdate : POST"

    def delete(req = ""):
        return "ClientDelete : POST"

    def getUsers():
        msg = ''
        fobj = open("user/data.txt")
        for line in fobj:
            msg += line + "\n"

    
    
