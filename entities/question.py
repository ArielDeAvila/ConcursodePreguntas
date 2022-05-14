import csv
import random

class Question():
    def __init__(self):
        self.information={}
        self.lists = []
        self.searchQuestions()
        self.fillInformation()
    
    def searchQuestions(self):
        with open("files/questions.csv") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.lists.append(row)
    
    def fillInformation(self):
        turn1 = random.randint(0,4)
        turn2 = random.randint(5, 9)
        turn3 = random.randint(10, 14)
        turn4 = random.randint(15, 19)
        turn5 = random.randint(20, 24)
        
        self.information["categoria1"]={
            "category": self.lists[turn1][0],
            "value": self.lists[turn1][7],
            "question": self.lists[turn1][1],
            "response1": self.lists[turn1][2],
            "response2": self.lists[turn1][3],
            "response3": self.lists[turn1][4],
            "response4": self.lists[turn1][5],
            "goodResponse": self.lists[turn1][6]
        }
        
        self.information["categoria2"] = {
            "category": self.lists[turn2][0],
            "value": self.lists[turn2][7],
            "question": self.lists[turn2][1],
            "response1": self.lists[turn2][2],
            "response2": self.lists[turn2][3],
            "response3": self.lists[2][4],
            "response4": self.lists[turn2][5],
            "goodResponse": self.lists[turn2][6]
        }
        
        self.information["categoria3"] = {
            "category": self.lists[turn3][0],
            "value": self.lists[turn3][7],
            "question": self.lists[turn3][1],
            "response1": self.lists[turn3][2],
            "response2": self.lists[turn3][3],
            "response3": self.lists[3][4],
            "response4": self.lists[turn3][5],
            "goodResponse": self.lists[turn3][6]
        }
        
        self.information["categoria4"] = {
            "category": self.lists[turn4][0],
            "value": self.lists[turn4][7],
            "question": self.lists[turn4][1],
            "response1": self.lists[turn4][2],
            "response2": self.lists[turn4][3],
            "response3": self.lists[turn4][4],
            "response4": self.lists[4][5],
            "goodResponse": self.lists[turn4][6]
        }
        
        self.information["categoria5"] = {
            "category": self.lists[turn5][0],
            "value": self.lists[turn5][7],
            "question": self.lists[turn5][1],
            "response1": self.lists[turn5][2],
            "response2": self.lists[turn5][3],
            "response3": self.lists[turn5][4],
            "response4": self.lists[turn5][5],
            "goodResponse": self.lists[turn5][6]
        }
        
   
        
             
        
    