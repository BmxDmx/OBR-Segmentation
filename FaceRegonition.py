import cv2

#Create a CascadeClassifier object using haar's cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread(".jpg")

#Read the image as a gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the co-ordinates of the image using detectMultiScale for face rectangle
#scaleFactor decreases shape by 5% until face is found, smaller value = greater accuracy
faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.05, minNeighbors = 5)
#Loop statement adds rectanglar face box using cv2.rectangle method
for x,y,w,h in faces:
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()