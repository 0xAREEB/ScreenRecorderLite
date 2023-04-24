from pyautogui import screenshot
import cv2 as cv
from numpy import array as nparray
from keyboard import is_pressed as Kb_is_pressed
from datetime import datetime

print("\t\t--------------------------\n\t\t0xRecorder Lite by 0xAreeB\n\t\t--------------------------\n\t\t    Press \"F8\" to Stop\n\t\t--------------------------\n\n")

resolution = (1920, 1080)

codec = cv.VideoWriter_fourcc(*'XVID')

now = datetime.now()

exte = ".avi" 
tstr = now.strftime("%d-%m-%Y_%H-%M-%S")
start = "Recording_"

filename = ""
filename += f"{start}{tstr}{exte}"
#filename += tstr
#filename += exte
#filename = str(filename)

print(filename)

fps = float(input("=> Video Speed (13 -> Normal):  "))

out = cv.VideoWriter(filename, codec, fps, resolution)

#cv.namedWindow("Live", cv.WINDOW_NORMAL)

#cv.resizeWindow("Live", 480, 270)

print("\nRecording Started..")
while True:
	img = screenshot()
	frame = nparray(img)
	frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	out.write(frame)
	#cv.imshow('Live', frame)
		
	if Kb_is_pressed("F8"):
		break
print("\nRecording Stoped..")
out.release()