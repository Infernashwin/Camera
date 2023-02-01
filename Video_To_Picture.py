import cv2
import matplotlib.py as plt
from deepface import DeepFace
import numpy
import os

cam = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Camera", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        img_path = f"C:\\Users\\User\\Desktop\\Ashwin's Projects\\Work In Progress\\Facial Recognition\\{img_name}"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img =  cv2.imread(img_name)
        plt.imshow(img)
        color_img = cv2.cvtColor    (img, cv2.COLOR_BGR2RGB)
        try:
            prediction = DeepFace.analyze(color_img)
            print(prediction)
        except:
            print("You need a better image")

        try:
            os.remove(img_path)
        except:
             pass
        img_counter += 1

cam.release()

cv2.destroyAllWindows()