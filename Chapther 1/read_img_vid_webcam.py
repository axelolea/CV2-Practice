import cv2 as cv

# Directories resources
DIR_IMAGES = '..\\src\\images\\'
DIR_VIDEO = '..\\src\\videos\\'

def img_show() -> None:
    """Display the images with CV2 Module.
    """
    img = cv.imread(DIR_IMAGES + 'image_01.png')
    cv.imshow("Img CV2", img)
    cv.waitKey(0)
    cv.destroyWindow('Img CV2')


def vid_show():
    """Display the video with CV2 Module.
    """
    cap = cv.VideoCapture(DIR_VIDEO + 'video_01.mp4')
    while True:
        success, img = cap.read()
        if success:
            cv.imshow('Video CV2', img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyWindow('Video CV2')


def webcam_show():
    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 100)
    while True:
        success, img = cap.read()
        cv.imshow('Webcam CV2', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyWindow('Webcam CV2')

# Envocations functions
img_show()
vid_show()
webcam_show()