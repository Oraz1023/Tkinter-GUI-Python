from tkinter import *
root=Tk()

"""
Напишите программу, состоящий из семи кнопок цвета 
которых соответсвует цветам радуги 
При нажатии на ту или иную кнопку в текстовом поле должен
вставляться код цвета а в метку - название цвета
"""
def get_color(text_color, hex_color):
    label['text']=text_color
    entry.delete(0,END)
    entry.insert(0, hex_color) #insert(index, str): вставляет в текстовое поле строку по определенному индексу

label=Label(root)  # метка
entry=Entry(root, width=30, justify="center")  #ввод

label.pack()
entry.pack()


button_red=Button(root,bg="#ff0000", command=lambda: get_color('red','#ff0000')).pack(fill=X)
button_orange=Button(root,bg="#ff7d00", command=lambda: get_color('orange','#ff7d00')).pack(fill=X)
button_yellow=Button(root,bg="#ffff00", command=lambda: get_color('yellow','#ffff00')).pack(fill=X)
button_green=Button(root,bg="#00ff00", command=lambda: get_color('green','#00ff00')).pack(fill=X)
button_blue=Button(root,bg="#007dff", command=lambda: get_color('blue','#007dff')).pack(fill=X)
button_dark_blue=Button(root,bg="#0000ff", command=lambda: get_color('dark_blue','#0000ff')).pack(fill=X)
button_violet=Button(root,bg="#7d00ff", command=lambda: get_color('violet','#7dff00')).pack(fill=X)
"""
 Анономный функции через лямбда вырожения вызываеться при нажатии кнопки 
"""
root.mainloop()



