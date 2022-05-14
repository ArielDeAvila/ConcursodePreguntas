from tkinter import *
import tkinter.font as tkFont

class MessageWindow(Frame):
    def __init__(self,master=None,acc=""):
        super().__init__(master)
        self.master = master
        self.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.acc = acc
        self.createWidgets()
        
    def createWidgets(self):
        self.Style = tkFont.Font(family="Lucida Grande", size=24)
        self.lbl_gane = Label(self,text=f"has ganado: ${self.acc}",font=self.Style,anchor="center")
        self.lbl_gane.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.1)