"""Name: Ambrea Williams
   
   Date: 06/21/2025

   Unit 8: Lab 8 - Coin Toss Game

   Description: Coin toss is a game where the user guesses heads or tails.
   The program simulates a coin toss and checks if the user's guess is correct.
   """

import random

""" The class mimics a coin with an amount of coins and a side up."""
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
    
""" Function to play a round of the coin toss game between two players."""    
def play_round(player1, player2):
    player1.toss()
    player2.toss()

    print(f"Player 1 toss: {player1.get_sideup()}, Player 2 toss: {player2.get_sideup()}")

    if player1.get_sideup() == player2.get_sideup():
        player1.set_amount(1)
        player2.set_amount(-1) # Player 1 loses a coin
        print("Coins matched! Player 1 gets a coin from Player 2.")
    else:
        player1.set_amount(-1)
        player2.set_amount(1)
        print("Coins didn't match! Player 2 gets a coin from Player 1.")

    print(f"Player 1 Coins: {player1.get_amount()}, Player 2 Coins: {player2.get_amount()}")

    """ Main function that starts the game and manages the player interactions."""

def main():
    player1 = Coin()
    player2 = Coin()

    user_input = input("Do you want to play? (y/n): ").lower()
    if user_input != "y":
        print("Game ended before starting.")
        return

    while user_input == "y":
        play_round(player1, player2)

        if player1.get_amount() == 0 or player2.get_amount() == 0: #updates coin amount
            break

        user_input = input("Do you want to continue playing? (y/n): ").lower()

    if player1.get_amount() > player2.get_amount():
        print("Player 1 wins the game!")
    elif player2.get_amount() > player1.get_amount():
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")

"""
    Runs the coin toss game between two players.

    Prompts the user to start the game and continues to play rounds as long as the user agrees
    and both players have coins remaining. Each round, both players toss a coin and exchange coins
    based on whether their tosses match. The game ends when the user chooses to stop or when a player
    runs out of coins. At the end, announces the winner or if the game is a tie.
    """        
def main():
    player1 = Coin()
    player2 = Coin()

    user_input = input("Do you want to play? (y/n): ").lower()
    if user_input != "y":
        print("Game ended before starting.")
        return

    while user_input == "y":
        play_round(player1, player2)

        if player1.get_amount() == 0 or player2.get_amount() == 0:
            break

        user_input = input("Do you want to continue playing? (y/n): ").lower()

    if player1.get_amount() > player2.get_amount():
        print("Player 1 wins the game!")
    elif player2.get_amount() > player1.get_amount():
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")

"""Main function that makes the game run. An verifies if all functions and classes are working correctly."""
if __name__ == "__main__":
    main() 