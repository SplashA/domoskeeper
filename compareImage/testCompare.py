import cv2
import numpy as np
import time

debut = time.time()

image1 = np.int16(cv2.imread("images/Image16.jpg"))
image2 = np.int16(cv2.imread("images/Image17.jpg"))

difference = np.subtract(image1, image2)

#result = np.array(difference)
A = np.array(difference)
idx = np.where((A >25) | (A<(-25)))

print(len(A[idx])/len(A.flat)*100)

print(str(time.time()-debut) + " secondes")