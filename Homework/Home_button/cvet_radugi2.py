from tkinter import*

root=Tk()
def get_color(text_color, hex_color):
    label['text']=text_color
    entry.delete(0,END)
    entry.insert(0, hex_color)

label=Label(root)  # метка
entry=Entry(root, width=30, justify="center")  #ввод

label.pack()
entry.pack()
colors={
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиалетовый"
}

for k,v in colors.items():
    Button(root, bg=k,command=lambda text=v,hex=k: get_color(text,hex)).pack(fill=X)

root.mainloop()