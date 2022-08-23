import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow('web', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
