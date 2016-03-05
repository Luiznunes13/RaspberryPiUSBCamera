##########################################################################
# Title: Raspberry Pi USB Camera Module Control Script
# Author: Patrick Walton
# Notes: I used this script on a raspberry pi to control 4 ELP camera modules in a fast moving environment. I also used USB Video Class (UVC) Linux Version to set the exposure.
##########################################################################

### Configuration ###
import cv2 #OpenCV library, www.opencv.org
import time
import subprocess

### Set Exposure in Linux Command Line using UVC ###
subprocess.call(["v4l2-ctl", "-d", "/dev/video0", "-c", "exposure_auto=1", "-c", "exposure_auto_priority=0", "-c", "exposure_absolute=1"])
subprocess.call(["v4l2-ctl", "-d", "/dev/video1", "-c", "exposure_auto=1", "-c", "exposure_auto_priority=0", "-c", "exposure_absolute=1"])

#### Initialize Cameras ###
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

#### Initialize Files and Variables ###
times = open("time data_exposure1.2.1.txt", "w")
images0 = []
images1 = []
time_data = []

print("Begin setup.")

#### Time to Setup. ###
# I used this time to take my camera setup from the desktop that interfaced with the PI out to the parking lot where I was testing capture in motion.

time.sleep(40)

print("Begin capture.")

#### Capture Images and Save to Lists ###
for i in range(1,40):
    images0.append(cap0.read())
    images1.append(cap1.read())
    time_data.append(time.clock())

print("Begin saving.")

### Save Data and Images ###
for i in time_data:
    times.write("%s\n" % i)
for i in range(0, len(images0)):
    cv2.imwrite("Capture1.3-0-" + str(i) + ".jpg", images0[i][1]) #Optional: Params for save quality. #images second index, bc VideoCapture.read() returns two vals
for i in range(0, len(images1)):
    cv2.imwrite("Capture1.3-1-" + str(i) + ".jpg", images1[i][1])

print("End capture.")

### Close All ###
times.close()
print("finished")
cv2.destroyAllWindows
cv2.VideoCapture(0).release()
