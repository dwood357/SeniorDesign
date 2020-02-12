# -*- coding: utf-8 -*-
"""
Serial script for reading the ultrasonic sensors, returns the distance in mm.

@author: Daniel Wood


"""


import serial
import time

class Ultrasonic(object):

    ser = 0
    range_mm = 0
    run_thread = True
    mm = 0

    def __init__(self, ultrasonic_port):

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = ultrasonic_port
        self.ser.timeout = 0.5
        # self.ser.rts = False
        # self.ser.dtr = False
        self.ser.open()

    def range(self):
        # starts with R followed by range in mm
        #returns the range in mm as a float
        self.read_the_port(self)
        
        return self.mm

    def read_the_port(self):

        # self.range_mm = self.ser.readline(5).decode('utf-8', errors='replace')
        bytesToRead = self.ser.inWaiting()
        data = self.ser.read(bytesToRead)

        if data.startswith(b'R'):
            sensorData = data.decode('utf-8').lstrip('R')
            print(sensorData)

        print(self.range_mm)
        # if (self.range_mm[0] == 'R'):

        #     spl = self.range_mm.split('R')
        #     self.range_mm = float(spl[1])
        #     print(self.range_mm)

        return self.range_mm

    def measure(self):

        timeStart = time.time()
        valueCount = 0

        while time.time() < timeStart + 3:
            #if self.ser.in_waiting:
                #bytesToRead = self.ser.in_waiting
            bytesToRead = 5
            valueCount += 1
            if valueCount < 2: # 1st reading may be partial number; throw it out
                continue
            testData = self.ser.read(bytesToRead)
            if not testData.startswith(b'R'):
                # data received did not start with R
                continue
            try:
                sensorData = testData.decode('utf-8').lstrip('R')
            except UnicodeDecodeError:
                # data received could not be decoded properly
                continue
            try:
                mm = int(sensorData)
            except ValueError:
                # value is not a number
                continue
            # self.ser.close()
            return print(self.mm)

        # ser.close()
        raise RuntimeError("Expected serial data not received")