# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:33:55 2020

@author: Adhiraj
"""


#making a tic tac toe game

def Input():
    symbol = ""
    players = [" "]
    while symbol not in ['x','o']:
        symbol = input("what do you wanna be player one 'x' or 'o': ")
        if(symbol not in ['x','o']):
            print("sorry!but you need to check your input properly")
            
    if(symbol.lower() == 'x'):
        players.append("x")
        print ("player one you are 'x' and player two you are 'o'")
        players.append("o")
    else:
        players.append("o")
        print("player one you are 'o' and player two you are 'x'")
        players.append("x")
    return players
#test input()

       

def consent():
    consent = ""
    while consent not in ["yes","no"]:
        consent = input("enter 'yes' to continue playing and enter 'no' to stop playing: ")
        if consent not in ["yes","no"]:
            print ("sorry!i need you to enter the command again !!!there was some problem with your input")
            
    return consent.lower()
#test consent()

def game_board(arr):
    
    
    print (f"{ arr[7]}   |  {arr[8]}   |  {arr[9]} \n"
      +f"{arr[0]}   |  {arr[0]}   |  {arr[0]} \n  "  
+"-"*11+f"\n {arr[4]}  |  {arr[5]}   |  {arr[6]}\n"
      +f"{arr[0]}   |  {arr[0]}   |  {arr[0]} \n  "
+"-"*11+f"\n {arr[1]}  |  {arr[2]}   |  {arr[3]}\n"
      +f"{arr[0]}   |  {arr[0]}   |  {arr[0]} \n")


def place_marker(arr,symbol,pos):
    arr[pos] = symbol


def win_check(arr,symbol):
    return (arr[1]==symbol and arr[2]==symbol and arr[3]==symbol or
            arr[4]==symbol and arr[5]==symbol and arr[6]==symbol or
            arr[7]==symbol and arr[8]==symbol and arr[9]==symbol or
            arr[9]==symbol and arr[5]==symbol and arr[1]==symbol or
            arr[7]==symbol and arr[5]==symbol and arr[3]==symbol or
            arr[1]==symbol and arr[4]==symbol and arr[7]==symbol or
            arr[8]==symbol and arr[5]==symbol and arr[2]==symbol or
            arr[3]==symbol and arr[6]==symbol and arr[9]==symbol)


import random
def choose_first():
    turn = random.randint(1,2)
    print ("lettsss choose at random!!!!!!!player "+str(turn)+" gets to go first")
    return turn


def space_check(arr,position):
    if(arr[position] == " "):
        return True
    else:
        return False
 
def full_board_check(arr):
    if(" "  in arr ):
        return True
    else:
        return False
    
def player_choice(arr):
    next_position = 0
    while next_position not in map(str,range(1,10)) or not space_check(arr,int(next_position)):
        next_position = input("enter  your next position: ")
        if(next_position not in map(str,range(1,10))):
            print ("please give a valid input!!!it should be a number")
        if not(space_check(arr,int(next_position))) and next_position  in map(str,range(1,10)):
            print("hey i am sorry its already occupied!!! Try again!!")
    return int(next_position)

#setting up the game here ...... encorporating while and functions


while True:
    print ("We would like you to choose your symbols .... whoever chooses the symbol first is gonna be designated"+ 
           " as player one remember.....  ;-)  \n")
    players = Input()
    
    turn = choose_first()
    
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']      
    while full_board_check(board):
            #player 1 x
            symbol = players[turn]
            board[player_choice(board)] = symbol
            game_board(board)
            if(win_check(board,symbol)):
                print("congrats !!!! You won the Game!!!")
                break
            #player 2
            if(symbol == "x"):
                symbol = 'o'
            else:
                symbol = "x"
            board[player_choice(board)] = symbol
            game_board(board)
            if(win_check(board,symbol)):
                print("congrats !!!! You won the Game!!!")
                break
            
    if (consent() == 'no'):
        print ("thanks guys for playin ")
        break
    else:
        print ("Lets play again bichesssss!!!")
        continue

        
        
    
        
    
    
    
            