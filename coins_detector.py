import numpy as np
import cv2
import matplotlib.pyplot as plt
from time import time

def detector(img):
    cimg=img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(3,3),0)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=170,param2=43,minRadius=0,maxRadius=0)
    
    try:
        circles = np.uint16(np.around(circles))
    except:
        cv2.imshow('output', cimg)
    else:
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            cv2.putText(cimg,  str(i[2]), (i[0] , i[1] ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('output',cimg)
    
# Recording section
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('detector1.mp4', fourcc, 20.0, (640, 480))

# Capturing part
cap = cv2.VideoCapture(0)
assert cap.isOpened()
while True:
    start_time = time()
            
    ret, frame = cap.read()
    assert ret
    print(type(frame))        
    detector(frame)
           
    end_time = time()
    fps = 1/np.round(end_time - start_time, 2)
    #print(f"Frames Per Second : {fps}")

    #output.write(frame)       
    cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
 
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
      
cap.release()
output.release()