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


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            #draws the line on the image (blue)
            cv2.line(line_image, (x1,y1), (x2,y2), (255, 0, 0), 10)
    return line_image






def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200,height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) 
    return masked_image




#imports the image
image = cv2.imread('test_image.jpg')

#verify we can see the image (3d array)
# print('base image')
# print(image)

#copy the array into a new var
lane_image = np.copy(image)

canny = canny(lane_image)
cropped_image = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)


#show the image
cv2.imshow('result', combo_image)

#show the image indefinitely until keypress
cv2.waitKey(0)