# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:24:29 2020

@author: Sudarshan
"""


class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)


class Student(Person):
    def __init__(self,fname,lname):
        self.fname=lname
        self.lname=fname

x=Student('Sudarshan',"Gadiyar")
x.printname()