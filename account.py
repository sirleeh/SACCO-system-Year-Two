import json
from datetime import datetime

class Account:
    account_count = 0

    @classmethod
    def generate_account_id(cls):
        cls.account_count += 1
        return f"A{cls.account_count:03d}"

    def __init__(self, member_id, balance=0, account_type="Savings"):
        self.__account_id =self.generate_account_id()
        self.__member_id = member_id
        self.__balance = balance
        self.__date_opened = datetime.now().strftime("%Y-%m-%d")
        self.account_type = account_type
        self.__status = "Active"

    # Getters
    def get_status(self):
        return self.__status

    def get_account_id(self):
        return self.__account_id

    def get_member_id(self):
        return self.__member_id

    def get_balance(self):
        return self.__balance

    def get_date_opened(self):
        return self.__date_opened

    # Methods
    def create_account(self):
        with open("accounts.json", "r") as f:
            accounts = json.load(f)

        self.__balance = 0
        accounts.append({
            "account_id": self.__account_id,
            "member_id": self.__member_id,
            "balance": self.__balance,
            "account_type": self.account_type,
            "status": self.__status,
            "date_opened": self.__date_opened
        })

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent=4)

        print(f"Account [{self.__account_id}] created for Member [{self.__member_id}]!")

    def check_balance(self, account_id=None):
        acc_id = account_id if account_id else self.__account_id
        with open("accounts.json", "r") as f:
            accounts = json.load(f)

        for acc in accounts:
            if acc["account_id"] == acc_id:
                self.__balance = acc["balance"]
                break

        print(f"Account [{acc_id}] Balance: UGX {self.__balance}")
        return self.__balance