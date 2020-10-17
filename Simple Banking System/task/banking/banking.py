from random import randint


def checksum(card_number):
    total = 0
    for i in range(0, len(card_number)):
        temp = int(card_number[i])
        if i % 2 != 1:
            temp *= 2
        if temp > 9:
            temp -= 9
        total += temp
    return total % 10 == 0


def generate_card_number():
    check = False
    while not check:
        card_number = "400000" + "".join([str(randint(0, 9)) for _i in range(0, 10)])
        check = checksum(card_number)
    return card_number


class APM:
    def __init__(self):
        self.card_data = {}
        self.logged_in = False
        self.current_card = None

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
            if user_choice == "1" and not self.logged_in:
                self.create_account()
            elif user_choice == "2" and not self.logged_in:
                self.login()
            elif user_choice == "1" and self.logged_in:
                self.show_balance()
            elif user_choice == "2" and self.logged_in:
                self.logout()
            print()

    def create_account(self):
        card_number = generate_card_number()
        pin = "".join([str(randint(0, 9)) for _i in range(0, 4)])
        self.card_data[card_number] = [pin, 0]
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
        elif self.card_data[card_number][0] == pin:
            print("You have successfully logged in!")
            self.logged_in = True
            self.current_card = card_number
        else:
            print("Wrong card number or PIN!")

    def logout(self):
        self.logged_in = False
        self.current_card = None
        print("You have successfully logged out!")

    def show_balance(self):
        print("Balance: {}".format(self.card_data[self.current_card][1]))


apm = APM()
apm.menu()
print("Bye!")