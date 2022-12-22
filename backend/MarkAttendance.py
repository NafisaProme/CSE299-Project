from wsgiref.handlers import format_date_time
from sre_constants import SUCCESS
from datetime import datetime
import numpy as np
import os
import face_recognition
import cv2


def attendance():
    # get the image list
    PATH = "backend/resources"
    imgs = []
    image_files = os.listdir(PATH)
    images = []
    # get the name of individual peoples
    persons_names = []

    # open all the image list
    for img_file in image_files:
        img = cv2.imread(f"{PATH}/{img_file}")
        images.append(img)
        person_name = img_file.split(".")[0]
        persons_names.append(person_name)

    # mark attendance
    def mark_attance_list(name):
        with open("backend/attendance.csv", "r+") as f:
            # get current data inside of the list
            current_lst = f.readlines()

            names = []

            for item in current_lst:
                entry = item.split(",")
                # get the name from the list
                names.append(entry[0])

            # show name and time
            if name not in names:
                cur_time = datetime.now()
                formatted_time = cur_time.strftime("%H:%M:%S")
                f.writelines(f"\n{name},{formatted_time}")

    # a function that will encode all of the images
    def faceEncodings(img_list):
        encoding_lst = []

        for image in img_list:
            encoding = face_recognition.face_encodings(image)[0]
            encoding_lst.append(encoding)
        return encoding_lst


    known_encodings_lst = faceEncodings(images)

    # retrieval and the test of the image
    img = cv2.imread("backend\\test_image\Test.jpg")
    while True:

        if not SUCCESS:
            break

        test_faces_location = face_recognition.face_locations(img)
        test_encoded = face_recognition.face_encodings(img, test_faces_location)

        for encoded_face, location in zip(test_encoded, test_faces_location):
            matches = face_recognition.compare_faces(
                known_encodings_lst, test_encoded[0])
            face_distances = face_recognition.face_distance(
                known_encodings_lst, test_encoded[0])
            # print(face_distances)
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name = persons_names[match_index]

                # loose the location
                y1, x2, y2, x1 = location
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                # show name beside img box
                cv2.putText(img, name, (x1+8, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                # call the function
                mark_attance_list(name)
        
        return