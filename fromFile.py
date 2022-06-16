# Instalar a biblioteca OpenCV direto do site não funcionou, instalei opencv-python dentro do pycharm;
# É necessário instalar o Visual Studio C++ (IDE), CMake, Wheels, DLIB e opencv-python
import sys
import cv2
import face_recognition
import pickle
import tkinter
from tkinter import filedialog


name = input("enter name")
ref_id = input("enter id")

try:
    f=open("ref_name.pkl","rb")

    ref_dictt=pickle.load(f)
    f.close()
except:
    ref_dictt={}
ref_dictt[ref_id]=name


f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()

try:
    f=open("ref_embed.pkl","rb")

    embed_dictt=pickle.load(f)
    f.close()
except:
    embed_dictt={}

#     OPEN file selection dialog
path = filedialog.askopenfilenames()

n = 0
for p in path:
    n+=1
    print (str(n) + "=>" + p)
    img = cv2.imread(p)

    img_small = cv2.resize(img,(100,100),interpolation=0)
    face_locations = face_recognition.face_locations(img_small)
    if face_locations:
        face_encoding = face_recognition.face_encodings(img)[0]
        if ref_id in embed_dictt:
            embed_dictt[ref_id] += [face_encoding]
        else:
            embed_dictt[ref_id] = [face_encoding]

f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f)
f.close()