from tkinter import *

def sina():
    if var1.get()==1:
        print("Male is 1")
    else:
        print("Male is 0")
    if var2.get()==1:
        print("FeMale is 1")
    else:
        print("FeMale is 0")

master = Tk()

var1 = IntVar()
Checkbutton(master,text="male",variable=var1).pack()
var2 = IntVar()
Checkbutton(master,text="female",variable=var2).pack()

button = Button(master,text='stop',width=25,command=sina)
button.pack()


mainloop()
