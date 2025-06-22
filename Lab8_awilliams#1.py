"""Name: Ambrea Williams
   
   Date: 06/21/2025

   Unit 8: Lab 8 - Coin Toss Game

   Description: Coin toss is a game where the user guesses heads or tails.
   The program simulates a coin toss and checks if the user's guess is correct.
   """

import random

class Coin:
    def __init__(self):
        self.__amount = 20
        self.__sideup = random.choice(["Heads", "Tails"])

    def toss(self):
        self.__sideup = "Heads" if random.randint(0, 1) == 0 else "Tails"

    def get_sideup(self):
        return self.__sideup

    def set_amount(self, change):
        self.__amount += change

    def get_amount(self):
        return self.__amount
    
    
