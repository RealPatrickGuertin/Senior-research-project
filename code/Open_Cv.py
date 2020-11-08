import cv2
import os
import numpy as np
import time

### Take in relative path ###

#fileDir = input("input file Directory: ")
fileDir = "images"

### get start time of program run for runtime analysis ###
start_time = time.time()

### function for reading in files of specified path ###
def FileRead(FileDir):
    for filename in os.listdir(fileDir):
        if filename.endswith(".jpg"):
            print(filename)
            img = cv2.imread(FileDir + "/" + filename)
            cv2.imshow("output", img)
            cv2.waitKey(10)

### use read file function ###
FileRead(fileDir)

### Print out the calculated runtime ###
print("--- %s seconds ---" % (time.time() - start_time))
