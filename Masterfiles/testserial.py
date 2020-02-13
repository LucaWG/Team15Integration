from time import sleep
import sys
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('255,0,')
sleep(1.9)
ser.write('0,0,')