from __future__ import print_function
import sys
import cv2 as cv

use_mask = False
img = None
templ = None
mask = None
image_window = "Source Image"
result_window = "Result window"
match_method = 0
max_Trackbar = 5

def main(argv):
    global img, templ, use_mask, mask
    img = cv.imread('smarties.png', cv.IMREAD_COLOR)
    templ = cv.imread('template.png', cv.IMREAD_COLOR)

    if img is None or templ is None:
        print("Can't read one of the images")
        return -1

    cv.namedWindow(image_window, cv.WINDOW_AUTOSIZE)
    cv.namedWindow(result_window, cv.WINDOW_AUTOSIZE)

    trackbar_label = 'Method: \n 0: SQDIFF \n 1: SQDIFF NORMED \n 2: TM CCORR \n 3: TM CCORR NORMED \n 4: TM COEFF \n 5: TM COEFF NORMED'
    cv.createTrackbar(trackbar_label, image_window, match_method, max_Trackbar, MatchingMethod)

    MatchingMethod(match_method)

    cv.waitKey(0)
    return 0

def MatchingMethod(param):
    global match_method
    match_method = param
    img_display = img.copy()

    method_accepts_mask = (cv.TM_SQDIFF == match_method or match_method == cv.TM_CCORR_NORMED)

    if use_mask and method_accepts_mask:
        result = cv.matchTemplate(img, templ, match_method, None, mask)
    else:
        result = cv.matchTemplate(img, templ, match_method)

    cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)

    _minVal, _maxVal, minLoc, maxLoc = cv.minMaxLoc(result, None)

    if match_method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        matchLoc = minLoc
    else:
        matchLoc = maxLoc

    cv.rectangle(img_display, matchLoc, (matchLoc[0] + templ.shape[1], matchLoc[1] + templ.shape[0]), (0, 0, 255), 2, 8, 0)
    cv.rectangle(result, matchLoc, (matchLoc[0] + templ.shape[1], matchLoc[1] + templ.shape[0]), (0, 0, 255), 2, 8, 0)
    cv.imshow(image_window, img_display)
    cv.imshow(result_window, result)

if __name__ == "__main__":
    main(sys.argv[1:])
