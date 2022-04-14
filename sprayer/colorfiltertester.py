"""
Script for testing color filter
Replaces unfiltered  pixels with a white pixel
Saves image as "filterTest.png"



#############################################################################

#Resolution settings
XRES, YRES = 1920, 1080

#############################################################################

import time
from PIL import Image
from picamera2.picamera2 import *

# The color filter you wish to apply to the image
def filter(r, g, b):
    if(g - r > 9):
        return True

# The function to replace pixels
def replacePixels(array):
    for x in range(XRES):
        for y in range(YRES):
            r = array[y, x, 0]
            g = array[y, x, 1]
            b = array[y, x, 2]
            # print(x, y)
            if(filter(int(r), int(g), int(b))):
                array[y, x, 0] = 255
                array[y, x, 1] = 255
                array[y, x, 2] = 0
            else:
                array[y, x, 0] = 0
                array[y, x, 1] = 0
                array[y, x, 2] = 0

camera = Picamera2()
camera.start_preview()
config = camera.still_configuration(main={"size": (XRES, YRES)})
camera.configure(config)

camera.start()
print("Camera warming up...")
time.sleep(2)

data = camera.capture_array()
print("Captured numpy array.")

img = Image.fromarray(data, mode="RGBA")
img.save("regular.png")
print("Saved regular.png")

print("Performing scan...")
startTime = time.time()
replacePixels(data)
print("Done. It took "+str(time.time() - startTime)+" seconds.")

img = Image.fromarray(data, mode="RGBA")
img.save("filtered.png")
print("Saved filtered.png")

camera.close()

print("Done.")

print("\n"+"Copy:"+"\n")
print("scp pi@raspi-64bit.local:/home/pi/tests/\\{regular.png,filtered.png\\} .\\")
print()
