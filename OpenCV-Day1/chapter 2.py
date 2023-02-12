import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("imagesrc/acm.jpg")
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(7,7),10)
canny = cv2.Canny(img,100,150)
dialation = cv2.dilate(canny,kernel,iterations=1) #edges thicker
erodded = cv2.erode(dialation,kernel,iterations=1)
print(img.shape)
imgResize = cv2.resize(img,(300,200))
imgcrop = img[0:300, 300:400]
#cv2.imshow("image", img)
#cv2.imshow("GRAY image", imgrey)
#cv2.imshow("BLUR image", blur)
cv2.imshow("canny image", canny)
cv2.imshow("dilation image", dialation)
cv2.imshow("eroded image", erodded)
cv2.imshow("resized image", imgResize)
cv2.imshow("cropped image", imgcrop)
cv2.waitKey(0)
