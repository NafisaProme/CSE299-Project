import cv2
# call image
Elon_Musk = cv2.imread("resources/Elon_Musk.jpg")
Bill_Gates = cv2.imread("resources/Bill_Gates.jpg")

# display images
cv2.imshow("Elon Musk", Elon_Musk)
cv2.imshow("Bill Gates",Bill_Gates)

# the image will wait after display
cv2.waitKey(10000)
