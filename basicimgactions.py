import cv2
image = cv2.imread('block.png')
if image is None:
 sys.exit("Could not read the image.")
cv2.imshow('block', image)
cv2.waitKey(0)
cv2.destroyAllWindows()