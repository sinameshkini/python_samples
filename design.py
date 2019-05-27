import datetime
import time
from tkinter import *
import tkinter.ttk as ttk
from urllib.request import urlretrieve
import serial
import os

root=Tk()
root.geometry("%dx%d+%d+%d"%(800,480,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')


color = 'lightblue'
top_fg_color = 'lightblue'
top_bg_color = '#111131'

#top = Frame(root,height=100,bg=top_bg_color)
#top.pack(fill="both",expand=1)

w = Canvas(root,width= 800,height= 100)
w.pack()
w.create_rectangle(0,0,800,100,fill=top_bg_color)

Label(root,text='SAJAB Management System',fg=top_fg_color,bg=top_bg_color,font="tahoma 24 bold",pady=10).place(x=150,y=5)

#Tab
tab = ttk.Notebook(root)
tab.pack(fill='both',expand='yes')

management_panel= Frame(bg=color)
station_list= Frame(bg=color)
add_station= Frame(bg=color)
admin_list= Frame(bg=color)

tab.add(management_panel,text='Management Panel')
tab.add(station_list,text='Stations List')
tab.add(add_station,text='Add Stations')
tab.add(admin_list,text='Admin List')
#end tab

def apply_sampling_rate():
    print(e1.get())


def send_data():
    urlretrieve("http://sajab.sazabgolestan.com/server.php?action=save&station_index=3&ha=2&hb=13&imei=9359374362","my picture")
    print ("send")

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
    #Sensor Display
#    u1 = str(u1)
#    temp = u1
#    loc = u1.find('R')
#    u1 = u1[loc+1:loc+6]
#    ss=Label(management_panel,text=u1)
#    ss.place(x=160,y=100)
    #end Sensor Display
    #Temprature Display
#    loc = temp.find('T')
#    temp = temp[loc+1:loc+4]
#    tt=Label(root,text=temp,fg=top_fg_color,bg=top_bg_color,font=("Ravie",10))
#    tt.place(x=60,y=50)
    #end Temprature Display
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

#############################TIME################################
time_xloc= 20
time_yloc= 5

hourLabel = Label(root,text=nowHour(),fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
hourLabel.place(x=time_xloc,y=time_yloc)
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
#############################DATE################################
date_xloc=10
date_yloc=30

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
#end time
temp_label = Label(root,text="Temp: ",fg=top_fg_color,bg=top_bg_color,font=("Ravie", 10))
temp_label.place(x=date_xloc,y=date_yloc+20)

sensors = ['Sensor 1','Sensor 2','Sensor 3','Sensor 4']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(management_panel,text=c,fg=top_bg_color,bg=color,relief=RIDGE,width=15).place(x=20,y=100+r*40)
    r=r+1
r=0
for c in relays:
    Label(management_panel,text=c,fg=top_bg_color,bg=color,relief=RIDGE,width=15).place(x=300,y=100+r*40)
    r=r+1

Label(management_panel,text="Sampling rate: ").grid(row=0)
e1=Entry(management_panel)
e1.grid(row=0,column=1)
Button(management_panel,text="Send",command=apply_sampling_rate).grid(row=2,column=1,sticky=W,pady=4)
#send = Button(root,text="Send Data",command = send_data).pack()

time.sleep(1)
root.mainloop()
