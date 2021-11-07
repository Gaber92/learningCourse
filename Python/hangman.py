import random


guess = None
secret = random.randint(1, 10)
print("Lets play a game!")
previousGuess = []

totalAttempts = 5

for attempt in range(5):
    guess = int(input("Guess what is the secret lottery number, you have " + str(totalAttempts - attempt) + " attempts left: "))
    previousGuess.append(guess)
    if guess < secret:
        print("Hint: Aim higher this time!")
        print("You have previously guessed: " + str(previousGuess))

    else:
        print("Hint: Aim lower this time!")
        print("You have previously guessed: " + str(previousGuess))

    if guess == secret:
        print("Congratulations you have won 1 billion euros!")
        break
    elif attempt < 4:
        if attempt == 3:
            print("LAST CHANCE:")

print("The secret number was " + str(secret))

