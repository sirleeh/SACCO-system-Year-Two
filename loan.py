import json
import uuid
from datetime import datetime

class Loan:
    def __init__(self, member_id, loan_amount, payment_period, payment_method, loan_purpose, guarantor_id):
        # Private attributes
        self.__loan_id = f"LN-{uuid.uuid4().hex[:8].upper()}"
        self.__member_id = member_id
        self.__loan_amount = loan_amount
        self.__current_balance = loan_amount
        self.__payment_period = payment_period
        self.__start_date = datetime.now().strftime("%Y-%m-%d")
        self.__status = "Pending"

        # Public attributes
        self.payment_method = payment_method
        self.loan_purpose = loan_purpose
        self.guarantor_id = guarantor_id

    # Getters
    def get_loan_id(self):
        return self.__loan_id
    def get_member_id(self):
        return self.__member_id
    def get_loan_amount(self):
        return self.__loan_amount
    def get_current_balance(self):
        return self.__current_balance
    def get_payment_period(self):
        return self.__payment_period
    def get_start_date(self):
        return self.__start_date
    def get_status(self):
        return self.__status

    # Methods
    def apply_for_loan(self):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        loans.append({
            "loan_id": self.__loan_id,
            "member_id": self.__member_id,
            "loan_amount": self.__loan_amount,
            "current_balance": self.__current_balance,
            "payment_period": self.__payment_period,
            "payment_method": self.payment_method,
            "loan_purpose": self.loan_purpose,
            "guarantor_id": self.guarantor_id,
            "start_date": self.__start_date,
            "status": self.__status
        })

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        print(f"Loan application [{self.__loan_id}] saved!")
