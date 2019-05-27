#Library
import datetime
import time
from tkinter import *
import tkinter.ttk as ttk
from urllib.request import urlretrieve
import serial
import os
import RPi.GPIO as GPIO
from hashlib import md5
#End Library
time.sleep(3)
#Firmwares
ultra1 = serial.Serial("/dev/ttyUSB1",baudrate=9600, timeout=1)
gsm = serial.Serial("/dev/ttyUSB0",baudrate=9600, timeout=1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT) #Relay 1
GPIO.setup(33,GPIO.OUT) #Relay 2
GPIO.setup(35,GPIO.OUT) #Relay 3
GPIO.setup(37,GPIO.OUT) #Relay 4
GPIO.setup(12,GPIO.OUT) #Sensor1 Enable
#End Firmwares



root=Tk()
root.geometry("%dx%d+%d+%d"%(800,400,100,50)) #x,y,horizental,vertical
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

global config_rate
config_rate = 60


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

time_xloc= 10
time_yloc= 10

date_xloc=10
date_yloc=30

table_x=20
table_y=120

step = 25
stepx = 38

global skiper
skiper = 0

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def find_data(file,name,next_name,space):
    data = file[file.find(name)+len(name)+space:file.find(next_name)-space]
    return data

def read_defualt():
    def_conf = open("default_conf.txt","r")
    global def_conf_str
    def_conf_str = str(def_conf.read())

    global default_sampling_rate
    default_sampling_rate=int(find_data(def_conf_str,'sampling_rate','bias_value',1))
    global default_bias_value
    default_bias_value=int(find_data(def_conf_str,'bias_value','coefficent',1))
    global default_coefficent
    default_coefficent=int(find_data(def_conf_str,'coefficent','max_level',1))
    global default_max_level
    default_max_level=int(find_data(def_conf_str,'max_level','hysteresis_value',1))
    global default_hysteresis_value
    default_hysteresis_value=int(find_data(def_conf_str,'hysteresis_value','mobile_phone1',1))
    global default_mobile_phone1
    default_mobile_phone1=str(find_data(def_conf_str,'mobile_phone1','mobile_phone2',1))
    global default_mobile_phone2
    default_mobile_phone2=str(find_data(def_conf_str,'mobile_phone2','mobile_phone3',1))
    global default_mobile_phone3
    default_mobile_phone3=str(def_conf_str[def_conf_str.find('mobile_phone3')+len('mobile_phone3')+1:])
    def_conf.close()

read_defualt()

def read_conf():
    conf=open("conf.txt","r")
    conf_str=str(conf.read())
    global sampling_rate
    sampling_rate=int(find_data(conf_str,'sampling_rate','bias_value',1))
    global bias_value
    bias_value=int(find_data(conf_str,'bias_value','coefficent',1))
    global coefficent
    coefficent=int(find_data(conf_str,'coefficent','max_level',1))
    global max_level
    max_level=int(find_data(conf_str,'max_level','hysteresis_value',1))
    global hysteresis_value
    hysteresis_value=int(find_data(conf_str,'hysteresis_value','mobile_phone1',1))
    global mobile_phone1
    mobile_phone1=str(find_data(conf_str,'mobile_phone1','mobile_phone2',1))
    global mobile_phone2
    mobile_phone2=str(find_data(conf_str,'mobile_phone2','mobile_phone3',1))
    global mobile_phone3
    mobile_phone3=str(conf_str[conf_str.find('mobile_phone3')+len('mobile_phone3')+1:])

    local_conf_file = open("local_conf.txt","r")
    local_conf_str = str(local_conf_file.read())
    crr = local_conf_str[local_conf_str.find('config_request_rate')+len('config_request_rate')+1:]
    crr = int(crr)
    global config_request_rate
    config_request_rate = crr


#End Variables


#Functions

def relay1():
    relay1_source = open("relay1_source.txt","w+")
    GPIO.setup(31,GPIO.OUT) #Relay 1
    if v1.get()==0:
        GPIO.output(31,0)
        relay1_source.write("0")
    else:
        GPIO.output(31,1)
        relay1_source.write("1")
    relay1_source.close()
