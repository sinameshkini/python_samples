from tkinter import *

root = Tk()
root.geometry("300x200")
root.title('Code Core')
root.configure(background='light gray')

l1=Label(root, text = "Hello World!",fg = "light green",bg = "darkgreen",font = "tahoma 16")
#l1.pack()
l1.place(x=100,y=50)


root.mainloop()
