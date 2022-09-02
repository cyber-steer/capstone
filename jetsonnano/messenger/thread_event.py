import threading


class Thread_Event:
    def __init__(self):
        self.a_event = threading.Event()
        self.b_event = threading.Event()

    def clearAll(self):
        self.a_event.clear()
        self.b_event.clear()
    def setAll(self):
        self.a_event.set()
        self.b_event.set()

    def is_set(self):
        return self.a_event.is_set() and self.b_event.is_set()


    # storage -> capture
    def get_a(self):
        return self.a_event
    # telegram -> capture
    def get_b(self):
        return self.b_event