def relay2():
    relay2_source = open("relay2_source.txt","w+")
    GPIO.setup(33,GPIO.OUT) #Relay 1
    if v2.get()==0:
        GPIO.output(33,0)
        relay2_source.write("0")
    else:
        GPIO.output(33,1)
        relay2_source.write("1")
    relay2_source.close()
def relay3():
    relay3_source = open("relay3_source.txt","w+")
    GPIO.setup(35,GPIO.OUT) #Relay 1
    if v3.get()==0:
        GPIO.output(35,0)
        relay3_source.write("0")
    else:
        GPIO.output(35,1)
        relay3_source.write("1")
    relay3_source.close()
def relay4():
    relay4_source = open("relay4_source.txt","w+")
    GPIO.setup(37,GPIO.OUT) #Relay 1
    if v4.get()==0:
        GPIO.output(37,0)
        relay4_source.write("0")
    else:
        GPIO.output(37,1)
        relay4_source.write("1")
    relay4_source.close()

def save_data():
    database = open("sajab_database.txt","a+")
    data = "\n%s/%s/%s - %s:%s:%s - Temprature:%d - Distance:%d" %(nowYear(),nowMonth(),nowDay(),nowHour(),nowMinute(),nowSecond(),sensor1_read(sen1,temp1)[1],sensor1_read(sen1,temp1)[0])
    database.write(data)
    database.close()



#Config request
def config_req():
    gsm.flushInput()
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
    data_link = "AT+HTTPPARA=\"URL\",\"http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3\"\r\n"
    gsm.write(data_link.encode('ascii'))
    time.sleep(1)
    gsm.write("AT+HTTPACTION=0\r\n".encode('ascii'))
    time.sleep(10)
    gsm.flushInput()
    gsm.write("AT+HTTPREAD\r\n".encode('ascii'))
    time.sleep(1)
    rcv = gsm.read(3000)
    print(rcv)
    print(type(rcv))
    rcv = str(rcv)
    print(type(rcv))
    rcv = rcv[rcv.find('{'):rcv.find('}')+1]
    print (rcv)
    if len(rcv)>20:
        global ser_conf
        ser_conf = open("server_conf.txt","w+")
        ser_conf.write(rcv)
        ser_conf.close()
        time.sleep(1)
        global status
        status = find_data(rcv,'status','name',3)
        global station_name
        station_name = str(find_data(rcv,'name','description',3))
        global description
        description = str(find_data(rcv,'description','price',3))
        global price
        price = str(find_data(rcv,'price','ha',3))
        global ha
        ha = int(find_data(rcv,'ha','hb',3))
        global hb
        hb = int(find_data(rcv,'hb','multi',3))
        global multi
        multi = int(find_data(rcv,'multi','sampling_rate',3))
        global sampling_rate
        sampling_rate = int(find_data(rcv,'sampling_rate','bias_value',3))
        global bias_value
        bias_value = int(find_data(rcv,'bias_value','coefficent',3))
        global coefficent
        coefficent = int(find_data(rcv,'coefficent','max_level',3))
        global max_level
        max_level = int(find_data(rcv,'max_level','hysteresis_value',3))
        global hysteresis_value
        hysteresis_value = int(find_data(rcv,'hysteresis_value','mobile_phone1',3))
        global mobile_phone1
        mobile_phone1 = str(find_data(rcv,'mobile_phone1','mobile_phone2',3))
        global mobile_phone2
        mobile_phone2 = str(find_data(rcv,'mobile_phone2','mobile_phone3',3))
        global mobile_phone3
        mobile_phone3 = str(rcv[rcv.find('mobile_phone3')+len('mobile_phone3')+3:rcv.find('}')-1])
        print (mobile_phone3)

        conf_str = "http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3&status=1&sampling_rate=%d&bias_value=%d&coefficent=%d&max_level=%d&hysteresis_value=%d&mobile_phone1=%s&mobile_phone2=%s&mobile_phone3=%s" %(sampling_rate,bias_value,coefficent,max_level,hysteresis_value,mobile_phone1,mobile_phone2,mobile_phone3)

        conf_file = open("conf.txt","w+")
        conf_file.write(conf_str)
        conf_file.close()
    else:
        print("Network connection ERROR!")
