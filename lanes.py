import cv2
import numpy as np
import matplotlib.pyplot as plt

#canny function takes in an image
def canny(image):
    #convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    #verify it turned gray
    # print('gray')
    # print(gray)

    blur = cv2.GaussianBlur(gray, (5,5),0)

    #verify it applies Gaussian Blur
    # print('blur')
    # print(blur)


    #canny looks at the gradient by calculating the
    #derivative between cells
    canny = cv2.Canny(blur,50,150)

    #verify it uses canny
    # print('canny')
    # print(canny)

    return canny




#imports the image
image = cv2.imread('test_image.jpg')

#verify we can see the image (3d array)
# print('base image')
# print(image)

#copy the array into a new var
lane_image = np.copy(image)

canny = canny(lane_image)




#show the image
plt.imshow(canny)

#show the image indefinitely until keypress
plt.show()