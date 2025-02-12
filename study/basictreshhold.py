from __future__ import print_function
import cv2 as cv
import argparse

max_value = 255
max_type = 4
max_binary_value = 255
window_name = 'Threshold Demo'


def Threshold_Demo(val):
    threshold_type = cv.getTrackbarPos(
        'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted', window_name)
    threshold_value = cv.getTrackbarPos('Value', window_name)

    if threshold_type == 0:
        _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, cv.THRESH_BINARY)
    elif threshold_type == 1:
        _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, cv.THRESH_BINARY_INV)
    elif threshold_type == 2:
        _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, cv.THRESH_TRUNC)
    elif threshold_type == 3:
        _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, cv.THRESH_TOZERO)
    else:
        _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, cv.THRESH_TOZERO_INV)

    cv.imshow(window_name, dst)


parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='block.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

# Convert the image to Gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.namedWindow(window_name)
cv.createTrackbar('Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted',
                  window_name, 0, max_type, Threshold_Demo)
cv.createTrackbar('Value', window_name, 0, max_value, Threshold_Demo)

# Call the function to initialize
Threshold_Demo(0)

# Wait until the user finishes the program
cv.waitKey()
