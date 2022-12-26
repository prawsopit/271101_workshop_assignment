#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
import numpy as np
import math


    
    

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 =  int(id)
                    cy15 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                 

            if cx4 > cx3 : 
                cv2.putText(img, "thumb", (10, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 161, 252), 3)
            

            if cy7 > cy8:
                cv2.putText(img, "index", (10, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (228, 103, 109), 3)
            
            if cy11 > cy12:
                cv2.putText(img, "middle", (10, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                (236, 85, 165), 3)

            if cy15 > cy16:
                cv2.putText(img, "ring", (10, 250), cv2.FONT_HERSHEY_PLAIN, 3,
                (126, 12, 284), 3)

            if cy19 > cy20:
                cv2.putText(img, "little", (10, 300), cv2.FONT_HERSHEY_PLAIN, 3,
                (118, 37, 251), 3)
            
            else:
                Nfing = 5
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    
    cv2.imshow("Image", img)
    k =cv2.waitKey(1)
    if k == ord('q'):
        break

    
#Closeing all open windows
#cv2.destroyAllWindows()