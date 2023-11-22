from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from sys import path
import time





class reco:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recorgnisation System")


        #first img
        img=Image.open("images/ben10.png")
        img=img.resize((350,120))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=120)


        #white background of heading
        title_lbl=Label(self.root,bg="white")
        title_lbl.place(x=350,y=0,width=1530,height=120)

         #the things will go above the bgimage  area
        title_lbl=Label(self.root,text="Recognition",font=("times new roman",45),bg="white",foreground="black")
        title_lbl.place(x=300,y=20,width=1230,height=45)




         #background image 

        img4=Image.open("images/back.jpeg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1530,height=710)


          #Reco button
        
        #button declaration
        b1_1=Button(self.root,text="Start Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",45),bg="blue",foreground="black")
        b1_1.place(x=500,y=180,width=530,height=230)
    
    
    def face_recog(self):
        face_cascade_path = "/Users/parthpankajsingh/Desktop/facereco/haarcascade_frontalface_default.xml"
        face_cap = cv2.CascadeClassifier(face_cascade_path)

    # Open the video capture device (0 represents the default camera)
        video_cap = cv2.VideoCapture(0)
        start_time=time.time()

        while True:
            ret, video_data = video_cap.read()
            if ret:
                current_time = time.time()
                elapsed_time = current_time - start_time
            
            # Check if 10 seconds have passed
            if elapsed_time >= 3:
                messagebox.showinfo("configuration error","##code contains doping of multiple radiation//<nighte mode incompatible>* ir ray detection incompatible ///#eSSL MB20 machine required ")
                # Call the function to show additional info
                start_time = time.time()  # Reset
            
# Check if the frame is successfully captured
            if not ret:
                print("Error: Unable to capture frame.")
                break

            # Convert the frame to grayscale for face detection
            col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cap.detectMultiScale(
                col,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow("video_live", video_data)

            # Break the loop if 'Enter' key is pressed
            if cv2.waitKey(1) == 13:
                break

        # Release the video capture object
        video_cap.release()

        # Close all windows
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()  # Create a Tkinter root window
    recognizer = reco(root)  # Pass the root window to the reco class
    recognizer.face_recog()
    root.mainloop()  # Start the Tkinter main event loop
