# Parent Account class
class Account:

    count = 0

    # Class method for auto-incrementing Account ID
    @classmethod
    def generate_id(cls):
        Account.count += 1
        return f"A{Account.count:03d}"

    def __init__(self, member, date_opened, account_id=None):
        if account_id is None:
            self.__account_id = Account.generate_id()
        else:
            self.__account_id = account_id
        self.member = member  # Composition: Account has a Member object
        self.__balance = 0    # Private attribute (encapsulation)
        self.__date_opened = date_opened
        self.account_type = "General"
        self.member.add_account(self)  # Member keeps track of its accounts

    def get_account_id(self):
        return self.__account_id

    # Property decorators for read-only attributes
    @property
    def balance(self):
        return self.__balance

    @property
    def date_opened(self):
        return self.__date_opened

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Deposit amount must be greater than zero")
            return False

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return False
        elif amount > self.__balance:
            print(f"Insufficient balance. Available: UGX {self.__balance}")
            return False
        else:
            self.__balance -= amount
            return True

    def __str__(self):
        return (f"{self.__account_id}\t{self.account_type}\t"
                f"{self.member.get_full_name()}\tUGX {self.__balance}")

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "account_id": self.__account_id,
            "member_id": self.member.get_member_id(),
            "account_type": self.account_type,
            "balance": self.__balance,
            "date_opened": self.__date_opened
        }


# Child class for Savings Account (Inheritance)
class SavingsAccount(Account):

    def __init__(self, member, date_opened, account_id=None):
        super().__init__(member, date_opened, account_id)
        self.account_type = "Savings"


# Child class for Fixed Deposit Account (Inheritance)
class FixedDepositAccount(Account):

    def __init__(self, member, date_opened, account_id=None):
        super().__init__(member, date_opened, account_id)
        self.account_type = "Fixed Deposit"

    # Method overriding: Fixed Deposit accounts do not allow withdrawals (Polymorphism)
    def withdraw(self, amount):
        print("Withdrawals are not allowed on a Fixed Deposit account")
        return False
