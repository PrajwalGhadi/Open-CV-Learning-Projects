'''Aim - By using openCV i tried to create an Shapes and text on image
Date = 9-11-2021
Author - Prajwal Ghadi '''

import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
print(img)
img[:] = 250,0,0
cv2.line(img, (0,0), (300, 300), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (200, 300), (0, 255, 0), 3)
cv2.circle(img, (450, 50), 50, (0, 0, 0), 3)
cv2.putText(img, "Learning OpenCV", (200, 200), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 150, 0), 3)
cv2.imshow("Image", img)
cv2.waitKey(0)