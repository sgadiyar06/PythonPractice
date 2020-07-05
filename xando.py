# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:01:35 2020

@author: Sudarshan
"""

#tictactoe
import numpy as np
board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
pl1='X'
pl2='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
             print(symbol,' WON')
             return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
             print(symbol,' WON')
             return True
    return False

def check_dia(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,' won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,' won')
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_dia(symbol)
    
def place(symbol):
    print(np.matrix(board))
    while True:
        row=int(input('Enter row no: '))
        col=int(input('Enter col no: '))
        if row>0 and col>0 and row<4 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Enter a valid input! ')
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(pl1)
            if won(pl1):
                break
        else:
            print('O turn')
            place(pl2)
            if won(pl2):
                break
    if not(won(pl1)) and not(won(pl2)):
            print('DRAW ')

play()