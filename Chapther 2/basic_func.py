import cv2
import numpy as np
DIR_IMAGES = '../images/'

img = cv2.imread(DIR_IMAGES + 'image_21.jpeg')

kernel = np.ones((5,5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(15,15),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(img, kernel, iterations=1)
imgEroded = cv2.erode(img, kernel, iterations=1)



cv2.imshow("Grey Image",imgGrey)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)