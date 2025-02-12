
import sys
import cv2 as cv
import numpy as np

def main(argv):
    window_name = 'filter2D Demo'

    imageName = argv[0] if len(argv) > 0 else 'block.png'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    if src is None:
        print('Error opening image!')
        print('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1

    ddepth = -1

    ind = 0
    while True:
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.array([[-1, -1, -1],
                            [-1,  9, -1],
                            [-1, -1, -1]], dtype=np.float32)

        dst = cv.filter2D(src, ddepth, kernel)

        cv.imshow(window_name, dst)
        c = cv.waitKey(500)
        if c == 27:
            break
        ind += 1

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
