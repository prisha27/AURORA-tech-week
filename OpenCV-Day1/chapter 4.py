import cv2
import numpy as np
img = cv2.imread("imagesrc/acm.jpg")
hor = np.hstack((img,img))
ver = np.vstack((img,img))
cv2.imshow("horizontal image", hor)
cv2.imshow("vertical stack", ver)
cv2.waitKey(0)

