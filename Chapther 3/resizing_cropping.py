import cv2

DIR_IMAGES = '../images/'

def resize_image():
    img = cv2.imread(DIR_IMAGES + 'image_01.jpeg')
    width = 200
    height = 150
    imgResize = cv2.resize(img,(width, height))
    cv2.imshow("Img Original", img)
    cv2.imshow("Img Resize", imgResize)
    cv2.waitKey(0)

resize_image()

def cropping_image():
    img = cv2.imread(DIR_IMAGES + 'image_01.jpeg')
    imgCropped = img[0:200, 200:500]
    cv2.imshow("Img Cropped", imgCropped)
    cv2.waitKey(0)

cropping_image()