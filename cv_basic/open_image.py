import cv2

#open image
img = cv2.imread("C:\\Users\\TechLand\\Pictures\\Camera Roll\\img.jpg")
#show image
cv2.imshow("title", img)
cv2.waitKey(0)