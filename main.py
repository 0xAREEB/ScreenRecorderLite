from pyautogui import screenshot
import cv2 as cv
from numpy import array as nparray
from keyboard import is_pressed as Kb_is_pressed
from datetime import datetime

# Print the welcome message
print("\t\t--------------------------\n\t\t0xRecorder Lite by 0xAreeB\n\t\t--------------------------\n\t\t    Press \"F8\" to Stop\n\t\t--------------------------\n\n")

# Set the Recording Resolution
resolution = (1920, 1080) 

# Get the current date and time
now = datetime.now() 

# Get the desired file extension from the user
fileExtension = "."
fileExtension += input("Enter Output Format (avi or mp4):  ")

# Format the date and time string
dateTimeString = now.strftime("%d-%m-%Y_%H-%M-%S")

# Set the file name prefix
filePrefix = "Recording_"

# Finalize the file name
filename = f"{filePrefix}{dateTimeString}{fileExtension}"

# Show the output file name on the console
print("\nFile Name:  " + filename + "\n")

# Set the video speed
speed = float(input("=> Video Speed (13 -> Normal):  "))

# Set the video codec based on the file extension
if fileExtension == ".mp4":
	codec = cv.VideoWriter_fourcc(*'mp4v')
else:
	codec = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter(filename, codec, speed, resolution)

# Clear memory
del fileExtension, filePrefix, dateTimeString, now

print("\nRecording Started..")

# Start the recording loop
while True:
	# Take a screenshot and create a frame
	img = screenshot() 
	frame = nparray(img)
	del img
	
	frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	
	# Write the frame to the output file
	out.write(frame)
	
	# Listen for the F8 key press to stop the recording
	if Kb_is_pressed("F8"):
		break

# Release the resources and print the recording stopped message
out.release()
print("\nRecording Stoped..")
