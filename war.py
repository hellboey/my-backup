# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:22:27 2020

@author: Adhiraj
"""
import random
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","King","Queen","Jack","Ace")
suits = ("Heart","Spades","Clubs","Diamond")
values = {"Two":2,
                  "Three":3,
                  "Four":4,
                  "Five":5,
                  "Six":6,
                  "Seven":7,
                  "Eight":8,
                  "Nine":9,
                  "Ten":10,
                  "King":11,
                  "Queen":12,
                  "Jack":13,
                  "Ace":14}
class Card():
    def __init__(self,suit,rank):
        """
        Parameters
        ----------
        suit : it consists the detail about a  particular suit
        rank : the rank of a particular card in a  deck
        
        #it is an __init__ function acts as a constructor to initalize rank,suit and value
        Returns
        -------
        None.

        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        """
        

        Returns
        -------
        str
         the above returned string helps to attain a string a string description of the object when printed 

        """
        return (f"{self.rank} of {self.suit}")
        
class Deck():
    def __init__(self):
        """
        this is a default constructor initializing
        the all_cards variable

        Returns
        -------
        None.

        """
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #self.all_cards.append(f"{rank} of {suit}")
                card_new = Card(suit,rank)
                self.all_cards.append(card_new)
    def shuffle(self):
        """
        shuffle uses the random to shuffle the deck of cards

        Returns
        -------
        list
            it helps to obtain the shuffled array of cards

        """
        random.shuffle(self.all_cards)
        return self.all_cards
    def deal_one(self):
        """
        helps in dealing one card at a time in a game

        Returns
        -------
        gives a card that is to be dealt to the player
        """
        return self.all_cards.pop()
class Player():
    def __init__(self,name):
        """
        it is a default constructor
        """
        self.all_cards = []
        self.name = name
    def remove(self):
        return self.all_cards.pop(0)
    
    def add(self,new_cards):
        if type(new_cards) == type([]):
            #list of a multiple card object
            return self.all_cards.extend(new_cards)
        else:
            #list of a single card object
            return self.all_cards.append(new_cards)
    
    def __str__(self):
        return (f"{self.name} has {len(self.all_cards)} cards")
go_on = True
deck = Deck()
deck.shuffle()
player_one = Player("Adhiraj")
player_two = Player("Akashleena")
for _ in range(26):
    player_one.all_cards.append(deck.deal_one())
    player_two.all_cards.append(deck.deal_one())
round = 0 
while go_on:
    
    round += 1
    print(f"round {round}")
    if(len(player_one.all_cards) == 0):
        print(f"{player_one.name} has 0 Cards ! {player_two.name} wins the game")
        break
    if(len(player_two.all_cards) == 0):
        print(f"{player_two.name} has 0 Cards ! {player_one.name} wins the game")
        break
    player_one_cards = []
    player_one_cards.append(player_one.remove())
    player_two_cards = []
    player_two_cards.append(player_two.remove())
    at_war = True
    while at_war:
        if (player_one_cards[-1].value > player_two_cards[-1].value):
            at_war = False
            player_one.add(player_one_cards)
            player_one.add(player_two_cards)
        if (player_two_cards[-1].value > player_one_cards[-1].value):
            at_war = False
            player_two.add(player_two_cards)
            player_two.add(player_one_cards)
        else:
            print("WAR!!!")
            if(len(player_one.all_cards) < 3):
                print (f"{player_one.name} lost the game!{player_two.name} won the match" )
                go_on = False
                break
            elif(len(player_two.all_cards) < 3):
                print (f"{player_two.name} lost the game!{player_one.name} won the match" )
                go_on = False
                break    
            else:
                for _ in range(3):
                    player_one_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())
            
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
    
        
    