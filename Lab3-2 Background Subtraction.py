import cv2
import numpy as np
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
#fourcc = cv2.VideoWriter_fourcc(*'XVID')          # 設定影片的格式為 MJPG
#out = cv2.VideoWriter('output_2.avi', fourcc, 60.0, (460,  640))  # 產生空的影片
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("can't not open camera")
    exit()
while(True):
    ret,img=cap.read()
    
    if not ret:
        break
    org=img
    arr=np.zeros((480,640,3),dtype=int)
    #output = cv2.Laplacian(img, -1, 1, 5)
    
    fgmask=fgbg.apply(img)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    arr_min_max=[]
    for x in range(fgmask.shape[1]):
        max=-1
        min=-1
        for y in range(fgmask.shape[0]):
            
            if fgmask[y][x]!=0 and min==-1 :
                min=y
                
            if  fgmask[y][x]!=0 and min!=-1:
                max=y
        if min!=-1:
            if max==-1:
                max=fgmask.shape[0]        
            arr_min_max.append((x,min,max))    
            
    for t in range(len(arr_min_max)):
        
        for y in range(arr_min_max[t][1],arr_min_max[t][2]):
            
                arr[y][arr_min_max[t][0]]=org[y][arr_min_max[t][0]] 

            
    cv2.imshow("Windows",np.uint8(arr))
    #out.write(np.uint8(arr))
    cv2.waitKey(50)
#out.release()
cap.release()   