from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()  # Создаем объект класса Tk
root.title('Мое 1ое GUI приложение')  # поменять заголовок

icon_path = 'Фото/python.png'  # Replace with the path to your .png icon

root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open(icon_path)))

root.geometry("600x400+1000+300")  # размеры окна при открытии высота ширина
root.resizable(True, False)  # можно разрешить или запретить изменение ширины или длины окна
root.config(background="red")  # меняем фон окна цвет
# root['bg']='red'

root.mainloop()  # метод главный цикл
