

import numpy
from PIL import Image

import cv2
import speech
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
font = cv2.FONT_HERSHEY_SIMPLEX
P = "D:\\haarcascade_frontalface_default.xml"

#为了方便直接运行，录制了一个模型里有的人脸视频进行识别
#cap = cv2.VideoCapture('1.mp4')

#调用摄像头
cap = cv2.VideoCapture(0)
d = cv2.CascadeClassifier(P)
color = (0, 255, 0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = d.detectMultiScale(gray, 1.2, 5)
    for (x, y, h, w) in faces:
        img = cv2.rectangle(img, (x - 50, y - 50), (x + w + 50, y + h + 50), (255, 0, 0), 2)
        img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if conf > 50:
            if img_id == 1:
                img_id = 'yangyiyi'
                print(img_id)
                output = '杨依依'
                speech.say(output)

            if img_id == 2:
                img_id = 'Hua Nephew'
                print(img_id)
                output = '侄子小华'
                speech.say(output)
        else:
            img_id = "Unknown"
        cv2.putText(img, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('box', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
