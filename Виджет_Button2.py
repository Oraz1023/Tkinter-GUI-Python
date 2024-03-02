import time
import locale
from tkinter import *
root=Tk()
root.title("Counter")
root.config(background="white")
root.geometry("600x400+1000+300")
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
def check_time():
    button_time['text']=time.strftime("%X")
    print(f"Время: {time.strftime('%X')}")
    #print(time.strftime("%H:%M:%S"))

def Calendar():
    button_cal['text']=time.strftime("%x")
    print(f"Дата: {time.strftime('%x')}")

clicks=0
def Counter():
    global clicks
    clicks+=1
    root.title(f"Counter: {clicks}")
button_time=Button(root,text="Check time",command=check_time,bg="red")
button_time.configure(width=20, height=5)
button_cal=Button(root,text="Calendar",command=Calendar,bg="orange")
button_cal.configure(width=20,height=5)
button_counter=Button(root,text="Counter", command=Counter,background="green")
button_counter.configure(width=20,height=5)
button_time.pack()
button_cal.pack()
button_counter.pack()


root.mainloop()