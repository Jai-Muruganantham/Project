import tkinter as tk
from tkinter import *
from tkinter import messagebox
top = tk.Tk()
top=Toplevel()
C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "images.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
top.mainloop