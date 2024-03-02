from tkinter import *
root=Tk()


# root.geometry("600x400+1000+300")

# f=Frame(root)
# f.pack(pady=10)
#
# button_list=[
#     '7','8','9',
#     '4','5','6',
#     '1','3','3',
#     '0',
# ]
#
# row=0
# column=0
#
# for i in button_list:
#     if i =="0":
#         Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#     column+=1
#     if column ==3:
#         column=0
#         row+=1


# button7=Button(f, text="7", padx=10,pady=5).grid(row=0, column=0)
# button8=Button(f, text="8", padx=10,pady=5).grid(row=0, column=1)
# button9=Button(f, text="9", padx=10,pady=5).grid(row=0, column=2)
# button4=Button(f, text="4", padx=10,pady=5).grid(row=1, column=0)
# button5=Button(f, text="5", padx=10,pady=5).grid(row=1, column=1)
# button6=Button(f, text="6", padx=10,pady=5).grid(row=1, column=2)
# button1=Button(f, text="1", padx=10,pady=5).grid(row=2, column=0)
# button2=Button(f, text="2", padx=10,pady=5).grid(row=2, column=1)
# button3=Button(f, text="3", padx=10,pady=5).grid(row=2, column=2)
# button0=Button(f, text="0", padx=10,pady=5).grid(row=3, column=0,columnspan=3)
#


label_user=Label(root, text="Login: ").grid(row=0,column=0,padx=10,pady=10,sticky=W)
entry_user=Entry(root).grid(row=0, column=1,columnspan=2,padx=10,sticky=W+E)

label_pass=Label(root, text="Password: ").grid(row=1,column=0,padx=10,sticky=W)
entry_pass=Entry(root,show="*").grid(row=1, column=1,columnspan=2,padx=10,sticky=W+E)


button_login= Button(root,text="Вход",padx=5).grid(row=2,column=0,pady=10)
button_reg= Button(root,text="Регистрация",padx=5).grid(row=2,column=1)
button_forgot= Button(root,text="Забыли пароль?",padx=5).grid(row=2,column=2,padx=10)







root.mainloop()