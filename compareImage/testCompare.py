import cv2
import numpy as np
import time

debut = time.time()

image1 = cv2.imread("images/filename2.jpg")
image2 = cv2.imread("images/filename3.jpg")

difference = image1-image2

#result = np.array(difference)
A = np.array(difference)
idx = np.where((A >25) | (A<(-25)))

print(len(idx[0]))
print(image1[0,0])
print(image2[0,0])
print(difference[0,0])
print(len(A[idx])/len(A.flat)*100)


'''for x in range(0,(len(difference)-1)):
    for y in range(0,len(difference[x])-1):
        for z in range(0,len(difference[x,y])-1):
            if difference[x,y,z] == 0:
                nbZero += 1
            else:
                nbNonZero += 1
print("nbZero: "+ str(nbZero))
print("nbNonZero: "+ str(nbNonZero))

percentDiff = (nbNonZero/(nbZero+nbNonZero)*100)

print("percentDiff: "+ str(percentDiff)+"%")'''

print(str(time.time()-debut) + " secondes")