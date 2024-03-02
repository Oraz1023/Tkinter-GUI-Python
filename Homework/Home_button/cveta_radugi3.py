from tkinter import*

root=Tk()
def get_color(text_color, hex_color):
    label['text']=text_color
    entry.delete(0,END)
    entry.insert(0, hex_color)

colors={
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиалетовый"
}


class Mybuttons:
    def __init__(self,master, text_color, hex_color): # master-ссылка на наше окно
        self.text_color=text_color
        self.hex_color=hex_color
        self.button=Button(root, bg=hex_color, command=self.get_color)
        self.button.pack(fill=X)

    def get_color(self):
        label['text'] = self.text_color
        entry.delete(0, END)
        entry.insert(0, self.hex_color)

label=Label(root)  # метка
entry=Entry(root, width=30, justify="center")  #ввод

label.pack()
entry.pack()

for k, v in colors.items():
    Mybuttons(root, v, k)


root.mainloop()
