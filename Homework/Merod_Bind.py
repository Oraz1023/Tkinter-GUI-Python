from tkinter import *

root = Tk()

root.geometry("300x100")


# def func_event(event,key):
#     print(event,key)
#
# entry=Entry(root, justify=CENTER, font="Arial 15")
# entry.pack(fill=X, expand=1,padx=10,ipady=10)
# entry.bind("<Button-1>", lambda event, key="Left click":func_event(event,key))
# entry.bind("<Button-2>", lambda event, key="Middle click":func_event(event,key))
# entry.bind("<FocusIn>", lambda event, key="Focus":func_event(event,key))



label1=Label(root,bg="#fff")
label1.pack()
colors={
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиалетовый"
}
class MyLabels:
    def __init__(self,master,color): # master-ссылка на наше окно
        self.color=color
        self.b=Label(master,bg=color,width=4,height=2)
        self.b.pack(side=LEFT,padx=1)
        self.b.bind("<Button-1>", lambda event, key="left":self.get_color(event,key))
        self.b.bind("<Button-3>", lambda event, key="right":self.get_color(event,key))

    def get_color(self,event,key):
        if key =="left":
            label1["bg"]=self.color
        else:
            label1["bg"]="#fff"


for k,v in colors.items():
    MyLabels(root,k)

root.mainloop()

