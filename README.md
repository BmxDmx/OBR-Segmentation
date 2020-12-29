# OBR-Segmentation
OBR Segmentation

The code used for Segmentantion by the Oxford Brookes Racing Team

The script converts dataset annotations from bounding boxes format to bitmaps that supervisely can understand. 
It is good for “Blue and white”, “Yellow and Black” and “Orange and White” cones.
The colour ranges can be changed to look for different colours, the colour values are in HSV, the colour ranges are defined in *semantic.py*
To use the code run *ConeBoundingBox.py*  and you need:
Numpy
OpenCV
