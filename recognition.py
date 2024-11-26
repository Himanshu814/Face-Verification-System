from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x500+300+150")
        self.root.title("Face Recognition System")

        self.root.protocol("WM_DELETE_WINDOW")


        title_lb1 = Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=10,width=700,height=40)

        img1 = Image.open(r"images\bg.jpg")
        img1 = img1.resize((700,500), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=50, width= 700,height=500)

        b1_1 = Button(self.root, text="Verify",command=self.recognition, cursor="hand2",font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b1_1.place(x=300, y=250, width=100, height=40)

    

    def verification(self,i,v,g,dob):
        already_in_file = set()
        with open("verified.csv","r+",newline="\n") as f:
            for line in f:
                already_in_file.add(line.split(",")[0])
            if((i not in already_in_file) and (v not in already_in_file) and (g not in already_in_file) and (dob not in already_in_file)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{v},{g},{dob},{dtString},{d1},Verified")




    def recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h , x:x+w])
                confidence = int((100*(1-predict/300)))

                conn= mysql.connector.connect(host="localhost",user="root",password="Salonid@123",database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select voterId from voter where voterId="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Vname from voter where voterId="+str(id))
                v = my_cursor.fetchone()
                v="+".join(v)

                my_cursor.execute("select Gender from voter where voterId="+str(id))
                g = my_cursor.fetchone()
                g="+".join(g)

                my_cursor.execute("select dob from voter where voterId="+str(id))
                dob = my_cursor.fetchone()
                dob="+".join(dob)


                if confidence>85:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{v}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Gender:{g}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"dob:{dob}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.verification(i,v,g,dob)

                elif confidence<60:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)

                coord = [x,y,w,h]

            return coord
        
        def face_recog(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap= cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            if not ret:
                print("Failed to capture image. Please check the camera.")
                break
            img = face_recog(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()




            

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()

