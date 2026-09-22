import json
import uuid
from datetime import datetime

class Account:
    def __init__(self, member_id, balance=0, account_type="Savings"):
        # Private attributes
        self.__account_id = f"ACC-{uuid.uuid4().hex[:8].upper()}"
        self.__member_id = member_id
        self.__balance = balance
        self.__date_opened = datetime.now().strftime("%Y-%m-%d")

        # Public attributes
        self.account_type = account_type
        self.status = "Active"

    # Getters
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

        accounts.append({
            "account_id": self.__account_id,
            "member_id": self.__member_id,
            "balance": self.__balance,
            "account_type": self.account_type,
            "status": self.status,
            "date_opened": self.__date_opened
        })

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent=4)

        print(f"Account [{self.__account_id}] created for Member [{self.__member_id}]!")

    def check_balance(self):
        with open("accounts.json", "r") as f:
            accounts = json.load(f)

        for acc in accounts:
            if acc["account_id"] == self.__account_id:
                self.__balance = acc["balance"]
                break

        print(f"Account [{self.__account_id}] Balance: UGX {self.__balance}")
        return self.__balance