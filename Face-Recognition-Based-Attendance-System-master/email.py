# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:41:19 2019

@author: jaimuruganantham
"""
import smtplib
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("attendancedetails19@gmail.com", "Attendance@19")
#Send the mail
msg = "Hi! jai message from python script"
#Hello!" # The /n separates the message from the headers
server.sendmail("Attendance Details", "jaimuruganantham@gmail.com", msg)
