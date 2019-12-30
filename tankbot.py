import RPi.GPIO as GPIO
import keyboard
from time import sleep

def Init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)  #blue
	GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)  #green
	GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW) #yellow
	GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW) #orange

	Welcome()


def Welcome():
	Stop()
	Forward()
	sleep(1)
	Reverse()
	sleep(1)
	Right()
	sleep(2)
	Left()
	sleep(2)

def Forward():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)

def Reverse():
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def Left():
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def Right():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def Stop():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)



def Close():
	GPIO.cleanup()