import serial
ser = serial.Serial('/dev/ttyACM0', 9600)#check at the start of each time
# ser.write('20,129,')# example

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
influ = 4 # beeeg boi
counting = 0
bigang = 45
angleoff = 0
buffer = .7;

def theta(vect):
	ins = 0
	ins2 = 0
	ins = (vect[2]-vect[0])
	ins2 = (vect[3]-vect[1])
	denom = math.pow((ins),2) + math.pow((ins2),2)
	if denom == 0:
		denom = 0.0001 #prevent divide by zero
	denom = math.sqrt(denom)
	thet = math.acos(ins/denom)# returns it in radians
	return thet

hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread


left = 255 # see if sin(theta) is better as well
right = 255
op = str(left) + "," + str(right) + ","
ser.write(op)


while True:
	try:
		sleep(2)
		x1 = x2
		y1 = y2
		# print (hedge.position()) # get last position and print
            	pos = hedge.position()
		print("X: " + str(pos[1]))
		print("Y: " + str(pos[2]))
		print("Z: " + str(pos[3]))
		# print("Time: " +str(pos[4]))
		# print(" ")

		x2 = pos[1] # new pos
		y2 = pos[2]
		x3 = 8.5 # destination
		y3 = -1.6
		vector1 = [x2, y2, x3, y3] # goal vector
		vector2 = [x1, y1, x2, y2] # current velocity vector
		theta1 = theta(vector1)
		theta2 = theta(vector2)
		tpf1 = theta1 * 57.29577951
		tpf2 = theta2 * 57.29577951 # now in degrees
		
		if abs(tpf1-tpf2) < bigang:
			angleoff = tpf1 - tpf2
			#if angleoff > 80
		
		#angleoff = tpf1 - tpf2 # pos is to the right, neg is to the left of goal based on direction
		if((x3 + buffer) > x2 > (x3 - buffer)) and ((y3 + buffer) > y2 > (y3 - buffer)):
			angleoff = 0;
			ser.write("0,0,0")
			print("there! turn right please.")
			sleep(10)
		if angleoff > 0:
			left = 255 # - angleoff * influ; # see if sin(theta) is better as well
			right = 255 - angleoff * influ;
			print(str(left)+" " +str(right))
			op = str(left) + "," + str(right) + ","
			ser.write(op)
		if angleoff < 0:
			left = 255 + angleoff * influ;
			right = 255# + angleoff * influ;
			print(str(left)+" " +str(right))
			op = str(left) + "," + str(right) + ","
			ser.write(op)
		print(" theta: " +str(angleoff))
		print(" ")
		# print("theta2: " +str(tpf1))
		# print("theta2: " +str(tpf2))
		#counting++
		
		

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit() 
