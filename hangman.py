# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:17:04 2020

@author: Sudarshan
"""
import random

movies=['iron man','hulk','captain america','thor','doctor strange','ant man','black panther','guardians of the galaxy','ultron','endgame','infinity wars','civil war']

def create_q(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    i=0
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def thank(p,q,r,s):
    print('Your scores are: ')
    print(p,' your score is ',q)
    print(r,' your score is ',s)
    print('Thank you for playing this game, hope you had fun! ')

def play():
    print("Welcome to the jumbled words game \n")
    p1name=input("Player 1 enter your name: ")
    p2name=input("Player2 enter your name: ")
    #scores
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            #player1
            print(p1name,' Your turn. ')
            picked_movie=random.choice(movies)
            qn=create_q(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input('Guess a character: ')              
                if(is_present(letter.lower(),picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('To guess the movie press 1 or 2 to unlock more characters: '))
                    if d==1:
                        ans=input('Enter the movie name: ')
                        if(ans.lower()==picked_movie):
                            print('This is correct!!')
                            pp1=pp1+1
                            not_said=False
                        else:
                            print('Wrong answer ')
                            break
                else:
                    print('This letter '+letter+' is not found')
                
            c=int(input('If you wanna continue this game enter 1 or to quit 0: '))
            if(c==0):
                thank(p1name,pp1,p2name,pp2)
                willing=False
        else:
            #player2
            print(p2name,' Your turn. ')
            picked_movie=random.choice(movies)
            qn=create_q(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input('Guess a character: ')
                
                if(is_present(letter.lower(),picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('To guess the movie press 1 or 2 to unlock more characters: '))
                    if d==1:
                        ans=input('Enter the movie name: ')
                        if(ans.lower()==picked_movie):
                            print('This is correct!!')
                            pp2=pp2+1
                            not_said=False
                        else:
                            print('Wrong answer ')
                            break
                else:
                    print('This letter '+letter+' is not found')
               
            c=int(input('If you wanna continue this game enter 1 or to quit 0: '))
            if(c==0):
                thank(p1name,pp1,p2name,pp2)
                willing=False
        turn=turn+1

play()