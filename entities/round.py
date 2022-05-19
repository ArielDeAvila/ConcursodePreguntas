import random
from Frames import message_frame
from tkinter import *

class Round():
    def __init__(self,questions=None,details=None,player=None):
        self.questions = questions
        self.details = details
        self.player = player
        
        self.details.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.questions.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)
        self.commandButtons()
        self.round()
        
    def orderQuestion(self):
        order = [1, 2, 3, 4]
        random.shuffle(order)

        return order
       
    def roundCount(self):
        self.player.info["count"] += 1 
        numCount = self.player.info["count"]
        
        return numCount
        
    def textQuestions(self):
        self.numCategory = str(self.roundCount())
        order = self.orderQuestion()
        
        self.txt1 = self.player.info["categoria" + self.numCategory]["response"+str(order[0])]
        self.txt2 = self.player.info["categoria" + self.numCategory]["response"+str(order[1])]
        self.txt3 = self.player.info["categoria" + self.numCategory]["response"+str(order[2])]
        self.txt4 = self.player.info["categoria" + self.numCategory]["response"+str(order[3])]
        txtCat = self.player.info["categoria" + self.numCategory]["category"]
        txtQtn = self.player.info["categoria" + self.numCategory]["question"]
        
        self.questions.btn1["text"] = self.txt1
        self.questions.btn2["text"] = self.txt2
        self.questions.btn3["text"] = self.txt3
        self.questions.btn4["text"] = self.txt4
        self.questions.lbl_category["text"] = txtCat
        self.questions.lbl_question["text"] = txtQtn
    
    def textDetails(self):
        self.details.lbl_enjuego_valor["text"] = self.player.info["categoria"+self.numCategory]["value"]
        self.details.lbl_acumulado_valor["text"] = str(self.player.info["acumulado"])
    
    def round(self):
        self.textQuestions()
        self.textDetails()
    
    def quitGame(self):
        acc = self.player.info["acumulado"]
        message_frame.MessageWindow(self.questions.master, acc,self.player)
    
    def nextRound(self):
        if int(self.numCategory) < 5:
            self.player.info["acumulado"] += int(self.player.info["categoria" + self.numCategory]["value"])
            self.round()
        else:
            self.player.info["acumulado"] += int(self.player.info["categoria" + self.numCategory]["value"])
            self.quitGame()
    
    def goodResponse(self,txt):
        num = self.player.info["categoria" + self.numCategory]["goodResponse"]
        goodResponse = self.player.info["categoria" + self.numCategory]["response"+str(num)]
        
        if txt == goodResponse:
            self.nextRound()
        else:
            self.quitGame()

    def commandButtons(self):
        self.questions.btn1["command"] =lambda: self.goodResponse(self.txt1)
        self.questions.btn2["command"] =lambda: self.goodResponse(self.txt2)
        self.questions.btn3["command"] =lambda: self.goodResponse(self.txt3)
        self.questions.btn4["command"] =lambda: self.goodResponse(self.txt4)
        
    
    