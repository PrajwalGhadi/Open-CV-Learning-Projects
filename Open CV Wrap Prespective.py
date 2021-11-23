'''Aim - Separating Selected part from the Original image
Date - 9-11-2021
Author - Prajwal Ghadi'''
import cv2
import numpy as np

img = cv2.imread("Resources/Cards.jpg")

width, height = 300, 500

pts1 = np.float32([[109,161], [218, 161], [109, 324], [219, 324]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
impOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("output", impOutput)

cv2.waitKey(0)