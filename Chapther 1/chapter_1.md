# Introducing a OpenCV Module

The OpenCV( Open Source Computer Vision) is a library of Python bindings designed to solve computer vision problems.

## Install and import Module

>Install cv2 module with pip

```bash
pip install opencv-python
```

Impoty module in your project

```python
#Import the cv2 module, and rename 'cv'
import cv2 as cv
```

### Read a image file
```python
#Read the image file
img = cv.imread(DIR_IMAGES + 'image_01.png')

#Open new window with show a img[array]
cv.imshow("Img CV2", img)

#Wait a press key for next de process
cv.waitKey(0)
```
> Result:
> ![Result Code](./../images/results/result_01.png)

Line code for closing image

```python
#Close Windows
cv.destroyWindow('Img CV2')
```

## Read a video file

```python

```