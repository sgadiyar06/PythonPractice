# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:36:51 2020

@author: Sudarshan
"""
import random

doors=[0]*3
goatdoor=[]
swap=0
dontswap=0

x=random.randint(0,2)
#the x door will contain the car
doors[x]="car"
for i in range(0,3):
    if(i==x):
        continue
    else:
        doors[i]='goat'
        goatdoor.append(i)
    choice=int(input('Enter your choice of door number: '))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open=random.choice(goatdoor)
ch=input('Do you want to swap (y/n)? ')
if(ch=='y'):
   if(doors[choice]=='goat'):
       print('You win')
       swap=swap+1
   else:
       print('Player lost')
else:
    if(doors[choice]=='goat'):
        print('You lost ')
    else:
        print('You won')
        dontswap=dontswap+1


print('Swap= ',swap)
print('Dontswap= ',dontswap)
    