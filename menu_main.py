from config import Config
from shared import Shared

class Menu_Main:
    
    def init_serial(self):
        print "[init serial on port %s, %s timeout:%s]" % (Config.port , Config.baudrate, Config.timeout)
        Shared.theSerial.port = Config.port
        Shared.theSerial.baudrate = Config.baudrate
        Shared.theSerial.timeout = Config.timeout
        Shared.theSerial.open()
    
    def safe_init(self):
        if Shared.theSerial.isOpen() == True:
            return
        self.init_serial()
    
    def read_n(self, size):
        self.safe_init()
        data = Shared.theSerial.read(size)
        print "[RCV] %s" % data        
    
    def send_standard(self):
        self.safe_init()
        Shared.theSerial.flushInput()
        Shared.theSerial.write(bytearray([0x04, 0x01, 0x02, 0x03, 'X']))
        self.read_n(4)
          
    def display(self):
        print "Main Menu - 0"
        print "-------------"
        print "1) Send standard test bytes [0x04 0x01 0x02 0x03 0x04]"
        print "2) Read 4 bytes"
        print "S) Initialize serial"
        
    def handle(self, input):
        if input == "1":
            self.send_standard()
        elif input == "2":
            self.read_n(4)
        elif input == 'S' or input == 's':
            self.init_serial()
        else:
            print "[invalid selection]"