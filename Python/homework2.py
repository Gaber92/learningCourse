secret = int(73)
guess = int(input("Guess what is the secret lottery number: "))

if guess == secret:
    print("Congratulations you have won 1 billion euros!")
if guess != secret:
    print("Your guess " + str(guess) + " was incorrect. Better luck next time!")