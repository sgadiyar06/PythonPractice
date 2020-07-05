# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:18:26 2020

@author: Sudarshan
"""

import random
#recursive function to find factorial
def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)

print('Program to find the factorial: ')
num=int(input('Enter the number: '))
if num==0:
    print('The factorial of 0 is 1')
elif num<0:
    print('The factorial does not exist for negative numbers')
else:
    print('The factorial of ',num,' is ',factorial(num))
    

        


