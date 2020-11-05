import cv2
import os
import numpy as np

for filename in os.listdir("images"):
    if filename.endswith(".jpg"):
        print(filename)
        img = cv2.imread("images/" + filename)
        cv2.imshow("output", img)
        cv2.waitKey(1)
