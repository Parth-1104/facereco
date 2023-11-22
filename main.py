from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import subprocess
from train import Train
from face_recognition import reco
import webbrowser
#from face_recognition import Face_Recognition


class Face_Recorgnition_system:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recorgnisation System")



#first img
        img=Image.open("images/ben10.png")
        img=img.resize((350,150))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg,bg="white")
        f_lbl.place(x=0,y=0,width=350,height=150)
#2nd image 
        #img2=Image.open("images/bennett.png")
        #img2=img2.resize((900,120))
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #f_lbl=Label(self.root,image=self.photoimg2)
        #f_lbl.place(x=350,y=0,width=920,height=120)

#image 3
       # img3=Image.open("images/pic3.jpeg")
        #img3=img3.resize((500,120))
       # self.photoimg3=ImageTk.PhotoImage(img3)
#
       # f_lbl=Label(self.root,image=self.photoimg3)
       # f_lbl.place(x=1000,y=0,width=500,height=120)

        title_lbl=Label(self.root,bg="white")
        title_lbl.place(x=350,y=0,width=1530,height=150)

        title_lbl2=Label(self.root,bg="#004aad")
        title_lbl2.place(x=0,y=150,width=1530,height=20)

        
        

        #background image 

        img4=Image.open("images/bg copy.jpeg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=170,width=1530,height=710)
 
        #the things will go above the bgimage area
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Arial",45),bg="black",foreground="white")
        title_lbl.place(x=0,y=200,width=1530,height=45)

        #students button
        
        img5=Image.open("images/student.png",)
        img5=img5.resize((230,230))
        self.photoimg5=ImageTk.PhotoImage(img5)
        #button declaration
        b1=Button(bg_img,image=self.photoimg5,command=self.student_detail)
        b1.place(x=50,y=180,width=230,height=230)

        b1_1=Button(bg_img,command=self.student_detail,text="Student Detail",cursor="spider",font=("times new roman",15,"bold"))
        b1_1.place(x=50,y=390,width=230,height=50)

        #detectface
        #students button
        img6=Image.open("images/face.png")
        img6=img6.resize((230,230))
        self.photoimg6=ImageTk.PhotoImage(img6)
        #button declaration
        b2=Button(bg_img,command=self.face_data,image=self.photoimg6)
        b2.place(x=330,y=180,width=230,height=230)

        b2_1=Button(bg_img,command=self.face_data,text="Face Detection",cursor="spider",font=("times new roman",15,"bold"))
        b2_1.place(x=330,y=390,width=230,height=50)

        


#attendence

        #students button
        img7=Image.open("images/attendence.png")
        img7=img7.resize((230,230))
        self.photoimg7=ImageTk.PhotoImage(img7)
        #button declaration
        b3=Button(bg_img,image=self.photoimg7)
        b3.place(x=610,y=180,width=230,height=230)

        b3_1=Button(bg_img,text="Attendance",cursor="spider",font=("times new roman",15,"bold"))
        b3_1.place(x=610,y=390,width=230,height=50)

        

        # train data button
        img9=Image.open("images/train.jpg.webp")
        img9=img9.resize((230,230))
        self.photoimg9=ImageTk.PhotoImage(img9)
        #button declaration
        b5=Button(bg_img,command=self.train_data,image=self.photoimg9)
        b5.place(x=885,y=180,width=230,height=230)

        b5_1=Button(bg_img,command=self.train_data,text="Train Database",cursor="spider",font=("times new roman",15,"bold"))
        b5_1.place(x=885,y=390,width=230,height=50)


        # 6 photos button
        img10 = Image.open("images/photos.png")
        img10 = img10.resize((230, 230))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        # button declaration
        b6 = Button(bg_img, command=self.open_img, image=self.photoimg10)
        b6.place(x=1150, y=180, width=230, height=230)

        b6_1 = Button(bg_img, text="Photos", command=self.open_img, cursor="spider", font=("times new roman",15,"bold"))
        b6_1.place(x=1150, y=390, width=230, height=50,)

       


    

    def open_img(self):
       try:
          subprocess.call(["open", "data"])
       except FileNotFoundError:
        print("Error: 'open' command not found. You might be using a non-macOS system.")
  
        #================Function button=====================
        
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=reco(self.new_window)

    def open_website(self):
        webbrowser.open("https://www.bennett.edu.in")

        
    




if __name__=="__main__":
    root=Tk()
    obj=Face_Recorgnition_system(root)
    root.mainloop()





