# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:49:51 2019

@author: jaimuruganantham
"""

#Import statements
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
    
    lbl3 = tk.Label(windowTake, text="Attendance : ",width=20  ,fg="red"  ,bg="sky blue"  ,height=2 ,font=('times', 15, ' bold  underline')) 
    lbl3.place(x=400, y=650)
    
    
    message2 = tk.Label(windowTake, text="" ,fg="red"   ,bg="snow2",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
    message2.place(x=700, y=650)
    
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
        else:
            if(is_number(Id)):
                res = "Enter Alphabetical Name"
                message.configure(text= res)
                messagebox.showerror("Enter the Alphabetical Name")
            elif(name.isalpha()):
                res = "Enter Numeric Id"
                message.configure(text= res)
                messagebox.showerror("Invalid data","Enter the Numeri Id")
            else:
                res="Enter the valid data"
                message.configure(text=res)
                messagebox.showerror("Ivalid Data","Enter the valid data")
        messagebox.showinfo("Image","Successfully Registered ..!")
    def DeletStudetnDetails():
        conn=sqlite3.connect("StudentDataBase.db")
        cur=conn.cursor() 
        registrationNo=int(txt.get()) 
        def deleteStudentDetails(registrationNo): 
            cmd="SELECT * FROM Student1 WHERE RegistrationNo="+str(registrationNo) 
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
                return isRecordExit 
        record=deleteStudentDetails(registrationNo) 
        if record==1: 
            cmd="DELETE FROM Student1 WHERE RegistrationNo="+str(registrationNo) 
            conn.execute(cmd)
            messagebox.showinfo("DeletedConfirmation","Deleted sucessfully")
            conn.commit()
  
        else: 
            messagebox.showinfo("Deleted","Oops!There is no such registration n1umber")

    def TrainImages():
        recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = getImagesAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("Trainner.yml")
        res = "Image Trained"#+",".join(str(f) for f in Id)
        message.configure(text= res)
        messagebox.showinfo("Trainner","Hi Your data is trainned")
    
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
    
    def TrackImages():
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Date','Time']
        attendance = pd.DataFrame(columns = col_names)    
        while True:
            ret, im =cam.read()
            im=cv2.flip(im,1)
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    ts = time.time()         
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+aa
                    attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    
                else:
                    Id='Unknown'                
                    tt=str(Id)  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im)
            if (cv2.waitKey(1)==ord('q')):
                break
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        attendance.to_csv(fileName,index=False)
        cam.release()
        cv2.destroyAllWindows()
        #print(attendance)
        res=attendance
        message2.configure(text= res)
        messagebox.showinfo("Images","Successfully Attendance taken...Enjoy.")
    
    clearButton = tk.Button(windowTake, text="Clear", command=clear  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton.place(x=950, y=200)
    clearButton2 = tk.Button(windowTake, text="Clear", command=clear2  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton2.place(x=950, y=300)    
    takeImg = tk.Button(windowTake, text="Take Images", command=TakeImages ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    takeImg.place(x=200, y=500)
    trainImg = tk.Button(windowTake, text="Train Images", command=TrainImages  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    trainImg.place(x=500, y=500)
    trackImg = tk.Button(windowTake, text="Track Images", command=TrackImages  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    trackImg.place(x=800, y=500)
    quitWindow = tk.Button(windowTake, text="Quit", command=windowTake.destroy  ,fg="red"  ,bg="cadet blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=1100, y=500)
    copyWrite = tk.Text(windowTake, background=windowTake.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
    copyWrite.tag_configure("superscript", offset=10)
    copyWrite.configure(state="disabled",fg="red"  )
    copyWrite.pack(side="left")
    copyWrite.place(x=800, y=750)
    windowTake.mainloop()

CreatTk()