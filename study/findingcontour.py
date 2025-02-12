from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random

def thresh_callback(val):
    threshold = val
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
    cv.imshow('Contours', drawing)

src = cv.imread('block.png')

if src is None:
    print('Could not open or find the image')
    exit(0)

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100
cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)

cv.waitKey()
