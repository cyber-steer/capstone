import pyrebase
import datetime
import json

class firebase_database():

    def __init__(self, delay = 10):
        self.delay = delay
        self.last_person = None
        with open("db/auth_database.json") as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db=firebase.database()

    def insert(self, q):
        while True:
            name = q.get()
            if name != "":
                self.set(name)
    # firebase에 추가
    def set(self, name):
        date = str(datetime.datetime.now())
        data = {name:date}
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
                key =key
                val =val
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