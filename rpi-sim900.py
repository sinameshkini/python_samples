import serial
import os, time

gsm = serial.Serial("/dev/ttyAMA0",baudrate=9600, timeout=1)

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
gsm.write("AT+HTTPPARA=\"URL\",\"http://sajab.sazabgolestan.com/server.php?action=save&station_index=3&ha=2&hb=3&imei=9359374362\"\r\n".encode('ascii'))
time.sleep(1)
gsm.write("AT+HTTPACTION=0\r\n".encode('ascii'))
time.sleep(10)
