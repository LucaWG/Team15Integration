import serial
ser = serial.Serial('/dev/ttyACM0', 9600)#check at the start of each time
# ser.write('20,129,')# example

from marvelmind import MarvelmindHedge
from time import sleep
import sys
import math

import matplotlib.pyplot as plt # for plotting

import curses # for keyboard inputs 
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
cnt = 1 # determine if its manual or auto
char = "e" # stop just in case for initial
raww = 'y'

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
influ = 4 # beeeg boi # also good
bigang = 45
angleoff = 0
buffer = .7;
steps = .5 # .5 is good
stepsOG = steps
iterat = 0;#place in way point vector
wpx = [8.5, 5.9, 2.6, 5.2]
wpy = [-1.5, -3.8, .7, 3]

num = 60 # plot vars
xvals = [None] * num
yvals =[None] * num
xb = [0,7.14,10.91,3.9, 0]
yb = [0, 4.755, 0, -5.846,0]
counting = 0
GO = True

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
		try:
			char = screen.getch()
			if char == ord('y'):
				cnt = cnt + 1
				if cnt%2 == 1:
					screen.addstr(0, 0, 'st auto   ')
				else:
					screen.addstr(0, 0, 'st manu   ')
			if  cnt%2 == 0:
				steps = .5
			        if char == ord('q'):
			       		break
			        elif char == ord('d'): # right
			        	# print doesn't work with curses, use addstr instead
					#print('d')
			        	screen.addstr(0, 0, 'right    ')
					ser.write('255,0,')
			        elif char == ord('a'): # left
			        	screen.addstr(0, 0, 'left     ')
					ser.write('0,255,')       
		        	elif char == ord('w'): # forwards
		        		screen.addstr(0, 0, 'forwards  ')
					ser.write('255,255,')       
		        	elif char == ord('s'): # backwards
		        		screen.addstr(0, 0, 'backwards ')
					ser.write('-255,-255,')
				elif char == ord('e'): # stop
					screen.addstr(0, 0, 'stop     ')
					ser.write('0,0,')
			else:	
				screen.addstr(0, 0, 'now auto   ')
				steps = stepsOG
				cnt = 1
		except KeyboardInterrupt:
			
			sleep(steps)
			x1 = x2
			y1 = y2
			# print (hedge.position()) # get last position and print
	            	pos = hedge.position()
			#print("X: " + str(pos[1])+"\n")
			#print("Y: " + str(pos[2])+"\n")
			#print("Z: " + str(pos[3]))
			#print("wpx: " + str(wpx[iterat]))
			#print("wpy: " + str(wpy[iterat]))
			# print("Time: " +str(pos[4]))
			# print(" ")
	
			x2 = pos[1] # new pos
			y2 = pos[2]
			x3 = wpx[iterat] # destination
			y3 = wpy[iterat]
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
				iterat = iterat + 1
				if(cnt % 2 == 1):
					if iterat == 4:
						iterat = 0
						ser.write("0,0,0,")
						sleep(5)
					ser.write("0,0,0")
					sleep(1)
					print("there! turn right please.")
					ser.write('255,0,')
					sleep(1.9)
					ser.write('0,0,')
					sleep(1)
					ser.write("255,255,")
					sleep(2)
	
				else: # if manual dont turn automatically
					if iterat == 4:
						iterat = 0
					
			if (angleoff > 0) and cnt % 2 == 1:
				left = 255 # - angleoff * influ; # see if sin(theta) is better as well
				right = 255 - angleoff * influ;
				print(str(left)+" " +str(right))
				op = str(left) + "," + str(right) + ","
				ser.write(op)
			if angleoff < 0  and cnt % 2 == 1:
				left = 255 + angleoff * influ;
				right = 255# + angleoff * influ;
				print(str(left)+" " +str(right))
				op = str(left) + "," + str(right) + ","
				ser.write(op)
			#print(" theta: " +str(angleoff))
			#print(" ")
			# print("theta2: " +str(tpf1))
			# print("theta2: " +str(tpf2))
	
			counting = counting + 1
			
			

        except KeyboardInterrupt:
		curses.nocbreak();
		screen.keypad(0)
		curses.echo()
		curses.endwin()
		hedge.stop()  # stop and close serial port
		sys.exit() 
