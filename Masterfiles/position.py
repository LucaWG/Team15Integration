from marvelmind import MarvelmindHedge
from time import sleep
import sys


hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread
while True:
	try:
		sleep(1)
		# print (hedge.position()) # get last position and print
            	pos = hedge.position()
		print("X: " + str(pos[1]))
		print("Y: " + str(pos[2]))
		print("Z: " + str(pos[3]))
		print("Time: " +str(pos[4]))
		print(" ")

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit() 
