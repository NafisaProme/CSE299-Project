import cv2
import face_recognition

# call image
Elon_Musk = cv2.imread("resources/Elon_Musk.jpg")
# test_Elon_Musk= cv2.imread("resources/test_Elon_Musk.jpg")
Bill_Gates = cv2.imread("resources/Bill_Gates.jpg")

# identify the face from thr image
#(top,right,bottom,left)
elon_face_location = face_recognition.face_locations(Elon_Musk)[0]
bill_face_location = face_recognition.face_locations(Bill_Gates)[0]
# test_face_location = face_recognition.face_locations(test_Elon_Musk)[0]


# rectangle around the face
cv2.rectangle(Elon_Musk,(elon_face_location[3], elon_face_location[0]),(elon_face_location[1],elon_face_location[2]),(255,255,0),3)
# cv2.rectangle(test_Elon_Musk,(test_face_location[3], test_face_location[0]),(test_face_location[1],test_face_location[2]),(255,255,0),3)
cv2.rectangle(Bill_Gates,(bill_face_location[3], bill_face_location[0]),(bill_face_location[1],bill_face_location[2]),(255,255,0),3)

# comparison between 2 images
encodedElon = face_recognition.face_encodings(Elon_Musk)[0]
# encodedTest = face_recognition.face_encodings(test_Elon_Musk)[0]
encodedBill = face_recognition.face_encodings(Bill_Gates)[0]
# print(encodedBill)

# comparison_result = face_recognition.compare_faces([encodedElon],encodedTest)
comparison_result = face_recognition.compare_faces([encodedElon],encodedBill)

# this will return a boolean result
print(comparison_result)



# display images
cv2.imshow("Elon Musk", Elon_Musk)
# cv2.imshow("test_Elon_Musk",test_Elon_Musk)
cv2.imshow("Bill Gates",Bill_Gates)

# the image will wait after display
cv2.waitKey(10000)
