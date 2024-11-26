from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2.face
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x500+300+150")
        self.root.title("Face Recognition System")


        title_lb1 = Label(self.root,text="TRAIN DATASET",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=10,width=700,height=40)

        img1 = Image.open(r"images\bg.jpg")
        img1 = img1.resize((700,500), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=50, width= 700,height=500)

        b1_1 = Button(self.root, text="Train data",command=self.train_classifier  , cursor="hand2",font=("times new roman",14,"bold"),bg="pink",fg="navyblue")
        b1_1.place(x=300, y=250, width=100, height=40)


    def train_classifier(self):
        data_dir="data"
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')
            imageNp= np.array(img,'uint8')
            try:
                filename = os.path.split(image)[1]
                filename_parts = filename.split('.')
                if len(filename_parts) > 1 and filename_parts[1].isdigit():
                    id = int(filename_parts[1])
                    ids.append(id)
                else:
                    raise ValueError("Filename format is invalid.")
            except ValueError as e:
                print(f"Error: {e}")

            faces.append(imageNp)
            
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids= np.array(ids)

        if len(ids) == len(faces) and len(ids) > 0:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
        else:
            print("Mismatch in faces and ids. Ensure they have the same length.")


        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()