from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student




class Face_Recorgnition_system:
    
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
        title_lbl.place(x=350,y=0,width=1530,height=120)

        #background image 

        img4=Image.open("images/bg copy.jpeg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1530,height=710)
 
        #the things will go above the bgimage area
        title_lbl=Label(self.root,text="FACE RECORGNISATION ATTENDENCE SYSTEM",font=("Comic Sans MS",35),bg="black",foreground="white")
        title_lbl.place(x=0,y=120,width=1530,height=45)

        #students button
        
        img5=Image.open("images/student.png",)
        img5=img5.resize((180,180))
        self.photoimg5=ImageTk.PhotoImage(img5)
        #button declaration
        b1=Button(bg_img,image=self.photoimg5,command=self.student_detail)
        b1.place(x=50,y=180,width=230,height=230)

        b1_1=Button(bg_img,text="STUDENT DETAIL",command=self.student_detail,cursor="spider",font=("times new roman",15,"bold"))
        b1_1.place(x=50,y=390,width=230,height=20)

        #detectface
        #students button
        img6=Image.open("images/face.png")
        img6=img6.resize((180,180))
        self.photoimg6=ImageTk.PhotoImage(img6)
        #button declaration
        b2=Button(bg_img,image=self.photoimg6)
        b2.place(x=300,y=180,width=230,height=230)

        b2_1=Button(bg_img,text="FACE DETECTION",cursor="spider",font=("times new roman",15,"bold"))
        b2_1.place(x=300,y=390,width=230,height=20)


#attendence

        #students button
        img7=Image.open("images/attendence.png")
        img7=img7.resize((180,180))
        self.photoimg7=ImageTk.PhotoImage(img7)
        #button declaration
        b3=Button(bg_img,image=self.photoimg7)
        b3.place(x=550,y=180,width=230,height=230)

        b3_1=Button(bg_img,text="ATTENEDENCE",cursor="spider",font=("times new roman",15,"bold"))
        b3_1.place(x=550,y=390,width=230,height=20)


        #helpdesk button
        img8=Image.open("images/helpdesk.png")
        img8=img8.resize((80,50))
        self.photoimg8=ImageTk.PhotoImage(img8)
        #button declaration
        b4=Button(self.root,image=self.photoimg8)
        b4.place(x=1240,y=0,width=80,height=50)

        b4_1=Button(self.root,text="HELPDESK",cursor="spider",font=("times new roman",15,"bold"))
        b4_1.place(x=1240,y=50,width=80,height=20)

        # train data button
        img9=Image.open("images/train.jpg.webp")
        img9=img9.resize((180,180))
        self.photoimg9=ImageTk.PhotoImage(img9)
        #button declaration
        b5=Button(bg_img,image=self.photoimg9)
        b5.place(x=800,y=180,width=230,height=230)

        b5_1=Button(bg_img,text="TRAIN DATA",cursor="spider",font=("times new roman",15,"bold"))
        b5_1.place(x=800,y=390,width=230,height=20)


        #6photos button
        img10=Image.open("images/photos.png")
        img10=img10.resize((180,180))
        self.photoimg10=ImageTk.PhotoImage(img10)
        #button declaration
        b6=Button(bg_img,image=self.photoimg10)
        b6.place(x=1040,y=180,width=200,height=230)

        b6_1=Button(bg_img,text="PHOTOS",cursor="spider",font=("times new roman",15,"bold"))
        b6_1.place(x=1040,y=390,width=200,height=20)

        #7 developer button
        img11=Image.open("images/dev.png")
        img11=img11.resize((80,50))
        self.photoimg11=ImageTk.PhotoImage(img11)
        #button declaration
        b7=Button(self.root,image=self.photoimg11)
        b7.place(x=1330,y=0,width=80,height=50)

        b7_1=Button(self.root,text="Developer",cursor="spider",font=("times new roman",15,"bold"))
        b7_1.place(x=1330,y=50,width=80,height=20)

        #exit button
        img12=Image.open("images/exit.png")
        img12=img12.resize((100,30))
        self.photoimg12=ImageTk.PhotoImage(img12)
        #button declaration
        b8=Button(bg_img,image=self.photoimg12)
        b8.place(x=1300,y=600,width=100,height=30)

        b8_1=Button(bg_img,text="EXIT",cursor="spider",font=("times new roman",15,"bold"))
        b8_1.place(x=1300,y=600,width=100,height=30)


        #================Function button=====================
        
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        







if __name__=="__main__":
    root=Tk()
    obj=Face_Recorgnition_system(root)
    root.mainloop()





