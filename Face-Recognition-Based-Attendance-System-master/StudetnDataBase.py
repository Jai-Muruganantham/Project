"""
Created on Tue Jan 29 23:22:53 2019

@author: jaimuruganantham
"""
import sqlite3
conn=sqlite3.connect("StudentDataBase.db") 
c=conn.cursor()
#c.execute("""create table Student1(RegistrationNo integer)""")
cmd="DELETE FROM Student1 WHERE RegistrationNo="+str(24) 
c.execute()
conn.close()