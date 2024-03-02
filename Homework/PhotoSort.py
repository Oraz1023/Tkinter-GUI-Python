from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import ttk
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    entry_path.delete(0, END)
    entry_path.insert(0, dir_path)


def function_start():
    current_path = entry_path.get()
    if current_path:
        for folder, subfolders, files in os.walk(current_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%Y-%m-%d")
                date_folder = os.path.join(current_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Success", "Сортировка выполнена успешно")
        entry_path.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Выберите папку с фотографиями")


root = Tk()
root.title("PhotoSort")
root.geometry("500x150+1000+300")
style = ttk.Style()
style.configure("my.TButton", font=("Helvetica", 15))
frame = Frame(root, bg="blue", bd=5)
frame.pack(pady=10, padx=10, fill=X)

entry_path = ttk.Entry(frame)
entry_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

button_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
button_dialog.pack(side=LEFT, padx=5)

button_start = ttk.Button(root, text="Start", style="my.TButton", command=function_start)
button_start.pack(fill=X, padx=10, pady=10)

root.mainloop()
