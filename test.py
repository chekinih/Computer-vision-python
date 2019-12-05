import cv2
import numpy as np
from COMMUN import strel
from COMMUN import mymorpho as mm

im = cv2.imread('Assets/cat.jpg')
cv2.imshow('Normal image', im)

el = strel.build('disque', 3)

imerosion = mm.myerosion(im, el)
cv2.imshow('eroted image', imerosion)

imGrad = 255-mm.mygradient(im,el)
cv2.imshow('gradient image', imGrad)

imDilate = mm.mydilatation(im, el)
cv2.imshow('dilated image', imDilate)
cv2.waitKey(0)

