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
        return self.__sideup # returns the current side of the coin

    def set_amount(self, change):
        self.__amount += change

    def get_amount(self):
        return self.__amount
    
def play_round(player1, player2):
    player1.toss()
    player2.toss()

    print(f"Player 1 toss: {player1.get_sideup()}, Player 2 toss: {player2.get_sideup()}")

    if player1.get_sideup() == player2.get_sideup():
        player1.set_amount(1)
        player2.set_amount(-1)
        print("Coins matched! Player 1 gets a coin from Player 2.")
    else:
        player1.set_amount(-1)
        player2.set_amount(1)
        print("Coins didn't match! Player 2 gets a coin from Player 1.")

    print(f"Player 1 Coins: {player1.get_amount()}, Player 2 Coins: {player2.get_amount()}")


