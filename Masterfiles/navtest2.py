import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('20,129,')

from marvelmind import MarvelmindHedge
from time import sleep
import sys
import math

x1 = 0;
x2 = 0;
y1 = 0;
y2 = 0;
vector1 = [0, 0, 0, 0]#x1,y1,x2,y2
vector2 = [0, 0, 0, 0]
vector3 =[4,2,5,6]#x5,y5
theta1 = 0
theta2 = 0
denom = 0
inside = 0
inside2 = 0
num = 0

def theta(vect):
	ins = 0
	ins2 = 0
	ins = (vect[2]-vect[0])
	ins2 = (vect[3]-vect[1])
	denom = math.pow((ins),2) + math.pow((ins2),2)
	denom = math.sqrt(denom)
	thet = math.acos(ins/denom)
	return thet

hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread
while True:
	try:
		sleep(1)
		x1 = x2
		y1 = y2
		# print (hedge.position()) # get last position and print
            	pos = hedge.position()
		# print("X: " + str(pos[1]))
		# print("Y: " + str(pos[2]))
		# print("Z: " + str(pos[3]))
		# print("Time: " +str(pos[4]))
		# print(" ")
		x2 = pos[1]
		y2 = pos[2]
		x1 = 4
		y1 = 2
		x2 = 3
		y2 = 4
		vector1 = [x1, y1, x2, y2]
		vector2 = [x1, y1, x1+1, y1]
		theta1 = theta(vector3)
		theta2 = theta(vector1)
		print("theta: " +str(theta1))
		print("theta2: " +str(theta2))
		
		

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit() 