#End Config request


#Send config
def send_config(datalink):
    gsm.flushInput()
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
    data_link = "AT+HTTPPARA=\"URL\",\"" + datalink + "\"\r\n"
    gsm.write(data_link.encode('ascii'))
    time.sleep(1)
    gsm.write("AT+HTTPACTION=0\r\n".encode('ascii'))
    time.sleep(10)



#End Send config


#Send Data
def send_data():
    gsm.flushInput()
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
    data_link = "AT+HTTPPARA=\"URL\",\"http://sajab.sazabgolestan.com/server.php?action=save&station_index=3&ha=%d&hb=3&imei=9359374362\"\r\n" %(sensor1_read(sen1,temp1)[0])
    gsm.write(data_link.encode('ascii'))
    time.sleep(1)
    gsm.write("AT+HTTPACTION=0\r\n".encode('ascii'))
    time.sleep(10)
    save_data()
#End Send Data
#Sensor Read
def sensor1_read(sen,temp):
    read_conf()
    def count():
        ultra1.flushInput()
        GPIO.output(12,0)
        global u1
        u1 = ultra1.read(12)
        u1 = str(u1)
        if len(u1)>5:
            t_loc = u1.find('T')
            global t1
            t1 = u1[t_loc+1:t_loc+4]
            loc = u1.find('R')
            u1 = u1[loc+1:loc+6]
            GPIO.output(12,1)
            sen.config(text=str(u1))
            sen.after(sampling_rate*500,count)
            temp.config(text=str(t1))
            global skiper
            skiper = skiper + 1
        else:
            print("Sensor connection ERROR!")
    count()
    global u1
    if len(u1)>3:
        return [int(u1),int(t1)]
    else:
        return [0,0]
#End Sensor read

def conf_req(conf):
    def count():
        read_conf()
        if skiper>3:
            config_req()
            send_data()
        print(skiper)
        print(config_request_rate)
        conf.after(config_request_rate*1000,count)
    count()

def read_pass():
    pass_file = open("passwd.txt","r")
    pass_main = str(pass_file.read())
    return pass_main

