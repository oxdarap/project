import sys
import cv2 as cv

def main(argv):
    kernel_size = 3
    window_name = "Laplace Demo"

    imageName = argv[0] if len(argv) > 0 else 'block.png'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)

    if src is None:
        print('Error opening image')
        print('Program Arguments: [image_name -- default block.png]')
        return -1

    src = cv.GaussianBlur(src, (3, 3), 0)
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    dst = cv.Laplacian(src_gray, cv.CV_16S, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst, alpha=3.0, beta=0)

    cv.imshow(window_name, abs_dst)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
