import cv2
import os
import numpy as np
import time
import CV2_func

### Take in relative path ###
#fileDir_1 = input("input directory of images: ")
fileDir_1 = "Resources/Images/Set_1"
faceCascade_1 = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

### get start time of program run for runtime analysis ###
start_time = time.time()

CV2_func.FileRead(fileDir_1, faceCascade_1)

numFaces = CV2_func.numFaces
numFaceHits = CV2_func.numFaceHits
numDoubles = CV2_func.numDoubles

numFaceMiss = numFaces - numFaceHits        # did not detect a face at all (not allowed in this set)
numErrors = numFaceMiss + numDoubles        # did not detect a face or had multiple hits (not allowed in this set)

print("Number of faces  : ", numFaces)
print("Number of Misses : ", numFaceMiss)
print("Number of doubles: ", numDoubles)
print("Number of errors : ", numErrors)
print("Percent Error    : ", (numErrors / numFaces)*100, "%")
print("--- %s seconds ---" % (time.time() - start_time))    ### Print out the calculated runtime ###
