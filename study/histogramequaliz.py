from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='block.png')
args = parser.parse_args()

src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src_gray)

cv.imshow('Source image', src_gray)
cv.imshow('Equalized Image', dst)
cv.waitKey()
