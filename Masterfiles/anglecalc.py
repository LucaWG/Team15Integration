import math

def theta(vect):
	ins = 0
	ins2 = 0
	ins = (vect[2]-vect[0])
	ins2 = (vect[3]-vect[1])
	denom = math.pow((ins),2) + math.pow((ins2),2)
	if denom == 0:
		denom = 0.0001 #prevent divide by zero
	denom = math.sqrt(denom)
	thet = math.degrees(math.acos(ins/denom))# returns it in radians
	return thet

x1 = 5.122
y1 = 3.241
x2 = 5.278
y2 = 2.979
x3 = 8.7
y3 = -1.5

v1 = [x1,y1,x2,y2]
v2 = [x2,y2,x3,y3]

theta1 = theta(v1)
theta2 = theta(v2)
theta3 = theta1 - theta2
print(str(theta3))