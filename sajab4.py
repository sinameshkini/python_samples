#Library
import datetime
import time
from tkinter import *
import tkinter.ttk as ttk
from urllib.request import urlretrieve
import serial
import os
import RPi.GPIO as GPIO
#End Library

#Firmwares
ultra1 = serial.Serial("/dev/ttyUSB0",baudrate=9600, timeout=1)
gsm = serial.Serial("/dev/ttyAMA0",baudrate=9600, timeout=1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT) #Relay 1
GPIO.setup(33,GPIO.OUT) #Relay 2
GPIO.setup(35,GPIO.OUT) #Relay 3
GPIO.setup(37,GPIO.OUT) #Relay 4
GPIO.setup(12,GPIO.OUT) #Sensor1 Enable
#End Firmwares



root=Tk()
root.geometry("%dx%d+%d+%d"%(800,480,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')

f1=open("relay1_source.txt","r")
f2=open("relay2_source.txt","r")
f3=open("relay3_source.txt","r")
f4=open("relay4_source.txt","r")



v1 = IntVar()
v1.set(int(f1.read()))  # initializing the choice, i.e. Python

v2 = IntVar()
v2.set(int(f2.read()))  # initializing the choice, i.e. Python

v3 = IntVar()
v3.set(int(f3.read()))  # initializing the choice, i.e. Python

v4 = IntVar()
v4.set(int(f4.read()))  # initializing the choice, i.e. Python

GPIO.output(31,v1.get())
GPIO.output(33,v2.get())
GPIO.output(35,v3.get())
GPIO.output(37,v4.get())

f1.close()
f2.close()
f3.close()
f4.close()



#Variables
station_name = "Golestan Uni"

pass_main='1120'
time_xloc= 20
time_yloc= 5

date_xloc=10
date_yloc=30

table_x=20
table_y=150

global default_sampling_rate
global default_bias_value
global default_coefficent
global default_max_level
global default_hysteresis_level
global default_mobile_phone1
global default_mobile_phone2
global default_mobile_phone3

step = 20
stepx = 40
global sampling_rate
sampling_rate=2
#End Variables


#Functions

def relay1():
    relay1_source = open("relay1_source.txt","w+")
    GPIO.setup(31,GPIO.OUT) #Relay 1
    if v1.get()==0:
        print("is off")
        GPIO.output(31,0)
        relay1_source.write("0")
    else:
        print("in on")
        GPIO.output(31,1)
        relay1_source.write("1")
    relay1_source.close()
def relay2():
    relay2_source = open("relay2_source.txt","w+")
    GPIO.setup(33,GPIO.OUT) #Relay 1
    if v2.get()==0:
        print("is off")
        GPIO.output(33,0)
        relay2_source.write("0")
    else:
        print("in on")
        GPIO.output(33,1)
        relay2_source.write("1")
    relay2_source.close()
def relay3():
    relay3_source = open("relay3_source.txt","w+")
    GPIO.setup(35,GPIO.OUT) #Relay 1
    if v3.get()==0:
        print("is off")
        GPIO.output(35,0)
        relay3_source.write("0")
    else:
        print("in on")
        GPIO.output(35,1)
        relay3_source.write("1")
    relay3_source.close()
def relay4():
    relay4_source = open("relay4_source.txt","w+")
    GPIO.setup(37,GPIO.OUT) #Relay 1
    if v4.get()==0:
        print("is off")
        GPIO.output(37,0)
        relay4_source.write("0")
    else:
        print("in on")
        GPIO.output(37,1)
        relay4_source.write("1")
    relay4_source.close()

#Send Data
def send_data():
    gsm.write("AT\r\n".encode('ascii'))
    rcv = gsm.read(10)
    print (rcv)
    gsm.write("AT+CSQ\r\n".encode('ascii'))
    time.sleep(1)
    gsm.write("AT+CGATT?\r\n".encode('ascii'))
    time.sleep(1)
    gsm.write("AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"\r\n".encode('ascii'))
    time.sleep(1)
    gsm.write("AT+SAPBR=3,1,\"APN\",\"mtnirancell\"\r\n".encode('ascii'))
    time.sleep(4)
    gsm.write("AT+SAPBR=1,1\r\n".encode('ascii'))
    time.sleep(2)
    gsm.write("AT+HTTPINIT\r\n".encode('ascii'))
    time.sleep(2)
    data_link = "AT+HTTPPARA=\"URL\",\"http://sajab.sazabgolestan.com/server.php?action=save&station_index=3&ha=%d&hb=3&imei=9359374362\"\r\n" %(sensor1_read(sen1))
    gsm.write(data_link.encode('ascii'))
    time.sleep(1)
    gsm.write("AT+HTTPACTION=0\r\n".encode('ascii'))
    time.sleep(10)
#End Send Data
#Sensor Read
def sensor1_read(sen):
    def count():
        GPIO.output(12,0)
        global u1
        u1 = ultra1.read(12)
        u1 = str(u1)
        loc = u1.find('R')
        u1 = u1[loc+1:loc+6]
        GPIO.output(12,1)
        sen.config(text=str(u1))
        sen.after(sampling_rate*500,count)
    count()
    return int(u1)
#End Sensor read

#Samle Rate read
#def sr_read(sr_label):
#    def count5():
#        sr_label.config(text=str(sampling_rate))
#        sr_label.after(sampling_rate*500,count5)
#    count5()
#End Samle Rate read

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
    global samp_rate
    samp_rate=Entry(setting_frame,width=8)
    samp_rate.place(x=140,y=45)
    samp_rate.insert(10,str(sampling_rate))
    Label(setting_frame,text="Sec.",fg=top_bg_color,bg=color,width=0).place(x=220,y=46)
    Label(setting_frame,text="Calibration:",fg=top_bg_color,bg=color,width=0).grid(row=2,column=0,ipadx=30,pady=8)
    Label(setting_frame,text="Bias Value:",fg=top_bg_color,bg=color,width=0).grid(row=3,column=0,ipadx=30,pady=8)
    global bs_value
    bs_value=Entry(setting_frame,width=8)
    bs_value.place(x=140,y=118)
    bs_value.insert(10,str(default_bias_value))
    Label(setting_frame,text="Coefficent:",fg=top_bg_color,bg=color,width=0).grid(row=4,column=0,ipadx=30,pady=8)
    global coef
    coef=Entry(setting_frame,width=8)
    coef.place(x=140,y=154)
    coef.insert(10,str(default_coefficent))
    Label(setting_frame,text="Alert:",fg=top_bg_color,bg=color,width=0).grid(row=0,column=3,ipadx=30,pady=8)
    Label(setting_frame,text="Max level:",fg=top_bg_color,bg=color,width=0).grid(row=1,column=3,ipadx=30,pady=8)
    global mx_level
    mx_level=Entry(setting_frame,width=8)
    mx_level.place(x=465,y=45)
    mx_level.insert(10,str(default_max_level))
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=545,y=46)
    Label(setting_frame,text="Hysteresis level:",fg=top_bg_color,bg=color,width=0).grid(row=2,column=3,ipadx=30,pady=8)
    global hys_level
    hys_level=Entry(setting_frame,width=8)
    hys_level.place(x=465,y=81)
    hys_level.insert(10,str(default_hysteresis_level))
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=545,y=82)
    Label(setting_frame,text="Mobile Phone 1:",fg=top_bg_color,bg=color,width=0).grid(row=3,column=3,ipadx=30,pady=8)
    global mob_phone1
    mob_phone1=Entry(setting_frame,width=15)
    mob_phone1.place(x=465,y=117)
    mob_phone1.insert(10,str(default_mobile_phone1))
    Label(setting_frame,text="Mobile Phone 2:",fg=top_bg_color,bg=color,width=0).grid(row=4,column=3,ipadx=30,pady=8)
    global mob_phone2
    mob_phone2=Entry(setting_frame,width=15)
    mob_phone2.place(x=465,y=153)
    mob_phone2.insert(10,str(default_mobile_phone2))
    Label(setting_frame,text="Mobile Phone 3:",fg=top_bg_color,bg=color,width=0).grid(row=5,column=3,ipadx=30,pady=8)
    global mob_phone3
    mob_phone3=Entry(setting_frame,width=15)
    mob_phone3.place(x=465,y=189)
    mob_phone3.insert(10,str(default_mobile_phone3))
    Button(setting_frame,text="OK",command=ok).place(x=30,y=220)
    Button(setting_frame,text="Set as default",command=setasdefault).place(x=120,y=220)
    Button(setting_frame,text="Default values",command=defaultvals).place(x=300,y=220)
    Button(setting_frame,text="Cancel",command=cncl).place(x=500,y=220)

def ok():
    global sampling_rate
    sampling_rate = int(samp_rate.get())
    print(int(samp_rate.get()))
    print(sampling_rate)
    bias_value = int(bs_value.get())
    coefficent = int(coef.get())
    max_level = int(mx_level.get())
    hysteresis_value = int(hys_level.get())
    mobile_phone1 = mob_phone1.get()
    mobile_phone2 = mob_phone2.get()
    mobile_phone3 = mob_phone3.get()

    conf_str = "http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3&status=1&sampling_rate=%d&bias_value=%d&coefficent=%d&max_level=%d&hysteresis_value=%d&mobile_phone1=%s&mobile_phone2=%s&mobile_phone3=%s" %(sampling_rate,bias_value,coefficent,max_level,hysteresis_value,mobile_phone1,mobile_phone2,mobile_phone3)

    conf_file = open("conf.txt","w+")
    conf_file.write(conf_str)
    conf_file.close()



    setting_frame.destroy()
def cncl():
    setting_frame.destroy()

def defaultvals():

    samp_rate.delete(0,END)
    samp_rate.insert(10,str(default_sampling_rate))
    bs_value.delete(0,END)
    bs_value.insert(10,str(default_bias_value))
    coef.delete(0,END)
    coef.insert(10,str(default_coefficent))
    mx_level.delete(0,END)
    mx_level.insert(10,str(default_max_level))
    hys_level.delete(0,END)
    hys_level.insert(10,str(default_hysteresis_level))
    mob_phone1.delete(0,END)
    mob_phone1.insert(10,str(default_mobile_phone1))
    mob_phone2.delete(0,END)
    mob_phone2.insert(10,str(default_mobile_phone2))
    mob_phone3.delete(0,END)
    mob_phone3.insert(10,str(default_mobile_phone3))

def setasdefault():
    default_conf_str = "http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3&status=1&sampling_rate=%d&bias_value=%d&coefficent=%d&max_level=%d&hysteresis_value=%d&mobile_phone1=%s&mobile_phone2=%s&mobile_phone3=%s" %(default_sampling_rate,default_bias_value,default_coefficent,default_max_level,default_hysteresis_value,default_mobile_phone1,default_mobile_phone2,default_mobile_phone3)

    default_conf_file = open("default_conf.txt","w+")
    default_conf_file.write(default_conf_str)
    default_conf_file.close()


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


color = 'lightblue'
top_fg_color = 'lightblue'
top_bg_color = '#111131'
#End Desigen Param

#Header
w = Canvas(root,width= 800,height= 100)
w.pack()
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
#Sensors Display
global sen1
sen1 = Label(root,fg=top_bg_color,bg=color)
sen1.place(x= table_x+130,y=table_y)
sensor1_read(sen1)
#End Sensors Display

#Relay control
Radiobutton(root,text="OFF",variable=v1,command=relay1,value=1).place(x= table_x+400,y=table_y)
Radiobutton(root,text="ON",variable=v1,command=relay1,value=0).place(x= table_x+500,y=table_y)

Radiobutton(root,text="OFF",variable=v2,command=relay2,value=1).place(x= table_x+400,y=table_y+stepx)
Radiobutton(root,text="ON",variable=v2,command=relay2,value=0).place(x= table_x+500,y=table_y+stepx)

Radiobutton(root,text="OFF",variable=v3,command=relay3,value=1).place(x= table_x+400,y=table_y+2*stepx)
Radiobutton(root,text="ON",variable=v3,command=relay3,value=0).place(x= table_x+500,y=table_y+2*stepx)

Radiobutton(root,text="OFF",variable=v4,command=relay4,value=1).place(x= table_x+400,y=table_y+3*stepx)
Radiobutton(root,text="ON",variable=v4,command=relay4,value=0).place(x= table_x+500,y=table_y+3*stepx)

#End Relay control



Label(root,text="Sampling rate:",fg=top_bg_color,bg=color,width=0).place(x=table_x+50,y=350)
global sr_label
sr_label = Label(root,fg=top_bg_color,bg=color)
sr_label.place(x=table_x+150,y=350)
#sr_read(sr_label)
Label(root,text="Sec.",fg=top_bg_color,bg=color,width=0).place(x=table_x+230,y=351)

Button(root,text="Setting",command=pass_check).place(x=700,y=410)
Button(root,text="Send Data",command=send_data).place(x=200,y=410)



#End Body


root.mainloop()
