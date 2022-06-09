from tkinter import *
from PIL import Image, ImageTk

v = Tk()
v.geometry('700x700')

load= Image.open(file="images.jpg")
render = ImageTk.PhotoImage(load)
img = Label(v, image=render)
img.image = render
img.place(x=100, y=100)

v.mainloop()