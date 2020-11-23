#Edges
laplacian = cv2.Laplacian(added_together, cv2.CV_64F)
soblex = cv2.Sobel(added_together,cv2.CV_64F,1,0,ksize=5)
sobley = cv2.Sobel(added_together,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('laplacian',laplacian)
cv2.imshow('soblex',soblex)
cv2.imshow('sobley',sobley)