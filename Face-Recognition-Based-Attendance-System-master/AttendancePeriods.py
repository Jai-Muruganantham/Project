# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:20:28 2019

@author: jaimuruganantham
"""

import sqlite3
conn=sqlite3.connect("StudentDataBase.db") 
c=conn.cursor()
#c.execute("""create table AttendancePeriod(Period integer)""")
#cmd="DELETE FROM Student1 WHERE RegistrationNo="+str(24) 
#c.execute(""" insert into AttendancePeriod values(0)
#          """)
c.execute("""create table StudentPeriod(Id integer,Period integer)""")
conn.close()