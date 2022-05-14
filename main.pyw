from Frames import start_frame
from tkinter import *


window = Tk()
window.wm_title("Concurso de preguntas")
window.wm_geometry("1000x620")

app = start_frame.StartWindow(window)

app.mainloop()

