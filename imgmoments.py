from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import random as rng

rng.seed(12345)


def thresh_callback(val):
    threshold = val

    canny_output = cv.Canny(src_gray, threshold, threshold * 2)

    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    mu = [cv.moments(cnt) for cnt in contours]
    mc = [(m['m10'] / (m['m00'] + 1e-5), m['m01'] / (m['m00'] + 1e-5)) for m in mu]

    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

    for i, color in enumerate([(rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256)) for _ in contours]):
        cv.drawContours(drawing, contours, i, color, 2)
        cv.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)

    cv.imshow('Contours', drawing)

    for i, m in enumerate(mu):
        print(' * Contour[{}] - Area (M_00) = {:.2f} - Area OpenCV: {:.2f} - Length: {:.2f}'.format(i, m['m00'],
                                                                                                    cv.contourArea(
                                                                                                        contours[i]),
                                                                                                    cv.arcLength(
                                                                                                        contours[i],
                                                                                                        True)))


parser = argparse.ArgumentParser(description='Code for Image Moments tutorial.')
parser.add_argument('--input', help='Path to input image.', default='stuff.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3, 3))
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100
cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)
cv.waitKey()
