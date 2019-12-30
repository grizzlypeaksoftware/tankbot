import RPi.GPIO as GPIO
import keyboard
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)  #blue
GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)  #green
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW) #yellow
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW) #orange


def Reset():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)










GPIO.cleanup()