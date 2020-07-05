# -*- coding: ut-8 -*-
"""
Created on Fri Apr 17 18:56:48 2020

@author: Sudarshan
"""

import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*8
card2=[0]*8
def cards():
    pos1=random.randint(0,7)
    pos2=random.randint(0,7)
    #pos1 and pos2 are the same symbol positions in card 1 and 2 resp
    samesymbol=random.choice(symbols)
    if(pos1==pos2):
        card2[pos1]=samesymbol
        card1[pos1]=samesymbol
    else:
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
        card1[pos2]=random.choice(symbols)
        symbols.remove(card1[pos2])
        card2[pos1]=random.choice(symbols)
        symbols.remove(card2[pos1])
    i=0
    while(i<8):
        if(i!=pos1 and i!=pos2):
            alpha1=random.choice(symbols)
            symbols.remove(alpha1)
            alpha2=random.choice(symbols)
            symbols.remove(alpha2)
            card1[i]=alpha1
            card2[i]=alpha2
        i=i+1
    return samesymbol
print('Welcome to the game, here are two cards with several alphabets')
p=0
s1=cards()
while(1):
    print('The first card is: ',card1)
    print('The second card is: ',card2)
    ch=input('Enter the common symbol: ')
    if(ch==s1):
        print('The answer is correct')
        p=p+1
    else:
        print("Sorry that's wrong!")
    n=int(input('Do you wanna play again press 1 else to quit press 0: '))
    if(n==0):
        break
    else:
        s1=cards()
print('Thank you for playing, your total score is: ',str(p))
