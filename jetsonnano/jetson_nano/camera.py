import datetime
import sys
import threading
import cv2
import os
import face_recognition
import numpy as np
class Camera():
    def __init__(self, path='registered', tolerance=0.45, develop=False):
        self.develop = develop
        self.path = path
        self.tolerance = tolerance
        self.classNames = []
        self.encoded_face_train = [] # 인코딩된 훈련 데이터 저장.
        self.cap  = cv2.VideoCapture(0)
        self.imgRead()
    def get_numbers(self):
        return self.classNames
    def set_names(self, names):
        self.classNames = names
        print(f'classNames : {self.classNames}')
    def imgRead(self):
        self.classNames = []
        self.encoded_face_train = []
        # images = []
        mylist = os.listdir(self.path)
        for cl in mylist:
            try:
                curImg = cv2.imread(f'{self.path}/{cl}')
                curImg = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
                encoded_face = face_recognition.face_encodings(curImg)[0]
                self.encoded_face_train.append(encoded_face)
                self.classNames.append(os.path.splitext(cl)[0])
            except:
                print(f'error : {cl}')

        # self.encoded_face_train = self.findEncodings(images)

    # 훈련 데이터를 인코딩하고 함수에 저장.
    # def findEncodings(self, images):
    #     self.encoded_face_train = []
    #     for curImg in images:
    #         curImg = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
    #         encoded_face = face_recognition.face_encodings(curImg)[0]
    #         self.encoded_face_train.append(encoded_face)
    def getData(self, update=False):
        name = ""
        success, frame = self.cap.read()
        img = cv2.resize(frame, (0,0), None, 0.25,0.25)  # 인식 부분에만 크기를 1/4로 조정. (초당 프레임 향상 효과)
        if update:
            self.update_drow(frame)
        else:
            faces_in_frame = face_recognition.face_locations(img)
            encoded_faces = face_recognition.face_encodings(img, faces_in_frame)

            name = self.getName(faces_in_frame , encoded_faces)
            if name != '':
                if name == 'Unknown':
                    self.draw(frame, name, faces_in_frame, 'red')
                else:
                    self.draw(frame, name, faces_in_frame, 'green')
        return frame, name
    def getName(self, faces_in_frame, encoded_faces):
        name =''
        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            faceDist = face_recognition.face_distance(self.encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)

            min_faceDist = min(faceDist)
            if min_faceDist < self.tolerance:
                name = self.classNames[matchIndex]
            else:
                name = 'Unknown'
            if self.develop:
                print(f'{name} : {min_faceDist}')
        return name
    def draw(self, frame, name, face_loc, color):
            if color == 'red' or color == 'Red' or color == "RED":
                color = (0,0,255)
            elif color == 'green' or color == 'Green' or color == 'GREEN':
                color = (0,255,0)

            y1,x2,y2,x1 = face_loc[0]
            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4  # 출력 프레임에 오버레이 하기 위해 4를 곱함.

            if name !='':
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
                cv2.rectangle(frame, (x1,y2-35),(x2,y2), color, cv2.FILLED)
                cv2.putText(frame, name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    def update_drow(self, frame):
        now = str(datetime.datetime.now().time())
        second = now.split(":")[-1]
        second = int(float(second))
        w, h, c = frame.shape
        messsege = 'UPDATE' + '.'* ((second%3)+1)
        cv2.putText(frame, messsege, (int(w/2),30), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    def data_update(self, patch_event, update_event, db, q):
        while True:
            patch_event.wait()

            self.imgRead()
            numbers = self.get_numbers()

            name_dict = {}
            self.set_names(db.changeName(self.classNames))
            for number, name in zip(numbers, self.classNames):
                name_dict[name] = number
            q.put(name_dict)

            update_event.clear()
            patch_event.clear()


    def imgCaptture(self, q, send, receive):
        while True:
            if receive.is_set():
                data = q.get()
                cv2.imwrite('Unknown.jpg', data['Unknown'])
                send.setAll()
                receive.clearAll()

if __name__ == '__main__':
    camera = Camera('../registered')
    while True:
        # start = time.time()
        frame, name = camera.getData()
        print(f'name : {name}')
        cv2.imshow('cam',frame)
        # end = time.time()
        # print(f"{end - start:.3f} sec")

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

