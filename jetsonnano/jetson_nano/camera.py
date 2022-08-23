import sys
import threading
import time

import cv2
import os
import face_recognition
import numpy as np
class Camera():
    def __init__(self, dirname = 'registered'):
        # 카메라 불러오기
        self.camera = cv2.VideoCapture(0)
        # 사진 인코딩 목록
        self.known_face_encodings = []
        # 사진파일 이름 목록
        self.known_face_names = []

        # dirname = 'registered'
        files = os.listdir(dirname)
        print("file :",files)

        for filename in files:
            # name:파일명, ext:확장자
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        self.face_locations = []
        self.face_encodings = []
        self.process_this_frame = True

    def get_frame(self):
        name = ""
        ret, frame = self.camera.read()
        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        small_frame = frame
        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            name = self.get_name(rgb_small_frame)

        self.process_this_frame = not self.process_this_frame
        if name != "":
            # print("name :",name)
            if name == 'Unknown':
                self.draw(frame, name, 'red')
            else:
                self.draw(frame, name, 'green')
        return frame, name

    def get_name(self, rgb_small_frame):
        # 얼굴 위치 찾기
        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        # 얼굴 인코딩
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        name = ''

        for face_encoding in self.face_encodings:
            # 사진들과 오차율
            distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            # 가장작은 오차율
            min_value = min(distances)
            print("dist :",min_value)


            # 등록된 인원일시
            # if min_value < 0.45:
            if min_value < 0.47:
                index = np.argmin(distances)
                name = self.known_face_names[index]
            # 등록된 인원이 아닐시
            else:
                name = "Unknown"
        self.process_this_frame = not self.process_this_frame
        return name
    def draw(self, frame, name, color):
        print('color :', color)
        if color == 'red' or color == 'Red' or color == "RED":
            color = (0,0,255)
        elif color == 'green' or color == 'Green' or color == 'GREEN':
            color = (0,255,0)
        print(self.face_locations)
        print(name)

        top, right, bottom, left = self.face_locations[0]
        print(f' top : {top}')
        print(f' right : {right}')
        print(f' bottom : {bottom}')
        print(f' left : {left}')
        if name != '' and name !='Unknown':
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

if __name__ == '__main__':
    # pass
    camera = Camera('../registered')
    while True:
        frame, name = camera.get_frame()
        print(f'name : {name}')
        cv2.imshow("webcam", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
