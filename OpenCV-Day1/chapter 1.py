import cv2
print("package imported successfully ")

#image imported

#img = cv2.imread("imagesrc/acm.jpg")
#cv2.imshow("image", img)
#cv2.waitKey(0) #explain waitkey

#video access
#c = cv2.VideoCapture("imagesrc/video.mp4")


#webcam access

c = cv2.VideoCapture(0) #0 here is the id of webcam
c.set(3, 640) #width
c.set(4, 480) #height
c.set(10, 100) #brightness

while True:
    success, img = c.read()
    cv2.imshow("webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'): #expalin masking
        break


