greetingMsg = "Hello, welcome to unit converter!"
print(greetingMsg)

while True: 
    print("Please enter the number of kilometers you would like to convert (digits only): ")

    km = float(input())
    miles = 0.62137119
    result = (km * miles)
    print("This is equivavlent to " + str(result) + " miles.")
    convertAgain = input("Would you like to convert again?")
    if convertAgain == "No" or convertAgain == "N" or convertAgain == "no" or convertAgain == "n":
        print("Thanks for using the app.")
        break
        
