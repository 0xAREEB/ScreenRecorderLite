from pyautogui import screenshot
import cv2 as cv
from numpy import array as nparray
from keyboard import is_pressed as Kb_is_pressed
from datetime import datetime

print("\t\t--------------------------\n\t\t0xRecorder Lite by 0xAreeB\n\t\t--------------------------\n\t\t    Press \"F8\" to Stop\n\t\t--------------------------\n\n")

# Recording Resolution
resolution = (1920, 1080) 

# Get Current Date and Time
now = datetime.now() 

# File Extension
fileExtension = "."
fileExtension += input("Enter Output Format (avi or mp4):  ")

dateTimeString = now.strftime("%d-%m-%Y_%H-%M-%S")

filePrefix = "Recording_"

#Final Name
filename = f"{filePrefix}{dateTimeString}{fileExtension}"

# Show Output File Name on Console
print("\nFile Name:  " + filename + "\n")

# Set Frames Rate
fps = float(input("=> Video Speed (13 -> Normal):  "))

# Set Video Codec
if fileExtension == ".mp4":
	codec = cv.VideoWriter_fourcc(*'mp4v')
else:
	codec = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter(filename, codec, fps, resolution)

# Clear some Memory
del fileExtension, filePrefix, dateTimeString, now

print("\nRecording Started..")
while True:
	img = screenshot() # Take Screenshot
	frame = nparray(img) # Create a frame
	del img
	frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	out.write(frame) # Write frame to Output Recording File
	
	# F8 Key Press Listener
	if Kb_is_pressed("F8"):
		break
out.release()
print("\nRecording Stoped..")
