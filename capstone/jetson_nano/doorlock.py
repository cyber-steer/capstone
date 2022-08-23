# import Jetson.GPIO as GPIO
import time

class Doorlock:
    # Pin Definitions
    output_pin = 18  # BCM pin 18, BOARD pin 12

    def open(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.HIGH)

        # curr_value = GPIO.HIGH
        print("Door Open")
        try:
            for i in range(1, 3):
                time.sleep(1)
                # print("Outputting {} to pin {}".format(curr_value, output_pin))
                # GPIO.output(self.output_pin, GPIO.LOW)
                
        finally:
            # GPIO.cleanup()
            pass

    def action(self, q):
        while True:
            name = q.get()
            if name !='' and name != 'Unknown':
                self.open()