# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:28:19 2019

@author: jaimuruganantham
"""
import csv
import pandas as pd 
df=pd.read_csv("StudentDetails\StudentDetails.csv")
email=df.loc[df['Id'] == 24]['Email'].values
print(email)