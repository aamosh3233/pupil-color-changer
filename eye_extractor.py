from  color_swap import eyes
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

def rect_to_bb(rect):

    # take a bounding predicted by dlib and convert it
    # to the format (x, y, w, h) as we would normally do
    # with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    # return a tuple of (x, y, w, h)
    return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)
    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords

# construct the argument parser and parse the arguments

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
image = cv2.imread('brown_eyes.jpg')
image = imutils.resize(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)
right_roi=[]
left_roi=[]

overlay=[]
for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    right_roi=image[shape[43][1]:shape[46][1],shape[43][0]:shape[46][0]]

    left_roi=image[shape[37][1]:shape[47][1],shape[37][0]:shape[40][0]]
    EYE = eyes(image, shape)
    overlay=EYE.transform_color(shape)

print('overlay shape==',overlay.shape)
overlay=cv2.cvtColor(overlay,cv2.COLOR_BGRA2BGR)
cv2.imwrite('output.jpg',overlay)
cv2.imshow('original ',image)
cv2.imshow('overlay', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
