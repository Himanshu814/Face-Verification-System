from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Voter_details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x770+0+0")
        self.root.title("Face Recognition System")



        self.var_voterId = StringVar()
        self.var_Vname = StringVar()
        self.var_fname = StringVar()
        self.var_Gender = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_country = StringVar()
        self.var_pincode = StringVar()


        #img 1
        img1 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\sides.jpg")
        img1 = img1.resize((500,175), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=0, width= 500,height=175)


        #img2
        img2 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\voter_mid.jpg")
        img2= img2.resize((500,175), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=500, y=0, width= 500,height=175)

        #img3
        img3 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\sides.jpg")
        img3 = img3.resize((500,175), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image = self.photoimg3)
        f_lbl.place(x=1000, y=0, width= 500,height=175)


        #bg img
        img4 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\bg.jpg")
        img4 = img4.resize((1500,600), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image = self.photoimg4)
        bg_img.place(x=0, y=175, width= 1500,height=700)

        title_lb1 = Label(bg_img,text="VOTER'S DETAILS",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=10,width=1500,height=40)

        #main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=20,y=60,width=1460, height=700)


        #left frame

        Left_frame = LabelFrame(main_frame,bd=2, relief=RIDGE, text="Voter's Details", font = ("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=700,height=500)


        # Current Location 
        current_location_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Location", font = ("times new roman",12,"bold"), fg="navyblue")
        current_location_frame.place(x=10, y=20, width=650, height=115)

        # Country
        country_label = Label(current_location_frame, text="Country", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        country_label.grid(row=0, column=0, padx=5, pady=10)

        country_combo = ttk.Combobox(current_location_frame,textvariable=self.var_country,width=25,  font = ("times new roman",8), state="readonly")
        country_combo["values"] = ("Select Country", "India")
        country_combo.current(0)
        country_combo.grid(row=0, column=1, padx=15, pady=10,sticky=W)

        # State
        state_label = Label(current_location_frame, text="State", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        state_label.grid(row=0, column=3, padx=10, pady=10)
 
        state_combo = ttk.Combobox(current_location_frame,textvariable=self.var_state, width=25,font = ("times new roman",8), state="readonly")
        state_combo["values"] = ("Select State", "Maharashtra","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana")
        state_combo.current(0)
        state_combo.grid(row=0, column=4, padx=15, pady=10, sticky=W)

        # City
        city_label = Label(current_location_frame, text="City", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        city_label.grid(row=1, column=0, padx=10, sticky=W)

        # combo box 
        city_combo = ttk.Combobox(current_location_frame,width=25,textvariable=self.var_city, font = ("times new roman",8), state="readonly")
        city_combo["values"] = ("Select City", "Nagpur", "Amravati", "Gondia", "Katol")
        city_combo.current(0)
        city_combo.grid(row=1, column=1, padx=15, pady=10, sticky=W)       
        
        # Pincode 
        pincode_label = Label(current_location_frame, text="Pincode", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        pincode_label.grid(row=1, column=3, padx=10, sticky=W)

        pincode_entry = ttk.Entry(current_location_frame,textvariable=self.var_pincode,width=25,font=("times new roman", 8))
        pincode_entry.grid(row=1, column=4, padx=15, pady=5, sticky=W)
        

        # voter information
        voter_detail_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Voter Details", font=("times new roman", 12, "bold"), fg="navyblue")
        voter_detail_frame.place(x=10, y=150, width=650, height=300)

        # Voter id
        voterId_label = Label(voter_detail_frame, text="Voter-ID:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        voterId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        voterId_entry = ttk.Entry(voter_detail_frame,textvariable=self.var_voterId, font=("times new roman", 8))
        voterId_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Voter name
        Vname_label = Label(voter_detail_frame, text="Voter-Name:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        Vname_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        Vname_entry = ttk.Entry(voter_detail_frame,textvariable=self.var_Vname,  font=("times new roman", 8))
        Vname_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        
        # Voter Fname
        fname_label = Label(voter_detail_frame, text="Father/Spouse Name:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        fname_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        fname_entry = ttk.Entry(voter_detail_frame,textvariable=self.var_fname , font=("times new roman", 8))
        fname_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        # Gender
        Gender_label = Label(voter_detail_frame, text="Gender:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        Gender_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Gender_combo = ttk.Combobox(voter_detail_frame,textvariable=self.var_Gender,font=("times new roman", 8), state="readonly")
        Gender_combo["values"] = ("Select Gender","Male", "Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # DOB
        dob_label = Label(voter_detail_frame, text="DOB:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        dob_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        dob_entry = ttk.Entry(voter_detail_frame,textvariable=self.var_dob , font=("times new roman", 8))
        dob_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)


        # Address
        address_label = Label(voter_detail_frame, text="Address:", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        address_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        address_entry = ttk.Entry(voter_detail_frame,textvariable=self.var_address,  font=("times new roman", 8))
        address_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)



        #buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(voter_detail_frame,variable=self.var_radio1 ,text = "Photo Samples", value ="Yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2 = ttk.Radiobutton(voter_detail_frame,variable=self.var_radio1,text = "No Photo Samples", value ="No")
        radiobtn2.grid(row=4,column=1)


        #button frame
        btn_frame = Frame(voter_detail_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=210,width=633,height=50)

        save_btn= Button(btn_frame,text="Save data",command=self.add_data,width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0,column=0)

        update_btn= Button(btn_frame,text="Update data",command=self.update_data,width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        update_btn.grid(row=0,column=1)

        delete_btn= Button(btn_frame,text="Delete data",command=self.delete_data,width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        delete_btn.grid(row=0,column=2)

        reset_btn= Button(btn_frame,text="Reset data",command=self.reset_data,width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(voter_detail_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=235,width=633,height=25)

        take_photo_btn= Button(btn_frame1,text="Take Photo Sample",command=self.generate_img,width=44,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn= Button(btn_frame1,text="Update Photo Sample",width=44,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        update_photo_btn.grid(row=0,column=1)


        

        #right frame

        Right_frame = LabelFrame(main_frame,bd=2, relief=RIDGE, text="Voter's Details", font = ("times new roman",12,"bold"))
        Right_frame.place(x=740, y=10, width=700,height=500)

        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search Details", font = ("times new roman",12,"bold"), fg="navyblue")
        search_frame.place(x=10, y=20, width=680, height=70)

        search_label = Label(search_frame, text="Search By", font=("times new roman", 10, "bold"), fg="navyblue", bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 8), state="readonly")
        search_combo["values"] = ("Search Option","City", "Gender","DoB")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame,width=20,  font=("times new roman", 8))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        search_btn= Button(search_frame,text="Search",width=14,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        search_btn.grid(row=0,column=3,padx=10)

        showAll_btn= Button(search_frame,text="Show All",width=14,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=10)



        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=105, width=680, height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.voter_table = ttk.Treeview(table_frame,columns=("voterId","Vname","fname","Gender","dob","address","city","state","country","pincode","photo"),xscrollcommand= scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.voter_table.xview)
        scroll_y.config(command=self.voter_table.yview)

        self.voter_table.heading("voterId", text="Voter Id")
        self.voter_table.heading("Vname", text="Name")
        self.voter_table.heading("fname", text="Father's Name")
        self.voter_table.heading("Gender", text="Gender")
        self.voter_table.heading("dob", text="DOB")
        self.voter_table.heading("address", text="Address")
        self.voter_table.heading("city", text="City")
        self.voter_table.heading("state", text="State")
        self.voter_table.heading("country", text="Country")
        self.voter_table.heading("pincode", text="Pincode")
        self.voter_table.heading("photo", text="Photo Status")

        self.voter_table["show"] = "headings"

        self.voter_table.pack(fill=BOTH, expand=1)
        self.voter_table.column("voterId", width=100)
        self.voter_table.column("Vname", width=100)
        self.voter_table.column("fname", width=100)
        self.voter_table.column("Gender", width=100)
        self.voter_table.column("dob", width=100)
        self.voter_table.column("address", width=100)
        self.voter_table.column("city", width=100)
        self.voter_table.column("state", width=100)
        self.voter_table.column("country", width=100)
        self.voter_table.column("pincode", width=100)
        self.voter_table.column("photo", width=100)


        self.voter_table.pack(fill=BOTH,expand=1)
        self.voter_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()




    def add_data(self):
        if self.var_country.get() == "Select Country" or self.var_city.get()=="Select City" or self.var_state.get()=="Select State" or self.var_voterId.get() =="" or self.var_Vname.get() =="" or self.var_pincode.get() =="":
            messagebox.showerror("Error","All fields are required",parent = self.root)

        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into voter values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                    self.var_voterId.get(),
                                    self.var_Vname.get(),
                                    self.var_fname.get(),
                                    self.var_Gender.get(),
                                    self.var_dob.get(),
                                    self.var_address.get(),
                                    self.var_city.get(),
                                    self.var_state.get(),
                                    self.var_country.get(),
                                    self.var_pincode.get(),
                                    self.var_radio1.get()
                                  )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Voter details has been added Sucessully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    


    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from voter")
        data = my_cursor.fetchall()

        if len(data)!= 0:
            self.voter_table.delete(*self.voter_table.get_children())
            for i in data:
                self.voter_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event):
        cursor_focus = self.voter_table.focus()
        content = self.voter_table.item(cursor_focus)
        data = content["values"]

        self.var_voterId.set(data[0])
        self.var_Vname.set(data[1])
        self.var_fname.set(data[2])
        self.var_Gender.set(data[3])
        self.var_dob.set(data[4])
        self.var_address.set(data[5])
        self.var_city.set(data[6])
        self.var_state.set(data[7])
        self.var_country.set(data[8])
        self.var_pincode.set(data[9])
        self.var_radio1.set(data[10])
        

    def update_data(self):
        if self.var_country.get() == "Select Country" or self.var_city.get()=="Select City" or self.var_state.get()=="Select State" or self.var_voterId.get() =="" or self.var_Vname.get() =="" or self.var_pincode.get() =="":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this details",parent = self.root)
                if Update>0:
                    conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update voter set Vname=%s,fname=%s,Gender=%s,dob=%s,address=%s,city=%s,state=%s,country=%s,pincode=%s,photo=%s where voterId=%s",
                                      
                                      (self.var_Vname.get(),
                                      self.var_fname.get(),
                                      self.var_Gender.get(),
                                      self.var_dob.get(),
                                      self.var_address.get(),
                                      self.var_city.get(),
                                      self.var_state.get(),
                                      self.var_country.get(),
                                      self.var_pincode.get(),
                                      self.var_radio1.get(),
                                      self.var_voterId.get()
                                      ))
                    
                    
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)


    def delete_data(self):
        if self.var_voterId.get()=="":
            messagebox.showerror("Error", "VoterId is required",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Voter","Do you want to remove this voter",parent=self.root)
                if delete>0:
                    conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from voter where voterId=%s"
                    val = (self.var_voterId.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted the Voter",parent = self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)


    def reset_data(self):
        self.var_voterId.set(""),
        self.var_Vname.set(""),
        self.var_fname.set(""),
        self.var_Gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_city.set("Select City"),
        self.var_state.set("Select State"),
        self.var_country.set("Select Country"),
        self.var_pincode.set(""),
        self.var_radio1.set("")


    
    def generate_img(self):
        if self.var_country.get() == "Select Country" or self.var_city.get()=="Select City" or self.var_state.get()=="Select State" or self.var_voterId.get() =="" or self.var_Vname.get() =="" or self.var_pincode.get() =="":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from voter")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update voter set Vname=%s,fname=%s,Gender=%s,dob=%s,address=%s,city=%s,state=%s,country=%s,pincode=%s,photo=%s where voterId=%s",
                                      
                                      (self.var_Vname.get(),
                                      self.var_fname.get(),
                                      self.var_Gender.get(),
                                      self.var_dob.get(),
                                      self.var_address.get(),
                                      self.var_city.get(),
                                      self.var_state.get(),
                                      self.var_country.get(),
                                      self.var_pincode.get(),
                                      self.var_radio1.get(),
                                      self.var_voterId.get()
                                      ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped= img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame= cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=f"data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generating data set completed!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Voter_details(root)
    root.mainloop()