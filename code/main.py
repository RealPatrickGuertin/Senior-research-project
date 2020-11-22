import cv2 
import CV2_func
import numpy as np
import time

### Take in relative path ###
#fileDir_1 = input("input directory of images: ")
fileDir_SET_1 = "Resources/Images/Set_1"
fileDir_SET_2 = "Resources/Images/Set_2"
fileDir_SET_3 = "Resources/Images/Set_3"
fileDir_SET_4 = "Resources/Images/Set_4"
#fileDir_SET_5 = "Resources/Images"
waitTime = int(input("how long should each image stay on screen in ms? (0: until manually close)"))
faceCascade_1 = cv2.CascadeClassifier("Resources/Trained_Sets/cascade.xml")

numFaces = []
numFaceHits = []
numDoubles = []
numFaceMiss = []
numErrors = []
errorPercent = []
runtimes = []
sets = [fileDir_SET_1, fileDir_SET_2, fileDir_SET_3, fileDir_SET_4]

### Loop through the sets of images
it = 0
for set_i in sets:
    ### get start and end time of program run for runtime analysis ###
    start_time = time.time()
    CV2_func.FindFace(set_i, faceCascade_1, waitTime)
    end_time = time.time() - start_time

    ### Values for error analysis ###
    numFaces.append(CV2_func.numFaces)
    numFaceHits.append(CV2_func.numFaceHits)
    numDoubles.append(CV2_func.numDoubles)
    numFaceMiss.append(numFaces[it] - numFaceHits[it])       # did not detect a face at all (not allowed in this set)
    numErrors.append(numFaceMiss[it] + numDoubles[it])       # did not detect a face or had multiple hits (not allowed in this set)
    if numFaces[it] != 0:
        runtimes.append((end_time/CV2_func.numFaces)*1000)
        errorPercent.append((numErrors[it] / numFaces[it])*100)
    else:
        runtimes.append(0)
        errorPercent.append(0)

    print("-------------------------------------")
    print("Number of Faces  : ", numFaces[it])
    print("Number of Misses : ", numFaceMiss[it])
    print("Number of Doubles: ", numDoubles[it])
    print("Number of Errors : ", numErrors[it])
    print("Total Error %    : ", errorPercent[it], "%")
    print("Time Elapsed     : ",  runtimes[it])
    print("-------------------------------------")

    CV2_func.numFaces = 0
    CV2_func.numFaceHits = 0
    CV2_func.numDoubles = 0
    it += 1
