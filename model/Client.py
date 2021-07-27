import json
import os

class Client():
    name = ""
    age = ""

    def __init__(self, name="", age=""):
        self.name = name
        self.age = age

    def getClient():
        msg = ''
        fobj = open("user/data.txt")
        for line in fobj:
            msg += line + "\n"

    def getClient(name):
        msg = ''
        fobj = open("user/data.txt")
        for line in fobj:
            msg += line + "\n"

    def save(self):
        obj = dict()
        obj["name"] = self.name
        obj["age"] = self.age

        data = json.dumps(obj)
        self.__storeData(data)
        return data

    def __storeData(self, data):
        if not os.path.exists("data"):
            os.mkdir("data")
        fobj = open("data/client.txt", "a")
        fobj.write(data + "\n")
        fobj.close()