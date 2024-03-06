# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:34:49 2019

@author: jaimuruganantham
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
windowAdmin=tk.Tk()
windowAdmin.title(">>>>>Login<<<<<<")
windowAdmin.configure(background='light blue')
#Title of the window
message = tk.Label(windowAdmin, text="AUTOMATED ATTENDANCE BY IMAGE PROCESSING USING IOT" ,bg="light cyan"  ,fg="blue"  ,width=60  ,height=2,font=('times', 30, 'italic bold underline')) 
message.place(x=70, y=20)

message = tk.Label(windowAdmin, text="Admin Login" ,bg="light cyan"  ,fg="blue"  ,width=50  ,height=1,font=('times', 30, 'italic bold underline')) 
message.place(x=170, y=150)
   
lbl = tk.Label(windowAdmin, text="User ID:",width=20  ,height=2  ,fg="red"  ,bg="sky blue" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=300)
    
txt = tk.Entry(windowAdmin,width=20  ,bg="snow2" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=700, y=315)
    
lbl2 = tk.Label(windowAdmin, text="Password",width=20  ,fg="red"  ,bg="sky blue"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=400)

txt2 = tk.Entry(windowAdmin,show="*",width=20  ,bg="snow2"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=415)

def login():
    if txt.get()=="" and txt2.get()=="":
        messagebox.showerror("Login","Enter the valid datas")
        txt.delete(0,'end')
        txt2.delete(0,'end')
    elif txt.get()=="":
        messagebox.showerror("Login","Enter the valid User Id")
        txt2.delete(0,'end')
    elif txt2.get()=="":
        messagebox.showerror("Login","Enter the valid Password")
        txt.delete(0,'end')
    else:
        UserId=int(txt.get())
        Password=txt2.get()
        conn=sqlite3.connect("StudentDataBase.db") 
        cursor=conn.execute("select UserId,Password from Login")
        def check(UserId): 
            cmd="SELECT * FROM Login WHERE UserId="+str(UserId)
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
            return isRecordExit 
        record=check(UserId) 
        if record!=1:
            messagebox.showerror("Login","UnAuthorized User")
        else:
            for row in cursor:
                if UserId==row[0] and Password==row[1]:
                    messagebox.showinfo("Login","Your are Loged in")         
        conn.commit()
        conn.close()
def signin():
    window1=tk.Tk()
    window1.title(">>>>>Login<<<<<<")
    window1.configure(background='light blue')
    #Title of the window
    message = tk.Label(window1, text="AUTOMATED ATTENDANCE BY IMAGE PROCESSING USING IOT" ,bg="light cyan"  ,fg="blue"  ,width=60  ,height=2,font=('times', 30, 'italic bold underline')) 
    message.place(x=70, y=20)
    
    message = tk.Label(window1, text="Signin" ,bg="light cyan"  ,fg="blue"  ,width=50  ,height=1,font=('times', 30, 'italic bold underline')) 
    message.place(x=170, y=150)
       
    lbl = tk.Label(window1, text="User ID:",width=20  ,height=2  ,fg="red"  ,bg="sky blue" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=400, y=300)
        
    txt = tk.Entry(window1,width=20  ,bg="snow2" ,fg="red",font=('times', 15, ' bold '))
    txt.place(x=700, y=315)
        
    lbl2 = tk.Label(window1, text="Password",width=20  ,fg="red"  ,bg="sky blue"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=400, y=400)
    
    txt2 = tk.Entry(window1,show="*",width=20  ,bg="snow2"  ,fg="red",font=('times', 15, ' bold ')  )
    txt2.place(x=700, y=415)
    
    def sign():
        UserId=int(txt.get())
        Password=txt2.get()
        conn=sqlite3.connect("StudentDataBase.db") 
        cursor=conn.execute("select UserId,Password from Login")
        def check(UserId): 
            cmd="SELECT * FROM Login WHERE UserId="+str(UserId)
            cursur=conn.execute(cmd) 
            isRecordExit=0 
            for row in cursur: 
                isRecordExit=1 
            return isRecordExit 
        record=check(UserId) 
        if record==1:
            messagebox.showerror("Signin","User Already signed in")
            window1.destroy()
            signin()
        elif record!=1:
            conn.execute("""insert into Login values(?,?)""",(UserId,Password,))
            messagebox.showinfo("Signin","You are signed in!! Enjoy...")
        conn.commit()
        conn.close()
        window1.destroy()
    LoginButton=tk.Button(window1,text="Signin",command=sign,width=10,height=1,fg="red",bg="sky blue",font=('times',15,'bold'))
    LoginButton.place(x=900,y=515)
    
    window1.mainloop()


LoginButton=tk.Button(windowAdmin,text="Login",command=login,width=10,height=1,fg="red",bg="sky blue",font=('times',15,'bold'))
LoginButton.place(x=700,y=515)
LoginButton=tk.Button(windowAdmin,text="Signin",command=signin,width=10,height=1,fg="red",bg="sky blue",font=('times',15,'bold'))
LoginButton.place(x=900,y=515)

windowAdmin.mainloop()