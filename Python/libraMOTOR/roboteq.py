import serial
# import numpy as np

class roboteq(object):


	ser = 0


	def __init__(self, motor_port):

		self.ser = serial.Serial()
		self.ser.baudrate = 115200
		self.ser.port = motor_port
		self.ser.open()

		

# Pin 2 is output from Motor controller
# Pin 3 is input from MCU
# Pin 5 is Ground

	def send_to_port(self,func):
		
		self.ser.write(func)

		return

	def read_the_port(self):

		return print(self.ser.readline(100))

	def set_acceleration(self, RPM):

		#sets acceleration rate in the form 0.1*RPM based on max RPM
		self.acceleration = "!AC 1 %c"%RPM 

		return self.ser.write(self.acceleration)

	def set_decceleration(self, RPM):

		#sets decceleration rate in the form 0.1*RPM based on max RPM
		self.decceleration = "!AC 1 %c"%RPM 

		return self.ser.write(self.decceleration)

	def save_config(self):
		#saves configuration to the EEPROM
		return self.ser.write("!EES")

	def STOP(self):
		#Software emergency stop
		return self.ser.write("!EX")

	def go_to_speed(self,power):
		#main command for activating the motor
		#accepts a number between -1000 - 1000
		#only used in open loop mode
		self.gts = '!G 1 %d'%power

		return self.ser.write(self.gts)

	def STOP_release(self):
		#releases emergency stop and resumes normal operation
		return self.ser.write("!MG")

	def go_to_position(self,pos):
		#only used in the position count mode, uses the encoder to move to desired position
		self.position = "!P 1 %d"%pos

		return self.ser.write(self.position)

	def go_to_rel_position(self,pos):
		#only used in position count mode
		#moves from current position to a relative position
		self.rel_position = "!PR 1 %d"%pos

		return self.ser.write(self.rel_position)

	def set_motor_speed(self,speed):
		#in closed loop speed mode causes the motor to spin at RPM speed
		#in closed loop position mode sets the RPM but does not start movement
		self.sms = "!S 1 %d"%speed
		#range -500000 to 500000
		return self.ser.write(self.sms)

	def read_motor_amps(self):
		#call this to return the motor amps from controller
		return self.ser.write("?A 1")

	def read_battery_amps(self):
		#call this to return battery amps
		#Amps*10?
		return self.ser.write("?BA 1")

	def read_encoder_count(self):
		#call this to return absolute encoder count
		return self.ser.write("?C 1")

	def read_encoder_relative(self):
		#returns count since last time it was alled
		return self.ser.write("?CR 1")

	def read_fault_flags(self):
		#reports status of controller fault conditions
		#FF = f1 + f2*2 + f3*4+..+fn*2n-1
		"""
		need to convert to binary
		f1 = Overheat
		f2 = Overvoltage
		f3 = Undervoltage
		f4 = short circuit
		f5 = emergency stop
		f6 = dont care
		f7 = MOSFET failed
		f8 = default configuration loaded at startup
		"""
		return self.ser.write("?FF")

	def read_firmware(self):
		#reports firmware and date in string
		return self.ser.write("?FID")

	def read_runtime_flags(self):
		#reports runtime status of each motor
		#FF = f1 + f2*2 + f3*4+..+fn*2n-1
		"""
		need to convert to binary
		f1 = Amps limit currently active
		f2 = motor stalled
		f3 = loop error detected
		f4 = safety switch active
		f5 = Forward limit triggered
		f6 = reverse limit triggered
		f7 = amps trigger activated
		"""
		return self.ser.write("?FM 1")

	def read_status_flags(self):
		#report the state of status flags
		#FF = f1 + f2*2 + f3*4+..+fn*2n-1
		"""
		need to convert to binary
		f1 = Serial Mode
		f2 = Pulse Mode
		f3 = Analog mode
		f4 = power stage off
		f5 = stall detected
		f6 = At limit
		f7 = nothing
		f8 = MicroBasic script runnig
		"""
		return self.ser.write("?FS")
	
	def read_PWM_level(self):
		#reprts the actual PWM level being used
		#1000 = 100% PWM
		return self.ser.write("?P 1")

	def read_temp(self):
		#reports temp in C with on degree resolution
		return self.ser.write("?T 1")

	def set_MAX_RPM(self,max_rpm):
		#sets the max rpm that is used with the acceleration and decelartion
		self.max_rpm = "^MXRPM 1 %d"%max_rpm

		return self.ser.write(self.max_rpm)