import cv2

def sobel(img):
    dst = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    dst = cv2.convertScaleAbs(dst)
    return dst
Ac=cv2.imread("one_piece.jpg")
Bc=cv2.imread("images.jpg")
Bc=cv2.resize(Bc,(Ac.shape[1],Ac.shape[0]))
Fused_1=Ac+Bc

Fused_2=Ac.copy()
Ag=cv2.cvtColor(Ac,cv2.COLOR_RGB2GRAY)
Bg=cv2.cvtColor(Bc,cv2.COLOR_RGB2GRAY)
As=sobel(Ag)
Bs=sobel(Bg)
for x in range(As.shape[1]):
    for y in range(Bs.shape[0]):
        if(As[y][x]<Bs[y][x]):
            Fused_2[y][x]=Bc[y][x]
cv2.imshow("img",Fused_1)
cv2.imshow("img_2",Fused_2)
cv2.waitKey(0)