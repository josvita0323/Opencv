#basic functions of opencv
import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#Converting an image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blur
blur =  cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)# here 7,7 helps in bluring the image and it should be an odd number
cv.imshow('blur',blur)

#Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('edges',canny)

canny1 = cv.Canny(blur,125,175)#for blur
cv.imshow('Edges',canny1)

#Dilating the image
dilated = cv.dilate(canny,(3,3),iterations= 3)
cv.imshow('dilate',dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Erode',eroded)

#Resize
resize = cv.resize(img,(500,500))
cv.imshow("resized",resize)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)