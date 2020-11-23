import cv2
import numpy as np
import matplotlib.pyplot as plt 


cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('Original',frame)
    cv2.imshow('fg',fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()









#Detection 
# img_rgb = cv2.imread('match.jpg')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('formatch.jpg',0)
# w, h = template.shape[::-1]


# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)


# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

# cv2.imshow('Detected',img_rgb)






#for the things below

# img = cv2.imread('watch.jpg')

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


# # HSV
# lower_red = np.array([150,100,50])
# higher_red = np.array([255,255,255])

# mask = cv2.inRange(hsv,lower_red,higher_red)
# res = cv2.bitwise_and(img,img,mask=mask)



# cv2.imshow('img',img)
# #cv2.imshow('res',res)


#blur types
# kernel = np.ones((15,15), np.float32)/225
# smothed = cv2.filter2D(res,-1,kernel)
# blur = cv2.GaussianBlur(res,(15,15),0)
# meadian = cv2.medianBlur(res,15)
# bialateral = cv2.bilateralFilter(res,15,75,75)
# cv2.imshow('smother',smothed)
# cv2.imshow('blur',blur)
# cv2.imshow('meadian',meadian)
# cv2.imshow('bialateral',bialateral)




#Morpology
# kernel = np.ones((5,5), np.uint8)
# erosion = cv2.erode(mask,kernel,iterations= 1)
# dialetion = cv2.dilate(mask,kernel,iterations= 1)

# opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN , kernel)
# closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
# cv2.imshow('erosion',erosion)
# cv2.imshow('dialetion',dialetion)
# cv2.imshow('closing',closing)
# cv2.imshow('opening',opening)




# #Edge detection
# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# edges = cv2.Canny(img,100,200)
# cv2.imshow('lap',laplacian)
# cv2.imshow('soblex',sobelx)
# cv2.imshow('sobley',sobely)
# cv2.imshow('egdes',edges)







# #Corner Detection
# img = cv2.imread('corner.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)

# corners = cv2.goodFeaturesToTrack(gray,1000,0.01,10)
# corners = np.int0(corners)

# for corner in corners:
#     x,y = corner.ravel()
#     cv2.circle(img,(x,y),3,255,-1)

# cv2.imshow('corner',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# #Object matching
# img1 = cv2.imread('opencv-feature-matching-template.jpg',0)
# img2 = cv2.imread('opencv-feature-matching-image.jpg',0)

# orb = cv2.ORB_create()

# kp1, des1 = orb.detectAndCompute(img1,None)
# kp2, des2 = orb.detectAndCompute(img2,None)

# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# matches = bf.match(des1,des2)
# matches = sorted(matches, key = lambda x:x.distance)

# img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
# plt.imshow(img3)
# plt.show()






#Grabcut Foreground Extraction
# img = cv2.imread('foreground.jpg')
# mask = np.zeros(img.shape[:2], np.uint8)

# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# rect = (50,50,300,600)

# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis]
# plt.imshow(img)
# plt.colorbar()
# plt.show()



# retval , threshold = cv2.threshold(img, 12,255, cv2.THRESH_BINARY)

# grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# retval2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
# gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
 

# cv2.imshow('original',img)
# cv2.imshow('threshold',threshold)
# cv2.imshow('threshold2',threshold2)
# cv2.imshow('gaus',gaus)
# cv2.waitKey(0)
# cv2.destroyAllWindows()









# img2 = cv2.imread('mainlogo.png')
# img1 = cv2.imread('3D-Matplotlib.png')

# rows ,cols, channels = img2.shape
# roi = img1 [0:rows,0:cols]

# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# mask_inv = cv2.bitwise_not(mask)

# img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
# img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows , 0:cols] = dst

# cv2.imshow('res',img1)

# cv2.imshow('mask',mask)

# add = cv2.add(img1,img2)
# weighted = cv2.addWeighted(img1,0.6 , img2 , 0.4 , 0)

# cv2.imshow('add',weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






# cv2.line(img,(0,0),(150,150), (255,255,255) , 15)
# cv2.rectangle(img, (15,25) , (200,150) , (0,255,0), 5)
# cv2.circle(img, (100,63), 55, (0,0,255) ,0)

# pts = np.array( [[10,5] ,[20,30],[70,30], [50,10]] , np.int32)
# cv2.polylines(img,[pts] ,True, (0,255,255),3)

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCv', (0,130), font , 1,(200,255,255),2, cv2.LINE_AA)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()