# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:44:46 2019

@author: jaimuruganantham
"""

import csv

with open('StudentDetails\StudentDetails.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            s=f'{row[2]}.'
            print(s)
            line_count += 1
    print(f'Processed {line_count} lines.')