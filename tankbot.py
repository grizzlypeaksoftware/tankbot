import RPi.GPIO as GPIO
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
	sleep(.5)
	Reverse()
	sleep(.5)
	Right()
	sleep(1)
	Left()
	sleep(1)
	Stop()

def No():
	Stop()
	Right()
	sleep(.25)
	Left()
	sleep(.25)
	Right()
	sleep(.25)
	Left()
	sleep(.25)
	Stop()

def Yes():
	Stop()
	Forward()
	sleep(.25)
	Reverse()
	sleep(.25)
	Forward()
	sleep(.25)
	Reverse()
	sleep(.25)
	Stop()

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
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def Right():
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)

def Stop():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)



def Close():
	GPIO.cleanup()