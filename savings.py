import json
from datetime import datetime
from account import Account

class Savings(Account):
    savings_count=0
    def __init__(self, member_id,balance,account_type, account_id, amount_saved, payment_method):
        Savings.savings_count += 1
        super().__init__(member_id,balance,account_type)
        self.__savings_id = f"S-{Savings.savings_count}"
        self.__account_id = account_id
        self.amount_saved = amount_saved
        self.__savings_date = datetime.now().strftime("%Y-%m-%d")
        self.payment_method = payment_method

    # Getters
    def get_savings_id(self):
        return self.__savings_id
    def get_member_id(self):
        return self.__member_id
    def get_account_id(self):
        return self.__account_id
    def get_amount_saved(self):
        return self.__amount_saved
    def get_savings_date(self):
        return self.__savings_date

    # Methods
    def record_savings(self):
        # Update account balance in accounts.json
        with open("accounts.json", "r") as f:
            accounts = json.load(f)

        for acc in accounts:
            if acc["account_id"] == self.__account_id:
                acc["balance"] += self.__amount_saved
                new_balance = acc["balance"]
                break

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent=4)

        # Append transaction record to savings.json
        with open("savings.json", "r") as f:
            savings = json.load(f)

        savings.append({
            "savings_id": self.__savings_id,
            "member_id": self.__member_id,
            "account_id": self.__account_id,
            "amount_saved": self.__amount_saved,
            "savings_date": self.__savings_date,
            "payment_method": self.payment_method,
            "new_balance": new_balance
        })

        with open("savings.json", "w") as f:
            json.dump(savings, f, indent=4)

        print(f"Saved UGX {self.__amount_saved} for Member [{self.__member_id}]. New Balance: UGX {new_balance}")