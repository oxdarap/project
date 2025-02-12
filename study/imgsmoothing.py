import sys
import cv2 as cv
import numpy as np

DELAY_CAPTION = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31
window_name = 'Smoothing Demo'

def main(argv):
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    imageName = argv[0] if len(argv) > 0 else 'block.png'
    src = cv.imread(cv.samples.findFile(imageName))

    if src is None:
        print('Error opening image')
        print('Usage: smoothing.py [image_name -- default ../data/lena.jpg] \n')
        return -1

    display_image('Original Image', src, DELAY_CAPTION)

    # Applying different types of blur
    apply_blur(src, 'Homogeneous Blur', cv.blur)
    apply_blur(src, 'Gaussian Blur', cv.GaussianBlur)
    apply_median_blur(src)
    apply_blur(src, 'Bilateral Blur', cv.bilateralFilter)

    # Done
    display_image('Done!', src, 0)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0

def display_image(caption, image, delay):
    temp_image = np.copy(image)
    rows, cols, _ = image.shape
    cv.putText(temp_image, caption, (int(cols / 4), int(rows / 2)),
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.imshow(window_name, temp_image)
    cv.waitKey(delay)

def apply_blur(image, blur_type, blur_function):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        if blur_type == 'Bilateral Blur':
            result = blur_function(image, i, i * 2, i / 2)
        else:
            result = blur_function(image, (i, i), 0)

        display_image(blur_type, result, DELAY_BLUR)

def apply_median_blur(image):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        result = cv.medianBlur(image, i)
        display_image('Median Blur', result, DELAY_BLUR)

if __name__ == "__main__":
    main(sys.argv[1:])
