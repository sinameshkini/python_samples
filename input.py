from tkinter import *
master = Tk()
master.geometry("%dx%d+%d+%d"%(800,480,100,50)) #x,y,horizental,vertical

def show_entry_fields():
    Label(master,text=e1.get()).grid(row=1,column=1)

Label(master,text="Name: ").grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
Button(master,text="Send",command=show_entry_fields).grid(row=2,column=1,sticky=W,pady=4)
mainloop()
