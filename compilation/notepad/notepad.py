from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

"""
для использования модулей диалоговых окон
обязательный для импортирования отдельно
"""


root = Tk()

root.geometry("1000x500+1000+300")

main_menu = Menu(root)
root.config(menu=main_menu)


def about_programm():
    messagebox.showwarning(title="About notepad", message="Программа Notepad версия 0.0.1")



def change_theme(theme):
    text['bg'] = theme_colors[theme]['text_bg']
    text['fg'] = theme_colors[theme]['text_fg']
    text['insertbackground'] = theme_colors[theme]['cursor']
    text['selectbackground'] = theme_colors[theme]['select_bg']


def notepad_quit():
    answer = messagebox.askokcancel(title="Выход", message="Закрыть программу")
    if answer:
        root.destroy()
def open_file():
    file_path=filedialog.askopenfilename(title="Выбор файла",
                                         filetypes=(("Текстовые документы","*.txt"),
                                                    ("Все файлы","*.*")))
    print(file_path)
    if file_path:
        text.delete('1.0', END)
        text.insert("1.0", open(file_path,encoding='utf-8').read())

def save_file():
    file_path=filedialog.asksaveasfilename(title="Выбор файла",
                                         filetypes=(("Текстовые документы","*.txt"),
                                                    ("Все файлы","*.*")))
    file=open(file_path,'w', encoding='utf-8')
    t=text.get('1.0', END)
    file.write(t)
    file.close()





# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command= open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=notepad_quit)
main_menu.add_cascade(label="Файл", menu=file_menu)

#    About
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light Theme", command=lambda: change_theme('Light'))
theme_menu_sub.add_command(label="Dark Theme", command=lambda: change_theme('Dark'))
theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_programm)
main_menu.add_cascade(label="Разное", menu=theme_menu)

frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=1)

theme_colors = {
    "Dark": {
        "text_bg": "#343D46", "text_fg": "#C6DEC1",
        "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "Light": {
        "text_bg": "#fff", "text_fg": "#000",
        "cursor": "#8000FF", "select_bg": "#777"
    }
}

text = Text(frame_text, bg=theme_colors['Dark']['text_bg'],
            fg=theme_colors['Dark']['text_fg'],
            padx=10, pady=10, wrap=WORD,
            insertbackground=theme_colors["Dark"]["cursor"],
            selectbackground=theme_colors["Dark"]["select_bg"], width=30,
            spacing3=10, font=("Courier New", 10))
text.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text.yview)
scroll.pack(fill=Y, side=LEFT)
text.config(yscrollcommand=scroll.set)

text.pack(fill=BOTH, expand=1)

root.mainloop()