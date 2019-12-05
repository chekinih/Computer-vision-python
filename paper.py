import cv2
import numpy as np
from COMMUN import strel
from COMMUN import mymorpho as mm

image_60_colored = cv2.imread('Assets/papier_60.png')
image_35_colored = cv2.imread('Assets/papier_35.png')
image_15_colored = cv2.imread('Assets/papier_15.png')

#keep the red color
image_60_uncolored = image_60_colored[:,:,2]
cv2.imshow('Normal image', image_60_uncolored)

min_ = np.sum(image_60_colored)
k = 0
for i in range(-90, 90, 5):
    elem = strel.build('ligne', 40, i)
    imGrad = mm.mygradient(image_60_uncolored, elem)
    sum = np.sum(imGrad)
    # print sum
    if sum < min_:
        min_ = sum
        k = i

# k will define the paper orientation
print k
cv2.waitKey(0)


