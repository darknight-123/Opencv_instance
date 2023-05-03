import cv2
import numpy as np
from matplotlib import pyplot as plt
cordition=[]
time=0
# read image
img = cv2.imread('one_piece.jpg')

# show image
cv2.imshow('image', img)

def prespective_transformation(cordition):
	pts1 = np.float32([cordition[0],cordition[1],cordition[2],cordition[3]])
	pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
	M=cv2.getPerspectiveTransform(pts1,pts2)
	dst=cv2.warpPerspective(img,M,(300,300))
	plt.subplot(121),plt.imshow(img),plt.title('Input')
	plt.subplot(122),plt.imshow(dst),plt.title('Output')
	plt.show()
#define the events for the
# mouse_click.
def mouse_click(event, x, y,
				flags,params):
	global time
	# to check if left mouse
	# button was clicked
	if event == cv2.EVENT_LBUTTONDOWN:
		
		# font for left click event
		font = cv2.FONT_HERSHEY_TRIPLEX
		LB = 'Left Button'
		
		# display that left button
		# was clicked.
		cv2.putText(img, LB, (x, y),
					font, 1,
					(255, 255, 0),
					2)
		cv2.imshow('image', img)
		
		cordition.append([x,y])
		if time==3:
			cv2.destroyAllWindows()
			prespective_transformation(cordition)
			
		time=time+1
		
		
		

cv2.setMouseCallback('image', mouse_click)

cv2.waitKey(0)

# close all the opened windows.
cv2.destroyAllWindows()
