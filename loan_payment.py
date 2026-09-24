import uuid
import json
from datetime import datetime

class LoanPayment:
    def __init__(self, loan_id, amount_paid, payment_method):
        # Private attributes
        self.__payment_id = f"PAY-{uuid.uuid4().hex[:8].upper()}"
        self.__loan_id = loan_id
        self.__amount_paid = amount_paid
        self.__payment_date = datetime.now().strftime("%Y-%m-%d")

        # Public attribute
        self.payment_method = payment_method

    # Getters
    def get_payment_id(self):
        return self.__payment_id
    def get_loan_id(self):
        return self.__loan_id
    def get_amount_paid(self):
        return self.__amount_paid
    def get_payment_date(self):
        return self.__payment_date
    def get_payment_method(self):
        return self.payment_method

    # Methods
    def make_payment(self):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == self.__loan_id:
                loan["current_balance"] -= self.__amount_paid
                if loan["current_balance"] == 0:
                    loan["status"] = "Cleared"
                remaining = loan["current_balance"]
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        # 2. Append to payments
        with open("payments.json", "r") as f:
            payments = json.load(f)

        payments.append({
            "payment_id": self.__payment_id,
            "loan_id": self.__loan_id,
            "amount_paid": self.__amount_paid,
            "payment_method": self.payment_method,
            "payment_date": self.__payment_date,
            "remaining_balance": remaining
        })

        with open("payments.json", "w") as f:
            json.dump(payments, f, indent=4)

        print(f"Paid: UGX {self.__amount_paid} | Remaining: UGX {remaining}")