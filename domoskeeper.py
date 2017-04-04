from cv2 import *
from datetime import datetime
from time import sleep


# function definitions

def photo_capture(frequency) :
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        now = datetime.now()
        filename = str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'_'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+':'+str(now.microsecond)+'.jpg'
        imwrite(filename,img) #save image
    sleep(frequency)


# code qui prend la photo
activated = 1
frequency = 2
while activated == 1:
    photo_capture(frequency)