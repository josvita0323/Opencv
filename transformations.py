import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
cv.waitKey(0)    