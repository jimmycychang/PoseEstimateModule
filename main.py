import cv2
import mediapipe as mp
import time
from PoseModule import poseDetector

num = int(input("Number:"))
if 0 <= num <= 32:
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture("1.mp4")
    detector = poseDetector()
        
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (960,540))
        img = detector.findPose(img)
        PosList = detector.findPosition(img, num)

        if len(PosList) != 0:
            print("Number "+str(num)+" Position is: "+str(PosList[num][1:]))

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        cv2.putText(img, ("fps:"+str(int(fps))), (5,30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0),2)                      
        cv2.imshow("image",img)
        key = cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            break
else:
        print("Wrong number, try again!!")