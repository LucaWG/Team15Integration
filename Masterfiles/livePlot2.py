from marvelmind import MarvelmindHedge
from time import sleep
import sys
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

# Create Figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
xOut = [5.08, 9.3, 5.8, 1.6, 5.08]
yOut = [3.74, -1.6, -4.3, .73, 3.74]
xIn = [4.98, 8, 5.9, 2.7, 4.98]
yIn = [2.29, -1.5, -3.37, 0.58,2.29]
wpn = 4 # num of waypoints
wpx = [8.5, 5.9, 2.6, 5.2]
wpy = [-1.5, -3.8, .7, 3]
buffer = .3;

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(buffer)

#x1 = wpx[0]+r*np.cos(theta)
#x2 = wpy[0]+r*np.sin(theta)

hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=15, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread

def animate(i,xs, ys):
	pos = hedge.position()
	xs.append(pos[1])
	ys.append(pos[2])

	ax.clear() 
	axes = plt.gca() 
	axes.set_xlim([0,10]) 
	#axes.set_ylim([-7, 7])
	for i in range(wpn):
		x1 = wpx[i]+r*np.cos(theta)
		x2 = wpy[i]+r*np.sin(theta)
		ax.plot(x1, x2)
	ax.plot(xOut,yOut)
	ax.plot(xIn,yIn)
	ax.plot(xs, ys) 

def main():

    while True:
        try:
            sleep(1)
            # print (hedge.position()) # get last position and print
            ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
            plt.show()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()
