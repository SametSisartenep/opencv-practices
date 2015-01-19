import cv2

grayImage = cv2.imread('pic2.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('pic2Gray.png', grayImage)
