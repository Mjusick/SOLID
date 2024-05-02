"""
Principle: Single Responsibility Principle
Rule: A class should have only one reason to change (should have only one responsibility).
Example: Correct implementation where DebitCardManager manages card details and AccountManager manages account balance operations.
"""


class DebitCardManager:
    def __init__(self):
        self.card_numbers = []

    def validate_card_number(self, card_number):
        if card_number in self.card_numbers:
            print("Card number found.")
        else:
            print("Card number not found. Please register your card.")

    def register_new_card(self, card_number):
        if card_number not in self.card_numbers:
            print("Adding card number to database.")
            self.card_numbers.append(card_number)
        else:
            print("Card number already exists.")


class AccountManager:
    def __init__(self):
        self.account_balance = 0

    def withdrawal(self, amount):
        if (self.account_balance - amount) >= 0:
            self.account_balance -= amount
            print(f"Account balance after withdrawal: {self.account_balance}")
        else:
            print(f"Withdrawal cancelled. Insufficient funds on account.")

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Account balance after deposit: {self.account_balance}")
