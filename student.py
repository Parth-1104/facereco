from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recorgnisation System")


        #===============variables==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_std_id=StringVar()
        self.var_year=StringVar()
        self.var_std_name=StringVar()
        #self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_sem=StringVar()
        self.var_radio2=StringVar()
        self.var_radio2=StringVar()
     #first img
        img=Image.open("images/ben10.png")
        img=img.resize((350,120))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=120)


        #white background
        title_lbl=Label(self.root,bg="white")
        title_lbl.place(x=350,y=0,width=1530,height=120)




         #background image 

        img4=Image.open("images/bg copy.jpeg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1530,height=710)
 
        #the things will go above the bgimage  area
        title_lbl=Label(self.root,text="STUDENTS DETAILS",font=("times new roman",35),bg="white",foreground="black")
        title_lbl.place(x=320,y=20,width=1230,height=45)

        main_frame=Frame(bg_img,bd=2,bg="grey")
        main_frame.place(x=0,y=0,width=1520,height=600)

#-------------------------------LEFT LABEL FRAME--------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="")
        Left_frame.place(x=10,y=10,width=700,height=580)

        #Academics box
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Academics",font=("times new roman",25,"bold"),foreground="black")
        current_course_frame.place(x=0,y=0,width=680,height=160)

        #multiple label(department)
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",18),bg="white",foreground="black")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",18),state="readonly",width=18)
        dep_combo["values"]=("Select Department","Computer Science","Mechanical","BJMC","LAW")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",18),bg="white",foreground="black")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",18),state="readonly",width=10)
        year_combo["values"]=("Select year","First","Second","third","Fourth","Fifth")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",18),bg="white",foreground="black")
        sem_label.grid(row=1,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",18),state="readonly",width=13)
        sem_combo["values"]=("Select Semester","First","Second")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

        #Gender

        gen_label=Label(current_course_frame,text="Gender:",font=("times new roman",18),bg="white",foreground="black")
        gen_label.grid(row=1,column=2,padx=10,sticky=W)

        gen_combo=ttk.Combobox(current_course_frame,textvariable=self.var_gender,font=("times new roman",18),state="readonly",width=13)
        gen_combo["values"]=("Select Gender","Male","Female")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        # Student information box
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",25,"bold"),foreground="black")
        class_Student_frame.place(x=0,y=165,width=680,height=250)
        
        
        
        #studentt id box
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",18),bg="white",foreground="black")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

       #entry box 
        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",18))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

         #studentt name box
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",18),bg="white",foreground="black")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

       #entry box 
        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",18))
        studentId_entry.grid(row=0,column=3,padx=10,sticky=W)


        #studentt roll no  box
        rollno_label=Label(class_Student_frame,text="Roll no:",font=("times new roman",18),bg="white",foreground="black")
        rollno_label.grid(row=2,column=2,padx=10,sticky=W)

       #entry box 
        rollno_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",18))
        rollno_entry.grid(row=2,column=3,padx=10,sticky=W)


        #dob  box
        DOB_label=Label(class_Student_frame,text="DOB:",font=("times new roman",18),bg="white",foreground="black")
        DOB_label.grid(row=1,column=0,padx=10,sticky=W)

       #entry box 
        DOB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",18))
        DOB_entry.grid(row=1,column=1,padx=10,sticky=W)

         #ph no   box
        phno_label=Label(class_Student_frame,text="contact no:",font=("times new roman",18),bg="white",foreground="black")
        phno_label.grid(row=1,column=0,padx=10,sticky=W)

       #entry box 
        phno_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",18))
        phno_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Email   box
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",18),bg="white",foreground="black")
        email_label.grid(row=1,column=2,padx=10,sticky=W)

       #entry box 
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",18))
        email_entry.grid(row=1,column=3,padx=10,sticky=W)

         #address  box
        Address_label=Label(class_Student_frame,text="address:",font=("times new roman",18),bg="white",foreground="black")
        Address_label.grid(row=2,column=0,padx=10,sticky=W)

       #entry box 
        Address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",18))
        Address_entry.grid(row=2,column=1,padx=10,sticky=W)



        #---------------------------------BUTTON SECTION --------------------------(Parth)

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=120,width=675,height=100)


        #button(save)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",18,"bold"))
        save_btn.grid(row=0,column=0,padx=20)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",18,"bold"))
        update_btn.grid(row=0,column=1,padx=20)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",18,"bold"))
        delete_btn.grid(row=0,column=2,padx=20)
        
        reset_btn=Button(btn_frame,text="reset",font=("times new roman",18,"bold"))
        reset_btn.grid(row=0,column=3,padx=20)

        #radio button

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(btn_frame,textvariable=self.var_radio1,text="with photo sample",value="Yes")
        radiobtn1.grid(row=1,column=0,padx=30,pady=20)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(btn_frame,textvariable=self.var_radio1,text="without photo sample",value="No")
        radiobtn2.grid(row=1,column=1)
        

        #face reco Box---------------------------------------

        btn_frame1=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=420,width=680,height=150)
        
        
        take_photo_btn=Button(btn_frame1,text="Face Scanner",font=("times new roman",18,"bold"))
        take_photo_btn.grid(row=0,column=0,padx=20)


        update_photo_btn=Button(btn_frame1,text="Update details",font=("Times New Roman",18,"bold"))
        update_photo_btn.grid(row=0,column=1,padx=20)
        





















#----------------------------RightLABEL FRAME--------------------------
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="")
        Right_frame.place(x=730,y=10,width=700,height=580)


#====================SEARCH SYSTEM++++++++++++++++==============================

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",25,"bold"),foreground="black")
        search_frame.place(x=0,y=10,width=680,height=150)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",18),foreground="black",bg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",18),state="readonly",width=18)
        search_combo["values"]=("Select","Roll no","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

       

        Search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",18))
        Search_entry.grid(row=0,column=2,padx=10,sticky=W)

        
        Search_btn=Button(search_frame,text="Search",font=("times new roman",18,"bold"))
        Search_btn.grid(row=1,column=0,padx=50)
        
        
        Showall_btn=Button(search_frame,text="Show All",font=("times new roman",18,"bold"))
        Showall_btn.grid(row=1,column=1,padx=50)



#================table frame=============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=170,width=680,height=350)


        #scroll bar=======

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Department","id","gen","course","year","sem","rollno","dob","Email","phone","photo","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("year",text="year")
        self.student_table.heading("course",text="course")
        self.student_table.heading("rollno",text="Rollno")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("Email",text="EmailID")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dob",text="BirthDate")
        self.student_table.heading("photo",text="photoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Department",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)

        #============funct dec


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            


        

        
        
        






        















if __name__=="__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()

