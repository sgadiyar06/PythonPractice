# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:10:31 2020

@author: Sudarshan
"""


import turtle
import random
turtle.bgcolor('black')
s=turtle.Turtle()

width=5
height=7

dot_dist=25
s.penup()
list_color=['white','yellow','brown','red','blue','green','orange','pink','violet','cyan','grey']
s.setpos(-250,250)


def spiral(m,n):
    k=0
    l=0
    f=0
    #k and l are index of starting row and col
    #s.color('white')
    col=random.randint(0,10)
    s.color(list_color[col])
    
    while(k<m and l<n):
        
        if(f==1):
            s.right(90)
        
        # printing the first row
        for i in range(l,n):
            #print(a[k][i],end=' ')
            s.dot()
        
            s.forward(dot_dist)
            
        k+=1
        f=1
        col=random.randint(0,10)
        s.color(list_color[col])
        
        s.right(90)
        
        #printing the last col
        for i in range(k,m):
            s.dot()
            s.forward(dot_dist)
            #print(a[i][n-1],end=' ')
            
        n-=1
        col=random.randint(0,10)
        s.color(list_color[col])
        
        s.right(90)
        
        
        if(k<m):
            #printing last row
            for i in range(n-1,l-1,-1):
                s.dot()
                s.forward(dot_dist)
                #print(a[m-1][i],end=' ')
        
            m-=1
        col=random.randint(0,10)
        s.color(list_color[col])
        s.right(90)
        if(l<n):
            #printing 1st col
            for i in range(m-1,k-1,-1):
                s.dot()
                s.forward(dot_dist)
                #print(a[i][l],end=' ')
            l+=1
        

    
spiral(20,20)
turtle.done()