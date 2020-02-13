from marvelmind import MarvelmindHedge
from time import sleep
import sys
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
