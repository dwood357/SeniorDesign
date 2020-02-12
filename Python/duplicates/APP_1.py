from tkinter import *
# from Ultrasonic import Ultrasonic
#from roboteq import roboteq
# from IMU import IMU
# from GPS import GPS
import os
#import RPi.GPIO as GPIO

class App(object):

    def __init__(self,root):
        self.l = 0
        #self.r = 0

        self.root = root
        # self.go_to_position(self,) #Hardcode coordinates to go to
        # self.travel_position(self.ft) #hardcoded ft to move
        
        #self.IMU = IMU('/dev/ttyAMA0')
        #self.left = roboteq('/dev/ttyUSB1')#check these nodes
        #self.right = roboteq('/dev/ttyUSB0')
        """
        self.gps = GPS('/dev/ttyUSB0')

        self.Ultra_left = Ultrasonic('/dev/ttyUSB ')
        self.Ultra_right = Ultrasonic('/dev/ttyUSB ')
        self.Ultra_back_left = Ultrasonic('/dev/ttyUSB ')
        self.Ultra_back_right = Ultrasonic('/dev/ttyUSB ')
        """
        #if self.left:
            #self.left.set_MAX_RPM(2100)#CHANGE
            #self.left.EPPR(Pulses)#change
        
        #if self.right:
            #self.right.set_MAX_RPM(2100)#change
            #self.right.EPPR(Pulses)#change
        """
        if self.gps:

            start_lat, start_lat_dir, start_lon, start_lon_dir = self.gps.get_position()

            time.sleep(3)

            while (self.gps.UTC_is_ready() == False) & (self.gps.date_is_ready() == False):

                time.sleep(0.1)

            #Set the Pi's time given GPS UTC and MM/DD/YYYY

            UTC = self.gps.get_UTC()

            UTC = [UTC[i:i+2] for i in range(0,len(UTC),2)]

            month,day,year = self.gps.get_date()

            date_string = str(month+'/'+day+'/'+year+ ' ' + '+' + UTC[0] +':'+ UTC[1] + ':'+ UTC[2])
            # print(date_string)

            UTC = str(UTC[0])+':'+str(UTC[1])+':'+str(UTC[2])

            cmd_date = 'sudo date -s' + date_string
            cmd_time = 'sudo date -s  -utc' + UTC

            os.system(cmd_date)
            os.system(cmd_time)
"""
    def go_to_position(self,lat,lon):
        #Autonomous Function
        self.start_lat, self.start_lat_dir, self.start_lon, self.start_lon_dir = self.gps.get_position()

        self.overall_distance = self.gps.distance(self.start_lon,self.start_lat,self.lon,self.lat)

        return self.overall_distance[1]

    def distance_to_go(self):
        #distance to given destination, in ft
        self.cur_lat, self.cur_lat_dir, self.cur_lon, self.cur_lon_dir = self.gps.get_position()

        self.dist = self.gps.distance(self.start_lon,self.start_lat,self.cur_lon,self.cur_lat)
        self.dist = self.dist[1]

        self.dist_to_go = self.overall_distance - self.dist

        print("Distance To GO: %f"%self.dist_to_go)

        return self.dist_to_go

    def travel_distance(self,ft):
        return self.ft



    def reading_all_sensors(self):
        
        self.IMU.read_the_port()
        self.gps.get_position()

        self.root.after(1,reading_all_sensors)
    def run_motors(self,l):

        if l != '':
            self.l = l
        #if r != '':
            #self.r = r

    def _print(self):
    	# print("A")
        # self.latitude, self.lat_dir, self.longitude, self.long_dir = self.gps.get_position()
        # self.RPM_L = self.left.read_encoder_RPM()
        # self.RPM_R = self.right.read_encoder_RPM()
        #Check the distance to go
        """
        D = self.distance_to_go()
        if D == 0:
            self.stop()
        else:
            continue
        #set the speed 
        """
        # self.left.go_to_speed(self.l)
        #self.right.go_to_speed(self.r)
        
        #Read the Sensors
        """
        self.IMU.reading_the_port()

        self.Ultra_left.range()
        self.Ultra_right.range()
        self.Ultra_back_left.range()
        self.Ultra_back_right.range()
        """
        print(20)

        self.root.after(10,app._print)

    def stop(self):
        self.left.STOP()
        self.right.STOP()


