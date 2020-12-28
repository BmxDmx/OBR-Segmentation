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
# Returns a list of bbox objects, each containing a color and list [pointA, pointB] => list of [[x1, y1], [x2, y2]]
def extractBoundingBoxes(json_path):
    fullList = []
    with open(json_path) as f:
        string = f.read()
        obj = json.loads(string)
        objects = obj["objects"]
        for numberOfCone in range(len(objects)):
            bbox = dict()
            bbox["coords"] = objects[numberOfCone]['points']['exterior']
            bbox["color"] = objects[numberOfCone]["classTitle"]
            fullList.append(bbox)
    return fullList

{
    "color": "yellow",
    "coords": [[x1, y1], [x2, y2]]
}


# Accepts the path to the image and the list of bounding box coordinates for that image
# Returns the list of masks (as images)
def extractMasks(image_path, bounding_boxes):
    image = cv2.imread(image_path)   
    
    # TODO: make createMask return the resulting mask
    # pass image path instead ot indexNumber
    
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

        image = cv2.imread(image_path)

        # Extract a mask for each bounding box in the corresponding image
        masks = []
        for bbox in bounding_boxes:
            x1 = bbox["coords"][0][0]
            y1 = bbox["coords"][0][1]
            x2 = bbox["coords"][1][0]
            y2 = bbox["coords"][1][1]
            mask = createMask(image, bbox["color"], x1, x2, y1, y2)
            masks.append(mask)

        # Convert the masks map into a string
        for mask in masks:
            # extract each string

        # Add the mask string to the annotation file (make a copy! don't modify the original)