import cv2 as cv
import numpy as np

def display_image(window_name, image, delay=3000):
    cv.imshow(window_name, image)
    cv.waitKey(delay)
    cv.destroyWindow(window_name)

if __name__ == "__main__":
    # Read and resize image
    image = cv.resize(cv.imread("src.png"), [1200, 446])

    # Change color palette to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    display_image("Original", image)

    # Invert the grayscale image
    gray_inverted = cv.bitwise_not(gray)
    display_image("Gray", gray_inverted)

    # Apply binary thresholding on the inverted grayscale image
    gray_threshold_binary = cv.adaptiveThreshold(gray_inverted, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                                  cv.THRESH_BINARY, 11, -2)
    display_image("Threshold Binary", gray_threshold_binary)

    # Extract horizontal and vertical information
    horizontal = np.copy(gray_threshold_binary)
    vertical = np.copy(gray_threshold_binary)

    cols = horizontal.shape[1]
    horizontal_size = cols // 230

    # Create a horizontal line as a kernel
    horizontal_structure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    # Decrease the size of objects in the image
    horizontal = cv.erode(horizontal, horizontal_structure)
    # Increase the size of all horizontal lines in the objects
    horizontal = cv.dilate(horizontal, horizontal_structure)

    display_image("Horizontal", horizontal)

    rows = vertical.shape[0]
    vertical_size = rows // 75

    # Create a vertical line as a kernel
    vertical_structure = cv.getStructuringElement(cv.MORPH_RECT, (1, vertical_size))

    # Decrease the size of objects in the image
    vertical = cv.erode(vertical, vertical_structure)
    # Increase the size of all vertical lines in the objects
    vertical = cv.dilate(vertical, vertical_structure)

    display_image("Vertical", vertical)

    # Create edges of objects on the thresholded image
    edges = cv.adaptiveThreshold(gray_threshold_binary, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                 cv.THRESH_BINARY, 3, -2)

    display_image("Edges", edges, delay=0)
