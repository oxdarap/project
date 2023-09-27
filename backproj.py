from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

def calculate_histogram_and_backproj(val):
    bins = val
    histSize = max(bins, 2)
    ranges = [0, 180]  # hue_range

    hist = cv.calcHist([hue], [0], None, [histSize], ranges, accumulate=False)
    cv.normalize(hist, hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

    backproj = cv.calcBackProject([hue], [0], hist, ranges, scale=1)

    cv.imshow('BackProj', backproj)

    w = 400
    h = 400
    bin_w = int(round(w / histSize))
    histImg = np.zeros((h, w, 3), dtype=np.uint8)
    for i in range(bins):
        cv.rectangle(histImg, (i * bin_w, h), ((i + 1) * bin_w, h - int(np.round(hist[i] * h / 255.0))),
                     (0, 0, 255), cv.FILLED)
    cv.imshow('Histogram', histImg)


parser = argparse.ArgumentParser(description='Code for Back Projection tutorial.')
parser.add_argument('--input', help='Path to input image.', default='block.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
ch = (0, 0)
hue = np.empty(hsv.shape, hsv.dtype)
cv.mixChannels([hsv], [hue], ch)
window_image = 'Source image'
cv.namedWindow(window_image)
bins = 25
cv.createTrackbar('* Hue  bins: ', window_image, bins, 180, calculate_histogram_and_backproj)
calculate_histogram_and_backproj(bins)
cv.imshow(window_image, src)
cv.waitKey()
