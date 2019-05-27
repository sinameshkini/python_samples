import serial
import os, time

port = serial.Serial("/dev/ttyUSB0",baudrate=115200, timeout=1)

port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CGATT=1'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+HTTPINIT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(2)

port.write('AT+HTTPPARA=\"URL\",\"http://sajab.sazabgolestan.com/server.php?action=save&station_index=3&ha=2&hb=3&imei=9359374362'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+HTTPACTION=0'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(6)

port.write('AT+HTTPREAD'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(2)

port.write('AT+HTTPREAD'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(2)
