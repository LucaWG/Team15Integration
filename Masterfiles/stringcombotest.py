import serial
ser = serial.Serial('/dev/ttyACM2', 9600)

A = 128
B = 75
op = str(A) + "," +str(B) + ","

print(op)
 
ser.write(op)
