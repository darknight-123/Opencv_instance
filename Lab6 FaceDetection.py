import cv2
  
# Reading the image
cap = cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    # Converting image to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Loading the required haar-cascade xml classifier file
    haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml')
    
    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
    
    # Iterating through rectangles of detected faces
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Detected faces', frame)
    cv2.waitKey(50)
  
