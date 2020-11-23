import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from semantic import createMask

# Separate the list of coordinates to x1,x2,y1,y2
def regionOfImageX1(coordinateList):
    x1 = coordinateList[0][0]
    return x1

def regionOfImageX2(coordinateList):
    x2 = coordinateList[1][0]
    return x2

def regionOfImageY1(coordinateList):
    y1 = coordinateList[0][1]
    return y1

def regionOfImageY2(coordinateList):
    y2 = coordinateList[1][1]
    return y2
    

# Loops though the folder NOT automatically 
for indexNumber in range (5):

    with open('./Training/ann/'+ str(indexNumber) +'.png.json') as f:
        fullList = []
        string = f.read()
        obj = json.loads(string)
        objects = obj["objects"]
        #print(len(objects))
        for numberOfCone in range(len(objects)):
            for  indexOfPoints in range(len(objects[numberOfCone]['points']['exterior'])):
                setOfCoorindates = (objects[numberOfCone]['points']['exterior'][indexOfPoints])
                #print('Coordinates = '+str(setOfCoorindates))
                count = 0 
                fullList.append(setOfCoorindates)
        #print(fullList)
        setOfLists = []
        count = 0 
        #List of 2 Lists with 4 Coordinate (topLeft,TopRight)
        for item in fullList:
            #print(item)
            setOfLists.append(item)
            if len(setOfLists) == 2:
                #print(setOfLists)
                tempX1 = regionOfImageX1(setOfLists)
                tempX2 = regionOfImageX2(setOfLists)
                tempY1 = regionOfImageY1(setOfLists)
                tempY2 = regionOfImageY2(setOfLists)
                setOfLists.clear()
    createMask(indexNumber,tempX1,tempX2,tempY1,tempY2)
            
