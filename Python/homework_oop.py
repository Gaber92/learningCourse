import random
import json

class Result():
    score = None
    player_name = None

    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name



def playGame():
    secret = random.randint(1, 10)
    player_name = input("Please enter your name: ")
    

    while True:
        question = int(input("Guess the secret number: "))
        if question == secret:
            print(f"Your guess {question} is the secret number!")
            break
        else: print("Sorry wrong guess! Try again.")

playGame()
print("Thanks for playing!")
