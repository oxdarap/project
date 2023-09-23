"""
@file sobel_demo.py
@brief Sample code using Sobel and/or Scharr OpenCV functions to make a simple Edge Detector
"""
import sys
import cv2 as cv

def main(argv):
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:\nsobel_demo.py <path_to_image>')
        return -1

    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)

    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    # Increase the brightness of the edges
    brightness_factor = 2.0  # Adjust this value to control brightness
    grad = cv.convertScaleAbs(grad, alpha=brightness_factor, beta=0)

    cv.imshow(window_name, grad)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(['block.png'])  # Using block.png as the image
