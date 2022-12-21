import cv2
import numpy as np


imgA = np.ones((100,150,3), np.uint8)
cv2.imshow("Image Array",imgA)
cv2.waitKey(0)

imgB = np.ones((100,150,3), np.uint8)
imgB[:,:] = 155,155,155
cv2.imshow("Image Color",imgB)
cv2.waitKey(0)

imgC = np.ones((100,150,3), np.uint8)
imgC[50:70,25:80] = 255,0,0
cv2.imshow("Image Segment Color",imgC)
cv2.waitKey(0)

imgD = np.ones((100,150,3), np.uint8)
cv2.line(imgD, (0,0),(imgD.shape[1],imgD.shape[0]),(0,255,0))
cv2.imshow("Image Line",imgD)
cv2.waitKey(0)


imgE = np.ones((100,150,3), np.uint8)
# use cv2.FILLED in tickness for completed draw rectangle
cv2.rectangle(imgE, (25,25),(80,50),(0,0,255), 10)
cv2.imshow("Image Rectangle",imgE)
cv2.waitKey(0)

imgF = np.ones((100,150,3), np.uint8)
cv2.circle(imgF, (50,50),20,(255,255,0), 5)
cv2.imshow("Image Circle",imgF)
cv2.waitKey(0)

imgG = np.ones((100,150,3), np.uint8)
cv2.putText(imgG,"OpenCV",(50,50),cv2.FONT_HERSHEY_PLAIN, 1 ,(0,255,255), 2)
cv2.imshow("Image Put Text",imgG)
cv2.waitKey(0)