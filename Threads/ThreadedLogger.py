import datetime
import threading
import os
from getkey import getkey, keys
#Todo clear the 'buff' so that we don't use a redicoulus amount of data

#Global buffer
buff = ""
shutdown = False

#This functions purely takes in the keys
def _LogKeys_():
    global shutdown
    global buff
    while not shutdown:
        key = getkey()
        #Special rules for specific keys
        if key == keys.ESCAPE:
            shutdown = True
            break
        elif key == keys.ENTER:
            buff += "\n"
            print(buff)
        elif key == keys.BACKSPACE:
            buff = buff[:-1]
        else:
            buff += key


def _OutBuffer_():
    global shutdown
    hasPrinted = False
    while not shutdown:
        timeStart = datetime.datetime.now()
        if ((timeStart.second % 10) == 0 and not hasPrinted):
            file = open("myFile.txt", "w")
            hasPrinted = True
            os.system("clear")
            print(str(timeStart) + " -- " + buff)
            file.write(buff)
            file.close()
        if ((timeStart.second % 10) == 1 and hasPrinted):
            hasPrinted = False

outBufThread = threading.Thread(target=_OutBuffer_)
outBufThread.start()
_LogKeys_()
outBufThread.join()
