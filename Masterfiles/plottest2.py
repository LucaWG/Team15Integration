from marvelmind import MarvelmindHedge
from time import sleep
import sys
import matplotlib.pyplot as plt

x1 = 0
y1 = 0
x2 = 1
y2 = 1
num = 40
xvals = [None] * num
yvals =[None] * num
xb = [0,7.14,10.91,3.9, 0]
yb = [0, 4.755, 0, -5.846,0]
counting = 0
GO = True

hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread
while GO:
	try:
		x1 = x2
		y1 = y2
		sleep(.5)
		# print (hedge.position()) # get last position and print
            	pos = hedge.position()
		print("X: " + str(pos[1]))
		print("Y: " + str(pos[2]))
		print("Z: " + str(pos[3]))
		print("Time: " +str(pos[4]))
		print(" ")
		x2 = pos[1]
		y2 = pos[2]
		xs = [x1, x2]
		ys = [y1, y2]
		xvals[counting] = x2
		yvals[counting] = y2
		if counting == (num-1):
			plt.plot(xvals,yvals, label = "current vel. vector")
			plt.plot(xb,yb)
			plt.show()
			GO = False
			
		counting = counting + 1
		
		
		

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit() 

