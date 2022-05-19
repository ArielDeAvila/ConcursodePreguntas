from entities import question

class Player():
    def __init__(self,name:str=""):
        self.name = name
        self.info = {}
        self.question()
        self.extraInfo()
             
    def question(self):
        searchInfo = question.Question()
        self.info = searchInfo.information
        
    def extraInfo(self):
        self.info["name"] = self.name
        self.info["count"] = 0
        self.info["acumulado"] = 0


        

