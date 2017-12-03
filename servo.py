import RPi.GPIO as GPIO
import time


print ("GPIO is: " + str(GPIO))
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

print ("Startin PWM")
pwm = GPIO.PWM(18, 50)
pwm.stop
pwm.start(20)
time.sleep (300)

print ("Stopping PWM")
pwm.stop()
