//This file is used to run a fatigue test inspection system. This enables the tester to go home and review the test images after the specimen breaks.

import cv2 #Open Source Computer vision Library for controlling cameras. Needed to be set up on Raspberry Pi. I Googled a walkthrough
import time
import subprocess

cycle_length = 15 #Number of pictures to take each capture sequence
n = 0 #Sequence number

#Loop Until Tester Quits
while True:
   
    #Initialize Lists to hold images during capture (cuts down on time between images, which prevents aliasing)
    images0 = []
    images1 = []
    images2 = []
    time_data = []

    #Output Sequence Number to screen
    print("Capture Sequence " + str(n))
    
    ###Capture Sequence###

    #Camera 0
    cap0 = cv2.VideoCapture(0)          #Initiate Camera
    cap0.set(3,1280)                    #Set image width
    cap0.set(4,1024)                    #Set image Height
    for i in range(0,cycle_length):
        images0.append(cap0.read())     #Capture image and add it to list
    cap0.release()                      #Close camera

    #Camera 1
    cap1 = cv2.VideoCapture(1)
    cap1.set(3,2000)
    cap1.set(4,2000)
    for i in range(0,cycle_length):
        images1.append(cap1.read())
    cap1.release()

    #Camera 2
    cap2 = cv2.VideoCapture(2)
    cap2.set(3,1280)
    cap2.set(4,1024)
    for i in range(0,cycle_length):
        images2.append(cap2.read())
    cap2.release()
        
    #Save
    for i in range(0, len(images0)):
        cv2.imwrite("Kapton1.0_0_" + str(n) + "." + str(i) + ".jpg", images0[i][1]) #Write image, see below for explanation of naming.
    for i in range(0, len(images1)):
        cv2.imwrite("Kapton1.0_1_" + str(n) + "." + str(i) +  ".jpg", images1[i][1]) #Timestamp adjustment for using same timestamp array.
    for i in range(0, len(images2)):
        cv2.imwrite("Kapton1.0_2_" + str(n) + "." + str(i) + ".jpg", images2[i][1])

    #Repeat about every 100 cycles.
    time.sleep((n + 1) * 190)
    n = n + 1
