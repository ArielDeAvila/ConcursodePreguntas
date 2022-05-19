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
        round1 = random.randint(0,4)
        round2 = random.randint(5, 9)
        round3 = random.randint(10, 14)
        round4 = random.randint(15, 19)
        round5 = random.randint(20, 24)
        
        self.information["categoria1"]={
            "category": self.lists[round1][0],
            "value": self.lists[round1][7],
            "question": self.lists[round1][1],
            "response1": self.lists[round1][2],
            "response2": self.lists[round1][3],
            "response3": self.lists[round1][4],
            "response4": self.lists[round1][5],
            "goodResponse": self.lists[round1][6]
        }
        
        self.information["categoria2"] = {
            "category": self.lists[round2][0],
            "value": self.lists[round2][7],
            "question": self.lists[round2][1],
            "response1": self.lists[round2][2],
            "response2": self.lists[round2][3],
            "response3": self.lists[2][4],
            "response4": self.lists[round2][5],
            "goodResponse": self.lists[round2][6]
        }
        
        self.information["categoria3"] = {
            "category": self.lists[round3][0],
            "value": self.lists[round3][7],
            "question": self.lists[round3][1],
            "response1": self.lists[round3][2],
            "response2": self.lists[round3][3],
            "response3": self.lists[3][4],
            "response4": self.lists[round3][5],
            "goodResponse": self.lists[round3][6]
        }
        
        self.information["categoria4"] = {
            "category": self.lists[round4][0],
            "value": self.lists[round4][7],
            "question": self.lists[round4][1],
            "response1": self.lists[round4][2],
            "response2": self.lists[round4][3],
            "response3": self.lists[round4][4],
            "response4": self.lists[4][5],
            "goodResponse": self.lists[round4][6]
        }
        
        self.information["categoria5"] = {
            "category": self.lists[round5][0],
            "value": self.lists[round5][7],
            "question": self.lists[round5][1],
            "response1": self.lists[round5][2],
            "response2": self.lists[round5][3],
            "response3": self.lists[round5][4],
            "response4": self.lists[round5][5],
            "goodResponse": self.lists[round5][6]
        }
        
   
        
             
        
    