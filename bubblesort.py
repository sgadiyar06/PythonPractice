# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:37:47 2020

@author: Sudarshan
"""


def bubble_sort(a):
    n=len(a)
    
    for i in range(n):
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                
a=[1,6,9,3,2,5]
bubble_sort(a)