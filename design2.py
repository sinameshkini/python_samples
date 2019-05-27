#Library
import datetime
import time
from tkinter import *
import tkinter.ttk as ttk
from urllib.request import urlretrieve
import serial
import os
#End Library

#Variables
station_name = "Golestan Uni"

pass_main='1120'
time_xloc= 20
time_yloc= 5

date_xloc=10
date_yloc=30

table_x=20
table_y=150

step = 20
stepx = 40
#End Variables

#Functions
#Functions for splitting the different components of date and time
def pass_check():
    global passcheck
    passcheck = Toplevel()
    passcheck.geometry("%dx%d+%d+%d"%(200,140,100,50)) #x,y,horizental,vertical
    passcheck.title('Setting')
    passcheck.configure(background='lightblue')
    Label(passcheck,text="Enter Password:",fg=top_bg_color,bg=color,width=0).place(x=40,y=20)
    global pass_in
    pass_in=Entry(passcheck,width=18)
    pass_in.place(x=25,y=50)

    Button(passcheck,text="OK",command=pass_check2).place(x=80,y=80)

def pass_check2():
    if pass_in.get()==pass_main:
        passcheck.destroy()
        setting()
    else:
        Label(passcheck,text="Password is wrong!",fg=top_bg_color,bg=color,width=0).place(x=40,y=110)

def setting():
    global setting_frame
    setting_frame = Toplevel()
    setting_frame.geometry("%dx%d+%d+%d"%(700,420,100,50)) #x,y,horizental,vertical
    setting_frame.title('Setting')
    setting_frame.configure(background='lightblue')
    Label(setting_frame,text="Station name:",fg=top_bg_color,bg=color,width=0).grid(row=0,column=0,ipadx=30,pady=8)
    Label(setting_frame,text=station_name,fg=top_bg_color,bg=color,width=0).grid(row=0,column=1,ipadx=30,pady=8)
    Label(setting_frame,text="Sampling rate:",fg=top_bg_color,bg=color,width=0).grid(row=1,column=0,ipadx=30,pady=8)
    sampling_rate=Entry(setting_frame,width=8).place(x=140,y=45)
    Label(setting_frame,text="Sec.",fg=top_bg_color,bg=color,width=0).place(x=220,y=46)
    Label(setting_frame,text="Calibration:",fg=top_bg_color,bg=color,width=0).grid(row=2,column=0,ipadx=30,pady=8)
    Label(setting_frame,text="Bias Value:",fg=top_bg_color,bg=color,width=0).grid(row=3,column=0,ipadx=30,pady=8)
    bias_value=Entry(setting_frame,width=8).place(x=140,y=118)
    Label(setting_frame,text="Coefficent:",fg=top_bg_color,bg=color,width=0).grid(row=4,column=0,ipadx=30,pady=8)
    coefficent=Entry(setting_frame,width=8).place(x=140,y=154)
    Label(setting_frame,text="Alert:",fg=top_bg_color,bg=color,width=0).grid(row=0,column=3,ipadx=30,pady=8)
    Label(setting_frame,text="Max level:",fg=top_bg_color,bg=color,width=0).grid(row=1,column=3,ipadx=30,pady=8)
    max_level=Entry(setting_frame,width=8).place(x=465,y=45)
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=545,y=46)
    Label(setting_frame,text="Hysteresis level:",fg=top_bg_color,bg=color,width=0).grid(row=2,column=3,ipadx=30,pady=8)
    hysteresis_level=Entry(setting_frame,width=8).place(x=465,y=81)
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=545,y=82)
    Label(setting_frame,text="Mobile Phone 1:",fg=top_bg_color,bg=color,width=0).grid(row=3,column=3,ipadx=30,pady=8)
    mobile_phone1=Entry(setting_frame,width=15).place(x=465,y=117)
    Label(setting_frame,text="Mobile Phone 2:",fg=top_bg_color,bg=color,width=0).grid(row=4,column=3,ipadx=30,pady=8)
    mobile_phone1=Entry(setting_frame,width=15).place(x=465,y=153)
    Label(setting_frame,text="Mobile Phone 3:",fg=top_bg_color,bg=color,width=0).grid(row=5,column=3,ipadx=30,pady=8)
    mobile_phone1=Entry(setting_frame,width=15).place(x=465,y=189)
    Button(setting_frame,text="OK",command=pass_check2).place(x=30,y=220)
    Button(setting_frame,text="Set as default",command=pass_check2).place(x=120,y=220)
    Button(setting_frame,text="Default values",command=pass_check2).place(x=300,y=220)
    Button(setting_frame,text="Cancel",command=cncl).place(x=500,y=220)

