import time
import serial
from shared import Shared
from cpconsole import CpConsole


if __name__ == '__main__':
    
    Shared.theSerial = serial.Serial()
    
    consoleThread = CpConsole()
    consoleThread.start()
    
    while(consoleThread.isAlive()):
        time.sleep(.005)

    print 'Exiting App...'
    
    if Shared.theSerial.isOpen():
        print 'Closing serial...'
        Shared.theSerial.close()
    
    exit()
    
    


    
