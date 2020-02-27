from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68) #making a sensor object using imported library

while (True):
	accelerometer_data = sensor.get_accel_data()#infinite while loop get accelerometer/gyro data
	gyroscope_data = sensor.get_gyro_data()
	print("acceleration data")
	print(accelerometer_data)
	print("gyro data")
	print(gyroscope_data)
	time.sleep(.5)

