# 03_face_recognition.py

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# UTF-8 string printing enabled
# def print_utf8_text(image, xy, text, color):  # utf-8 characters
#     fontName = 'FreeSansBold.ttf'  # 'FreeSansBold.ttf' # 'FreeMono.ttf' 'FreeSerifBold.ttf' ******* Freeserif.ttf olmadı ****
#     font = ImageFont.truetype(fontName, 24)  # select font
#     img_pil = Image.fromarray(image)  # convert image to pillow mode
#     draw = ImageDraw.Draw(img_pil)  # prepare image
#     draw.text((xy[0],xy[1]), text, font=font,
#               fill=(color[0], color[1], color[2], 0))  # b,g,r,a
#     image = np.array(img_pil)  # convert image to cv2 mode (numpy.array())
#     return image

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
# initiate id counter
id = 0
# names related to ids: example ==> Hamza: id=1,  etc
with open("musteriler.txt","r") as dosya:
    musteriler = dosya.readlines()
names = ["none"]

for eleman in musteriler:   
    isimler = eleman.split(")")[1].split("-")[0]
    names.append(isimler)

# Initialize and start realtime video capture
cam = cv2.VideoCapture(1)
cam.set(3, 1000)  # set video widht
cam.set(4, 800)  # set video height
# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
while True:
    ret, img = cam.read()
    # img = cv2.flip(img, -1)  # Flip vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(140 - confidence))
        else:
            id = "bilinmiyor"
            confidence = "  {0}%".format(round(140 - confidence))

        color = (255,255,255)
        # img=print_utf8_text(img,(x + 5, y - 25),str(id),color)
        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)


    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27 or k==ord('q'):
        break


# Do a bit of cleanup
print("\n [INFO] Programdan çıkıyor ve ortalığı temizliyorum")
cam.release()
cv2.destroyAllWindows()