import cv2
image = cv2.imread('block.png')
if image is None:
 sys.exit("image reading error")
resize = cv2.resize(image,(250,250))
(rows,colls) = image.shape[:2]
center = (colls // 2,rows // 2)
rotate_mat = cv2.getRotationMatrix2D(center,50,1)
rotate = cv2.warpAffine(image, rotate_mat, (colls, rows))
flip = cv2.flip(image, 0)
cv2.imshow('original',image)
cv2.imshow('resized',resize)
cv2.imshow('rotated',rotate)
cv2.imshow('flipped',flip)
cv2.waitKey(0)
cv2.destroyAllWindows()