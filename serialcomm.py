import sys
import glob
import serial

def sendAT(port, cmd, waitForReply=False):
    out='';prev='x'
    try:
        s = serial.Serial(port, baudrate=115200, timeout=0.5)
        s.write(('AT '+cmd+'\r').encode());
        if waitForReply == True:
            while prev != out:
                prev=out
                out+= str((s.read(1)).decode('UTF-8'))        

        s.close()
    except (OSError, serial.SerialException):
        pass
    return (out)
            
def openFMPort():
    """ tries to open the first serial port where a FlipMouse is connected

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            the serial port (or None is case no FlipMouse was found)
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    #result = []
    for port in ports:
        try:
            reply=sendAT(port,'ID',True)
            # print (" got reply from "+ port +":"+reply)
            if "FLipmouse" in reply:
                return port
        except (OSError, serial.SerialException):
            pass
    return None
