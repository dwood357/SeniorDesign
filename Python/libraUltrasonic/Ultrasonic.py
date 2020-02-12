import serial


class Ultrasonic(object):

    ser = 0
    range_mm = 0
    run_thread = True
    
    def __init__(self, ultrasonic_port):

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = ultrasonic_port
        self.ser.timeout = 0.1
        self.ser.rts(True)
        self.ser.open()

    def range(self):
        # starts with R followed by range in mm
        #returns the range in mm as a float
        self.read_the_port(self)
        
        return self.range_mm

    def read_the_port(self):

        self.range_mm = self.ser.readline().decode('ascii', errors='replace')
        print(self.range_mm)
        if (self.range_mm[0] == 'R'):

            spl = self.range_mm.split('R')
            self.range_mm = float(spl[1])
            print(self.range_mm)

        return self.range_mm