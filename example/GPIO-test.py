try:
    import RPi.GPIO as GPIO    
except:
    import VPi.GPIO as GPIO

import time

print("set mode")
GPIO.setmode(GPIO.BCM)
print("set warning false")
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)
time.sleep(1)
GPIO.output(15,GPIO.LOW)