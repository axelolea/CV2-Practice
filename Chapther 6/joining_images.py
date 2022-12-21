import cv2
import numpy as np

DIR_IMAGES = '../images/'


img = cv2.imread(DIR_IMAGES + 'image_21.jpeg')


imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

width = img.shape[1] #173
height = img.shape[0] #292


cv2.imshow("Horizontal Image",imgHor)
cv2.imshow("Vertical Image",imgVer)
cv2.waitKey(0)