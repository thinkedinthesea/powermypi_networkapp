#
# POWERMYPINETWORKAPP 
#
#
#THINKEDINTHESEA
#
#release 1.0
#090119
import time
from socket import *
import os
import logging
from errno import ENETUNREACH
import sys
#
time.sleep(15)
logging.basicConfig(filename="/home/pi/powermypi_networkapp/log",level=logging.DEBUG,format="%(asctime)s %(message)s")
logging.debug("Application Started")
#
myPort=1234
try:
    s=socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
except IOError as e:
    if e.errno == ENETUNREACH:
        logging.debug("Network Error. Quitting...")
        sys.exit(0)
#
ip_address = s.getsockname()[0]
#print(ip_address)
logging.debug("Network IP:"+ip_address+" Port:"+str(myPort))
ss = socket(AF_INET, SOCK_STREAM)
ss.bind((ip_address, myPort))
ss.listen(5)
#
stringOut="Hello World!!!"
while True:
    connection, address=ss.accept()
    data=connection.recv(10)
    if data:
        stri=data.decode("utf-8")
        if (stri=="POWER\n"):
            os.system("sudo poweroff")
            break
        if (stri=="REBOOT\n"):
            os.system("sudo reboot")
            break
        if (stri=="COMMAND1\n"):
            logging.debug("COMMAND1")
            #add your command here
        if (stri=="COMMAND2\n"):
            logging.debug("COMMAND2")
            #add your command here
        if (stri=="COMMAND3\n"):
            logging.debug("COMMAND3")
            #add your command here
        if (stri=="COMMAND4\n"):
            logging.debug("COMMAND4")
            #add your command here
        if (stri=="INFO\n"):
            print("INFO")
            connection.sendall(stringOut.encode())
    time.sleep(0.1)
