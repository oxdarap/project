import sys
import cv2 as cv
import numpy as np
from random import randint

def main(argv):
    borderType = cv.BORDER_CONSTANT
    window_name = "copyMakeBorder Demo"

    image_name = argv[0] if len(argv) > 0 else 'block.png'
    # Load an image
    src = cv.imread(cv.samples.findFile(image_name), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: copy_make_border.py [image_name -- default block.png] \n')
        return -1

    print('\n'
          '\t copyMakeBorder Demo: \n'
          ' -------------------- \n'
          ' ** Press \'c\' to set the border to a random constant value \n'
          ' ** Press \'r\' to set the border to be replicated \n'
          ' ** Press \'ESC\' to exit the program ')

    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    top = int(0.05 * src.shape[0])  # shape[0] = rows
    bottom = top
    left = int(0.05 * src.shape[1])  # shape[1] = cols
    right = left

    while True:
        value = [randint(0, 255), randint(0, 255), randint(0, 255)]

        dst = cv.copyMakeBorder(src, top, bottom, left, right, borderType, None, value)

        cv.imshow(window_name, dst)

        key = cv.waitKey(500)
        if key == 27:
            break
        elif key == 99:  # 99 = ord('c')
            borderType = cv.BORDER_CONSTANT
        elif key == 114:  # 114 = ord('r')
            borderType = cv.BORDER_REPLICATE

    return 0

if __name__ == "__main__":
    main(['block.png'])
