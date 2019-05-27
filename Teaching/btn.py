from tkinter import *

root = Tk()
root.geometry("300x200")
root.title('Code Core')
root.configure(background='light gray')

def chang_txt():
    l1.config(text="Changed!")

l1=Label(root, text = " Hello World!",fg = "light green",bg = "darkgreen",font = "tahoma 16")
l1.pack()
#l1.place(x=10,y=10)

button = Button(root,text='Change text',command=chang_txt)
button.pack()


root.mainloop()
