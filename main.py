from pyautogui import screenshot
import cv2 as cv
from numpy import array as nparray
from keyboard import is_pressed as Kb_is_pressed
from datetime import datetime

print("\t\t--------------------------\n\t\t0xRecorder Lite by 0xAreeB\n\t\t--------------------------\n\t\t    Press \"F8\" to Stop\n\t\t--------------------------\n\n")

resolution = (1920, 1080) # Recording Resolution
codec = cv.VideoWriter_fourcc(*'XVID')

now = datetime.now() # Get Current Date and Time

# File Name
fileExtension = ".avi" # Extension can be avi, mp4 etc.
dateTimeString = now.strftime("%d-%m-%Y_%H-%M-%S")
filePrefix = "Recording_"
filename = ""
filename += f"{filePrefix}{dateTimeString}{fileExtension}"

# Show Output File Name on Console
print(filename)

fps = float(input("=> Video Speed (13 -> Normal):  "))

out = cv.VideoWriter(filename, codec, fps, resolution)

print("\nRecording Started..")
while True:
	img = screenshot()
	frame = nparray(img)
	frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	out.write(frame)
		
	if Kb_is_pressed("F8"):
		break
print("\nRecording Stoped..")
out.release()
