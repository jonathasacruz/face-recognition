#RECONHECIMENTO FACIAL DE PESSOAS DESAPARECIDAS
#TURMA: CCO7NA
#PROFESSOR: JOÃO PAULO SANTOS
#ALUNOS:
# Ewerthon Santana de Almeida - 201907971
# Jônathas Alves da Cruz - 201902375
# Leandro Henrique Amorim - 201702295
# Micael Sousa Barbosa - 201907965
# Renan Monteiro Batista - 201903050


import sys
import cv2
import face_recognition
import pickle

name = input("enter name")
ref_id = input("enter id")

try:
    f=open("ref_name.pkl","rb") #Lê/Cria o arquivo de nomes
    ref_dictt=pickle.load(f) #Carrega o arquivo de nomes num dicionário
    f.close()
except:
    ref_dictt={}
ref_dictt[ref_id]=name #Adiciona ao dicionário de nomes, o nome registrado anteriormente


f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f) #Grava no arquivo de nomes o nome adicionado, de forma serializada.
f.close()

try:
    f=open("ref_embed.pkl","rb") #Lê/Cria o arquivo de faces codificadas
    embed_dictt=pickle.load(f) #Carrega o arquivo de codificações de faces num dicionário
    f.close()
except:
    embed_dictt={}

for i in range(5): #Faz a captura das imagens utilizando reconhecimento facial
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:

        check, frame = webcam.read()

        cv2.imshow("Capturing", frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        key = cv2.waitKey(1)

        if key == ord('s'):
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
pickle.dump(embed_dictt,f)
f.close()