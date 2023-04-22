import numpy as np
import cv2
import matplotlib.pyplot as plt
from time import time

def detector(img):
    y1 = 120
    y2 = 160
    mid = int((y1+y2)/2)
    cimg=img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=200,param2=43,minRadius=0,maxRadius=0)
    cv2.line(cimg, (0,y1), (640,y1), (255,0,0), 1)
    cv2.line(cimg, (0,y2), (640,y2), (255,0,0), 1)
    cv2.line(cimg, (0,mid), (640,mid), (0,255,255), 1)
    try:
        circles = np.uint16(np.around(circles))
    except:
        cv2.imshow('output', cimg)
    else:
        for i in circles[0,:]:
            if y1 < i[1] < y2:
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
                cv2.putText(cimg,  str(i[2]), (i[0] , i[1] ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        cv2.imshow('output',cimg)

# Recording section
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('Coins_Counter_Video1.mp4', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)
assert cap.isOpened()
while True:
    start_time = time()
            
    ret, frame = cap.read()
    assert ret
    
    
    detector(frame)
           
    end_time = time()
    fps = 1/np.round(end_time - start_time, 2)
    #print(f"Frames Per Second : {fps}")
     
    cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
    
    #output.write(frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
      
cap.release()
cv2.destroyAllWindows()
