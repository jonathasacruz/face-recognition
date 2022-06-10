# Instalar a biblioteca OpenCV direto do site não funcionou, instalei opencv-python dentro do pycharm;
# É necessário instalar o Visual Studio C++ (IDE), CMake, Wheels, DLIB e opencv-python

import sys
import cv2
import face_recognition
import pickle

name=input("enter name") #Nome e ID para o rosto que está sendo treinado
ref_id=input("enter id")

try:
    f=open("ref_name.pkl","rb") #Abre(cria) o arquivo ref_name no modo leitura/binário

    ref_dictt=pickle.load(f) #Pickle: serialização do arquivo "f" e armazenamento num dicionário de referências
    f.close()
except:
    ref_dictt={}
ref_dictt[ref_id]=name #Armazena o nome com o id atribuído


f=open("ref_name.pkl","wb") #Abre o arquivo ref_name no modo escrita/binário
pickle.dump(ref_dictt,f) #Escreve o dicionário atualizado no arquivo "f"
f.close()

try: #Cria o arquivo e dicionário de referência de imagens incorporadas
    f=open("ref_embed.pkl","rb")

    embed_dictt=pickle.load(f)
    f.close()
except:
    embed_dictt={}

for i in range(5): #Captura das imagens
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0) #captura o fluxo da webcam do comuptador, pode ser alterado para receber arquivos
    while True:

        check, frame = webcam.read() #Captura do fluxo da webcam

        cv2.imshow("Capturing", frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        key = cv2.waitKey(1)

        if key == ord('s'): #Cria o dicionário de rostos reconhecidos pela biblioteca face_recognition
            face_locations = face_recognition.face_locations(rgb_small_frame)
            if face_locations != []:
                face_encoding = face_recognition.face_encodings(frame)[0]
                if ref_id in embed_dictt:
                    embed_dictt[ref_id] += [face_encoding]
                else:
                    embed_dictt[ref_id] = [face_encoding]
                webcam.release()
                cv2.waitKey(1)
                cv2.destroyAllWindows()
                break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f) #grava as alterações
f.close()