import cv2
import numpy as np
from COMMUN import strel
from COMMUN import mymorpho as mm

el = strel.build('disque', 3)
image_numbers = cv2.imread('Assets/numbers.png')
cv2.imshow('Normal image', image_numbers)

# this will extract the background of the image
im_open = mm.myopen(image_numbers, el, 1)
cv2.imshow('Opened image', im_open)

# IdemPotence: apply two or more times the opened (mm.myopen)
IdemPotence= mm.myopen(image_numbers, el, 2)
cv2.imshow('Opened * 2 image ', IdemPotence)

# We can see that the result of the image do not change
if np.array_equal(im_open, IdemPotence):
    print("idempotence verifiee")
else:
    print("idempotence nonk verifiee")

# To extract the numbers in the image, we should make a difference between the original image and it s opened image
extraction_numbers = image_numbers - im_open
cv2.imshow('Extraction numbers image ', extraction_numbers)

pixel_indice_sup = extraction_numbers[:,:,:]>50
extraction_numbers[pixel_indice_sup] = 255
cv2.imshow('Accurate Extraction', extraction_numbers)

im_close = mm.myclose(image_numbers, el)
cv2.imshow('Closed image', im_close)

cv2.waitKey(0)
