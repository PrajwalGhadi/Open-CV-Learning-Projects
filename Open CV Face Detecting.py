'''
Aim - Face Detection using OpenCv
Date - 12-11-2021
Author - Prajwal Ghadi
'''

import cv2
import numpy as np

facecascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/Lenna_(test_image).png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = facecascade.detectMultiScale(imgGray, 2, 4)
### Creating Bounding Box on Face
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("output", img)
cv2.waitKey(0)