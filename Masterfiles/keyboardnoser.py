#import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)#check ports first
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

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
        	break
        elif char == ord('d'):
        	# print doesn't work with curses, use addstr instead
		print('d')
        	#screen.addstr(0, 0, 'right')
		#ser.write('255,0,')
        elif char == ord('a'):
        	screen.addstr(0, 0, 'left ')
		#ser.write('0,255,')       
        elif char == ord('w'):
        	screen.addstr(0, 0, 'up   ')
		#ser.write('255,255,')       
        elif char == ord('s'):
        	screen.addstr(0, 0, 'down ')
		#ser.write('0,0,')
finally:
	# shut down cleanly
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
 