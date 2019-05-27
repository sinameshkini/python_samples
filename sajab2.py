#Library
import datetime
import time
from tkinter import *
import tkinter.ttk as ttk
from urllib.request import urlretrieve
import serial
import os
#import RPi.GPIO as GPIO
#End Library


#Variables
time_xloc= 20
time_yloc= 5

date_xloc=10
date_yloc=30
#End Variables

#Functions for splitting the different components of date and time
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
hourLabel.grid(row=0,column=0)
hour_label(hourLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=("Ravie",14))
colon.place(x=time_xloc+22,y=time_yloc)

minuteLabel = Label(root, text = nowMinute(),fg=top_fg_color,bg=top_bg_color,font=("Ravie",10))
minuteLabel.place(x=time_xloc+26,y=time_yloc)
minute_label(minuteLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=("Ravie",14))
colon.place(x=time_xloc+48,y=time_yloc)

secondLabel = Label(root, text = nowSecond(),fg=top_fg_color,bg=top_bg_color,font=("Ravie",10))
secondLabel.place(x=time_xloc+52,y=time_yloc)
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
data_frame = Frame(root,width=800,height=500).place(x=0,y=100)

sensors = ['Sensor 1','Sensor 2','Sensor 3','Sensor 4']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(data_frame,text=c,fg=top_bg_color,bg=color,relief=RIDGE,width=15).grid(row=r,column=5,padx=4,pady=8)
    r=r+1
r=0
for c in relays:
    #Label(data_frame,text=c,fg=top_bg_color,bg=color,relief=RIDGE,width=15).grid(row=r+40,column=5,padx=4,pady=4)
    r=r+1

#End Body


mainloop()
