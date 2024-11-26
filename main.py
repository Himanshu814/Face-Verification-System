from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
from voter import Voter_details
import os
from train import Train
from recognition import Face_recognition
from verification import Verify

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x770+0+0")
        self.root.title("Face Recognition System")


        #img 1
        img1 = Image.open(r"images\a.jpg")
        img1 = img1.resize((500,200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=0, width= 500,height=200)


        #img2
        img2 = Image.open(r"images\middle.jpg")
        img2= img2.resize((500,200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=500, y=0, width= 500,height=200)

        #img3
        img3 = Image.open(r"images\b.jpg")
        img3 = img3.resize((500,200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image = self.photoimg3)
        f_lbl.place(x=1000, y=0, width= 500,height=200)



        #bg img
        img4 = Image.open(r"images\bg.jpg")
        img4 = img4.resize((1500,600), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image = self.photoimg4)
        bg_img.place(x=0, y=200, width= 1500,height=600)

        title_lb1 = Label(bg_img,text="FACE VERIFICATION VOTING SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1500,height=40)



        # voters details button
        img5 = Image.open(r"images\card.jpg")
        img5 = img5.resize((150,150), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image= self.photoimg5,command=self.details, cursor="hand2")
        b1.place(x=275, y=80, width=150, height=150)


        b1_1 = Button(bg_img, text="Voter Details",command=self.details, cursor="hand2",font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b1_1.place(x=275, y=230, width=150, height=30)


        # verification button
        img6 = Image.open(r"images\verification.jpg")
        img6 = img6.resize((150,150), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img, image= self.photoimg6, cursor="hand2")
        b2.place(x=675, y=80, width=150, height=150)


        b2_1 = Button(bg_img, text="Verification", cursor="hand2",command=self.face_reg,font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b2_1.place(x=675, y=230, width=150, height=30)



        # verified voters button
        img7 = Image.open(r"images\verified.jpg")
        img7 = img7.resize((150,150), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img, image= self.photoimg7, cursor="hand2")
        b3.place(x=1075, y=80, width=150, height=150)


        b3_1 = Button(bg_img, text="Verified Voters", cursor="hand2",command=self.verification,font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b3_1.place(x=1075, y=230, width=150, height=30)



        # train data button

        img8 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\training.jpg")
        img8 = img8.resize((150,150), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img, image= self.photoimg8, cursor="hand2",command=self.train_details)
        b4.place(x=275, y=300, width=150, height=150)


        b4_1 = Button(bg_img, text="Train data", cursor="hand2",command=self.train_details,font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b4_1.place(x=275, y=450, width=150, height=30)

       
       
        # Voter Image button
        img9 = Image.open(r"images\voter_imgs.jpg")
        img9 = img9.resize((150,150), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img, image= self.photoimg9, cursor="hand2",command=self.open_img)
        b5.place(x=675, y=300, width=150, height=150)


        b5_1 = Button(bg_img, text="Voter Image", cursor="hand2",command=self.open_img,font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b5_1.place(x=675, y=450, width=150, height=30)


        

        
        #exit button

        img10 = Image.open(r"C:\Users\salon\OneDrive\Desktop\voting system\images\exit.jpg")
        img10 = img10.resize((150,150), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img, image= self.photoimg10, cursor="hand2",command=self.iexit)
        b6.place(x=1075, y=300, width=150, height=150)


        b6_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iexit,font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b6_1.place(x=1075, y=450, width=150, height=30)





    def open_img(self):
        os.startfile("data")



    def iexit(self):
        self.iexit= tkinter.messagebox.askyesno("face recognition","are you sure?",parent= self.root)
        if self.iexit>0:
              self.root.destroy()

        else:
              return



    def details(self):
            self.new_window = Toplevel(self.root)
            self.app = Voter_details(self.new_window)


    def train_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)


    def face_reg(self):
            self.new_window = Toplevel(self.root)
            self.app = Face_recognition(self.new_window)


    def verification(self):
            self.new_window = Toplevel(self.root)
            self.app = Verify(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
