import os

class Model:

    def checkDirectory(self):
        if not os.path.exists("data"):
            os.mkdir("data")
    
    def checkFile(self, path):
        if not os.path.exists(path):
            open(path, "a").close()
