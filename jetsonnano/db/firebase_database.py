import random
import threading
import time
from queue import Queue
import datetime

import json

from db.firebase_connet import Firebase


class firebase_database(Firebase):

    def __init__(self, delay = 10, path='db/auth_database.json'):
        super().__init__(path)
        self.registered_data = None
        self.delay = delay
        self.last_person = None
        # with open(path) as f:
        #     config = json.load(f)
        # firebase = pyrebase.initialize_app(config)
        self.db= self.firebase.database()

    def insert(self, q):
        while True:
            name = q.get()
            self.set(name)

    # firebase에 추가
    def set(self, name):
        date = str(datetime.datetime.now())
        data = self.registered_data[name]
        data['time'] = date
        # print(data)
        # data = {name:date}
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        if self.cooldowncheck(name):
            self.last_person = data
            self.db.child("club").child(year).child(month).child(day).push(data)
            return True
        else:
            return False

    def cooldowncheck(self, name): # 마지막과 동일하면 False DB저장하려면 True
        if self.last_person == None:
            return True
        else:
            for key, val in self.last_person.items():
                key = key
                val = val
            # if key != name:
            #     return True
            now = datetime.datetime.now()
            date = val
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
            hour = int(date[11:13])
            minute = int(date[14:16])
            second = int(date[17:19])
            date = datetime.datetime(year, month, day, hour, minute, second)
            difference = (now - date).seconds
            if difference > self.delay:
                return True
            else:
                return False
        print("error")
    def changeName(self, numbers):
        while True:
            self.registered_data = {}
            names = []
            # numbers = list(self.db.child("registered").shallow().get().val())
            for number in numbers:
                name = self.db.child('registered').child(number).child('name').get().val()
                engname = self.db.child('registered').child(number).child('engname').get().val()
                self.registered_data[engname] = {
                    'number': number,
                    'name' : name
                }
                names.append(engname)
            return names
    def observer(self, q, e):
        data = {'insert': '201813066'}
        self.db.child("log").push(data)
        while True:
            registered = self.db.child("log").get()
            if registered != None and registered.val() != None:
                print('observer :',registered)
                e.set()
                for people in registered.each():
                    key = people.key()
                    data = self.db.child('log').child(key).get().val()
                    data = dict(data)
                    q.put(data)
                    self.db.child('log').child(key).remove()

if __name__ == '__main__':
    db = firebase_database(path='./auth_database.json')
    db = db.db
    time.sleep(5)
    for i in range (19,23):
        for j in range(random.randint(10,30)):
            db.child("club").child('2022').child('08').child(i).push('data')

