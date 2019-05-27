from tkinter import *
from threading import Timer
global step
step = 1
counter = 0
def count():
    global counter
    global label
    counter+=1
    label.config(text=str(counter))
    Timer(step,count).start()

timer1 = Timer(step,count)
timer1.start()


def reset_counter():
    global counter
    counter = 0
def apply():
    print("applyed")
    global step
    step = int(e1.get())
    print (int(e1.get()))
    print (step)
root = Tk()

label = Label(root,fg="green")
label.pack()

button = Button(root,text='reset',width=25,command=reset_counter)
button.pack()
global e1
e1=Entry(root)
e1.pack()
Button(root,text="apply",command=apply).pack()

root.mainloop()
