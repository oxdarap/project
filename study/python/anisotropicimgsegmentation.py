import cv2 as cv
import numpy as np
import argparse

W = 52
C_Thr = 0.43
LowThr = 35
HighThr = 57


def calcGST(inputIMG, w):
    img = inputIMG.astype(np.float32)
    imgDiffX = cv.Sobel(img, cv.CV_32F, 1, 0, 3)
    imgDiffY = cv.Sobel(img, cv.CV_32F, 0, 1, 3)
    imgDiffXY = cv.multiply(imgDiffX, imgDiffY)

    imgDiffXX = cv.multiply(imgDiffX, imgDiffX)
    imgDiffYY = cv.multiply(imgDiffY, imgDiffY)
    J11 = cv.boxFilter(imgDiffXX, cv.CV_32F, (w, w))
    J22 = cv.boxFilter(imgDiffYY, cv.CV_32F, (w, w))
    J12 = cv.boxFilter(imgDiffXY, cv.CV_32F, (w, w))

    tmp1 = J11 + J22
    tmp2 = J11 - J22
    tmp2 = cv.multiply(tmp2, tmp2)
    tmp3 = cv.multiply(J12, J12)
    tmp4 = np.sqrt(tmp2 + 4.0 * tmp3)
    lambda1 = 0.5 * (tmp1 + tmp4)
    lambda2 = 0.5 * (tmp1 - tmp4)

    imgCoherencyOut = cv.divide(lambda1 - lambda2, lambda1 + lambda2)

    imgOrientationOut = cv.phase(J22 - J11, 2.0 * J12, angleInDegrees=True)
    imgOrientationOut = 0.5 * imgOrientationOut

    return imgCoherencyOut, imgOrientationOut


parser = argparse.ArgumentParser(description='Code for Anisotropic image segmentation tutorial.')
parser.add_argument('-i', '--input', help='Path to input image.', default='block.png')
args = parser.parse_args()

imgIn = cv.imread(args.input, cv.IMREAD_GRAYSCALE)

if imgIn is None:
    print('Could not open or find the image: {}'.format(args.input))
    exit(0)

imgCoherency, imgOrientation = calcGST(imgIn, W)
_, imgCoherencyBin = cv.threshold(imgCoherency, C_Thr, 255, cv.THRESH_BINARY)
_, imgOrientationBin = cv.threshold(imgOrientation, LowThr, HighThr, cv.THRESH_BINARY)
imgBin = cv.bitwise_and(imgCoherencyBin, imgOrientationBin)
imgCoherency = cv.normalize(imgCoherency, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
imgOrientation = cv.normalize(imgOrientation, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
cv.imshow('result.jpg', np.uint8(0.5 * (imgIn + imgBin)))
cv.imshow('Coherency.jpg', imgCoherency)
cv.imshow('Orientation.jpg', imgOrientation)
cv.waitKey(0)
