import RPi.GPIO as GPIO
import threading
import time
pins={21:"sw",20:"DT"}
def comprovar(pin):
    print(f"Detectat en {pins[pin]}canvi a {GPIO.input(pin)}")
    print("-------------------------------------")    

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    """
    sw=21
    dt=20
    clk=16
    """
  
    #pins={"sw":21,"dt":20}
    
    for i in pins:
        GPIO.setup(i,GPIO.IN)
        print(f"{i} = {pins[i]}")
        GPIO.add_event_detect(i,GPIO.BOTH,callback=comprovar,bouncetime=200)
    while True:
        time.sleep(0.1)
