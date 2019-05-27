import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT) #Relay 1
GPIO.setup(33,GPIO.OUT) #Relay 2
GPIO.setup(35,GPIO.OUT) #Relay 3
GPIO.setup(37,GPIO.OUT) #Relay 4

GPIO.setup(31,GPIO.IN) #Relay 1
GPIO.setup(33,GPIO.IN) #Relay 2
GPIO.setup(35,GPIO.IN) #Relay 3
GPIO.setup(37,GPIO.IN) #Relay 4
global relay1_status = GPIO.input(31)
global relay2_status = GPIO.input(33)
global relay3_status = GPIO.input(35)
global relay4_status = GPIO.input(37)

print(relay1_status)
print(relay2_status)
print(relay3_status)
print(relay4_status)
