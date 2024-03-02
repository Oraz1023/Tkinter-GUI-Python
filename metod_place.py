from tkinter import *

root=Tk()
root.geometry("600x400+1000+300")


# label1=Label(root,text="Hello world!", bg="#3498db",
#               fg='#fff', font="16",padx=20,pady=8)
# label1.place(x=100,y=0)
# # #
# label2=Label(root,text="Hello world!", bg="#2ecc71",
#              fg='#fff', font="16",padx=20,pady=8)
# label2.place(relx=0.5,rely=0.5, anchor=CENTER)

#
# button1=Button(text="Button 1",bg="#3498db",
#                fg='#fff', font="16",padx=20,pady=8 )
# button1.place(x=0,y=0)
# button1=Button(text="Button 1",bg="#2ecc71",
#                fg='#fff', font="16",padx=20,pady=8 )
# button1.place(relx=0.5,rely=0.5,anchor=CENTER)
# button1=Button(text="Button 1",bg="#ff0000",
#                fg='#fff', font="16",padx=20,pady=8 )
# button1.place(relx=1,rely=1,anchor="se")

label=Label(root,bg="#000")
label.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)


button2=Button(text="Button 1",bg="#3498db",
               fg='#fff', font="16",padx=20,pady=8 )
button2.place(relx=0.5,rely=0.5, anchor="c")



root.mainloop()