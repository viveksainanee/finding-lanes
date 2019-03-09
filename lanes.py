import cv2
import numpy as np

#imports the image
image = cv2.imread('test_image.jpg')

#verify it is a 2D array
print(image)

#copy the array into a new var
lane_image = np.copy(image)

#convert to grayscale
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

#verify it turned gray
print(gray)

blur = cv2.GaussianBlur(gray, (5,5),0)

#canny looks at the gradient by calculating the
#derivative between cells
canny = cv2.Canny(blur,50,150)


#show the image
cv2.imshow('result', canny)

#show the image indefinitely until keypress
cv2.waitKey(0)