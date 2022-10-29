from sre_constants import SUCCESS
import cv2
import face_recognition

# capture video
cap = cv2.VideoCapture(0)

while True:
    SUCCESS, img = cap.read()

    if not SUCCESS:
        break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
