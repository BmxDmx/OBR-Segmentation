import cv2
import numpy as np
import matplotlib.pyplot as plt

#### Each if these functions return a mask for essential colours
# They take the image in hsv
def extractWhite(hsv):
    whiteLower = np.array([0, 0, 100])
    whiteUpper = np.array([180, 90, 255])
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



def createMask(name,x1,x2,y1,y2):
    # img = cv2.imread('./Training/img/'+str(name)+'.png', cv2.IMREAD_COLOR) 
    
    # #rectROI = cv2.rectangle(316,397,445,557)
    # imgROI = img[int(y1):int(y2),int(x1):int(x2)]                    # [y1:y2,x1:x2]
    # cv2.imshow('imgROI',imgROI)

    
    img = cv2.imread('../Training/img/68.png',cv2.IMREAD_COLOR)
    resised_img = cv2.resize(img,(853,480))

    #Img color conversion
    gray = cv2.cvtColor(resised_img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(resised_img,cv2.COLOR_BGR2HSV)
    
    # Masks
    mask_blue = extractBlue(hsv)
    mask_white = extractWhite(hsv)
    mask_orange = extractOrange(hsv)
    mask_yellow = extractYellow(hsv)
    mask_black = extractBlack(hsv)

    # Result
    res_blue = cv2.bitwise_and(resised_img,resised_img,mask=mask_blue)
    res_white = cv2.bitwise_and(resised_img,resised_img,mask=mask_white)
    res_orange = cv2.bitwise_and(resised_img,resised_img,mask=mask_orange)
    res_yellow = cv2.bitwise_and(resised_img,resised_img,mask=mask_yellow)
    res_black = cv2.bitwise_and(resised_img,resised_img,mask=mask_black)

    #Added images
    added_yellow = cv2.addWeighted(res_yellow,0.5,res_black,0.5,-20)
    added_blue = cv2.addWeighted(res_blue,0.5,res_white,0.5,0)
    added_together = cv2.addWeighted(added_blue,0.5,added_yellow,0.5,10)
    addedYellowBlackMask = cv2.addWeighted(mask_yellow,0.5,mask_black,0.5,1)






    #Display all the images
    cv2.imshow('resised_img',resised_img)
    # cv2.imshow('gray',gray)
    # cv2.imshow('thresh',thresh)
    # cv2.imshow('thresh_inv',thresh_inv)
    # cv2.imshow('thresh_gray',thresh_gray)

    cv2.imshow('mask_blue',mask_blue)
    cv2.imshow('res_blue',res_blue)

    cv2.imshow('mask_white',mask_white)
    # cv2.imshow('res_white',res_white)

    # cv2.imshow('mask_orage',mask_orage)
    # cv2.imshow('res_orange',res_orange)

    cv2.imshow('mask_yellow',mask_yellow)
    #cv2.imshow('res_yellow',res_yellow)

    cv2.imshow('mask_black',mask_black)
    #cv2.imshow('res_black',res_black)

    # cv2.imshow('added_yellow',added_yellow)
    # cv2.imshow('added_blue',added_blue)
    # cv2.imshow('added_together',added_together)
    print(mask_yellow)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

createMask(1,1,1,1,1)