import tkinter
from tkinter import *

root = Tk()

root.geometry("600x400+1000+300")

main_menu = Menu(root)
root.config(menu=main_menu)


def about_programm():
    print("About")


# File


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu)

#    About
help_menu = Menu(main_menu, tearoff=0)

help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="онлайн")
help_menu_sub.add_command(label="офлайн")
help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе", command=about_programm)
main_menu.add_cascade(label="Справка", menu=help_menu)
# main_menu.add_command(label="File")
# main_menu.add_command(label="About")
# frame_manu=Frame(root, bg="black", height=40)
# frame_manu.pack(fill=X)
# frame_manu.pack(fill=X)
frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=1)

text = Text(frame_text, bg="black", fg="white",
            padx=10, pady=10, wrap=WORD,
            insertbackground="#EDA756",
            selectbackground="#4E5A65",
            spacing3=10)
text.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text.yview)
scroll.pack(fill=Y, expand=1, side=LEFT)
text.config(yscrollcommand=scroll.set)
print(text['width'], text['height'])

text.pack(fill=BOTH, expand=1)

root.mainloop()
