import serial
import threading
import numpy as np
import time
import math


class GPS(object):

    
    ser = 0
    date_data = 0
    UTC = 0
    longitude = 0
    long_dir = 0
    latitude = 0
    lat_dir = 0
    Speed = 0
    day = 0
    month = 0
    year = 0
    run_thread = True


    def __init__(self, gps_port):

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = gps_port
        self.ser.open()
        #nmea_string = self.ser.readline().decode('ascii', errors='replace')
        #print(nmea_string)
        self.GPS_Serial_Thread = threading.Thread(target=self.reading_the_port)
        self.GPS_Serial_Thread.start()
    
    def UTC_is_ready(self):
        #waits until UTC is an actual value
        UTC = self.UTC

        return UTC != 0 

    def date_is_ready(self):
        #waits until date is an actual value

        day_data = self.day
        
        return day_data != 0

    def get_UTC(self):
        #Returns UTC as a str
        UTC = str(self.UTC)

        return UTC

    def get_date(self):
        #Returns date as a str
        month = str(self.month)
        day = str(self.day)
        year = str(self.year)

        return month,day,year

    def speed(self):
        
        speed = self.speed

        return speed

    def get_position(self):
        #returns an array wit numbers used to calc distance traveled in other function
        lon = self.longitude 
        lat = self.latitude

        return lon, lat


    def distance(self,lon1,lat1,lon2,lat2):

        lon1 = lon1/100
        lat1 = lat1/100
        lon2 = lon2/100
        lat2 = lat2/100

        #convert to radians
        lon1,lat1,lon2,lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        #haversine distance formula
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        #radians

        c = 2*atan2(sqrt(a), sqrt(1-a))

        # c = 2 * asin(sqrt(a)) 
        #kilometers
        km = 6367 * c
        #ft
        ft = km*3280.84
        
        # distance = km*1000 #change to m        

        return km,ft


    def reading_the_port(self):
        #parses the individual NMEA sentences and stores them in var
        print('Hello GPS thread')

        f = open('nmea_sentences.txt', 'w+')

        while self.run_thread:

            nmea_string = self.ser.readline().decode('ascii', errors='replace')
            #print(nmea_string)

            if (nmea_string[0:6] == '$GNRMC'):

                data = nmea_string.split(',')
                print(data)

                self.UTC = data[1]
                self.latitude = data[3]
                self.lat_dir = data[4]
                self.longitude = data[5]
                self.long_dir = data[6]
                self.Speed = data[7]
                self.date = data[9]
                
                #Parses date to put in individual variables for passing to raspberry pi
                date = str(date)
                date = [date[i:i+2] for i in range(0,len(date),2)]

                self.day = date[0]
                self.month = date[1]
                self.year = '20' + date[2]

                self.date_data = np.array([self.UTC, self.month, self.day, self.year])
                self.str_data = np.array([self.UTC, self.latitude, self.lat_dir, self.longitude, self.long_dir, self.Speed, self.day, self.month, self.year])

                # print(str(self.str_data))

                f.write(str(self.str_data))
                f.write('\n')
                f.flush()

        f.close()

    def stop(self):
        self.run_thread = False