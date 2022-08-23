from queue import Queue


class Thread_Messenger:
    def __init__(self):
        self.realtime_queue = Queue()
        self.storage_queue = Queue()
        self.telegram_queue = Queue()
        self.doorlock_queue = Queue()

    def get_realtime(self):
        return self.realtime_queue
    def get_storage(self):
        return self.realtime_queue
    def get_telegram(self):
        return self.realtime_queue
    def get_doorlock(self):
        return self.realtime_queue

    def put(self, keyword):
        self.realtime_queue.put(keyword)
        self.storage_queue.put(keyword)
        self.telegram_queue.put(keyword)
        self.doorlock_queue.put(keyword)