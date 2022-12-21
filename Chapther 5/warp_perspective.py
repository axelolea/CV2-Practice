import cv2
import numpy as np

DIR_IMAGES = '../images/'

img = cv2.imread(DIR_IMAGES + 'image_21.jpeg')

width = img.shape[1] #173
height = img.shape[0] #292

pts1 = np.float32([[10,50],[150,80],[30,200],[150,230]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_out = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image Warp Perspective",img_out)
cv2.waitKey(0)