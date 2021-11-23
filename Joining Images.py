'''Aim - Joining images in Horizontal or Vertical Stack
Date - 10-11-2021
Author - Prajwal Ghadi'''

import cv2
import numpy as np

img = cv2.imread("Resources/Lenna_(test_image).png")

hor_imgs = np.hstack((img, img))
ver_imgs = np.vstack((img, img))

cv2.imshow("output", hor_imgs)
cv2.imshow("output", ver_imgs)
cv2.waitKey(0)
