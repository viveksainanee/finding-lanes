import cv2
import numpy as np

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

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200,height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask




#imports the image
image = cv2.imread('test_image.jpg')

#verify we can see the image (3d array)
# print('base image')
# print(image)

#copy the array into a new var
lane_image = np.copy(image)

canny = canny(lane_image)




#show the image
cv2.imshow('result', region_of_interest(canny))

#show the image indefinitely until keypress
cv2.waitKey(0)