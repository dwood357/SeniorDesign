from roboteq import roboteq
import serial 
from Ultrasonic import Ultrasonic
import time


motor = roboteq('COM7')

motor.read_firmware()

motor.set_MAX_RPM(3100)

while True:

	motor.go_to_speed(500)

