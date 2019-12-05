import cv2
import numpy as np
from COMMUN import strel
from COMMUN import mymorpho as mm

gamma4 = strel.build('diamant', 1)
gamma8 = strel.build('carre', 2)

line_horizontal = strel.build('ligne', 2, 0)
line_vertical = strel.build('ligne', 4, 90)

image_salt_pepper = cv2.imread('Assets/SaltPepper.png')
cv2.imshow('Normal image', image_salt_pepper)

# We will remove the salt and pepper noise using an opening with gamma4
# followed by a closing with 2 gamma8
im_open = mm.myopen(image_salt_pepper, gamma4, 1)
cv2.imshow('Opened image', im_open)
im_close = mm.myclose(im_open, gamma8)
cv2.imshow('Close opened image', im_close)

# Another way to remove the salt and pepper noise is to apply an opening
# with an horizontal line structuring element followed by a closing with
# a vertical line structuring element
im_open_line = mm.myopen(image_salt_pepper, line_horizontal, 1)
cv2.imshow('Opened image line', im_open_line)
im_close_line = mm.myclose(im_open_line, line_vertical)
cv2.imshow('Close opened image line', im_close_line)

cv2.waitKey(0)
