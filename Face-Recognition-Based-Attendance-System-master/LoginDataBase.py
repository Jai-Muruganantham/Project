# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:57:30 2019

@author: jaimuruganantham
"""

#Logint database
import sqlite3

conn=sqlite3.connect("StudentDataBase.db")
conn.execute("""Create table Login(UserId integer,Password text)""")
conn.execute("""insert into Login values(24,'jai')""")
conn.commit()
conn.close()