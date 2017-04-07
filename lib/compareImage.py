# Module de comparaison de 2 images
import cv2
import numpy as np
import time

def compareImage(img1,img2):
    debut = time.time()


    image1 = np.int16(cv2.imread(img1))
    image2 = np.int16(cv2.imread(img2))

    difference = np.subtract(image1, image2)

    A = np.array(difference)
    idx = np.where((A >25) | (A<(-25)))

    return (float(len(A[idx]))/len(A.flat)*100)