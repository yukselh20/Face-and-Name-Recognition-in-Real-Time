# 01_face_dataset.py
import cv2
import os

cam = cv2.VideoCapture(1)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
# face_id = input('\n enter user id end press <return> ==>  ')


id = 1
ad = input("Müşterinin adını giriniz: ")
soyad = input("Müşterinin soyadını giriniz: ")
tcNo = input("Müşterinin Tc numarasını giriniz: ")

with open("musteriler.txt","r") as dosya:
    musterilerListesi = dosya.readlines()

if len(musterilerListesi) == 0:
    id = 1
else:
    with open("musteriler.txt","r") as dosya:
        id = int(musterilerListesi[-1].split(")")[0])  +1

        
with open("musteriler.txt","a+") as dosya:
    dosya.write("{}){}-{}-{}\n".format(id,ad,soyad,tcNo))

face_id = id

print("\n [INFO] Initializing face capture. Look at the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):
    ret, img = cam.read()
    # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 100: # Take 30 face sample and stop video //profil ayarlama....
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

