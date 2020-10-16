from random import randint


def create_account():
    card_number = "".join([randint(0, 9) for _i in range(0, 10)])
    pin = "".join([randint(0, 9) for _i in range(0, 4)])
    card_data[card_number] = pin
    print()
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)


def login():
    pass


card_data = {}

print("1. Create an account")
print("2. Log into account")
print("0. Exit")

exit_choice = False

while not exit_choice:
    user_choice = input()
    if user_choice == "1":
        create_account()
    elif user_choice == "2":
        login()
    elif user_choice == "0":
        exit_choice = True
