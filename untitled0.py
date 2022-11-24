# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 2022

@author: Keviweto
"""

from tkinter import*
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)


open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file =Label(root, text="File name")
label_file.place(relx=0.28 , rely=0.03 , anchor=CENTER )

input_file = Entry(root)
input_file.place(relx = 0.48, rely=0.03, anchor=CENTER)

text = Text(root,height=40, width=85, bg="Yellow", fg="white")
text.place(relx=0.5 , rely=0.55 , anchor=CENTER )



root.mainloop()