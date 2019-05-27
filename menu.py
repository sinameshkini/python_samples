from tkinter import *
def tabenew():
    print ("gozine entekhab shod")
def tabeopen():
    print ("gozine baz kardan entekhab shod")
def tabehelp():
    print ("‫rahnama barname")
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=tabenew)
filemenu.add_command(label="Open...", command=tabeopen)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=tabehelp)
mainloop()
