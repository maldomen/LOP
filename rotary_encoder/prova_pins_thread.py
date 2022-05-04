import RPi.GPIO as GPIO
import threading


def comprovar(nom,pin):
    print(f"thread {nom} pin {pin}")
    GPIO.setup(pin,GPIO.IN)
    while True:
        GPIO.wait_for_edge(pin,GPIO.BOTH,bouncetime=200)
        print(f"Detectat en {pin}canvi a {GPIO.input(pin)}")
        

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    """
    sw=21
    dt=20
    clk=16
    """
    thnum=0
    th=[]
    #pins={"sw":21,"dt":20}
    pins={"DT":20,"sw":21}
    for i in pins:
        print(f"{i} = {pins[i]}")
        th.append(threading.Thread(target=comprovar,args=(i,pins[i])))
        th[thnum].start()
        thnum +=1

