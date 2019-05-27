from Tkinter import *

root = Tk()
root.geometry("300x200")
root.title('Sina Meshkini')
root.configure(background='white')


def f1():
    print v
    Label(root,text=e1).pack()
w = Label(root, text = " Hello Sina!",fg = "light green",bg = "darkgreen",font = "tahoma 16 bold italic").pack()
v = IntVar()
Radiobutton(root,text="Python",padx=20,variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="C++",padx=20,variable=v,value=2).pack(anchor=W)
var1 = IntVar()

Checkbutton(root,text="male",variable=var1).pack()
e1=Entry(root).pack()
btn = Button(root,text="Test",width=25,command=f1)
btn.pack(side = "left")


root.mainloop()
