import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
blan = np.zeros((500,500,3), dtype = 'uint8')
blank2 = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blank',blank)
 
#1.paint the image 
# blank[:] = 0,255,0
# cv.imshow('green',blank) 

#paint only small portion
blan[400:500, 400:500] = 0,255,255  #blan[top-bottom, left-right]
cv.imshow('yellow_box',blan)

#2.Draw a rectangle
cv.rectangle(blank2,(0,250),(100,500),(0,255,0),thickness=2) #to fill the box we can use cv.FILLED or -1 in thickness =??)
cv.imshow('Reactangle',blank2)

#3.Draw a circle
cv.circle(blank2,(blank2.shape[1]//2,blank2.shape[0]//2),50,(255,255,0),thickness=3)
cv.imshow("circle",blank2)

#4.Draw a line
cv.line(blan,(0,0),(blan.shape[1]//2,blan.shape[0]//2),(255,255,255),thickness = 3)
cv.imshow('line',blan)

#5.Write text
cv.putText(blank,'hello',(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("text",blank)

cv.waitKey(0)