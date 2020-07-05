# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:02:00 2020

@author: Sudarshan
"""

a=[]

print("")
n=int(input('How many students?'))

for i in range(0,n):   
    a.append(input("Enter student name: "))
    
print("The student list is:")
for item in a:
    print(item)

