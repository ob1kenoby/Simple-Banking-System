from random import randint


card_data = {}


def create_account():
    card_number = "400000" + "".join([str(randint(0, 9)) for _i in range(0, 10)])
    pin = "".join([str(randint(0, 9)) for _i in range(0, 4)])
    card_data[card_number] = pin
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)


def login():
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    print()
    if card_number not in card_data:
        print("Wrong card number or PIN!")
        if card_data[card_number] != pin:
            print("Wrong card number or PIN!")
    elif card_data[card_number] == pin:
        print("You have successfully logged in!")


user_choice = ""
while not user_choice == "0":
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    print()
    user_choice = input()
    if user_choice == "1":
        create_account()
    elif user_choice == "2":
        login()
    print()
