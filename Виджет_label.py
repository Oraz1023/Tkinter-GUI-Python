from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root=Tk()
root.geometry("600x400+1000+300")


# l=Label(root, text="Текст в строке 1\nСтрока2\nСтрока3\nСтрока4\nСтрока5",
#         bg="red", fg="#fff",font=("Comic Sans MS", 10, "bold"),
#         justify=LEFT,width=50, height=10, anchor="nw")

#

img= PhotoImage(file="Фото/python1.png")
l_logo=ttk.Label(root, image=img)
# # l.pack()
l_logo.pack()
root.mainloop()










