# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:21:36 2020

@author: Sudarshan
"""

#magic square

def magic_square(n):
    
    magicSquare=[]
    magicSquare = [[0 for i in range(n)]
                    for j in range(n)]
    
    i=n//2
    j=n-1
    count=1
    
    num=n*n
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count=count+1
        i=i-1
        j=j+1
        
    for i in range(n):
        print()
        for j in range(n):
            print(magicSquare[i][j],end=' ')

n=int(input('Enter the dimension of the magic square: '))
if(n%2!=0): 
 print('The magic square is: ')
 magic_square(n)
 sum=n*(n**2+1)/2
 print()
 print('Sum of each row/col/diagonal = '+str(int(sum)))
else: print('even number is not possible')