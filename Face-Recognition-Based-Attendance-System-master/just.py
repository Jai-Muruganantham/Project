# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:28:40 2019

@author: jaimuruganantham
"""
import cv2 
import sqlite3 
import os
detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') 
while(True):
    print("********************Student Information System********************")
    print("Enter your option")
    index=int(input("Press 1. Insert New Student Details\nPress 2. Update Student Details\nPress 3. Delete Student Details\nPress 4. Exit\n"))
    if index==1:         
        
        conn=sqlite3.connect("StudentDataBase.db") 
        cur=conn.cursor() 
        registrationNo=int(input("Enter the Registration No:")) 
        while(len(str(abs(registrationNo)))<12): 
            print ("Please enter valid register no(12 digits)") 
            registrationNo=int(input("Enter the registration no:")) 
        #seqNo=int(input("Enter the Sequential no:")) 
        def insertStudentDetails(registrationNo): 
            cmd="SELECT * FROM Student WHERE registrationNo="+str(registrationNo) 
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
            return isRecordExit 
        record=insertStudentDetails(registrationNo) 
        if record==1:
            print("Registration Number Already exist")
        if record!=1: 
            name=input("Enter the Name of the student:") 
            gender=input("Enter the gender(M/F):") 
            while gender != 'M' and gender != 'F': 
                print ("Please enter valid gender")
                gender=input("Enter the gender(M/F):") 
            age=int(input("Enter the age:")) 
            cur.execute('''insert into Student(registrationNo,name,gender,age) values(?,?,?,?)''',(registrationNo,name,gender,age)) 
            print("Student Information Updated Succefully")
            conn.commit() 
            conn.close()
            mypath="dataset/"+str(registrationNo)+""
            print(mypath)
            if not os.path.isdir(mypath):
                os.makedirs(mypath)
            sampleNum=0
            take=input("Are you ready to take sample?(Y/N)")
            while take=="N" or take=="n":
                 take=input("Are you ready to take sample?(Y/N)")
            cam = cv2.VideoCapture(0) 
            if take=="y" or take=="Y":
                while(sampleNum<20):
                    ret, img = cam.read()
                    img=cv2.flip(img,1) 
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.2, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                        sampleNum=sampleNum+1
                        cv2.imwrite(mypath+"/User."+str(registrationNo)+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        cv2.imshow('frame',img)
                        print("User Sample ",sampleNum,"taken")
                        if cv2.waitKey(20) & 0xFF == ord('q'):
                            break
                cam.release() 
                cv2.destroyAllWindows()  
            else:
                print("Please ready for take.......")
    if index==2:
        conn=sqlite3.connect("StudentDataBase.db")
        cur=conn.cursor()                                                           
        registrationNo=int(input("Enter the registration no:")) 
        while(len(str(abs(registrationNo)))<12): 
                print ("Please enter valid register no(12 digits)")
                registrationNo=int(input("Enter the registration no:")) 
        def updateStudentDetails(registrationNo): 
            cmd="SELECT * FROM Student WHERE registrationNo="+str(registrationNo) 
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
            return isRecordExit 
        record=updateStudentDetails(registrationNo) 
        if record==1: 
            while(True):
                field=int(input("Please Press the number to change\n1.Student Name\n2.Age\n3.Gender\n4.Exit\n")) 
                if field==1: 
                    name1=input("Enter the Name of the student:") 
                    cmd="update Student set name =? Where registrationNo=?" 
                    cursur=conn.execute(cmd,(str(name1),int(registrationNo))) 
                    conn.commit() 
                    print ("Updated successfully")
                elif field==2: 
                    age=int(input("Enter the age:")) 
                    cmd="update Student set age =? Where registrationNo=?" 
                    cursur=conn.execute(cmd,(int(age),int(registrationNo))) 
                    conn.commit() 
                    print ("Updated successfully") 
                elif field==3: 
                    gender1=input("Enter the gender(M/F):") 
                    cmd="update Student set gender =? Where registrationNo=?" 
                    cursur=conn.execute(cmd,(str(gender1),int(registrationNo))) 
                    conn.commit() 
                    print ("Updated successfully") 
                elif field==4:
                    break;
                else:
                    print("Enter the valid option")
        else: 
            print ("Oops!There is no such registration number")
    if index==3:
        conn=sqlite3.connect("StudentDataBase.db")
        cur=conn.cursor() 
        registrationNo=int(input("Enter the registration no:")) 
        while(len(str(abs(registrationNo)))<12): 
            print ("Please enter valid register no(12 digits)")
            registrationNo=int(input("Enter the registration no:")) 
        def deleteStudentDetails(registrationNo): 
            cmd="SELECT * FROM Student WHERE registrationNo="+str(registrationNo) 
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
                return isRecordExit 
        record=deleteStudentDetails(registrationNo) 
        if record==1: 
            cmd="DELETE FROM Student WHERE registrationNo="+str(registrationNo) 
            conn.execute(cmd) 
            conn.commit() 
            print ("Deleted sucessfully")
        else: 
            print ("Oops!There is no such registration n1umber")
    if index==4:
        break
    if index>4:
        print("Enter The Valid Option")
        