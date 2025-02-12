import cv2 as cv
import numpy as np

kernel = np.array((
    [1, 1, 1],
    [1, -1, -1],
    [1, 1, -1]), dtype="int")

input_image = np.array((
    [0, 0, 0, 0, 255, 255, 255, 0],
    [0, 255, 255, 0, 255, 0, 0, 255],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 255, 255, 0],
    [0, 255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")

output_image = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel)

rate = 50

kernel_display = (kernel + 1) * 127
kernel_display = np.uint8(kernel_display)
kernel_display = cv.resize(kernel_display, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)

input_image_display = cv.resize(input_image, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
output_image_display = cv.resize(output_image, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)

cv.imshow("Kernel", kernel_display)
cv.moveWindow("Kernel", 0, 0)

cv.imshow("Original", input_image_display)
cv.moveWindow("Original", 0, 200)

cv.imshow("Hit or Miss", output_image_display)
cv.moveWindow("Hit or Miss", 500, 200)

cv.waitKey(0)
cv.destroyAllWindows()
