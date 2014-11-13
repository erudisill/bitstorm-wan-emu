import time
import threading
from menu_main import Menu_Main

class CpConsole(threading.Thread):
    
    menus = []
    
    def __init__(self, *args):
        self._target = self.console_handler
        self._args = args
        self.__lock = threading.Lock()      
        self.closing = False # A flag to indicate thread shutdown
        
        self.menu_current = 0 # Main menu
        
        threading.Thread.__init__(self)
        
    def run(self):
        self._target(*self._args)
    
    def shutdown_thread(self):
        print 'shutting down CpConsole...'

        self.__lock.acquire()
        self.closing = True
        self.__lock.release()
        
    def menu_init(self):
        self.menus = [ Menu_Main() ]
           
    def menu_display(self):
        print
        self.menus[self.menu_current].display()
        print "?) Redisplay menu"
        print "X) Exit"
        print
           
    def console_handler(self):
        
        print "\n============================================"
        print "cpserial - Spike for BitStorm ZB development"
        print "============================================"

        self.menu_init()
        self.menu_display()
                
        while not self.closing:
            # get keyboard input
            input = raw_input(">> ")
            if input == 'exit' or input == 'EXIT' or input == 'X' or input == 'x':
                self.shutdown_thread()
            elif input == '?':
                self.menu_display()
            else:
                self.menus[self.menu_current].handle(input)

            time.sleep(.0001)