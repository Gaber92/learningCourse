import random
import datetime

print(datetime.datetime.today())

while True:
    secret = random.randint(1, 30)
    attempts = 0
    previous_attempts = []
    player_name = input("what's your name? ")
    
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        previous_attempts.append(guess)
        attempts += 1
    
        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
        print(previous_attempts)
    
    if input("Do you want to repeat the game? [y/n] ").lower() == "n":
        break
    
print("thanks for playing with us!")