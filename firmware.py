import picamera
import picamera.array
from time import sleep
from gpiozero import LED

xres = 736
yres = 480

thresh = 10
rsens = 0.9
bsens = 0.9

noz = LED(26)

#pwr = LED(4)
#pwr.on()
#led = LED(5)
#noz = LED(31)

def analyzeV(points):
    x = int(xres/2) - 1
    for y in range(yres):
        R = points.array[y,x,0]
        G = points.array[y,x,1]
        B = points.array[y,x,2]
        if(G > thresh and R/G < rsens and B/G < bsens):
            return True
    return False

def analyzeH(points):
    y = int(yres/2) - 1
    for x in range(xres):
        R = points.array[y,x,0]
        G = points.array[y,x,1]
        B = points.array[y,x,2]
        if(G > thresh and R/G < rsens and B/G < bsens):
            return True
    return False

camera = picamera.PiCamera()
camera.resolution = (xres, yres)

while(True):
    output = picamera.array.PiRGBArray(camera, size=(xres,yres))
    camera.capture(output, format='rgb', use_video_port=True)
    if(analyzeV(output)):
        noz.on()
        #led.on()
        sleep(1)
    else:
        noz.off()
        #led.off()
