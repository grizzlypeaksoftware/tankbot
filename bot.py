import tankbot
import keyboard

tankbot.Init()

while True:
	if keyboard.is_pressed("s"):
		tankbot.Stop()
	if keyboard.is_pressed("up"):
		tankbot.Forward()
	if keyboard.is_pressed("down"):
		tankbot.Reverse()
	if keyboard.is_pressed("right"):
		tankbot.Right()
	if keyboard.is_pressed("left"):
		tankbot.Left()	
	if keyboard.is_pressed("1"):
		tankbot.No()	
	if keyboard.is_pressed("2"):
		tankbot.Yes()	
	if keyboard.is_pressed("3"):
		tankbot.Welcome()	

	if keyboard.is_pressed("q"):
		tankbot.Stop()
		break
	
tankbot.Close()
