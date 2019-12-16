import RPi.GPIO as GPIO
import time
NULL_CHAR = chr(0)
# from kb.keycode import key
from keyMap.map import keyMap
def write_report(report):
    print (report)
    print (report.encode())
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
matrix = keyMap.matrix
COL = [5,6,13,19]
ROW = [18,23,24,25]

for j in range(4):
            GPIO.setup(COL[j], GPIO.OUT)
            GPIO.output(COL[j], 0)

for i in range(4):
            GPIO.setup(ROW[i], GPIO.IN)

while True:
    for j in range(4):

        GPIO.output(COL[j],1)
        for i in range(4):
            if GPIO.input(ROW[i]) == 1:

                #print ("col = ",(j+1))
                #print ("row = ",(i+1))

                m = ((i * 4) + j)
                #print ("postion = ",(m))
                #print (matrix [m])
                #print (" ")
                time.sleep(0.1)
		#write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
		write_report(NULL_CHAR*2+chr(matrix[m])+NULL_CHAR*5)
		write_report(NULL_CHAR*8)
		#write_report(chr(97))
                while(GPIO.input(ROW[i]) == 1):
                    GPIO.output(21,1)
                    time.sleep (0.2)

        GPIO.output(21,0)
        GPIO.output(COL[j],0)