def speed(entries):
    i = 0
    speed = []
    for entry in entries:
        field = entry[0]
        speed = entry[1].get()
        speed = int(speed)
        print('%s: "%s"' % (field, speed))
        if i == 0:
            left = speed
        if i == 1:
            right = speed
        i = i +1


    # print(speed)
    # app.run_motors(left)
    
    left_amp['text'] = 'Left AMPS: ' + str(left) #left.read_motor_amps()
    right_amp['text'] = 'Right AMPS: ' + str(right)#right.read_motor_amps()
    print(type(speed))
    return left,right

def down():
    print(2)
    #trigger solenoid pin to incrementally tilt main arm down
    # GPIO.output(16, GPIO.HIGH)
    # GPIO.output(18, GPIO.HIGH)
    # time.sleep(sleep_time)
    # GPIO.output(16, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)

def up():
    print(1)
    #trigger motor pin to incrementally tilt main arm up
    # GPIO.output(13, GPIO.HIGH)
    # GPIO.output(18, GPIO.HIGH)
    # time.sleep(sleep_time)
    # GPIO.output(13, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)

def tilt_down():
    print(3)
    #Trigger solenoid pin to incrementally tilt down
    # GPIO.output(11, GPIO.HIGH)
    # GPIO.output(18, GPIO.HIGH)
    # time.sleep(sleep_time)
    # GPIO.output(11, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)

def tilt_up():
    print(4)
    #Trigger solenoid pin to incrementally title up
    # GPIO.output(12, GPIO.HIGH)
    # GPIO.output(18, GPIO.HIGH)
    # time.sleep(sleep_time)
    # GPIO.output(12, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)

def hydraulic_motor():
    print(5)
    # GPIO.output(18, GPIO.HIGH)
    # time.sleep(sleep_time)
    # GPIO.output(18, GPIO.LOW)


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width = 15, text = field, anchor = 'w')
        ent = Entry(row)
        row.pack(side=TOP, fill = X, padx = 10, pady = 10)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand = YES, fill = X)
        entries.append((field, ent))
    return entries

# GPIO.setup(12, GPIO.OUT)# Tilt Up
# GPIO.setup(11, GPIO.OUT)# Tilt Down
# GPIO.setup(13, GPIO.OUT)#ARM UP
# GPIO.setup(16, GPIO.OUT)#ARM Down
# GPIO.setup(18, GPIO.OUT)#Motor On

sleep_time = 2

fields = 'Left', 'Right'

root = Tk()
app = App(root)



ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: speed(e)))

b1 = Button(root, text = 'UP',
            command = (lambda e=ents: up()))
b1.pack(side=LEFT, padx=5, pady = 5)

b2 = Button(root, text = 'DOWN',
            command = (lambda e=ents: down()))
b2.pack(side=LEFT, padx = 5, pady = 5)

b3 = Button(root, text = 'Tilt Forward',
            command = (lambda e=ents: tilt_up()))
b3.pack(side=LEFT, padx = 5, pady = 5)

b4 = Button(root, text = 'Tilt Backwards',
            command = (lambda e=ents: tilt_down()))
b4.pack(side=LEFT, padx=5, pady=5)

b5 = Button(root, text = 'Quit', command = root.quit)
b5.pack(side=LEFT, padx = 5, pady = 5)
left = 0
right = 0


left_amp = Label(root, text = 'Left AMPS:')
left_amp.pack(side = TOP)

right_amp = Label(root, text = 'Right AMPS:')
right_amp.pack(side = TOP)


app._print()
root.mainloop()

