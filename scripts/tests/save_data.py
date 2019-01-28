import serial
import csv
from time import sleep
# ser.write('0&-48'.encode()) # format is:  desired speed on motor A & desired speed on motor B
# ser.close() # close it if you are done seding data, otherwise keep connection open

with open(r'encoders.csv', 'a',newline='') as csvfile:
    ser = serial.Serial("COM3",250000) #TODO: match baudrate with the one in the arduino code
    sleep(2) # for some reason I need this before sending msgs
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    while 1:
        # try:
            line = ser.readline()
            data = line.decode("utf-8", errors="ignore").strip().split('&')
            writer.writerow(data)
        # finally:
        #     csvfile.close()
        #     ser.close()