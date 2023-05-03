import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def hist(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    return cdf_normalized

img=cv.imread('one_piece.jpg',0)
equ = cv.equalizeHist(img)#均質化
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cdf_normalized_orginal=hist(img)
cdf_normalized_equ=hist(equ)
cdf_normalized_clahe=hist(cl1)
#######################################################
plt.subplot(3,2,1)
plt.title("Orginal_image")
plt.imshow(img,cmap='gray')
plt.subplot(3,2,2)
plt.title("Orginal_histrogram")
plt.plot(cdf_normalized_orginal, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
#######################################################
plt.subplot(3,2,3)
plt.title("Equlization_image")
plt.imshow(equ,cmap='gray')
plt.subplot(3,2,4)
plt.title("Equlization_histrogram")
plt.plot(cdf_normalized_equ, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

########################################################
plt.subplot(3,2,5)
plt.title("Clahe_image")
plt.imshow(cl1,cmap='gray')
plt.subplot(3,2,6)
plt.title("Clahe_histrogram")
plt.plot(cdf_normalized_clahe, color = 'b')
plt.hist(cl1.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()