import cv2
import numpy as np
img = cv2.imread("imagesrc/cards.jpg")
width, height = 250, 350
pt = np.float32([[392, 652],[543, 702], [466, 930], [278, 841]])
pt2 = np.float32([[0,0],[width, 0],[height,0],[width,height]])
#img = np.zeros((512, 512, 3), np.uint8)
#img[0:100, 100:200] = 255, 255, 0   #blue colour  #complete image gets coloured
#cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 2)
#cv2.rectangle(img, (100,100), (200,250), (0,255,0), 3)
#cv2.circle(img, (50,50), 30, (0,0,255), cv2.FILLED)
#cv2.putText(img,"WE WELCOME YOU", (100,300), cv2.FONT_HERSHEY_DUPLEX, 1, (0,150,255), 3)
matrix = cv2.getPerspectiveTransform(pt,pt2)
final = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("shape", final)
cv2.waitKey(0)
