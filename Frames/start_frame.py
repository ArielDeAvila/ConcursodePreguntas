from Frames import question_frame, details_frame, history_frame
from entities import jugador, round
from tkinter import *
import tkinter.font as tkFont


class StartWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.createWidgets()
    
    def changeFrame(self):
        name = self.box.get()
        self.destroy()
        
        player = jugador.Player(name)
        details = details_frame.detailWindow(self.master,player)
        questions = question_frame.QuestionWindow(self.master, player,details)
        
        round.Round(questions,details,player)
        
    def createWidgets(self):
        self.labelStyle = tkFont.Font(family="Lucida Grande", size=48)
        self.generalStyle = tkFont.Font(family="Lucida Grande", size=14)
        
        self.lbl = Label(self,text="¡Bienvenido!",font=self.labelStyle)
        self.name = Label(self, text="Ingrese su nombre", font=self.generalStyle)
        self.box = Entry(self)
        self.btn = Button(self, text="Comenzar", command=self.changeFrame, font=self.generalStyle)
        
        self.btn_history = history_frame.historyButton(self)
        
        self.lbl.place(relx=0.32,rely=0.1)
        self.name.place(relx=0.26,rely=0.35)
        self.box.place(relx=0.43,rely=0.36)
        self.btn.place(relx=0.57,rely=0.34)
        
        
        
        