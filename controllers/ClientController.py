from app.Controller import Controller
from model.Client import Client

class ClientController(Controller):
    
    def index(req = ""):
        client = Client()
        return client.get()

    def get(req, index):
        client = Client()
        return client.get(index)

    def add(req):
        client = Client()
        client.name = req["name"]
        client.age = req["age"]

        res = client.save()
        return res

    def update(req, index):
        client = Client(index)
        client.name = req["name"]
        client.age = req["age"]

        res = client.save()
        return res

    def delete(req, id):
        client = Client(id)
        return client.delete()

    def getUsers():
        msg = ''
        fobj = open("user/data.txt")
        for line in fobj:
            msg += line + "\n"

    
    
