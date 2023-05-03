
import cv2 as cv
import numpy as np
#Gamma function 利用相片裡的像素值配合 alpha*(原始值)+beta 改變圖片亮度
alpha_slider_max = 100
title_window = 'Linear Blend'
def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    
    new_image = np.zeros(src1.shape, src1.dtype)
    new_image = cv.convertScaleAbs(src1, alpha=alpha, beta=beta)#使用迴圈方式太慢會當掉
    #dst = cv.addWeighted(src1, alpha, new_image, beta, 0.0)
    cv.imshow(title_window, new_image)
image="one_piece.jpg"
src1 = cv.imread(image)


cv.namedWindow(title_window)
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv.waitKey()