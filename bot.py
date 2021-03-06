import tankbot
import keyboard
import time as _time

tankbot.Init()

recorded = []
recording_started = False

def ControlSwitch(key, event):
	global recording_started

	#print(key)
	#print(event.event_type)

	if key == "s":
		tankbot.Stop()
	if key == "up":
		tankbot.Forward()
	if key == "down":
		tankbot.Reverse()
	if key == "right":
		tankbot.Right()
	if key == "left":
		tankbot.Left()	
	if key == "1":
		tankbot.No()	
	if key == "2":
		tankbot.Yes()	
	if key == "3":
		tankbot.Welcome()	
	if key == "f1":
		keyboard.start_recording()
		recording_started = True
	if key == "f2":
		try:
			if recording_started == True:
				recording_started = False
				Playback(keyboard.stop_recording())
			else:
				Playback(recorded)
		except Exception as inst:
			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)          # __str__ allows args to be printed directly,
	if key == "q":
		tankbot.Stop()
		return False
	return True


def Playback(rec):
	last_time = None    
	global recorded
	recorded = rec

	for event in rec:
		if last_time is not None:
			_time.sleep(event.time - last_time)
		last_time = event.time
		key =  event.scan_code or event.name
		if event.name != "f2":
			check = ControlSwitch(event.name, event)


continueLoop = True

while continueLoop:
	try:
		key = keyboard.read_key()
		event = keyboard.read_event()

		if event.event_type == "up":
			continueLoop = ControlSwitch(key, event)

	except Exception as inst:
			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)          # __str__ allows args to be printed directly,
	
tankbot.Close()
