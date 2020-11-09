import cv2
import os
import numpy as np
import time

### Take in relative path ###
#fileDir = input("input directory of images: ")
fileDir = "Resources/Images/Set_1"
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

### get start time of program run for runtime analysis ###
start_time = time.time()

### loop through detected faces and draw box around them ###
def FindFaces(img, faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

### function for reading in files of specified path ###
def FileRead(FileDir):
    for fileName in os.listdir(fileDir):
        if fileName.endswith(".jpg"):
            print(fileName)
            img = cv2.imread(fileDir + "/" + fileName)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(imgGray, 1.3, 4)
            FindFaces(img, faces) 
            cv2.imshow("output", img)
            cv2.waitKey(500)

FileRead(fileDir)

### Print out the calculated runtime ###
print("--- %s seconds ---" % (time.time() - start_time))
