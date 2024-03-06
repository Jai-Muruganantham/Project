# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:03:10 2019

@author: jaimuruganantham
"""

import sqlite3
conn = sqlite3.connect("StudentDataBase.db")
print ("Opened database successfully");
cursor = conn.execute("SELECT Period from AttendancePeriod")
for row in cursor:
   print ("Id = ", row[0])
print ("Operation done successfully")
conn.close()