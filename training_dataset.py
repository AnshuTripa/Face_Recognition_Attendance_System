import os,cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #create empty face list
    faceSamples = []
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id = os.path.split(imagePath)[-1].split(".")[1]  # keep ID as string

        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids

faces,Ids = getImagesAndLabels('dataSet/')
recognizer.train(faces, np.array([i for i in range(len(Ids))]))  # use numeric labels temporarily
recognizer.write('trainer/trainer.yml')
if os.path.exists(os.getcwd()+'/trainer/trainer.yml'):
    os.system("python message_gui.py")