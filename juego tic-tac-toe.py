# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:41:19 2021

@author: hoyos
"""

from random import randrange
board={1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def DisplayBoard(board):
    print(' ',board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('-----+-----+-----')
    print(' ',board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-----+-----+-----')
    print(' ',board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    return board
DisplayBoard(board)
print("!comencemos¡")
board[5]='X'
print()
DisplayBoard(board)

def EnterMove(board):
    o=int(input("ingresa movimiento: "))
    if board[o]=='O':
        print("casilla ocupada")
        return EnterMove(board)
    elif board[o]=='X':
        print("casilla ocupada")
        return EnterMove(board)
    else:
        board[o]='O'
    if estado(board)==False:
        print("!felicidades ha ganado¡")
        return DisplayBoard(board)
    else:
        return DisplayBoard(board), print(), enter(board)

def enter(board):
    x=(randrange(1,10))
    if board[x]=='O':
        return enter(board)
    elif board[x]=='X':
        return enter(board)   
    else:
        board[x]='X'
    if estado(board)==False:
        print("!Suerte para la proxima¡")
        return  DisplayBoard(board)
    return DisplayBoard(board),EnterMove(board)


def estado(board):
    h={1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[1,4,7],5:[2,5,8],6:[3,6,9],7:[1,5,9],8:[3,5,7]}
    for i in h:
        k=[]
        for j in h[i]:
            k.append(board[j])
        if k==['O','O','O']:
            return False
        elif k==['X','X','X']:
            return False
        else:
            continue      


EnterMove(board)