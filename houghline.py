import sys
import cv2 as cv
import numpy as np


def main(argv):
    default_file = 'block.png'
    filename = argv[0] if len(argv) > 0 else default_file
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Error opening image!')
        print('Usage: hough_lines.py [image_name -- default ' + default_file + ']')
        return -1

    dst = cv.Canny(src, 50, 200, None, 3)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho, theta = lines[i][0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow('Source', src)
    cv.imshow('Detected Lines (in red) - Standard Hough Line Transform', cdst)
    cv.imshow('Detected Lines (in red) - Probabilistic Line Transform', cdstP)

    cv.waitKey()
    return 0


if __name__ == '__main__':
    main(['sudoku.png'])