def cncl():
    setting_frame.destroy()

def nowYear():
    now = datetime.datetime.now()
    year = now.year
    return str(year)

def nowMonth():
    now = datetime.datetime.now()
    month = now.month
    return str(month)

def nowDay():
    now = datetime.datetime.now()
    day = now.day
    return str(day)

def nowHour():
    now = datetime.datetime.now()
    hour = now.hour
    return str(hour)

def nowMinute():
    now = datetime.datetime.now()
    minute = now.minute
    return str(minute)

def nowSecond():
    now = datetime.datetime.now()
    second = now.second
    return str(second)

def year_label(label):
  def count1():
    label.config(text=nowYear())
    label.after(1000, count1)
  count1()

def month_label(label):
  def count2():
    label.config(text=nowMonth())
    label.after(1000, count2)
  count2()

def day_label(label):
  def count3():
    label.config(text=nowDay())
    label.after(1000, count3)
  count3()

def hour_label(label):
  def count4():
    label.config(text=nowHour())
    label.after(1000, count4)
  count4()

def minute_label(label):
  def count5():
    label.config(text=nowMinute())
    label.after(1000, count5)
  count5()

def second_label(label):
  def count6():
    label.config(text=nowSecond())
    label.after(1000, count6)
  count6()

def about():
   filewin = Toplevel(root)
   tx ="""
    Development by: Sina Meshkini
    +98 911 380 6028
    SinaMeshkini7@gmail.com
    @SinaMeshkini
    """
   message = Message(filewin, text=tx, relief = RIDGE , width = 400)
   message.pack(fill="both", expand="yes")
#End Functions

#Desigen Param
root=Tk()
root.geometry("%dx%d+%d+%d"%(800,480,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')


color = 'lightblue'
top_fg_color = 'lightblue'
top_bg_color = '#111131'
#End Desigen Param

#Header
w = Canvas(root,width= 800,height= 100)
w.place(x=0,y=0)
w.create_rectangle(0,0,800,100,fill=top_bg_color)

Label(root,text='SAJAB Management System',fg=top_fg_color,bg=top_bg_color,font="tahoma 24 bold",pady=10).place(x=150,y=5)

#Time
hourLabel = Label(root,text=nowHour(),fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
hourLabel.place(x=time_xloc,y=time_yloc)
hour_label(hourLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=("Ravie",14))
colon.place(x=time_xloc+step,y=time_yloc-5)

minuteLabel = Label(root, text = nowMinute(),fg=top_fg_color,bg=top_bg_color,font=("Ravie",10))
minuteLabel.place(x=time_xloc+2*step,y=time_yloc)
minute_label(minuteLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=("Ravie",14))
colon.place(x=time_xloc+3*step,y=time_yloc-5)

secondLabel = Label(root, text = nowSecond(),fg=top_fg_color,bg=top_bg_color,font=("Ravie",10))
secondLabel.place(x=time_xloc+4*step,y=time_yloc)
second_label(secondLabel)
#End Time

#Date
yearLabel = Label(root,text=nowYear(),fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
yearLabel.place(x=date_xloc,y=date_yloc)
year_label(yearLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color)
colon.place(x=date_xloc+36,y=date_yloc)

monthLabel = Label(root,text=nowMonth(),fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
monthLabel.place(x=date_xloc+45,y=date_yloc)
month_label(monthLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color)
colon.place(x=date_xloc+60,y=date_yloc)

dayLabel = Label(root,text=nowDay(),fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
dayLabel.place(x=date_xloc+68,y=date_yloc)
day_label(dayLabel)
#End Date

#Temp
temp_label = Label(root,text="Temp: ",fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
temp_label.place(x=date_xloc,y=date_yloc+20)
#End Temp
#End Header

#Body
sensors = ['Sensor 1:','Sensor 2:','Sensor 3:','Sensor 4:']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(root,text=c,fg=top_bg_color,bg=color,width=0).place(x=table_x,y=table_y+r*stepx)
    r=r+1
r=0
for c in relays:
    Label(root,text=c,fg=top_bg_color,bg=color,width=0).place(x=table_x+300,y=table_y+r*stepx)
    r=r+1

Label(root,text="Sampling rate:",fg=top_bg_color,bg=color,width=0).place(x=table_x+50,y=350)
global sampling_rate
sampling_rate=Entry(root,width=8)
sampling_rate.place(x=table_x+150,y=350)
Label(root,text="Sec.",fg=top_bg_color,bg=color,width=0).place(x=table_x+230,y=351)

Button(root,text="Setting",command=pass_check).place(x=700,y=420)



#End Body




root.mainloop()
