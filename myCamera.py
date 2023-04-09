import picamera 
import os
import time 

camera = None
fileName = ""

def takePicture(): 
	global camera
	global fileName

	if len(fileName) != 0: 
		os.unlink(fileName)
	if camera == None:
		camera = picamera.PiCamera()

	takeTime = time.time()
	fileName ="./static/%d.jpg"%(takeTime*10) 
	camera.capture(fileName, use_video_port=True) 
	return "%d.jpg"%(takeTime*10)

def stopPicture(): 
	camera = None
	fileName = ""