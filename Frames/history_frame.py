from tkinter import *
from entities import history

class historyWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.createWidgets()
        self.fillContent()
    
    def fillContent(self):
        content = history.historyMatch()
        for row in content.listPlayer:
            self.lbl_name["text"] += "\n"+row[0]
            self.lbl_round["text"] += "\n"+row[1]
            self.lbl_acc["text"] += "\n"+row[2]
        
    def createWidgets(self):
        self.title_name = Label(self,text="Nombre")
        self.title_round = Label(self, text="Turnos")
        self.title_acc = Label(self, text="Premio")
        
        self.lbl_name= Label(self,anchor="n")
        self.lbl_round = Label(self,anchor="n")
        self.lbl_acc = Label(self, anchor="n")
        
        self.title_name.place(relx=0, rely=0, relwidth=0.33, relheight=0.05)
        self.title_round.place(relx=0.34, rely=0, relwidth=0.33, relheight=0.05)
        self.title_acc.place(relx=0.68, rely=0, relwidth=0.32, relheight=0.05)
        
        self.lbl_name.place(relx=0,rely=0.04,relwidth=0.33,relheight=0.95)
        self.lbl_round.place(relx=0.34,rely=0.04,relwidth=0.33,relheight=0.95)
        self.lbl_acc.place(relx=0.68,rely=0.04, relwidth=0.32,relheight=0.95)
    
class historyButton(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(relx=0.05,rely=0.1,relwidth=0.1,relheight=0.1)
        self.createWidgets()
    
    def openWindow(self):
        historyFrame = Tk()
        historyFrame.wm_title("Historial de jugadores")
        historyFrame.wm_geometry("400x600")
        
        historyWindow(historyFrame)        
    
    def createWidgets(self):
        self.btn_history = Button(self, bitmap="hourglass",command=self.openWindow)
        self.btn_history.place(relwidth=1, relheight=1)
    