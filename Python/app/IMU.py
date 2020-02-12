# -*- coding: utf-8 -*-
"""
Serial script for reading and setting heading variable from IMU.

@author: Daniel Wood


"""



import serial



class IMU(object):

    ser = 0

    run_thread = True


    def __init__(self, imu_port):

        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = imu_port
        self.ser.open()

    def reading_the_port(self):
        #parses the individual NMEA sentences and stores them in var
        #$PCHRA,time, roll, pitch,yaw, heading, all in degrees
        nmea_string = self.ser.readline().decode('ascii', errors='replace')
            #print(nmea_string)
        if (nmea_string[0:6] == '$PCHRA'):

            data = nmea_string.split(',')
            print(data)

                self.time = data[1]
                self.roll = data[2]
                self.pitch = data[3]
                self.yaw = data[4]
                self.heading = data[5]
                
        return #self.count,self.time,self.sensor_x,self.sensor_y,self.sensor_x

    def stop(self):
        self.run_thread = False