from tkinter import *

class QuestionWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self):
                
        self.lbl_category = Label(self)
        self.lbl_question = Label(self, bg='grey')
        self.btn1 = Button(self, bg='yellow', fg='blue')
        self.btn2 = Button(self, bg='yellow', fg='blue')
        self.btn3 = Button(self, bg='yellow', fg='blue')
        self.btn4 = Button(self, bg='yellow', fg='blue')
        

        self.lbl_category.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        self.lbl_question.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)
        self.btn1.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.25)
        self.btn2.place(relx=0, rely=0.75, relwidth=0.5, relheight=0.25)
        self.btn3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.25)
        self.btn4.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.25)



