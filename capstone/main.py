import threading
from queue import Queue

import cv2
from datetime import datetime
import time
from jetson_nano.camera import Camera
from jetson_nano.doorlock import Doorlock
from db.firebase_database import firebase_database
from db.firebase_storage import firebase_storage
from messenger.Telegram import Telegram
from messenger.thread_messenger import Thread_Messenger

if __name__ == '__main__':
    camera = Camera()
    realtime_db = firebase_database(30)
    storage = firebase_storage()
    telegram = Telegram()
    doorlock = Doorlock()
    q = Thread_Messenger()

    realtime_thread = threading.Thread(target=realtime_db.insert, args=(q.get_realtime(),), daemon=True)
    storage_thread = threading.Thread(target=storage.insert, args=(q.get_storage(),), daemon=True)
    telegram_thread = threading.Thread(target=telegram.send, args=(q.get_telegram(),), daemon=True)
    doorlock_thread = threading.Thread(target=doorlock.action, args=(q.get_doorlock(),), daemon=True)

    realtime_thread.start()
    storage_thread.start()
    telegram_thread.start()
    doorlock_thread.start()

    while True:
        frame, name = camera.get_frame()
        print(f'name : {name}')
        cv2.namedWindow("webcam", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("webcam", frame)

        # 등록된 인원이 아닐경우
        if name == 'Unknown':
            # 이미지 캡쳐
            capImg = cv2.imwrite('Unknown.jpg', frame)
            print("capture img")
        q.put(name)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print("end")