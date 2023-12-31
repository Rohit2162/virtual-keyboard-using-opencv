import streamlit as st
import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = HandDetector(detectionCon=0.9)

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
]

ClickedText = ""
keyboard = Controller()


def drawALL(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (126, 121, 113), cv2.FILLED)
        cv2.putText(
            img,
            button.text,
            (x + 20, y + 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (255, 255, 255),
            3,
        )
    return img


class Button:
    def __init__(self, pos, text, size=None):
        if size is None:
            size = [80, 80]
        self.pos = pos
        self.text = text
        self.size = size


# myButton = Button([100,100],'Q')
# myButton1 = Button([200,100],'W')
# myButton2 = Button([300,100],'E')
# myButton3 = Button([400,100],'R')
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    drawALL(img, buttonList)

    if lmlist:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            if x < lmlist[8][0] < x + w and y < lmlist[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
                cv2.putText(
                    img,
                    button.text,
                    (x + 20, y + 65),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 255, 255),
                    3,
                )
                l, _, _ = detector.findDistance(8, 12, img)
                # print(l)
                if l < 50:
                    keyboard.press(button.text)
                    cv2.rectangle(
                        img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED
                    )
                    cv2.putText(
                        img,
                        button.text,
                        (x + 20, y + 65),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 255, 255),
                        3,
                    )
                    ClickedText += button.text
                    sleep(0.2)
    cv2.rectangle(img, (55, 345), (1100, 450), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, ClickedText, (60, 425), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

    # cv2.rectangle(img,(100,100),(200,200),(0,0,0),cv2.FILLED)
    # cv2.putText(img,'Q',(120,180),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),5)
    # myButton = Button([100,100],'Q')

    # img = myButton1.draw(img)
    # img = myButton2.draw(img)
    # img = myButton3.draw(img)
    cv2.imshow("Camera Feed", img)
    cv2.waitKey(1)

st.title("Virtual Keyboard App")

# Create Streamlit widgets for user interaction
text_input = st.text_input("Enter text:")
virtual_keyboard_button = st.button("Show Virtual Keyboard")

if virtual_keyboard_button:
    # Call your OpenCV virtual keyboard code here
    # and display the result
    st.write("Virtual Keyboard Output: ")
    # Call your OpenCV functions here and display the result
