import serial
ser = serial.Serial('/dev/ttyACM0', 9600)#check ports first
# ser.write('20,129,') #example

import curses
 
# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
cnt = 0

try:	
    while True:
        char = screen.getch()
	if char == ord('y'):
		cnt = cnt + 1
		if cnt%2 == 1:
			screen.addstr(0, 0, 'st auto   ')
		else:
			screen.addstr(0, 0, 'st manu   ')
	if  cnt%2 == 0:
	        if char == ord('q'):
	        	break
	        elif char == ord('d'): # right
	        	# print doesn't work with curses, use addstr instead
			#print('d')
	        	screen.addstr(0, 0, "right    ")
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
finally:
	# shut down cleanly
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
 