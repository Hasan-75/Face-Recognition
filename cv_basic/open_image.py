import cv2

#open image
img = cv2.imread(".\\images\\war.jpg")
#show image
cv2.imshow("title", img)
cv2.waitKey(0)