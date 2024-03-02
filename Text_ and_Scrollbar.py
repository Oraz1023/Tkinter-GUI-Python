import tkinter
from tkinter import *
root=Tk()


root.geometry("600x400+1000+300")


frame_manu=Frame(root, bg="black", height=40)
frame_text=Frame(root)
frame_manu.pack(fill=X)
frame_manu.pack(fill=X)
frame_text.pack(fill=BOTH, expand=1)
label_menu=Label(frame_manu, text="Menu",bg="silver",
                            fg="black",font="Arial 10")
label_menu.place(x=10,y=10)

def add_str():
    text.insert('2.4', "Hello")
def del_str():
    text.delete('2.4','2.10')
    #text.delete('1.0',END)
def get_str():
    print(text.get('1.0',END))


btn_add= Button(root,text="Add", command=add_str).place(x=75,y=10)
btn_del= Button(root,text="Delete", command=del_str).place(x=125,y=10)
btn_get= Button(root,text="Get", command=get_str).place(x=190,y=10)

text=Text(frame_text,bg="black", fg="white",
                    padx=10,pady=10, wrap=WORD,
                    insertbackground="#EDA756",
                    selectbackground="#4E5A65",
                    spacing3=10)
text.pack(fill=BOTH, expand=1, side=LEFT)

scroll=Scrollbar(frame_text, command=text.yview)
scroll.pack(fill=Y, expand=1, side=LEFT)
text.config(yscrollcommand=scroll.set)
print(text['width'], text['height'])



text.pack(fill=BOTH,expand=1)


root.mainloop()