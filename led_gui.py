from Tkinter import *
import RPi.FPIO as GPIO

LED = 40
def LED_ON():
    global LED
    GPIO.output(LED,GPIO.HIGH)
    print "ON"

def LED_OFF():
    global LED
    GPIO.output(LED,GPIO.LOW)
    print "OFF"


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)

root = Tk()

buttonon = Button(root,text="ON",width=25,cammand=LED_ON)
buttonon.pack(side = "left")
buttonoff = Button(root,text="OFF",width=25,cammand=LED_OFF)
buttonoff.pack(side = "right")
root.mainloop()
