# -*- coding: utf-8 -*-
"""
Script with all functions that roboteq can receive or send over serial.

@author: Daniel Wood


"""


import serial
# import numpy as np

class roboteq(object):


    ser = 0


    def __init__(self, motor_port):

        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = motor_port
        self.ser.timeout = 0.1
        self.ser.open()



    def send_to_port(self,func):
        
        self.ser.write(func)

        return

    def read_the_port(self):

        print(self.ser.readline().decode('ascii',errors='replace'))
        return

    def set_acceleration(self, RPM):

        #sets acceleration rate in the form 0.1*RPM based on max RPM
        self.acceleration = "!AC 1 %c"%RPM 

        return self.ser.write(b'!AC 1 %c\r'%RPM)

    def set_decceleration(self, RPM):

        #sets decceleration rate in the form 0.1*RPM based on max RPM
        # self.decceleration = "!AC 1 %c"%RPM 

        return self.ser.write(b"!AC 1 %c\r"%RPM)

    def save_config(self):
        #saves configuration to the EEPROM
        # string = "!EES"
        return self.ser.write(b"!EES\r")

    def STOP(self):
        #Software emergency stop
        # string = "!EX"
        return self.ser.write(b"!EX\r")

    def go_to_speed(self,power):
        #main command for activating the motor
        #accepts a number between -1000 - 1000
        #only used in open loop mode
        # self.gts = '!G 1 %d'%power

        return self.ser.write(b'!G 1 %d\r'%power)

    def STOP_release(self):
        #releases emergency stop and resumes normal operation
        # string = "!MG"
        return self.ser.write(b"!MG\r")

    def go_to_position(self,pos):
        #only used in the position count mode, uses the encoder to move to desired position
        # self.position = "!P 1 %d"%pos

        return self.ser.write(b"!P 1 %d\r"%pos)

    def go_to_rel_position(self,pos):
        #only used in position count mode
        #moves from current position to a relative position
        # self.rel_position = "!PR 1 %d"%pos

        return self.ser.write(b"!PR 1 %d\r"%pos)

    def set_motor_speed(self,speed):
        #in closed loop speed mode causes the motor to spin at RPM speed
        #in closed loop position mode sets the RPM but does not start movement
        # self.sms = "!S 1 %d"%speed
        #range -500000 to 500000
        return self.ser.write(b"!S 1 %d\r"%speed)

    def read_motor_amps(self):
        #call this to return the motor amps from controller
        # string = "?A 1"
        return self.ser.write(b"?A 1\r")

    def read_battery_amps(self):
        #call this to return battery amps
        #Amps*10?
        # string = "?BA 1"
        return self.ser.write(b"?BA 1\r")

    def read_encoder_count(self):
        #call this to return absolute encoder count
        # string = "?C 1"
        return self.ser.write(b"?C 1\r")

    def read_encoder_relative(self):
        #returns count since last time it was alled
        # string = "?CR 1"
        return self.ser.write(b"?CR 1\r")

    def read_Encoder_RPM(self):
    	#main query for RPM, will do negative numbers
    	print(self.ser.write(b"?S 1\r"))
    	
    	return
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
        # string = "?FF"
        return self.ser.write(b"?FF\r")

    def read_firmware(self):
        #reports firmware and date in string
        # string = b"?FID\r"

        return self.ser.write(b"?FID\r")

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
        # string = "?FM 1"
        return self.ser.write(b"?FM 1\r")

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
        # string = "?FS"
        return self.ser.write(b"?FS\r")
    
    def read_PWM_level(self):
        #reprts the actual PWM level being used
        #1000 = 100% PWM
        # string = "?P 1"
        return self.ser.write(b"?P 1\r")

    def read_temp(self):
        #reports temp in C with on degree resolution
        # string = "?T 1"
        return self.ser.write(b"?T 1\r")

    def set_MAX_RPM(self,max_rpm):
        #sets the max rpm that is used with the acceleration and decelartion
        # self.max_rpm = "^MXRPM 1 %d"%max_rpm

        return self.ser.write(b"^MXRPM 1 %d\r"%max_rpm)

    def EPPR(self,PPR):

    	#sets the configuration for Pulses per revolution
    	#has to be used to get an encoder feedback
    	return self.ser.write(b"^EPPR 1 %d\r"%PPR)