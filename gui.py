
from tkinter import *
import tkinter.ttk as ttk
import RPi.GPIO as GPIO
import time

r1 = 31
r2 = 33
r3 = 35
r4 = 37
rel1_s=0
rel2_s=0
rel3_s=0
rel4_s=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)
GPIO.setup(r4,GPIO.OUT)

def tab_new():
    print ("New")
def tab_open():
    print ("Open")
def tab_help():
    print ("‫Help")
def stopProg():
    root.destroy()
def transfertext():
    global label1
    label1.config(text = "sina")

def rel1():
    global rel1_s
    if rel1_s == 1:
        GPIO.output(r1,0)
        rel1_s=0
    else:
        GPIO.output(r1,1)
        rel1_s=1
def rel2():
    global rel2_s
    if rel2_s == 1:
        GPIO.output(r2,0)
        rel2_s=0
    else:
        GPIO.output(r2,1)
        rel2_s=1
def rel3():
    global rel3_s
    if rel3_s == 1:
        GPIO.output(r3,0)
        rel3_s=0
    else:
        GPIO.output(r3,1)
        rel3_s=1
def rel4():
    global rel4_s
    if rel4_s == 1:
        GPIO.output(r4,0)
        rel4_s=0
    else:
        GPIO.output(r4,1)
        rel4_s=1


color = '#111131'

root=Tk()
root.geometry("%dx%d+%d+%d"%(800,600,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')

nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

main = Frame(bg=color)
monitoring = Frame(bg=color)
control = Frame(bg=color)

nb.add(main,text='Main')
nb.add(monitoring,text='Monitoring')
nb.add(control,text='Control')

#____  Main Tab __________
Label(main,text='SAJAB Management System',fg='#8888f1',bg=color,font="tahoma 24 bold",pady=10).pack()
#btn1f1 = Button(f1,text='btn1')
#btn1f1.pack(side='left',anchor='nw',padx=50,pady=50)
#_______End

#____  Monitoring Tab
sensors = ['Sensor 1','Sensor 2','Sensor 3','Sensor 4']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(monitoring,text=c,fg='white',bg=color,relief=RIDGE,width=15).place(x=20,y=100+r*40)
    r=r+1
r=0
for c in relays:
    Label(monitoring,text=c,fg='white',bg=color,relief=RIDGE,width=15).place(x=300,y=100+r*40)
    r=r+1
global rel1_s
global rel2_s
global rel3_s
global rel4_s
Button(monitoring,text='Toggle',command=rel1).place(x=450,y=100)
Button(monitoring,text='Toggle',command=rel2).place(x=450,y=140)
Button(monitoring,text='Toggle',command=rel3).place(x=450,y=180)
Button(monitoring,text='Toggle',command=rel4).place(x=450,y=220)

btn_refresh = Button(monitoring,text='Refresh')
btn_refresh.place(x=20,y=400)
#btn_refresh.pack(side='left',anchor='nw',padx=50,pady=50)
#_______End

#____  Control Tab

#btn1f1 = Button(f1,text='btn1')
#btn1f1.pack(side='left',anchor='nw',padx=50,pady=50)
#_______End
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=tab_new)
filemenu.add_command(label="Open...", command=tab_open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=tab_help)

btn1 = Button(root,text="Exit",command = stopProg).pack()
btn1 = Button(root,text="Click Here!",command = transfertext).pack()
label1=Label(root,text="Orginal Text",fg="green")
label1.pack()

#top=Toplevel()
#top.mainloop()

root.mainloop()

