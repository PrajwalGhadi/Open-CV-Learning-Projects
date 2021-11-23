# Date: 31-10-2021
# Aim: All content present below is only for study purpose
# Author - Prajwal Ghadi


import cv2
import numpy as np
''' The Below template is used to read or load the image using openCV'''
Image = cv2.imread("Resources/Lenna_(test_image).png")
#
# cv2.imshow("Output", Image)
# cv2.waitKey(0)

''' This template is used to read the video file using openCV'''
# Video = cv2.imread("Resources/Video.mp3")
#
# while True:
#     Success, img = video.read() ### Success variable will take the boolean values & img Variable will take the image
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


'''Creating Gray image'''

# grayImage = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GrayImage", grayImage)
#
#
# '''Blur Image '''
# Kernel = np.ones((7, 7), np.uint8)
# ksize = (7, 7)
# BlurImage = cv2.GaussianBlur(grayImage, ksize, 0)
# cv2.imshow("BlurImage", BlurImage)
# # cv2.waitKey(0)
#
#
#n '''Canny Image'''
# CannyImage = cv2.Canny(grayImage, 150, 200)
# cv2.imshow("CannyImage", CannyImage)
# # cv2.waitKey(0)
#
# '''Dialation Image'''
# DialationImage = cv2.dilate(grayImage, Kernel)
# cv2.imshow("DialationImage", DialationImage)
# # cv2.waitKey(0)
#
# '''Erode Image'''
# ErodeImage = cv2.erode(grayImage, Kernel)
# cv2.imshow("ErodeImage", ErodeImage)
# cv2.waitKey(0)


'''Resizing Image'''

print(Image.shape)  # Checking ImageSize for Cropping or Resizing

CropImage = Image[250: 400, 200:350]

cv2.imshow("Output", Image)
cv2.imshow("CroppedImage", CropImage)
cv2.waitKey(0)

