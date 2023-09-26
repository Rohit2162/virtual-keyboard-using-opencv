import cv2

# Opening up the integrated camera in the local system
capture = cv2.VideoCapture(0)
while True:
    success, image = capture.read()
    cv2.imshow("Camera", image)
    cv2.waitKey(1)