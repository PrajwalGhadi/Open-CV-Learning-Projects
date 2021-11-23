'''Aim - Document Scanner using Open CV
Date - 12-11-2021
Author - Prajwal Ghadi'''

import cv2
import numpy as np

WidthImg = 640
HeightImg = 500

cap = cv2.VideoCapture(0)
cap.set(3, WidthImg)
cap.set(4, HeightImg)
cap.set(10, 500)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
    imgCanny = cv2.Canny(img, 100, 100)
    imgDial = cv2.dilate(imgCanny, (5, 5), iterations=2)
    imgThreshold = cv2.erode(img, (5, 5), iterations= 1)

    return imgThreshold

while True:
    success, img = cap.read()
    img = cv2.resize(img, (WidthImg, HeightImg))
    imgThres = preProcessing(img)
    cv2.imshow("Result", imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break