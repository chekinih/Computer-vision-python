import cv2
import numpy as np
from COMMUN import strel
from COMMUN import mymorpho as mm

el = strel.build('disque', 10)
gamma4 = strel.build('diamant', 1)

image_rice_grains = cv2.imread('Assets/rice.png')
cv2.imshow('Normal image', image_rice_grains)

# This will extract the background of the image
im_open = mm.myopen(image_rice_grains, el, 1)
cv2.imshow('Opened image', im_open)

# To extract the rices in the image, we should make a difference between the original image and its opened image
extraction_rices = image_rice_grains - im_open
cv2.imshow('Extraction rice grains ', extraction_rices)

# Get pixels that are > 40 (rice grains) and transform them to white ones(255) in order
# to have a clear image of the rice grains
pixel_indice_sup = extraction_rices[:,:,:] > 40
extraction_rices[pixel_indice_sup] = 255
cv2.imshow('Accurate Extraction', extraction_rices)

# Applay an opening with gamma4 structuring element to the last image in order to remove
# the noise
im_open2 = mm.myopen(extraction_rices, gamma4, 1)
cv2.imshow('Accuratee Extraction', im_open2)

el2 = strel.build('disque', 2)
imGrad = mm.mygradient(im_open2,el2)
cv2.imshow('gradient image', imGrad)

height= image_rice_grains.shape[0]

width = image_rice_grains.shape[1]
max_area = -1
max_coordinates = -1
for i in range(0, height):
    for j in range(0, width):
        if np.array_equal(im_open2[i, j],[255,255,255]):
            k = j
            for jj in range (j,width):
                if np.array_equal(im_open2[i, jj], [255, 255, 255]):
                    k = jj
                    continue
                else:
                    break
            kk = i
            for ii in range(i,height):
                if np.array_equal(im_open2[ii, k], [255, 255, 255]):
                    kk = ii
                    continue
                else:
                    break
            if ((ii-i) * (jj-i)) > max_area:
                max_area = ((ii-i) * (jj-i))
                max_coordinates = [i,j]
print(max_area)
ii, jj = max_coordinates
print(ii," ,",jj)
for i in range(ii, height):
    for j in range(jj, width):
        if np.array_equal(im_open2[i, j],[255,255,255]):
            im_open2[i, j] = [0,0,255]
            continue
        else:
            break
#cv2.imshow('Change', im_open2)

# transform the border of the image to black (0)
image_rice_grains[0,:] = 0
image_rice_grains[:,0] = 0
image_rice_grains[height-1,:] = 0
image_rice_grains[:,width-1] = 0

ell = strel.build('disque', 4)

imErode = mm.myerosion(extraction_rices, ell)
cv2.imshow('eroted image', imErode)

cv2.waitKey(0)
