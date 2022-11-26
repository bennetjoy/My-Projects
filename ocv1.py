import cv2
import face_recognition
 
imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Bill gates.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgElon)&#91;0]
encodeElon = face_recognition.face_encodings(imgElon)&#91;0]
cv2.rectangle(imgElon,(faceLoc&#91;3],faceLoc&#91;0]),(faceLoc&#91;1],faceLoc&#91;2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)&#91;0]
encodeTest = face_recognition.face_encodings(imgTest)&#91;0]
cv2.rectangle(imgTest,(faceLocTest&#91;3],faceLocTest&#91;0]),(faceLocTest&#91;1],faceLocTest&#91;2]),(255,0,255),2)
 
results = face_recognition.compare_faces(&#91;encodeElon],encodeTest)
faceDis = face_recognition.face_distance(&#91;encodeElon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis&#91;0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)