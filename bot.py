import tankbot
import keyboard

tankbot.Init()

while True:
	if keyboard.is_pressed("s"):
		tankbot.Stop()
	if keyboard.is_pressed("f"):
		tankbot.Forward()
	if keyboard.is_pressed("b"):
		tankbot.Reverse()
	if keyboard.is_pressed("r"):
		tankbot.Right()
	if keyboard.is_pressed("l"):
		tankbot.Left()	
	if keyboard.is_pressed("q"):
		tankbot.Stop()
		break
	if keyboard.is_pressed("\x1b[A"):
		print("up")
		tankbot.Forward()
		
tankbot.Close()
