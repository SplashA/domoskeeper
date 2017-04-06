from cv2 import *
import cv2 as cv2
from datetime import datetime
from time import sleep
from lib import compareImage
from lib import postEvent
from lib import smsTwilio
import os
import base64 as base64

# function definitions

def photo_capture(frequency) :
    imagePath = 'images'
    while activated == 1:
        cam = VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        img = cv2.resize(img,(400,225))
        if s:    # frame captured without any errors
            now = datetime.now()
            filename = str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'_'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+':'+str(now.microsecond)+'.jpg'
            if (('.DS_Store' in os.listdir(imagePath)) and len(os.listdir(imagePath))==1) or (len(os.listdir(imagePath))==0):
                imwrite(imagePath + "/" + filename,img) #save image
                print(os.listdir(imagePath))
            else :
                if len(os.listdir(imagePath))==1:
                    os.remove(imagePath + "/" + os.listdir(imagePath)[0])
                    imwrite(imagePath + "/" + filename,img)
                    print(os.listdir(imagePath)[0] + " - "  + filename)
                    
                else:
                    os.remove(imagePath + "/" + os.listdir(imagePath)[1])
                    imwrite(imagePath + "/" + filename,img)
                    print(os.listdir(imagePath)[1] + " - " + filename)

        sleep(frequency)

def video_capture(counter, maxTime) :
    cap = VideoCapture(0)
    # video = VideoWriter('record.avi',cv.CV_FOURCC('M','J','P','G'),32,(640,360),1)
    fourcc = cv.CV_FOURCC('M','J','P','G')
    video = VideoWriter('output.avi', fourcc, 20, (680, 480))
    while True:
        ret,img = cap.read()
        video.write(img)
        imshow('Video Stream', img)

        counter +=1
        if counter >= maxTime:
            cap.release()
            video.release()
            destroyAllWindows()
            break

counter = 0
maxTime=1000
activated = 1
frequency = 2
photo_capture(frequency)
# video_capture(counter, maxTime)