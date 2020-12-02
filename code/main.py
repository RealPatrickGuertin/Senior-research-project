import cv2 
import CV2_func
import numpy as np
import time

### Take in relative path ###
fileDir_SET_1 = "Resources/Images/Set_1"
fileDir_SET_2 = "Resources/Images/Set_2"
fileDir_SET_3 = "Resources/Images/Set_3"
fileDir_SET_4 = "Resources/Images/Set_4"

trainedSet_0 = "Resources/Trained_Sets/haarcascade_frontalface_default.xml"
trainedSet_1 = "Resources\Trainer\T_Set_1\classifier\cascade.xml"
trainedSet_2 = "Resources\Trainer\T_Set_2\classifier\cascade.xml"
trainedSet_3 = "Resources\Trainer\T_Set_3\classifier\cascade.xml"
trainedSet_4 = "Resources\Trainer\T_Set_4\classifier\cascade.xml"

waitTime = int(input("how long should each image stay on screen in ms? (0: until manually close)"))
faceCascade = cv2.CascadeClassifier(trainedSet_3)
sets = [fileDir_SET_1, fileDir_SET_2, fileDir_SET_3]

numFaces = []
numFaceHits = []
numDoubles = []
numFaceMiss = []
numErrors = []
errorPercent = []
runtimes = []

### Loop through the sets of images
it = 0
for set_i in sets:
    ### get start and end time of program run for runtime analysis ###
    start_time = time.time()
    CV2_func.FindFace(set_i, faceCascade, waitTime)
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
