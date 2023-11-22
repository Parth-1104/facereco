from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class reco:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ...

        # Train button
        b1_1 = Button(self.root, text="Start Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 45), bg="blue", foreground="black")
        b1_1.place(x=500, y=180, width=530, height=230)

    def face_recog(self):
        face_cascade_path = "haarcascade_frontalface_default.xml"
        face_cap = cv2.CascadeClassifier(face_cascade_path)

        # Folder path containing images
        image_folder = "/Users/parthpankajsingh/Desktop/facereco/data"

        for filename in os.listdir(image_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(image_folder, filename)

                # Read the image
                img = cv2.imread(image_path)

                # Convert the frame to grayscale for face detection
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Detect faces
                faces = face_cap.detectMultiScale(
                    gray_img,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                # Draw rectangles around the detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display the resulting frame
                cv2.imshow("Image", img)
                cv2.waitKey(0)  # Wait for a key press before moving to the next image

        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    recognizer = reco(root)
    root.mainloop()
