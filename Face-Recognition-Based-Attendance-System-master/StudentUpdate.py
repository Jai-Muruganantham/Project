# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 02:51:15 2019

@author: jaimuruganantham
"""
import tkinter as tk

windowUpdate=tk.Tk()
windowUpdate.title("Admin User")
windowUpdate.configure(background='light blue')
message = tk.Label(windowUpdate, text="AUTOMATED ATTENDANCE BY IMAGE PROCESSING USING IOT" ,bg="light cyan"  ,fg="blue"  ,width=60  ,height=2,font=('times', 30, 'italic bold underline')) 
message.place(x=70, y=20)
message = tk.Label(windowUpdate, text="Student Updater" ,bg="light cyan"  ,fg="blue"  ,width=50  ,height=1,font=('times', 30, 'italic bold underline')) 
message.place(x=170, y=150)

FaceDetectionWindow = tk.Button(windowUpdate, text="Register Details", command=None ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
FaceDetectionWindow.place(x=650, y=400)
MianAttendanceWindow = tk.Button(windowUpdate, text="Delete Details", command=None ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
MianAttendanceWindow.place(x=650, y=450)
quiteWindow = tk.Button(windowUpdate, text="Back", command=AdminUser  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quiteWindow.place(x=650, y=500)

windowUpdate.mainloop()