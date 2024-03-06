# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:55:28 2019

@author: jaimuruganantham
"""
import tkinter as tk
import sqlite3
from tkinter import messagebox

def DeleteUser():
    windowDelete=tk.Tk()
    windowDelete.title("Delete User")
    windowDelete.configure(background='light blue')
    message = tk.Label(windowDelete, text="AUTOMATED ATTENDANCE BY IMAGE PROCESSING USING IOT" ,bg="light cyan"  ,fg="blue"  ,width=60  ,height=2,font=('times', 30, 'italic bold underline')) 
    message.place(x=70, y=20)
    message = tk.Label(windowDelete, text="Admin" ,bg="light cyan"  ,fg="blue"  ,width=50  ,height=1,font=('times', 30, 'italic bold underline')) 
    message.place(x=170, y=150)
    lbl = tk.Label(windowDelete, text="Enter ID:",width=20  ,height=2  ,fg="red"  ,bg="sky blue" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=400, y=400)
    txt = tk.Entry(windowDelete,width=20  ,bg="snow2" ,fg="red",font=('times', 15, ' bold '))
    txt.place(x=700, y=415)
    def DeleteUser2():
        conn=sqlite3.connect("StudentDataBase.db")
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
        conn.close()
    LoginButton=tk.Button(windowDelete,text="Deltet User",command=DeleteUser2,width=10,height=1,fg="red",bg="sky blue",font=('times',15,'bold'))
    LoginButton.place(x=700,y=515)
    LoginButton=tk.Button(windowDelete,text="Back",command=None,width=10,height=1,fg="red",bg="sky blue",font=('times',15,'bold'))
    LoginButton.place(x=900,y=515) 
    windowDelete.mainloop()

DeleteUser()