import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from semantic import createMask
import os       # For working with the filesystem

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


# Accepts the path to json file with annotations (Supervisely style)
# Returns a list of coordinates for each bounding box => list of lists
def extractBoundingBoxes(json_path):
    fullList = []
    with open(json_path) as f:
        string = f.read()
        obj = json.loads(string)
        objects = obj["objects"]
        #print(len(objects))
        for numberOfCone in range(len(objects)):
            for  indexOfPoints in range(len(objects[numberOfCone]['points']['exterior'])):
                setOfCoorindates = (objects[numberOfCone]['points']['exterior'][indexOfPoints])
                #print('Coordinates = '+str(setOfCoorindates))
                fullList.append(setOfCoorindates)
        #print(fullList)
    return fullList


# Accepts the path to the image and the list of bounding box coordinates for that image
# Returns the list of masks (as images)
def extractMasks(image_path, bounding_boxes):
    setOfLists = []
    count = 0 
    #List of 2 Lists with 4 Coordinate (topLeft,TopRight)
    for item in bounding_boxes:
        #print(item)
        setOfLists.append(item)
        if len(setOfLists) == 2:
            #print(setOfLists)
            tempX1 = regionOfImageX1(setOfLists)
            tempX2 = regionOfImageX2(setOfLists)
            tempY1 = regionOfImageY1(setOfLists)
            tempY2 = regionOfImageY2(setOfLists)
            setOfLists.clear()
    
    # TODO: make createMask return the resulting mask
    # pass image path instead ot indexNumber
    mask = createMask(indexNumber,tempX1,tempX2,tempY1,tempY2)
    return mask


# A standard condition that ensures this code is only run when this .py is explicitly executed / called
# otherwise the code will be triggered when this .py file is imported by other .py files
# here it's just a formality I guess
if __name__ == "__main__":
    # Define paths to data directories
    images_dir = "./2019-09-05 Millbrook/img/"
    annotations_dir = "./2019-09-05 Millbrook/ann/"
    seg_annotations_dir = "./2019-09-05 Millbrook/segment_ann/"

    # Check if the ./segment_ann folder exists. If not - creeate one
    if not os.path.exists(seg_annotations_dir):
        print("segment_ann directory not found. Creating...")
        os.mkdir(seg_annotations_dir)

    # Loop through all annotations and corresponding images
    # annotation_json is the name of each .json file
    for annotation_json in os.listdir(annotations_dir):
        # Extract the name of the resource (common part of the annotation and image pair)
        # os.path.join() just takes the strings of paths and joins them
        # (ex. if you pass "path", "to", "some.file", it will return "path/to/some.file")
        image_path = os.path.join(images_dir, annotation_json.replace(".json", ""))
        #print(image_path)

        # Extract bounding boxes coordinates
        bounding_boxes = extractBoundingBoxes(annotations_dir + annotation_json)
        #print(bounding_boxes)

        # ... not done yet:

        # Create the masks for each bounding box in the corresponding image
        # masks = extractMasks(image_path, bounding_boxes)

        # Convert the masks map into a string

        # Add the mask string to the annotation file (make a copy! don't modify the original)