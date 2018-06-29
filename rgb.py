import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('R', # name of value
                   'title', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func

cv2.createTrackbar('G', # name of value
                   'title', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func

cv2.createTrackbar('B', # name of value
                   'title', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

	ret, frame = cap.read()
	if not ret: continue
	
	R = cv2.getTrackbarPos('R','title')
	G = cv2.getTrackbarPos('G','title')
	B = cv2.getTrackbarPos('B', 'title')
    ## do something by using v
	if(B!=0):
		frame[:,:,0]=B
	elif(G!=0):
		frame[:,:,1]=G
	elif(R!=0):
		frame[:,:,2]=R

	cv2.imshow('title', frame)  # show in the win

	k = cv2.waitKey(1)
	if k == ord('q') or k == 27:
		break

cap.release()
cv2.destroyAllWindows()
