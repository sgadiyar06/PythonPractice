# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:43:42 2020

@author: Sudarshan
"""

import random
#linear search
# def linear_search(n,num):
    
#     a=[]
#     for i in range(n):
#         #a[i]=int(input('Enter the number: '))
#         a.append(i)
#         #a.append(random.randint(0,60))
#     print('The array is: ')
#     for i in range(n):
#         print(a[i],end='\n')
    
#     #num=int(input(('Enter the number you want to search: ')))
#     found=0
#     count=0
#     for i in range(n):
#         count+=1
#         if(num==a[i]):
#             print('The value ',num,' is in position number= ',i)
#             found=1
#             break
#     if(found!=1):
#         print('not found')
#     print('No of iterations= ',count)
#binary search
def binary_search():
    fp=0
    
    found=0
    n=int(input('Enter the size of the array: '))
    a=[]
    lp=n
    for i in range(n):
        #a[i]=int(input('Enter the number: '))
        a.append(i)
    num=int(input('Enter the number you wanna find: '))
    count=0
    while(fp<=lp and found==0):
        mid=(fp+lp)//2
        count+=1
        if(num==a[mid]):
            print('Element found at position: ',mid)
            print('Iterations: ',count)
            found=1
            break
        else:
            if(num<a[mid]):
                lp=mid-1
            else:
                fp=mid+1
    if(found==0):
        print('Number not found')
binary_search()