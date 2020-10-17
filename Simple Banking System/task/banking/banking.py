from random import randint


class APM:
    def __init__(self):
        self.card_data = {}
        self.logged_in = False

    def menu(self):
        user_choice = ""
        while user_choice != "0":
            if self.logged_in:
                print("1. Show balance")
                print("2. Log out")
            else:
                print("1. Create an account")
                print("2. Log into account")
            print("0. Exit")
            print()
            user_choice = input()
            if user_choice == "1" and self.logged_in:
                self.create_account()
            elif user_choice == "2" and self.logged_in:
                self.login()
            print()

    def create_account(self):
        card_number = "400000" + "".join([str(randint(0, 9)) for _i in range(0, 10)])
        pin = "".join([str(randint(0, 9)) for _i in range(0, 4)])
        self.card_data[card_number] = pin
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)

    def login(self):
        card_number = input("Enter your card number: ")
        pin = input("Enter your PIN: ")
        print()
        if card_number not in self.card_data:
            print("Wrong card number or PIN!")
            if self.card_data[card_number] != pin:
                print("Wrong card number or PIN!")
        elif self.card_data[card_number] == pin:
            print("You have successfully logged in!")
        self.logged_in = True
