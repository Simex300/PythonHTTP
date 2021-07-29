from app.Model import Model
import json
import os
import re

class Client(Model):
    __counter = 0
    __loc = "data/client.txt"
    __fileLine = -1
    id = -1
    name = ""
    age = ""

    def __init__(self, id = ""):
        self.checkDirectory()
        self.checkFile(self.__loc)
        if id != "":
            self.get(id)
        self.__counter = self.__count()

    def get(self):
        res = ""
        fobj = open(self.__loc)
        for line in fobj:
            res += line
        fobj.close()
        return res

    def get(self, id):
        res = ""
        count = -1
        fobj = open(self.__loc)
        for line in fobj:
            count += 1
            if re.search('"id": %s' % id, line):
                res = line
                break
        
        self.__fileLine = count
        self.__loadJSON(json.loads(res))
        return res

    def save(self):
        obj = dict()
        if self.id != -1: 
            obj["id"] = self.id
        else: 
            obj["id"] = self.__counter
        obj["name"] = self.name
        obj["age"] = self.age
        data = json.dumps(obj)
        self.__storeData(data)
        
        return data

    def delete(self):
        fobj = open(self.__loc, "r")
        alldata = fobj.readlines()
        res = alldata.pop(self.__fileLine)

        fobj = open(self.__loc, "w")
        fobj.writelines(alldata)
        fobj.close()
        return res

    def __storeData(self, data):
        if self.__fileLine > -1:
           fobj = open(self.__loc, "r")
           alldata = fobj.readlines()
           alldata[self.__fileLine] = data + "\n"

           fobj = open(self.__loc, "w")
           fobj.writelines(alldata)
           fobj.close()
        
        else:
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

    def __loadJSON(self, data):
        print("jsonData", data)
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
