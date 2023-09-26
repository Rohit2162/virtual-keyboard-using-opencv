import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

# Opening up the integrated camera in the local system
capture = cv2.VideoCapture(0)
# Setting up the width x height of the video frame
capture.set(3, 1280)
capture.set(4, 720)

# Intializing hand detection using cvzone library
# "detection confidence" and it's typically a threshold or confidence level for detecting hands. In this case, it's set to 0.8, meaning that the detector should only consider a hand as detected if it's at least 80% confident that a hand is present in the analyzed image or frame.
detector = HandDetector(detectionCon=0.8)


class Button:
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.text = text
        self.size = size

        x, y = self.pos
        w, h = self.size
        cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 0), cv2.FILLED)
        cv2.putText(
            image,
            "Q",
            (120, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (255, 255, 255),
            5,
        )


while True:
    success, image = capture.read()
    immage = detector.findHands(image)  # finds the hand in the frame
    lmlist, bboxInfo = detector.findPosition(
        image
    )  # helps finds landmarks for the hand in the frame, lmlist - landmark list, bboxInfo - bounding box

    cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 0), cv2.FILLED)
    cv2.putText(image, "Q", (120, 180), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)

    cv2.imshow("Camera", image)
    cv2.waitKey(1)
