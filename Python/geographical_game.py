import random



country_capital_pairs = {
    "Slovenia": "Ljubljana",
    "Germany": "Berlin",
    "Ireland": "Dublin",
    "Croatia": "Zagreb",
    "Austria": "Wien",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Poland": "Warsav",
    "Hungary": "Budapest",
}

random_country = random.choice(list(country_capital_pairs.keys()))
while True:
    answear = input(f"What is the capital city of {random_country}? ")

    if answear == country_capital_pairs[random_country]:
        print(f"You have guessed the capital of {random_country} which is {country_capital_pairs[random_country]}.")
        break
    else:
        print("Sorry, try again.")

print("Thanks for playing")