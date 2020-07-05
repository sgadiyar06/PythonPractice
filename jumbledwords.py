# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:06:30 2020

@author: Sudarshan
"""
import random
#jumbled words game
def choose():
    words=['competition','rainbow','anaconda','programming','mathematics','player','computer','mobile','coffee','milkshake','calculator']
    a=random.choice(words)
    return a

def jumble(b):
    nw="".join(random.sample(b,len(b)))
    return nw

def thank(p,q,r,s):
    print("Thank you for playing "+str(p)+" , your score was "+str(q))
    print("Thank you for playing "+str(r)+" , your score was "+str(s))

def play():
    print("Welcome to the jumbled words game \n")
    p1name=input("Player 1 enter your name")
    p2name=input("Player2 enter your name")
    #scores
    pp1=0
    pp2=0
    turn=0
    while(1):
        #choosing a word
        picked_word=choose()
        #jumbling the word
        jw=jumble(picked_word)
        
        #player 1
        if turn%2==0:
            print(p1name,'Your turn. ')
            print('The word is: '+jw)
            ans=input('Guess the word: ')
            
            if ans==picked_word:
                print('The answer is correct!!!')
                pp1=pp1+1
                print('Your score is: ',pp1)
            else: 
                print('Sorry, wrong answer! :(')
         
        #player 2
        else:
            print(p2name,"It's your turn now.")
            print('The word is: '+jw)
            ans=input('Guess the word: ')
            if ans==picked_word:
                print('The answer is correct!!!')
                pp2=pp2+1
                print('Your score is: ',pp2)
            else: 
                print('Sorry, wrong answer! :(')
        c=int(input('Enter 1 if you want to continue or 0 if you want to quit'))
        if c==0:
            print('Your scores are: ')
            thank(p1name,pp1,p2name,pp2)
            break
        turn=turn+1
        
play()        