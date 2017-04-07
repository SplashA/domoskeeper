# import des lbrairies
from cv2 import *
import cv2 as cv2
from datetime import datetime
from time import sleep
from lib import compareImage
from lib import postEvent
from lib import smsTwilio
from lib import sendMail
import os
import base64 as base64

# Fonction de capture de photos
def photo_capture(frequency) :
    # Chemin des images
    imagePath = 'images'
    # La boucle prend des photos toutes les demies secondes et compare les photos pour vérifier s'il y a du changement
    while activated == 1:
        cam = VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        # Changement de résolution de l'image
        img = cv2.resize(img,(400,225))
        if s:    # si la capture s'est passée sans soucis
            now = datetime.now()
            # Création du fichier .jpg avec une concaténation de la date
            filename = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'_'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+':'+str(now.microsecond)+'.jpg'
            print(os.listdir(imagePath))
            # On teste si le dossier contient une image ou moins
            if (len(os.listdir(imagePath))<=1):
                imwrite(imagePath + "/" + filename,img) #save image
            else :
                # Si le dossier contient 2 images, on supprime la plus ancienne et on ajoute la nouvelle
                os.remove(imagePath + "/" + os.listdir(imagePath)[0])
                imwrite(imagePath + "/" + filename,img)
                # On compare les différences entre les deux images (ici: 25% de différence)
                if compareImage.compareImage(imagePath + "/" + os.listdir(imagePath)[0],imagePath + "/" + os.listdir(imagePath)[1])>25:
                    # Conversion de l'image en Base64 puis envoi dans la base MongoDB
                    with open(imagePath + "/" + os.listdir(imagePath)[1], "rb") as image_file:
                        encoded_string = "data:image/jpeg;base64," + base64.b64encode(image_file.read())
                    image_file.close()
                    postEvent.postEvent("58e5f7fb4b1ddb6d74af09aa","7433cb51f42f144a80ee36645b791548caaf473638992a3579013c1e71309dc9d70349296ac82a10cac7feeb67daa52f",encoded_string,now)
                    #smsTwilio.sendSms("+33644644866","+33699045380","Il y a eu du changement")
                    #sendMail.sendMail("julien.tellier@gmail.com")
                    print("Plus de 25 de diff")
                else:
                    print("Moins de 25 de diff")

        sleep(frequency)

activated = 1
frequency = 0.5
photo_capture(frequency)