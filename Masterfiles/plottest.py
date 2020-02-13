from marvelmind import MarvelmindHedge
from time import sleep
import sys
import matplotlib.pyplot as plt

x1 = 0
y1 = 0
x2 = 1
y2 = 1


hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread
while True:
	try:
		x1 = x2
		y1 = y2
		sleep(1)
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
		plt.plot(xs,ys, label = "current vel. vector")
		plt.show()

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit() 
