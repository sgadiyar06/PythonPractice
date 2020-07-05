# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:18:45 2020

@author: Sudarshan
"""


def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print('Fibonacci series: ')
n=int(input('Number of elements needed in the series: '))
if n<0:
    print('Invalid')
else:
    for i in range(n):
        print(fibonacci(i))