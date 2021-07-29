from app.Model import Model
import json
import os

class Client(Model):
    __counter = 0
    __loc = "data/client.txt"
    name = ""
    age = ""

    def __init__(self, name="", age=""):
        self.checkDirectory()
        self.checkFile(self.__loc)
        self.name = name
        self.age = age
        self.__counter = self.__count()

    def get(self, name="", age=""):
        res = ""
        fobj = open(self.__loc)
        if name == "" and age == "":
            for line in fobj:
                res += line + "\n"
        else:
            for line in fobj:
                if line.index(name) >= 0 or line.index(age) >= 0:
                    res += line
                    break
        fobj.close()
        return res

    def save(self):
        obj = dict()
        obj["id"] = self.__counter
        obj["name"] = self.name
        obj["age"] = self.age
        data = json.dumps(obj)
        self.__storeData(data)
        
        return data

    def __storeData(self, data):
        fobj = open(self.__loc, "a")
        fobj.write(data + "\n")
        fobj.close()

    def __count(self):
        fobj = open(self.__loc)
        count = 0
        for line in fobj:
            count += 1
        fobj.close()
        return count
    
    def count(self):
        return self.__count