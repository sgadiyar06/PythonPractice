# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:16:46 2020

@author: Sudarshan
"""

#fizzbuzz
def fizzbuzz(r):
    for i in range(1,r):
        if (i%3==0 and i%5==0):
            print(str(i)+'= fizzbuzz')
        elif (i%3==0):
            print(str(i)+'= fizz')
        elif (i%5==0):
            print(str(i)+'= buzz')
        else:
            print(i)