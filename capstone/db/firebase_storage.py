import pyrebase
import json
from datetime import datetime

class firebase_storage():
    with open("db/auth.json") as f:
        config = json.load(f)
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # unknown
    def img_insert(self, date):
        print("img_insert")
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        self.storage.child("club").child(year).child(month).child(day).child(date[11:19]).put("unknown.jpg")
    def insert(self, q):
        while True:
            name = q.get()
            if name == 'Unknown':
                self.img_insert(str(datetime.now()))