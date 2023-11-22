from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from sys import path





class Train:
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
        title_lbl=Label(self.root,text="Train Data",font=("times new roman",45),bg="white",foreground="black")
        title_lbl.place(x=300,y=20,width=1230,height=45)




         #background image 

        #img4=Image.open("images/back.jpeg")
        #img4=img4.resize((1530,710))
        #self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,background="sky blue")
        bg_img.place(x=0,y=150,width=1530,height=710)
 
       


         #Train button
        
        #button declaration
        b1_1=Button(self.root,text="Start Training",command=self.train_classifier,cursor="hand2",font=("times new roman",45),bg="blue",foreground="black")
        b1_1.place(x=500,y=180,width=530,height=230)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        #video_cap = cv2.VideoCapture(0)
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            if cv2.waitKey(1) == 13:
                break

        # Release the video capture object
        #video_cap.release()

        # Close all windows
        cv2.destroyAllWindows()
        #==========train classifire============
        clf= cv2.FaceRecognizerSF()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

















if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() 