import tkinter


from tkinter import *

class historyWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(relx=0,rely=0)
        self.createWidgets()
    
    def createWidgets(self):
        pass
    
class historyButton(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(relx=0.05,rely=0.1,relwidth=0.1,relheight=0.1)
        self.createWidgets()
    
    def createWidgets(self):
        self.btn_history = Button(self, bitmap="hourglass")
        self.btn_history.place(relwidth=1, relheight=1)
    