from tkinter import *
import tkinter.font as tkFont
from Frames import message_frame, history_frame

class detailWindow(Frame):
    def __init__(self,master=None,player:dict={}):
        super().__init__(master)
        self.master = master
        self.player = player
        self.place(relx=0,rely=0,relwidth=1,relheight=0.5)
        self.createWidgets()
        
    def quit_game(self):
        acc = self.lbl_acumulado_valor.cget("text")
        
        message_frame.MessageWindow(self.master,acc)
             
        
    def createWidgets(self):
        self.accStyle = tkFont.Font(family="Lucida Grande", size=14)
        self.Style = tkFont.Font(family="Lucida Grande", size=24)
        self.juegoStyle = tkFont.Font(family="Lucida Grande", size=38)
        
        self.lbl_acumulado = Label(self,text="Acumulado",font=self.accStyle,fg="red")
        
        self.lbl_acumulado_valor = Label(
            self, text=self.player.info["acumulado"], font=self.accStyle, anchor="e")
        
        self.lbl_enjuego = Label(self,text="Premio en juego",font=self.juegoStyle,fg="red",anchor="center")
        
        self.lbl_enjuego_valor = Label(self, text=
            self.player.info["categoria1"]["value"], font=self.Style, anchor="center")
        
        self.btn_quit = Button(self,text="Retirarse",font=self.accStyle,command=self.quit_game)
        
        self.history = history_frame.historyButton(self)
        
        self.lbl_acumulado.place(relx=0.85,rely=0.2)
        self.lbl_acumulado_valor.place(relx=0.85,rely=0.3,relwidth=0.1)
        self.lbl_enjuego.place(relwidth=0.5,relx=0.25,rely=0.25)
        self.lbl_enjuego_valor.place(relwidth=0.5,relx=0.25,rely=0.55)
        self.btn_quit.place(relx=0.85, rely=0.65,relwidth=0.1)
        