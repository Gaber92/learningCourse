import random
import datetime
import json

all_games_data = []

with open("high_scores.json") as all_g_d_handler:
    all_games_data = json.loads(all_g_d_handler.read())

while True:
    secret = random.randint(1, 10)
    attempts = 0
    previous_attempts = []
    player_name = input("what's your name? ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        previous_attempts.append(guess)
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            game_data = {
                "player_name": player_name,
                "score": attempts,
                "timestamp": str(datetime.datetime.now())
            }
            all_games_data.append(game_data)
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
        print(previous_attempts)

    if input("Do you want to repeat the game? [y/n] ").lower() == "n":
        break

with open ("all_games_data", "w") as all_g_d_handler:
    all_g_d_handler.write(json.dumps(all_games_data))

print("thanks for playing with us!")
print(all_games_data)