def change_pass():
    global changepass
    changepass = Toplevel()
    changepass.geometry("%dx%d+%d+%d"%(420,180,100,50)) #x,y,horizental,vertical
    changepass.title('Change Password')
    changepass.configure(background='lightblue')
    Label(changepass,text="Enter Old Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20)
    global old_pass
    old_pass=Entry(changepass,width=18,font=(14))
    old_pass.place(x=230,y=20)

    global new_pass1
    Label(changepass,text="Enter New Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20+stepx)
    new_pass1=Entry(changepass,width=18,font=(14))
    new_pass1.place(x=230,y=20+stepx)

    global new_pass2
    Label(changepass,text="Confirm New Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20+2*stepx)
    new_pass2=Entry(changepass,width=18,font=(14))
    new_pass2.place(x=230,y=20+2*stepx)

    def op_change_pass():
        if str(make_md5(str(old_pass.get()))) == read_pass():
            if str(new_pass1.get()) == str(new_pass2.get()):
                pass_file = open("passwd.txt","w+")
                pass_file.write(str(make_md5(str(new_pass1.get()), encoding='utf-8')))
                pass_file.close()
                changepass.destroy()
                warning = Toplevel()
                warning.geometry("%dx%d+%d+%d"%(150,70,100,50)) #x,y,horizental,vertical
                warning.title('Done')
                warning.configure(background='lightblue')
                Label(warning,text="Password Changed!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
                Button(warning,text="OK",command=warning.destroy).place(x=70,y=40)
            else:
                warning = Toplevel()
                warning.geometry("%dx%d+%d+%d"%(250,80,100,50)) #x,y,horizental,vertical
                warning.title('Warning')
                warning.configure(background='lightblue')
                Label(warning,text="Entered pass isn't match!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
                Button(warning,text="OK",command=warning.destroy).place(x=70,y=50)
        else:
            warning = Toplevel()
            warning.geometry("%dx%d+%d+%d"%(250,80,100,50)) #x,y,horizental,vertical
            warning.title('Warning')
            warning.configure(background='lightblue')
            Label(warning,text="Entered pass is wrong!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
            Button(warning,text="OK",command=warning.destroy).place(x=70,y=50)



    Button(changepass,text="OK",command=op_change_pass,font=(14)).place(x=20,y=140)
    Button(changepass,text="Cancel",command=changepass.destroy,font=(14)).place(x=80,y=140)



def pass_check():
    global passcheck
    passcheck = Toplevel()
    passcheck.geometry("%dx%d+%d+%d"%(220,140,100,50)) #x,y,horizental,vertical
    passcheck.title('Setting')
    passcheck.configure(background='lightblue')
    Label(passcheck,text="Enter Password:",fg=top_bg_color,bg=color,font=(14)).place(x=40,y=20)
    global pass_in
    pass_in=Entry(passcheck,width=18,font=(14),show='*')
    pass_in.place(x=25,y=50)

    Button(passcheck,text="OK",command=pass_check2,font=(14)).place(x=80,y=80)

def pass_check2():
    print(make_md5(str(pass_in.get()), encoding='utf-8'))
    print(read_pass())
    if make_md5(str(pass_in.get()), encoding='utf-8')==read_pass():
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
    Label(setting_frame,text="Station name:",fg=top_bg_color,bg=color,font=(14)).grid(row=0,column=0,ipadx=30,pady=8)
    global st_name
    st_name=Entry(setting_frame,width=15,font=(14))
    st_name.place(x=180,y=10)
    st_name.insert(10,str(station_name))
    Label(setting_frame,text="Sampling rate:",fg=top_bg_color,bg=color,font=(14)).grid(row=1,column=0,ipadx=30,pady=8)
    read_conf()
    global samp_rate
    samp_rate=Entry(setting_frame,width=8,font=(14))
    samp_rate.place(x=180,y=10+stepx)
    samp_rate.insert(10,str(sampling_rate))
    Label(setting_frame,text="Sec.",fg=top_bg_color,bg=color).place(x=270,y=10+stepx)
    Label(setting_frame,text="Calibration:",fg=top_bg_color,bg=color,font=(14)).grid(row=2,column=0,ipadx=30,pady=8)
    Label(setting_frame,text="Bias Value:",fg=top_bg_color,bg=color,font=(14)).grid(row=3,column=0,ipadx=30,pady=8)
    global bs_value
    bs_value=Entry(setting_frame,width=8,font=(14))
    bs_value.place(x=180,y=10+3*stepx)
    bs_value.insert(10,str(bias_value))
    Label(setting_frame,text="Coefficent:",fg=top_bg_color,bg=color,font=(14)).grid(row=4,column=0,ipadx=30,pady=8)
    global coef
    coef=Entry(setting_frame,width=8,font=(14))
    coef.place(x=180,y=10+4*stepx)
    coef.insert(10,str(coefficent))
    Label(setting_frame,text="Set config rate:",fg=top_bg_color,bg=color,font=(14)).grid(row=5,column=0,ipadx=30,pady=8)
    global set_co_r
    set_co_r=Entry(setting_frame,width=8,font=(14))
    set_co_r.place(x=180,y=10+5*stepx)
    set_co_r.insert(10,config_request_rate)
    Label(setting_frame,text="Sec.",fg=top_bg_color,bg=color).place(x=270,y=10+5*stepx)

    Label(setting_frame,text="Alert:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10)
    Label(setting_frame,text="Max level:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+stepx)
    global mx_level
    mx_level=Entry(setting_frame,width=8,font=(14))
    mx_level.place(x=500,y=10+stepx)
    mx_level.insert(10,str(max_level))
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color).place(x=600,y=10+stepx)
    Label(setting_frame,text="Hysteresis level:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+2*stepx)
    global hys_value
    hys_value=Entry(setting_frame,width=8,font=(14))
    hys_value.place(x=500,y=10+2*stepx)
    hys_value.insert(10,str(hysteresis_value))
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=600,y=10+2*stepx)
    Label(setting_frame,text="Mobile Phone 1:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+3*stepx)
    global mob_phone1
    mob_phone1=Entry(setting_frame,width=15,font=(14))
    mob_phone1.place(x=500,y=10+3*stepx)
    mob_phone1.insert(10,str(mobile_phone1))
    Label(setting_frame,text="Mobile Phone 2:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+4*stepx)
    global mob_phone2
    mob_phone2=Entry(setting_frame,width=15,font=(14))
    mob_phone2.place(x=500,y=10+4*stepx)
    mob_phone2.insert(10,str(mobile_phone2))
    Label(setting_frame,text="Mobile Phone 3:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+5*stepx)
    global mob_phone3
    mob_phone3=Entry(setting_frame,width=15,font=(14))
    mob_phone3.place(x=500,y=10+5*stepx)
    mob_phone3.insert(10,str(mobile_phone3))
    Button(setting_frame,text="OK",command=ok,font=(14)).place(x=20,y=320)
    Button(setting_frame,text="Set as default",command=setasdefault,font=(14)).place(x=90,y=320)
    Button(setting_frame,text="Default values",command=defaultvals,font=(14)).place(x=230,y=320)
    Button(setting_frame,text="Change Pass",command=change_pass,font=(14)).place(x=400,y=320)
    Button(setting_frame,text="Cancel",command=cncl,font=(14)).place(x=580,y=320)

def ok():
    global sampling_rate
    sampling_rate = int(samp_rate.get())
    print(int(samp_rate.get()))
    print(sampling_rate)
    bias_value = int(bs_value.get())
    coefficent = int(coef.get())
    config_request_rate = int(set_co_r.get())
    max_level = int(mx_level.get())
    hysteresis_value = int(hys_value.get())
    mobile_phone1 = mob_phone1.get()
    mobile_phone2 = mob_phone2.get()
    mobile_phone3 = mob_phone3.get()

    conf_str = "http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3&status=1&sampling_rate=%d&bias_value=%d&coefficent=%d&max_level=%d&hysteresis_value=%d&mobile_phone1=%s&mobile_phone2=%s&mobile_phone3=%s" %(sampling_rate,bias_value,coefficent,max_level,hysteresis_value,mobile_phone1,mobile_phone2,mobile_phone3)

    conf_file = open("conf.txt","w+")
    conf_file.write(conf_str)
    conf_file.close()

    local_conf_str = "config_request_rate=%d" %(int(config_request_rate))
    local_conf_file = open("local_conf.txt","w+")
    local_conf_file.write(local_conf_str)
    local_conf_file.close()


    sr_label.config(text=sampling_rate)

    send_config(conf_str)

    setting_frame.destroy()
def cncl():
    setting_frame.destroy()


def defaultvals():
    read_defualt()
    samp_rate.delete(0,END)
    samp_rate.insert(10,str(default_sampling_rate))
    bs_value.delete(0,END)
    bs_value.insert(10,str(default_bias_value))
    coef.delete(0,END)
    coef.insert(10,str(default_coefficent))
    mx_level.delete(0,END)
    mx_level.insert(10,str(default_max_level))
    hys_value.delete(0,END)
    hys_value.insert(10,str(default_hysteresis_value))
    mob_phone1.delete(0,END)
    mob_phone1.insert(10,str(default_mobile_phone1))
    mob_phone2.delete(0,END)
    mob_phone2.insert(10,str(default_mobile_phone2))
    mob_phone3.delete(0,END)
    mob_phone3.insert(10,str(default_mobile_phone3))



def setasdefault():
    read_defualt()
    default_sampling_rate = int(samp_rate.get())
    default_bias_value = int(bs_value.get())
    default_coefficent = int(coef.get())
    default_max_level = int(mx_level.get())
    default_hysteresis_value = int(hys_value.get())
    default_mobile_phone1 = mob_phone1.get()
    default_mobile_phone2 = mob_phone2.get()
    default_mobile_phone3 = mob_phone3.get()

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
hourLabel = Label(root,text=nowHour(),fg=top_fg_color,bg=top_bg_color,font=(14))
hourLabel.place(x=time_xloc,y=time_yloc)
hour_label(hourLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=time_xloc+step,y=time_yloc)

minuteLabel = Label(root, text = nowMinute(),fg=top_fg_color,bg=top_bg_color,font=(14))
minuteLabel.place(x=time_xloc+2*step,y=time_yloc)
minute_label(minuteLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=time_xloc+3*step,y=time_yloc)

secondLabel = Label(root, text = nowSecond(),fg=top_fg_color,bg=top_bg_color,font=(14))
secondLabel.place(x=time_xloc+4*step,y=time_yloc)
second_label(secondLabel)
#End Time

#Date
yearLabel = Label(root,text=nowYear(),fg=top_fg_color,bg=top_bg_color,font=(14))
yearLabel.place(x=date_xloc,y=date_yloc)
year_label(yearLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=date_xloc+45,y=date_yloc)

monthLabel = Label(root,text=nowMonth(),fg=top_fg_color,bg=top_bg_color,font=(14))
monthLabel.place(x=date_xloc+55,y=date_yloc)
month_label(monthLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=date_xloc+75,y=date_yloc)

dayLabel = Label(root,text=nowDay(),fg=top_fg_color,bg=top_bg_color,font=(14))
dayLabel.place(x=date_xloc+85,y=date_yloc)
day_label(dayLabel)
#End Date

#Temp
temp_label = Label(root,text="Temp: ",fg=top_fg_color,bg=top_bg_color,font=(14))
temp_label.place(x=date_xloc,y=date_yloc+stepx)
#End Temp
#End Header

#Body
sensors = ['Sensor 1:','Sensor 2:','Sensor 3:','Sensor 4:']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(root,text=c,fg=top_bg_color,bg=color,font=(14)).place(x=table_x,y=table_y+r*stepx)
    r=r+1
r=0
for c in relays:
    Label(root,text=c,fg=top_bg_color,bg=color,font=(14)).place(x=table_x+300,y=table_y+r*stepx)
    r=r+1
#Sensors Display
global sen1
sen1 = Label(root,fg=top_bg_color,bg=color,font=(14))
sen1.place(x= table_x+130,y=table_y)
#sensor1_read(sen1)
#End Sensors Display

#Temprature Display
global temp1
temp1 = Label(root,fg=color,bg=top_bg_color,font=(14))
temp1.place(x= 70,y=date_yloc+stepx)
sensor1_read(sen1,temp1)
#End Temprature Display
confr = Label(root,fg=color,bg=top_bg_color,font=(14))
confr.place(x=0,y=0)
conf_req(confr)

#Relay control
Radiobutton(root,text="OFF",variable=v1,command=relay1,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y)
Radiobutton(root,text="ON",variable=v1,command=relay1,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y)

Radiobutton(root,text="OFF",variable=v2,command=relay2,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+stepx)
Radiobutton(root,text="ON",variable=v2,command=relay2,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+stepx)

Radiobutton(root,text="OFF",variable=v3,command=relay3,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+2*stepx)
Radiobutton(root,text="ON",variable=v3,command=relay3,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+2*stepx)

Radiobutton(root,text="OFF",variable=v4,command=relay4,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+3*stepx)
Radiobutton(root,text="ON",variable=v4,command=relay4,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+3*stepx)

#End Relay control



Label(root,text="Sampling rate:",fg=top_bg_color,bg=color,font=(14)).place(x=table_x,y=table_y+4*stepx)
global sr_label
sr_label = Label(root,fg=top_bg_color,bg=color,font=(14))
sr_label.place(x=table_x+130,y=table_y+4*stepx)
sr_label.config(text=sampling_rate)
#sr_read(sr_label)
Label(root,text="Sec.",fg=top_bg_color,bg=color,font=(14)).place(x=table_x+160,y=table_y+4*stepx)

Button(root,text="Setting",command=pass_check,font=(14)).place(x=630,y=360)
Button(root,text="Send Data",command=send_data,font=(14)).place(x=200,y=360)
Button(root,text="Config request",command=config_req,font=(14)).place(x=400,y=360)



#End Body


root.mainloop()
