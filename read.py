import cv2 as cv
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
  

cv.waitKey(0)  # this is used so the image doesn't get disspeared
                 #  as soon as it pops up and gets dissapeared by a click
# capture = cv.VideoCapture('Videoes/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video',frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()    
# cv.destroyAllWindows()   

