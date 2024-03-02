from tkinter import *
# from tkinter import ttk
root=Tk()

root.geometry('600x400+1000+400')


def clicked():
    print("Clicked")

#button=Button(root, text="Кнопка",command=clicked, width=7,font="Arial 20 italic")
#убираем скобки от функции чтобы она работала по команде
# а не по функции, по функции заработает 1 раз,
# а по команде заработает по клику.
# button=Button(root, text="Кнопка",command=clicked, width=7,font=("Comic Sans MS", 20))
button=Button(root,text="Кнопка\nTkinter",justify=LEFT)
button.configure(width=20, height=5)
# button['font']="Arial"
# button['font']='Comic Sans MS'20


button.pack() #Для размещения виджета в окне отвечает методы
# button.grid() #упаковщики
# button.place()

root.mainloop()