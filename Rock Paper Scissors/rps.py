import time
import random


def run():
    class Game:
        def __init__(self, newPlayerName):
            self.playerName = newPlayerName
            self.playerHand = "NA"
            self.botHand = "Na"
            self.winner = "No winner yet"
            print("New instance of game class for " + self.playerName)

        # 1 = scissors
        # 2 = rock
        # 3 = paper

        def runGame(self):
            if ((self.playerHand == 2 or self.playerHand == 2) and self.botHand == 1):
                self.winner = 'You win'
            elif ((self.playerHand == 2 or self.playerHand == 2) and self.botHand == 2):
                self.winner = 'You tie.'
            elif ((self.playerHand == 2 or self.playerHand == 2) and self.botHand == 3):
                self.winner = 'You lose.'
            elif ((self.playerHand == 3 or self.playerHand == 3) and self.botHand == 1):
                self.winner = 'You lose.'
            elif ((self.playerHand == 3 or self.playerHand == 3) and self.botHand == 2):
                self.winner = 'You win!'
            elif ((self.playerHand == 3 or self.playerHand == 3) and self.botHand == 3):
                self.winner = 'You tie.'
            elif ((self.playerHand == 1 or self.playerHand == 1) and self.botHand == 1):
                self.winner = 'You tie.'
            elif ((self.playerHand == 1 or self.playerHand == 1) and self.botHand == 2):
                self.winner = 'You lose.'
            elif ((self.playerHand == 1 or self.playerHand == 1) and self.botHand == 3):
                self.winner = 'You win!'
            else:
                self.winner = 'INVALID input, try again'

    def main():
        PG = random.randint(1, 3)
        BG = random.randint(1, 3)

        myGame = Game("Mario")

        myGame.playerHand = PG
        myGame.botHand = BG
        myGame.runGame()
        print(myGame.winner)

    def again():
        main()
        A = input("Again??")
        if A == "no":
            return
        elif A == "yes":
            again()

    again()

run()