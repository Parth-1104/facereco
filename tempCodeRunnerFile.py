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
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Arial",45),bg="black",foreground="white")
        title_lbl.place(x=0,y=200,width=1530,height=45)
