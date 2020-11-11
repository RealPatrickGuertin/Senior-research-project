import cv2 
import CV2_func
import numpy as np
import matplotlib.pyplot as plt
import time

### Take in relative path ###
#fileDir_1 = input("input directory of images: ")
cascade = "Resources/haarcascade_frontalface_default.xml"
fileDir_SET1 = "Resources/Images/Set_1"
fileDir_SET2 = "Resources/Images/Set_2"
fileDir_SET3 = "Resources/Images/Set_3"
waitTime = int(input("how long should each image stay on screen in ms? (0: until manually close)"))
faceCascade_1 = cv2.CascadeClassifier(cascade)

numFaces = []
numFaceHits = []
numDoubles = []
numFaceMiss = []
numErrors = []
errorPercent = []
runtimes = []
sets = [fileDir_SET1, fileDir_SET2, fileDir_SET3]

### Loop through the sets of images
it = 0
for set_i in sets:
    ### get start and end time of program run for runtime analysis ###
    start_time = time.time()
    CV2_func.FindFace(set_i, faceCascade_1, waitTime)
    end_time = time.time() - start_time
    runtimes.append(end_time)

    ### Values for error analysis ###
    numFaces.append(CV2_func.numFaces)
    numFaceHits.append(CV2_func.numFaceHits)
    numDoubles.append(CV2_func.numDoubles)
    numFaceMiss.append(numFaces[it] - numFaceHits[it])       # did not detect a face at all (not allowed in this set)
    numErrors.append(numFaceMiss[it] + numDoubles[it])       # did not detect a face or had multiple hits (not allowed in this set)
    errorPercent.append((numErrors[it] / numFaces[it])*100)

    print("Number of Faces  : ", numFaces)
    print("Number of Misses : ", numFaceMiss)
    print("Number of Doubles: ", numDoubles)
    print("Number of Errors : ", numErrors)
    print("Total Error %    : ", errorPercent, "%")
    print("Time Elapsed     : ",  end_time)

    it += 1
