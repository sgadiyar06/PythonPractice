# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:24:24 2020

@author: Sudarshan
"""

#biggest of three numbers
#print("Program to find out largest of 3 numbers")
#a,b,c=input("Enter your numbers").split()
#a=int(a)
#b=int(b)
#c=int(c)
#
#if a>b and a>c:
#    print("The first number ",a," is the largest")
#elif a<b and b>c:
#    print("The second number ",b," is the largest")
#elif c>a and c>b:
#    print("The third number: ",c," is the largest")
    
#printing patterns
n=int(input("Enter a number"))
i=j=0
a='*'
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end='')


