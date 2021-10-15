# def print_greeting():
#     print("Hello!")
#
#
# def print_greeting_for_user(user_name):
#     print("Hello " + user_name)
#
#
# def construct_greeting_for_user(user_name):
#     return "Hello " + user_name
#
#
# def constant_greeting(user_name, num):
#     for x in range(num):
#         print("Hello " + user_name)


def pozdravi(imena):
    for ime in imena:
        print ("Hello " + ime)


names = ["matej", "luka", "neza", "joze", "micka"]



pozdravi(names)

# if __name__ == "__main__":
#     greeting1 = construct_greeting_for_user("Luka")
#     print(greeting1)
#     player1 = "Matic"
#     constant_greeting("Luka", 10)
