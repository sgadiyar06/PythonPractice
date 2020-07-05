# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:44:42 2020

@author: Sudarshan
"""

with open('file1.txt','r+') as myfile:
    print(myfile.read())
    myfile.write(' I am Sudarshan')
myfile.close()

