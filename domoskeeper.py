from cv2 import *
from datetime import datetime

# code qui prend la photo
frequency = 2
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    destroyWindow("cam-test")
    now = datetime.now()
    filename = str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'_'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+':'+str(now.microsecond)+'.jpg'
    imwrite(filename,img) #save image
