import cv2
import face_recognition

# call image
Elon_Musk = cv2.imread("backend\\resources\Elon_Musk.jpg")
# Jeff_Bezos = cv2.imread("resources/Jeff_Bezos.jpg")
test_Elon_Musk = cv2.imread("backend\\resources\\test_Elon_Musk.jpg")

# identify the face from thr image
#(top,right,bottom,left)
elon_face_location = face_recognition.face_locations(Elon_Musk)[0]
# jeff_face_location = face_recognition.face_locations(Jeff_Bezos)[0]
test_face_location = face_recognition.face_locations(test_Elon_Musk)[0]


# rectangle around the face
cv2.rectangle(Elon_Musk,(elon_face_location[3], elon_face_location[0]),(elon_face_location[1],elon_face_location[2]),(255,255,0),3)
cv2.rectangle(test_Elon_Musk,(test_face_location[3], test_face_location[0]),(test_face_location[1],test_face_location[2]),(255,255,0),3)
# cv2.rectangle(Jeff_Bezos,(jeff_face_location[3], jeff_face_location[0]),(jeff_face_location[1],jeff_face_location[2]),(255,255,0),3)

# comparison between 2 images
encodedElon = face_recognition.face_encodings(Elon_Musk)[0]
# encodedJeff = face_recognition.face_encodings(Jeff_Bezos)[0]
encodedTest = face_recognition.face_encodings(test_Elon_Musk)[0]
# print(encodedBill)

comparison_result = face_recognition.compare_faces([encodedElon],encodedTest)
# comparison_result = face_recognition.compare_faces([encodedElon],encodedJeff)

# this will return a boolean result
print(comparison_result)

# face distance measure between 2 image
face_distances = face_recognition.face_distance([encodedElon],encodedTest)
print(face_distances)

# display images
cv2.imshow("Elon Musk", Elon_Musk)
# cv2.imshow("Jeff Bezos",Jeff_Bezos)
cv2.imshow("test_Elon_Musk",test_Elon_Musk)

# the image will wait after display
cv2.waitKey(10000)
