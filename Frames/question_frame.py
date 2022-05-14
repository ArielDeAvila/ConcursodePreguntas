from tkinter import *
from Frames import message_frame
import random

class QuestionWindow(Frame):
    def __init__(self, master=None,player:dict={},details=None):
        super().__init__(master)
        self.master = master
        self.player = player
        self.acc = details
        self.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
        self.createWidgets()

    def accAdd(self):
        num1 = int(self.player.info["categoria"+self.numCategory]["value"])
        num2 = self.player.info["acumulado"]
        num3 = num2 + num1
        self.player.info["acumulado"] = num3
        self.acc.lbl_acumulado_valor["text"] = str(num3)
    
    def quitGame(self):
        self.accAdd()
        acc = str(self.player.info["acumulado"])
        message_frame.MessageWindow(self.master, acc)
    
    def evaluateResponse(self,txt:str):
        valueGoodQuestion = self.player.info["categoria" + self.numCategory]["goodResponse"]
        value1 = txt
        value2 = self.player.info["categoria" + self.numCategory]["response"+valueGoodQuestion]
        if value1 == value2:
            return True
        else:
            return False
        
    def turn(self,txt:str):
        if self.player.info["count"]<5:
            if self.evaluateResponse(txt):
                self.accAdd()
                self.createWidgets()
                self.acc.lbl_enjuego_valor["text"] = self.player.info["categoria" + self.numCategory]["value"]
            else:
                self.quitGame()
        else:
            self.quitGame()    
    
    def orderQuestion(self):
        lists = [1,2,3,4]
        random.shuffle(lists)
        
        return lists       
    
    def turnCount(self):
        num = self.player.info["count"]
        numberCount = num + 1
        self.player.info["count"] = numberCount
        
        return numberCount
    
    def createWidgets(self):
        self.numCategory = str(self.turnCount())
        order = self.orderQuestion()
        
        txt1 = self.player.info["categoria" + self.numCategory]["response"+str(order[0])]
        txt2 = self.player.info["categoria" + self.numCategory]["response"+str(order[1])]
        txt3 = self.player.info["categoria" + self.numCategory]["response"+str(order[2])]
        txt4 = self.player.info["categoria" + self.numCategory]["response"+str(order[3])]
        
        self.lbl_category = Label(self,text=self.player.info["categoria"+self.numCategory]["category"])
        self.lbl_question = Label(self, text=self.player.info["categoria"+self.numCategory]["question"], bg='grey')
        self.btn1 = Button(
            self, text=txt1, command=self.turn(txt1), bg='yellow', fg='blue')
        self.btn2 = Button(
            self, text=txt2, command=self.turn(txt2), bg='yellow', fg='blue')
        self.btn3 = Button(
            self, text=txt3, command=self.turn(txt3), bg='yellow', fg='blue')
        self.btn4 = Button(
            self, text=txt4, command=self.turn(txt4), bg='yellow', fg='blue')
        

        self.lbl_category.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        self.lbl_question.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)
        self.btn1.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.25)
        self.btn2.place(relx=0, rely=0.75, relwidth=0.5, relheight=0.25)
        self.btn3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.25)
        self.btn4.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.25)



