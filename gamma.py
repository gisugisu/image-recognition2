import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   20, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

	ret, frame = cap.read()
	if not ret: continue
	v = cv2.getTrackbarPos('value', 'title')*0.5  # of the win
	gamma=v
	print(gamma)
	gamma=gamma+0.001
	look_up_table = np.zeros((256, 1), np.uint8)
	for i in range(256):
		look_up_table[i] = 255 * pow(float(i) / 255, 1.0 / gamma)
		
	frame = cv2.LUT(frame, look_up_table)
## do something by using v
    
	cv2.imshow('title', frame)  # show in the win

	k = cv2.waitKey(1)
	if k == ord('q') or k == 27:
		break

cap.release()
cv2.destroyAllWindows()
