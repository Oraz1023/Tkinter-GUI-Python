from tkinter import *

root = Tk()
root.geometry("600x400+1000+300")

# f_top=Frame(root)
# f_bottom=Frame(root)
# f_top.pack()
# f_bottom.pack()

#
# f_top = LabelFrame(root, text="Top Frame", padx=10, pady=10)
# f_bottom = LabelFrame(root, text="Bottom Frame",padx=10, pady=10)
# f_top.pack(pady=10)
# f_bottom.pack()
#
# label1 = Label(f_top, text="1", font="15", fg="red", bg="blue", width=8, height=4).pack(side=LEFT)
# label2 = Label(f_top, text="2", font="15", fg="red", bg="green", width=8, height=4).pack(side=LEFT)
# label3 = Label(f_bottom, text="3", font="15", fg="red", bg="yellow", width=8, height=4).pack(side=LEFT)
# label4 = Label(f_bottom, text="4", font="15", fg="red", bg="white", width=8, height=4).pack(side=LEFT)

label1 = Label(root, text="1", font="15", fg="red", bg="blue", width=8, height=4).pack(expand=1, fill=BOTH)



root.mainloop()
