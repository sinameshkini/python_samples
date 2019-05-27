from tkinter import *

root = Tk()
root.geometry("300x200")
root.title('Code Core')
root.configure(background='light gray')

def chang_txt():
    l1.config(text=e1.get())

def new():
    f = Frame(root,width=50,height=50,background="green")
    f.grid(row= 4,column=0)

l1=Label(root, text = " Hello World!",fg = "light green",bg = "darkgreen",font = "tahoma 16")
l1.grid(row=0,column=0)
#l1.place(x=10,y=10)

Label(root,text="Enter your name: ").grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)

button = Button(root,text='Change text',command=chang_txt)
button.grid(row=2,column=0)

button1 = Button(root,text='new window',command=new)
button1.grid(row=3,column=0)

root.mainloop()
