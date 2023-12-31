import cv2
from keras.models import model_from_json
import numpy as np


def get_emotions():
    file = open("emotion_analysis.json", "r")
    model = file.read()
    file.close()
    my_model = model_from_json(model)

    my_model.load_weights("emotion_analysis.h5")
    haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade=cv2.CascadeClassifier(haar_file)

    def feature_extraction(image):
        feature = np.array(image)
        feature = feature.reshape(1,48,48,1)
        return feature/255.0

    web_cam=cv2.VideoCapture(0)
    label_map = {0:'anger', 1:'disgust', 2:'fear', 3:'joyful', 4: 'sadness', 5: 'surprise', 6: 'neutral'}
    print("Will now run...")
    while True:
        _,im=web_cam.read()
        gray_color=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(im,1.3,5)
        try: 
            for (p,q,r,s) in faces:
                image = gray_color[q:q+s,p:p+r]
                cv2.rectangle(im,(p,q),(p+r,q+s),(255,0,0),2)
                image = cv2.resize(image,(48,48))
                img = feature_extraction(image)
                pred = my_model.predict(img)
                prediction_label = label_map[pred.argmax()]
                cv2.putText(im, '% s' %(prediction_label), (p-10, q-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2, (0,0,255))
            cv2.imshow("Output",im)
            cv2.waitKey(27)
        except cv2.error:
            raise ValueError()

    return None