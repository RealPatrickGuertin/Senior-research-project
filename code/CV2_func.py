import cv2
import os

numFaces = 0
numFaceHits = 0
numDoubles = 0

### function for reading in files of specified path ###
def FindFace(fileDir, faceCas, waitTime):
    global numFaces
    global numFaceHits
    global numDoubles

    for fileName in os.listdir(fileDir):
        if fileName.endswith(".jpg"):
            numFaces += 1

            img = cv2.imread(fileDir + "/" + fileName)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCas.detectMultiScale(imgGray, 1.3, 4)

            ### loop through detected faces and draw box around them ###
            numRuns = 0
            for (x,y,w,h) in faces:
                numRuns += 1
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
                
                if(numRuns == 1):
                    numFaceHits += 1
                elif(numRuns == 2):
                    numDoubles += 1
                #wufwu
            cv2.imshow("output", img)
            cv2.waitKey(waitTime)
