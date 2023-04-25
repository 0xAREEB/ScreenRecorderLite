from pyautogui import screenshot
import cv2 as cv
from numpy import array as nparray
from keyboard import is_pressed as Kb_is_pressed
from datetime import datetime
import argparse
from os.path import splitext as splitPathText

print("\t\t--------------------------\n\t\t0xRecorder Lite by 0xAreeB\n\t\t--------------------------\n\t\t    Press \"F8\" to Stop\n\t\t--------------------------\n\n")

# Get command Line Arguments
parser = argparse.ArgumentParser(description='Screen Recorder')
parser.add_argument('--output', '-o', type=str, default='recording.avi', help='Output file name')
parser.add_argument('--fps', '-fps', type=float, default=13.0, help='Frame Rate')
parser.add_argument('--width', '-sx', type=int, default=1920, help='Recording Width')
parser.add_argument('--height', '-sy', type=int, default=1080, help='Recording Height')
args = parser.parse_args()

# Set the recording resolution
resolution = (args.width, args.height)

# Set output file name
filename = args.output

# Set frames per second
fps = args.fps

# Show the output file name on the console
print("\n\tResolution:  \"" + str(args.width) + "x"+str(args.height)+"\"\n\n\tName:  \"" + filename + "\"\n\tFPS:   \"" + str(fps) + "\"\n")

# Set the video codec based on the file extension
if splitPathText(filename)[1] == ".mp4":
	codec = cv.VideoWriter_fourcc(*'mp4v')
else:
	codec = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter(filename, codec, fps, resolution)

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
