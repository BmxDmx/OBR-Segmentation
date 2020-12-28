import cv2
import numpy as np
import matplotlib.pyplot as plt

#### Each if these functions return a mask for essential colours
# They take the image in hsv
def extractWhite(hsv):
    whiteLower = np.array([20, 20, 150])
    whiteUpper = np.array([180, 70, 255])
    #whiteUpper = np.array([196, 216, 255])
    mask = cv2.inRange(hsv,whiteLower,whiteUpper)
    return mask
    

def extractBlue(hsv):
    blueLower = np.array([100, 150, 50])
    blueUpper = np.array([150, 255, 255])
    mask = cv2.inRange(hsv,blueLower,blueUpper)
    return mask

def extractOrange(hsv):
    orangeLower = np.array([0, 100, 100])
    orangeUpper = np.array([20, 255, 255])
    mask = cv2.inRange(hsv,orangeLower,orangeUpper)
    return mask

def extractYellow(hsv):
    yellowLower = np.array([20, 100, 60])
    yellowUpper = np.array([35, 255, 255])
    mask = cv2.inRange(hsv,yellowLower,yellowUpper)
    return mask

def extractBlack(hsv):
    blackLower = np.array([0, 0, 0])
    blackUpper = np.array([180, 255, 80])
    mask = cv2.inRange(hsv,blackLower,blackUpper)
    return mask

#This function returns the mask file of one cone
#Image = hsv values of the image that has already been read and corresponds to extractBoundingBoxes() annotation 
#cone_colour = string outputted from function extractBoundingBoxes()
#x1, x2, y1, y2 int value outputted from function extractBoundingBoxes()
def createMask(image, cone_colour, x1, x2, y1, y2):       #Parameters: Image, cone colour, co-ordinates of bounding box   /// return the mask file
    img = image

    #Crop coordinates out of original image
    bounding_box_image = img[int(y1):int(y2), int(x1):int(x2)]                    # [y1:y2, x1:x2]

    #bitwise mask back onto original image
    #Return image

    #Image HSV conversion
    hsv_of_cone = cv2.cvtColor(bounding_box_image, cv2.COLOR_BGR2HSV)
    
    #If statements based on cone_colour to return the correct function to be called on the bounding box image
    mask = np.zeros((y2-y1, x2-x1), dtype=bool)     
    mask[0][0] = True
    if cone_colour == "yellow":
        yellow_mask = extractYellow(hsv_of_cone)
        black_mask = extractBlack(hsv_of_cone)
        mask = cv2.add(yellow_mask, black_mask)
    elif cone_colour == "orange":
        orange_mask = extractOrange(hsv_of_cone)
        black_mask = extractBlack(hsv_of_cone)
        mask = cv2.add(orange_mask, black_mask)
    elif cone_colour == "blue":
        blue_mask = extractBlue(hsv_of_cone)
        white_mask = extractWhite(hsv_of_cone)
        mask = cv2.add(blue_mask, white_mask)
    
    mask = mask.astype(bool)
    return mask

    
    # #Masks
    # mask_blue = extractBlue(hsv_of_cone)
    # mask_white = extractWhite(hsv_of_cone)
    # mask_orange = extractOrange(hsv_of_cone)
    # mask_yellow = extractYellow(hsv_of_cone)
    # mask_black = extractBlack(hsv_of_cone)

    # #Result
    # # res_blue = cv2.bitwise_and(resized_img,resized_img,mask=mask_blue)
    # # res_white = cv2.bitwise_and(resized_img,resized_img,mask=mask_white)
    # # res_orange = cv2.bitwise_and(resized_img,resized_img,mask=mask_orange)
    # # res_yellow = cv2.bitwise_and(resized_img,resized_img,mask=mask_yellow)
    # # res_black = cv2.bitwise_and(resized_img,resized_img,mask=mask_black)

    # #Added images
    # added_yellow = cv2.addWeighted(res_yellow,0.5,res_black,0.5,-20)
    # added_blue = cv2.addWeighted(res_blue,0.5,res_white,0.5,0)
    # added_together = cv2.addWeighted(added_blue,0.5,added_yellow,0.5,10)
    # addedYellowBlackMask = cv2.addWeighted(mask_yellow,0.5,mask_black,0.5,1)


    # #Edges

    # # edges = cv2.Canny(added_together,200,200)

    # # cv2.imshow('edges',edges)


    # #Blurring and Smotthing and Morphological transformation but it doesn't  really work

    # # kernel = np.ones((2,2),np.uint8)
    # # erosion = cv2.erode(mask_yellow,kernel,iterations = 1)
    # # erosionBlack = cv2.erode(mask_black,kernel,iterations=1)
    # # dialetion = cv2.dilate(mask_yellow,kernel,iterations = 1)
    # #blurr = cv2.bilateralFilter(res_yellow,15,75,75)

    # # added_blue1 = cv2.addWeighted(res_blue,0.8,erosion,0.2,0)
    # # added_together1 = cv2.addWeighted(added_blue1,0.5,added_yellow,0.5,10)


    # #cv2.imshow('blurr',blurr)
    # #cv2.imshow('erosion',erosion)
    # #cv2.imshow('erosionBlack',erosionBlack)
    # #cv2.imshow('dialetion',dialetion)
    # #cv2.imshow('added_together1',added_together1)
    # #cv2.imshow('addedYellowBlackMask',addedYellowBlackMask)



    # #Thresholds
    # # ret, thresh = cv2.threshold(resized_img,150,255,cv2.THRESH_BINARY_INV)
    # # ret2,thresh_gray = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    # # thresh_inv = cv2.bitwise_not(thresh)


    # #Display all the images
    # cv2.imshow('resized_img',resized_img)
    # # cv2.imshow('gray',gray)
    # # cv2.imshow('thresh',thresh)
    # # cv2.imshow('thresh_inv',thresh_inv)
    # # cv2.imshow('thresh_gray',thresh_gray)

    # cv2.imshow('mask_blue',mask_blue)
    # #cv2.imshow('res_blue',res_blue)

    # cv2.imshow('mask_white',mask_white)
    # # cv2.imshow('res_white',res_white)

    # # cv2.imshow('mask_orange',mask_orange)
    # # cv2.imshow('res_orange',res_orange)

    # cv2.imshow('mask_yellow',mask_yellow)
    # #cv2.imshow('res_yellow',res_yellow)

    # cv2.imshow('mask_black',mask_black)
    # #cv2.imshow('res_black',res_black)

    # # cv2.imshow('added_yellow',added_yellow)
    # # cv2.imshow('added_blue',added_blue)
    # #cv2.imshow('added_together',added_together)



    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
