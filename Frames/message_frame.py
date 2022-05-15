from tkinter import *
import tkinter.font as tkFont
from Frames import start_frame
from entities import result

class MessageWindow(Frame):
    def __init__(self,master=None,acc="",pj=None):
        super().__init__(master)
        self.master = master
        self.player = pj
        self.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.acc = acc
        self.createWidgets()
        
    def endGame(self):
        result.historyResults(self.player)
        start_frame.StartWindow(self.master)
        
    def createWidgets(self):
        self.Style = tkFont.Font(family="Lucida Grande", size=24)
        
        self.lbl_gane = Label(self,text=f"has ganado: ${self.acc}",font=self.Style,anchor="center")
        self.btn = Button(self,text="Aceptar",font=self.Style,command=self.endGame)
        
        self.lbl_gane.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.1)
        self.btn.place(relx=0.4,rely=0.65,relwidth=0.2,relheight=0.15)