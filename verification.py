from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2.face
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog



myData=[]
class Verify:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")


        self.var_voterId= StringVar()
        self.var_Vname= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_time= StringVar()
        self.var_date= StringVar()
        self.var_verification= StringVar()


        img1 = Image.open(r"images\bg.jpg")
        img1 = img1.resize((1500,600), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x=0, y=0, width= 1500,height=700)

        title_lb1 = Label(bg_img,text="Verified Voters",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=10,width=1500,height=40)

        #main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=15,y=100,width=1460, height=700)

        Left_frame = LabelFrame(main_frame,bd=2, relief=RIDGE, text="Voter's Details", font = ("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=700,height=500)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=15,y=30,width=650,height=450)



        voterId_label = Label(left_inside_frame, text="Voter ID:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        voterId_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

        voterId = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_voterId,font=("times new roman", 8))
        voterId.grid(row=0, column=1, padx=15, pady=15, sticky=W)



        Vname_label = Label(left_inside_frame, text="Voter Name:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        Vname_label.grid(row=1, column=0, padx=15, pady=15, sticky=W)

        Vname = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Vname,font=("times new roman", 8))
        Vname.grid(row=1, column=1, padx=15, pady=15, sticky=W)




        gender_label = Label(left_inside_frame, text="Gender:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        gender_label.grid(row=2, column=0, padx=15,pady=15, sticky=W)

        gender = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_gender,font=("times new roman", 8))
        gender.grid(row=2, column=1, padx=15, pady=15, sticky=W)



        dob_label = Label(left_inside_frame, text="Date of Birth:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        dob_label.grid(row=3, column=0, padx=15,pady=15, sticky=W)

        dob = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_dob,font=("times new roman", 8))
        dob.grid(row=3, column=1, padx=15, pady=15, sticky=W)



        time_label = Label(left_inside_frame, text="Time:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        time_label.grid(row=4, column=0, padx=15,pady=15, sticky=W)

        time = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_time,font=("times new roman", 8))
        time.grid(row=4, column=1, padx=15, pady=15, sticky=W)



        date_label = Label(left_inside_frame, text="Date:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        date_label.grid(row=5, column=0, padx=15,pady=15, sticky=W)

        date = ttk.Entry(left_inside_frame,width=25,textvariable=self.var_date,font=("times new roman", 8))
        date.grid(row=5, column=1, padx=15, pady=15, sticky=W)



        verification_label = Label(left_inside_frame, text="Verification status:", font = ("times new roman",10,"bold"), bg="white", fg="navyblue")
        verification_label.grid(row=6, column=0, padx=15,pady=15, sticky=W)


        verification_combo = ttk.Combobox(left_inside_frame,width=25,textvariable=self.var_verification, font = ("times new roman",8), state="readonly")
        verification_combo["values"] = ("Status","Verifed","Non Verified")
        verification_combo.current(0)
        verification_combo.grid(row=6, column=1, padx=12, pady=12, sticky=W) 


        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=375,width=633,height=50)

        save_btn= Button(btn_frame,text="Import.csv",width=21,command=self.importcsv,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0,column=0)

        update_btn= Button(btn_frame,text="Export.csv",width=21,command=self.exportcsv,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        update_btn.grid(row=0,column=1)

        delete_btn= Button(btn_frame,text="Delete data",width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        delete_btn.grid(row=0,column=2)

        reset_btn= Button(btn_frame,text="Reset data",width=21,font=("times new roman", 10, "bold"), fg="white", bg="navyblue")
        reset_btn.grid(row=0,column=3)



        Right_frame = LabelFrame(main_frame,bd=2, relief=RIDGE, text="Details of Verified Voters", font = ("times new roman",12,"bold"))
        Right_frame.place(x=740, y=10, width=700,height=500)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=40,y=30,width=600,height=400)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.VerifiedTable = ttk.Treeview(table_frame,column=("voterId","Vname","Gender","dob","time","date","verification"),xscrollcommand= scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.VerifiedTable.xview)
        scroll_y.config(command=self.VerifiedTable.yview)

        self.VerifiedTable.heading("voterId",text="VoterID")
        self.VerifiedTable.heading("Vname",text="Voter Name")
        self.VerifiedTable.heading("Gender",text="Gender")
        self.VerifiedTable.heading("dob",text="Date of Birth")
        self.VerifiedTable.heading("time",text="Time")
        self.VerifiedTable.heading("date",text="Date")
        self.VerifiedTable.heading("verification",text="Verification Status")

        self.VerifiedTable["show"]="headings"


        self.VerifiedTable.pack(fill=BOTH,expand=1)

        self.VerifiedTable.bind("<ButtonRelease>",self.get_cursor)


    
    def fetchData(self,rows):
        self.VerifiedTable.delete(*self.VerifiedTable.get_children())
        for i in rows:
            self.VerifiedTable.insert("",END,values=i)


    def importcsv(self):
        global myData
        myData.clear()
        fln= filedialog.askopenfilename(initialdir = os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)


    def exportcsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("no data","no data found to export",parent = self.root)
                return False
            fln= filedialog.askopenfilename(initialdir = os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write= csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.append(i)
                messagebox.showinfo("data export","Successful")

        except Exception as es:
            messagebox.showerror("error", f"due to :{str(es)}",parent=self.root)




    def get_cursor(self,event=""):
        cursor_row = self.VerifiedTable.focus()
        content=self.VerifiedTable.item(cursor_row)
        rows = content['values']

        if rows:
            self.var_voterId.set(rows[0]),
            self.var_Vname.set(rows[1]),
            self.var_gender.set(rows[2]),
            self.var_dob.set(rows[3]),self.var_time.set(rows[4]),
            self.var_date.set(rows[5]),
            self.var_verification.set(rows[6])

        else:
            messagebox.showwarning("Selection Error", "No valid data selected.", parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Verify(root)
    root.mainloop()