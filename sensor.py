import serial
import os, time
from tkinter import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
ultra1 = serial.Serial("/dev/ttyUSB0",baudrate=9600, timeout=1)

root=Tk()
root.geometry("%dx%d+%d+%d"%(800,600,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

def sensor1_read(sen):
    def count():
        GPIO.output(12,0)
        u1 = ultra1.read(12)
        u1 = str(u1)
        loc = u1.find('R')
        u1 = u1[loc+1:loc+6]
        GPIO.output(12,1)
        sen.config(text=str(u1))
        sen.after(1000,count)
    count()
global sen
sen = Label(root,fg='white',bg='black')
sen.pack()

sensor1_read(sen)
root.mainloop()