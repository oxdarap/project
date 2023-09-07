import cv2
image = cv2.imread('block.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('original', image)
cv2.imshow('grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
