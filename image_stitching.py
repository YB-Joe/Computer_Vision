import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


def detect_local_features(img):
    # grady scaale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # SIFT to detect features
    sift = cv2.xfeatures2d.SIFT_create()
    # key points and descriptors from sift
    kp, des = sift.detectAndCompute(img_gray, None)
    return kp, des
'''
def match_key_points(keyPoints1, keyPoints2, [descriptors1], [descriptors2]):
    BFM = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    match = BFM.match(descriptors1, descriptors2)
    image1 = []
    image2 = []
    # for matching
    for mat in matches:
        image1_match = mat.trainIdx
        image2_match = mat.queryIdx
        p1 = descriptors1[image1_match].pt
        p2 = descriptors2[image2_match].pt
        image1.append(p1)
        image2.append(p2)
    return image1, image2
'''
def match_key_points(keyPoints1, keyPoints2, [descriptors1], [descriptors2]):
    # defined the threshold
    threshold = 0.6

def main():
    # read images
    img_a = cv2.imread('pictures/keble_a.jpg', 1)
    img_b = cv2.imread('pictures/keble_b.jpg', 1)
    img_c = cv2.imread('pictures/keble_c.jpg', 1)

if __name__ == "__main__":
    main()
