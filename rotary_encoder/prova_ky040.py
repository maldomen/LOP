from time import sleep
import RPi.GPIO as GPIO
from ky040.KY040 import KY040


CLOCKPIN = 16
DATAPIN = 20
SWITCHPIN = 21
zoom=0

def rotaryChange(direction):
    global zoom
    if direction:
        zoom+=1
    else:
        zoom-=1
    print(zoom)
    

def switchPressed():
    print(f"click {zoom}")


GPIO.setmode(GPIO.BCM)

ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed,rotaryBouncetime=50)

ky040.start()

try:
    while True:
        sleep(0.1)
finally:
    ky040.stop()
    GPIO.cleanup()
