import cv2 
import numpy as np
import time
import CV2_func

### Take in relative path ###
#fileDir_1 = input("input directory of images: ")
fileDir_1 = "Resources/Images/Set_1"
waitTime = int(input("how long should each image stay on screen in ms? (0: until manually close)"))
faceCascade_1 = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

### get start time of program run for runtime analysis ###
start_time = time.time()

### Call function to find faces ###
CV2_func.FindFace(fileDir_1, faceCascade_1, waitTime)

numFaces = CV2_func.numFaces
numFaceHits = CV2_func.numFaceHits
numDoubles = CV2_func.numDoubles

numFaceMiss = numFaces - numFaceHits        # did not detect a face at all (not allowed in this set)
numErrors = numFaceMiss + numDoubles        # did not detect a face or had multiple hits (not allowed in this set)

print("Number of Faces  : ", numFaces)
print("Number of Misses : ", numFaceMiss)
print("Number of Doubles: ", numDoubles)
print("Number of Errors : ", numErrors)
print("Total Error %    : ", (numErrors / numFaces)*100, "%")
print("Time Elapsed     :  %s Seconds" % (time.time() - start_time))    ### Print out the calculated runtime ###
