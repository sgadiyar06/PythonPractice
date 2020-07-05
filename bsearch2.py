# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:50:44 2020

@author: Sudarshan
"""

import random
#binary search using recursive function
def binary_search(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=(start+end)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binary_search(l,x,start,mid-1)
        elif l[mid]<x:
            return binary_search(l,x,mid+1,end)


found=0
b=True
print('Program to perform binary search')
n=int(input('Enter size of the array: '))
print('Do you want to create an array or use a random one')
a=int(input('Enter 1 to create a random array or 2 to make your own array: '))
if a==1:
    l=[]
    for i in range(n):
        l.append(random.randint(1,100))
        l.sort()
elif a==2:
    l=[0]*n
    for i in range(n):
        l[i]=int(input('Enter the element: '))
    l.sort()
else:
    print('Run the program again and enter a valid input this time -_-')
    b=False

if b:
    print('The array chosen to perform binary search is: ')
    for i in range(n):
        print(l[i])
    num=int(input('Enter the number you want to search in the array: '))
    found=binary_search(l,num,0,n)
    if found<0:
        print('Element not found ')
    else:
        print('Element found at position number ',found+1)