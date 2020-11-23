import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('./Training/img/onecone.png', cv2.IMREAD_COLOR) 

resised_img = cv2.resize(img,(853,480))

#Img color conversion
gray = cv2.cvtColor(resised_img,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(resised_img,cv2.COLOR_BGR2HSV)


# Colour boundries nympy arrays
blueLower = np.array([100, 150, 50])
blueUpper = np.array([150, 255, 255])

whiteLower = np.array([20, 20, 150])
whiteUpper = np.array([180, 70, 255])
#whiteUpper = np.array([196, 216, 255])

orangeLower = np.array([0, 100, 100])
orangeUpper = np.array([20, 255, 255])

yellowLower = np.array([20, 100, 60])
yellowUpper = np.array([35, 255, 255])

blackLower = np.array([0, 0, 0])
blackUpper = np.array([180, 255, 50])

#Masks
mask_blue = cv2.inRange(hsv,blueLower,blueUpper)
mask_white = cv2.inRange(hsv,whiteLower,whiteUpper)
mask_orage = cv2.inRange(hsv,orangeLower,orangeUpper)
mask_yellow = cv2.inRange(hsv,yellowLower,yellowUpper)
mask_black = cv2.inRange(hsv,blackLower,blackUpper)

#Result
res_blue = cv2.bitwise_and(resised_img,resised_img,mask=mask_blue)
res_white = cv2.bitwise_and(resised_img,resised_img,mask=mask_white)
res_orange = cv2.bitwise_and(resised_img,resised_img,mask=mask_orage)
res_yellow = cv2.bitwise_and(resised_img,resised_img,mask=mask_yellow)
res_black = cv2.bitwise_and(resised_img,resised_img,mask=mask_black)


#Added images
added_yellow = cv2.addWeighted(res_yellow,0.5,res_black,0.5,-20)
added_blue = cv2.addWeighted(res_blue,0.5,res_white,0.5,0)
added_together = cv2.addWeighted(added_blue,0.5,added_yellow,0.5,10)


#Edges

# edges = cv2.Canny(added_together,200,200)

# cv2.imshow('edges',edges)


#Blurring and Smotthing and Morphological transformation but it doesn't  reallu work

# kernel = np.ones((2,2),np.uint8)
# erosion = cv2.erode(res_white,kernel,iterations = 1)
# dialetion = cv2.dilate(res_white,kernel,iterations = 1)
# blurr = cv2.bilateralFilter(res_yellow,15,75,75)

# added_blue1 = cv2.addWeighted(res_blue,0.8,erosion,0.2,0)
# added_together1 = cv2.addWeighted(added_blue1,0.5,added_yellow,0.5,10)

# cv2.imshow('blurr',blurr)
# cv2.imshow('erosion',erosion)
# cv2.imshow('dialetion',dialetion)
# cv2.imshow('added_together1',added_together1)




#Thresholds
# ret, thresh = cv2.threshold(resised_img,150,255,cv2.THRESH_BINARY_INV)
# ret2,thresh_gray = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
# thresh_inv = cv2.bitwise_not(thresh)


#Display all the images
cv2.imshow('resised_img',resised_img)
# cv2.imshow('gray',gray)
# cv2.imshow('thresh',thresh)
# cv2.imshow('thresh_inv',thresh_inv)
# cv2.imshow('thresh_gray',thresh_gray)

# cv2.imshow('mask_blue',mask_blue)
cv2.imshow('res_blue',res_blue)

# cv2.imshow('mask_white',mask_white)
# cv2.imshow('res_white',res_white)

# cv2.imshow('mask_orage',mask_orage)
# cv2.imshow('res_orange',res_orange)

cv2.imshow('mask_yellow',mask_yellow)
cv2.imshow('res_yellow',res_yellow)

# cv2.imshow('mask_black',mask_black)
# cv2.imshow('res_black',res_black)

# cv2.imshow('added_yellow',added_yellow)
# cv2.imshow('added_blue',added_blue)
cv2.imshow('added_together',added_together)



cv2.waitKey(0)
cv2.destroyAllWindows()