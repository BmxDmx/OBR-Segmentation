import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from semantic import createMask
import os       # For working with the filesystem
from SupervislyDecodingEncoding import mask_2_base64


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


def createMaskDummy(image, colour, x1, x2, y1, y2):
    # imgROI = image[int(y1):int(y2),int(x1):int(x2)]
    # blueLower = np.array([100, 150, 50])
    # blueUpper = np.array([150, 255, 255])
    # hsv = cv2.cvtColor(imgROI,cv2.COLOR_BGR2HSV)
    # mask_blue = cv2.inRange(hsv,blueLower,blueUpper)
    # res_blue = cv2.bitwise_and(imgROI,imgROI,mask=mask_blue)

    ones = np.ones((y2-y1, x2-x1), dtype=bool)
    ones[0][0] = False
    print(ones)
    return ones

# A standard condition that ensures this code is only run when this .py is explicitly executed / called
# otherwise the code will be triggered when this .py file is imported by other .py files
# here it's just a formality I guess
if __name__ == "__main__":
    # Define paths to data directories
    images_dir = "../Training/To Do/2020-03-22 Wheatley augmented/img"
    annotations_dir = "../Training/To Do/2020-03-22 Wheatley augmented/ann/"
    seg_annotations_dir = "../Training/Done/segment_ann/"

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
        #bounding_boxes = extractBoundingBoxes(annotations_dir + annotation_json)
        #print(bounding_boxes)

        image = cv2.imread(image_path)

        # Add the mask string to the annotation file (make a copy! don't modify the original)
        new_objects = []
        with open(annotations_dir + annotation_json) as f:
            string = f.read()
            annotations_obj = json.loads(string)
            for objIndex in range(len(annotations_obj["objects"])):

                # Extract a bitmap for each bounding box
                coords = annotations_obj["objects"][objIndex]['points']['exterior']
                colour = annotations_obj["objects"][objIndex]["classTitle"]
                x1 = coords[0][0]
                y1 = coords[0][1]
                x2 = coords[1][0]
                y2 = coords[1][1]

                if x2-x1 == 0 or y2-y1 == 0:
                    continue
                mask = createMask(image, colour, x1, x2, y1, y2)
                if  np.all(mask == np.zeros((y2-y1, x2-x1),dtype=bool)): #Checks if the numpy matrix is full of False or True values if it's return True we skip.
                    continue
                if  np.all(mask == np.ones((y2-y1, x2-x1),dtype=bool)):
                    mask[0][0] = False
                string = mask_2_base64(mask)

                # Modify annotations object
                annotations_obj["objects"][objIndex]["geometryType"] = "bitmap"
                annotations_obj["objects"][objIndex]["bitmap"] = {
                    "data": string,
                    "origin": [x1, y1]
                }
                del annotations_obj["objects"][objIndex]["points"]
                new_objects.append(annotations_obj["objects"][objIndex])

        annotations_obj["objects"] = new_objects
        # Write a new json file
        with open(seg_annotations_dir + annotation_json, "w") as new_f:
            json.dump(annotations_obj, new_f)

        