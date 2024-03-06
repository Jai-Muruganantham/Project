# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:51:44 2019

@author: jaimuruganantham
"""
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
#import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import messagebox
import sqlite3

def CreatTk():
    #Creating Window for GUI
    windowTake = tk.Tk()
    #Creating Title for Window
    windowTake.title("Face_Recogniser")
    #Setting Backgroud Color
    windowTake.configure(background='light blue')
    #Configuring windows
    windowTake.grid_rowconfigure(0, weight=1)
    windowTake.grid_columnconfigure(0, weight=1)
    
    message = tk.Label(windowTake, text="AUTOMATED ATTENDANCE BY IMAGE PROCESSING USING IOT" ,bg="light cyan"  ,fg="blue"  ,width=60  ,height=3,font=('times', 30, 'italic bold underline')) 
    
    message.place(x=70, y=20)
    
    lbl = tk.Label(windowTake, text="Enter ID:",width=20  ,height=2  ,fg="red"  ,bg="sky blue" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=400, y=200)
    
    txt = tk.Entry(windowTake,width=20  ,bg="snow2" ,fg="red",font=('times', 15, ' bold '))
    txt.place(x=700, y=215)
    
    lbl2 = tk.Label(windowTake, text="Enter Name",width=20  ,fg="red"  ,bg="sky blue"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=400, y=300)
    
    txt2 = tk.Entry(windowTake,width=20  ,bg="snow2"  ,fg="red",font=('times', 15, ' bold ')  )
    txt2.place(x=700, y=315)
    
    lbl3 = tk.Label(windowTake, text="Notification : ",width=20  ,fg="red"  ,bg="sky blue"  ,height=2 ,font=('times', 15, ' bold underline ')) 
    lbl3.place(x=400, y=400)
    
    message = tk.Label(windowTake, text="" ,bg="snow2"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=700, y=400)
        
    def clear():
        txt.delete(0, 'end')    
        res = ""
        message.configure(text= res)
    
    def clear2():
        txt2.delete(0, 'end')    
        res = ""
        message.configure(text= res)    
        
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
     
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
     
        return False
    
    def TakeImages():
        try:
            Ids=int(txt.get())
        except:
            messagebox.showerror("Error","Enter the value Id")
            windowTake.destroy()
            CreatTk()
        if txt.get()=="" and txt2.get()=="":
            messagebox.showerror("Error","Invalid data")
            windowTake.destroy()
            CreatTk()
        else:
            conn=sqlite3.connect("StudentDataBase.db") 
            cur=conn.cursor() 
            registrationNo=int(txt.get())
            def insertStudentDetails(registrationNo): 
                cmd="SELECT * FROM Student1 WHERE RegistrationNo="+str(registrationNo) 
                cursur=conn.execute(cmd) 
                isRecordExit=0 
                for row in cursur: 
                    isRecordExit=1 
                return isRecordExit 
            record=insertStudentDetails(registrationNo) 
            if record==1:
                messagebox.showerror("Ivalid Data","Registration Number Already exist")
                windowTake.destroy()
                CreatTk()
            Id=(txt.get())
            name=(txt2.get())
            if(is_number(Id) and name.isalpha()):
                cam = cv2.VideoCapture(0)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    ret, img = cam.read()
                    img=cv2.flip(img,1)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                        #incrementing sample number 
                        sampleNum=sampleNum+1
                        #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        #display the frame
                        cv2.imshow('frame',img)
                    #wait for 100 miliseconds 
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 100
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID : " + Id +" Name : "+ name
                row = [Id , name]
                with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                message.configure(text= res)
                cur.execute('''insert into Student1(RegistrationNo) values(?)''',(registrationNo,)) 
                conn.commit()
                conn.close()
                messagebox.showinfo("Image","Successfully Registered ..!")
            else:
                if(is_number(Id)):
                    res = "Enter Alphabetical Name"
                    message.configure(text= res)
                    messagebox.showerror("Error","Enter the Alphabetical Name")
                elif(name.isalpha()):
                    res = "Enter Numeric Id"
                    message.configure(text= res)
                    messagebox.showerror("Invalid data","Enter the Numeri Id")
                else:
                    res="Enter the valid data"
                    message.configure(text=res)
                    messagebox.showerror("Ivalid Data","Enter the valid data")
    
    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths)
        
        #create empth face list
        faces=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)        
        return faces,Ids
    
    clearButton = tk.Button(windowTake, text="Clear", command=clear  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton.place(x=950, y=200)
    clearButton2 = tk.Button(windowTake, text="Clear", command=clear2  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton2.place(x=950, y=300)    
    takeImg = tk.Button(windowTake, text="Register", command=TakeImages ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    takeImg.place(x=950, y=500)
    copyWrite = tk.Text(windowTake, background=windowTake.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
    copyWrite.tag_configure("superscript", offset=10)
    copyWrite.configure(state="disabled",fg="red"  )
    copyWrite.pack(side="left")
    copyWrite.place(x=800, y=750)
    windowTake.mainloop()

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
CreatTk()