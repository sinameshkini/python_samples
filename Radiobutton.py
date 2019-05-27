from tkinter import *
root = Tk()
v= IntVar()
Label(root,text="Select once:").pack()
Radiobutton(root,text="python",variable=v,value=1).pack()
Radiobutton(root,text="Java",variable=v,value=2).pack()
mainloop()
