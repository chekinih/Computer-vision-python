import cv2
import numpy as np

def myerosion(im,el):
    return cv2.erode(im, el)

def mydilatation(im,el):
    return cv2.dilate(im, el)

def mygradient(im,el):
    return mydilatation(im,el) -  myerosion(im,el)

def myclose(im, el):
    delatedIm = mydilatation(im,el)
    return myerosion(delatedIm, el)

def myopen(im, el, idemPo = 1):
    result = im
    for i in range(idemPo):
        result = mydilatation(myerosion(result, el),el)
    return result
