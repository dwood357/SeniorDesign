import time
import os
import argparse
from libraGPS.GPS import GPS
from libraMOTOR.roboteq import roboteq
from libraUltrasonic.Ultrasonic import Ultrasonic
from libraIMU.IMU import IMU
import sys
import threading
import queue

infoStr = """This is the main script for AG Robot Control"""
parser = argparse.ArgumentParser(description=infoStr)
parser.add_argument('--r',
                    '-r',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for right motor serial port')
parser.add_argument('--l',
                    '-l',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for left motor serial port')
parser.add_argument('--gps',
                    '-g',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for GPS serial port')
parser.add_argument('--u',
                    '-u',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for Ultrasonic Sensors serial port')
parser.add_argument('--w',
                    '-w',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for Ultrasonic Sensors serial port')
parser.add_argument('--v',
                    '-v',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for Ultrasonic Sensors serial port')
parser.add_argument('--z',
                    '-z',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for Ultrasonic Sensors serial port')
parser.add_argument('--i',
                    '-i',
                    type=str,
                    default='/dev/ttyUSB',
                    help='dev node for IMU Sensor serial port')
parser.add_argument('--lat',
                    '-la',
                    type=float,
                    default=0.0,
                    help='Hardcoded Position to achieve')
parser.add_argument('--lon',
                    '-lo',
                    type=float,
                    default=0.0,
                    help='Hardcoded Position to achieve')


args = parser.parse_args()


def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))

def foobar():
    input_queue = queue.Queue()

    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    last_update = time.time()
    i = 0
    d=0
    datal = []
    datar = []
    data = []
    while i<10:

        if time.time()-last_update>0.5:
            # sys.stdout.write(".")
            last_update = time.time()
            d=d+1
        if not input_queue.empty():
            
            print ("Left,Right:")#, input_queue.get())
            a = input_queue.get()
            if a != '\n':
            	
            	a.strip()
            	data.append(a)
            # right.strip('\n')
            # a.split(",")
            # a.strip(",")
            # left = a[:0]
            # right = a[:1]
            
            # datal.append(left)
            # datar.append(right)
            	i = i+1
    # print(datal)
    # print(datar)
    print(data)
    print(a)
    print(d)

#Position will be floats in [lat,lon]

target_position = np.array([args.lat,args.lon])

run = True

#Initialize left and right motor

left_motor = roboteq(args.l)
right_motor = roboteq(args.r)

#Initialize the Ultrasonic Sensors
#TODO: figure how the 4 sensors send there info together

# # ultrasonic_1 = Ultrasonic(args.u)
# # ultrasonic_2 = Ultrasonic(args.w)
# # ultrasonic_3 = Ultrasonic(args.v)
# ultrasonic_4 = Ultrasonic(args.z)


#Initialize the IMU

imu = IMU(args.i)


#optionally synces the pi's time with the GPS

if args.gps:

    gps = GPS(args.gps)

    time.sleep(3)

    while (gps.UTC_is_ready() == False) & (gps.date_is_ready() == False):

        time.sleep(0.1)

    #Set the Pi's time given GPS UTC and MM/DD/YYYY

    UTC = gps.get_UTC()

    UTC = [UTC[i:i+2] for i in range(0,len(UTC),2)]

    month,day,year = gps.get_date()

    date_string = str(month+'/'+day+'/'+year+ ' ' + '+' + UTC[0] +':'+ UTC[1] + ':'+ UTC[2])
    # print(date_string)

    UTC = str(UTC[0])+':'+str(UTC[1])+':'+str(UTC[2])

    cmd_date = 'sudo date -s' + date_string
    cmd_time = 'sudo date -s  -utc' + UTC

    os.system(cmd_date)
    os.system(cmd_time)



left_motor.set_MAX_RPM(3100)
left_motor.read_the_port()

right_motor.set_MAX_RPM(3100)
right_motor.read_the_port()

while run:
	# left,right = map(int, input("left,Right: ").split())
	# left_speed = input("Left Speed: ")
	# right_speed = input('Right Speed: ')

	# if left_speed == '':
	# 	continue
	# elif left_speed != '':
	# 	l_speed = left_speed

	# if right_speed == '':
	# 	continue
	# elif right_speed != '':
	# 	r_speed = right_speed
    if speed == 'Full':
    	l_speed = 1000
    	r_speed = 1000
    if speed == 'Half':
    	l_speed = 500
    	r_speed = 500
    if speed == 'Right':
    	l_speed = 700
    	r_speed = 250
    if speed == 'Left':
    	l_speed = 250
    	r_speed = 750
    if speed == 'Tight Left':
    	l_speed = 10
    	r_speed = 750
    if speed == 'Tight Right':
    	l_speed = 750
    	r_speed = 10

	current_lon, current_lat = float(gps.get_position())
	count,time,sensor_x,sensor_y,sensor_x = imu.reading_the_port()
	#check range to see if we should stop
	range_mm_1 = ultrasonic_1.range()
	
	if range_mm_1 == 9999:
		print("No Target Detected")
	else range_mm_1 <= 50:
		print("Range No Longer Accurate")
		run = False
	
	range_mm_2 = ultrasonic_2.range()
	
	if range_mm_2 == 9999:
		print("No Target Detected")
	else range_mm_2 <= 50:
		print("Range No Longer Accurate")
		run = False
	
	range_mm_3 = ultrasonic_3.range()
	
	if range_mm_3 == 9999:
		print("No Target Detected")
	else range_mm_3 <= 50:
		print("Range No Longer Accurate")
		run = False
	
	range_mm_4 = ultrasonic_4.range()
	
	if range_mm_4 == 9999:
		print("No Target Detected")
	else range_mm_4 <= 50:
		print("Range No Longer Accurate")
		run = False


	# # motor.set_acceleration(2500)
	# # motor.read_the_port()

	left_motor.go_to_speed(l_speed)
	left_motor.read_the_port()

	IMU.read_the_port()

	right_motor.go_to_speed(r_speed)
	right_motor.read_the_port()