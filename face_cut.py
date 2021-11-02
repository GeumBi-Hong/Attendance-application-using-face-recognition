import cv2
import os

class Face_cut:
    def __init__(self):
         

    def facecrop(image):
        facedata = "haarcascade_frontalface_alt.xml"
        cascade = cv2.CascadeClassifier(facedata)

        img = cv2.imread(image)

        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x-5,y-5), (x+w+5,y+h+5), (255,255,255))

            sub_face = img[y-5:y+h+5, x-5:x+w+5]
            fname, ext = os.path.splitext(image)
            print(fname)
            cv2.imwrite(fname+"_cut"+ext, sub_face)
        return

