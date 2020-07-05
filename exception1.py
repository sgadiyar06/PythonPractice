# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:56:42 2020

@author: Sudarshan
"""


#exception handling


try:
    a=int(input('Enter a number for division: '))
    b=int(input('Enter another number for division: '))
    c=a/b
    print("a/b = ",c)
except ZeroDivisionError:
    print("Cannot be zero, invalid")
except:
    print('Some other error')

# l=[dir()]
# for i in len(l):
#     print(l[i])