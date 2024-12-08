import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame,scale=0.75): #changing resolution for photo,video,live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)


def ChanegRes(width,height):  #changing resolution for live video
    capture.set(3,height)
    capture.set(4,width)    

resize_img = rescaleFrame(img)
cv.imshow('image',resize_img)

capture = cv.VideoCapture('Videoes/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()    
cv.destroyAllWindows()   

cv.waitKey(0) 
