from datetime import datetime


class Loan:

    def __init__(self, loan_id: str, member_id: str, loan_amount: int, payment_period: str):
        # Public Attributes
        self.loan_id = loan_id
        self.member_id = member_id
        self.loan_amount = loan_amount
        self.payment_period = payment_period
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.guarantors = []

        # Private Attributes
        self.__loan_balance = loan_amount
        self.__status = "Pending"

    # Getters
    def get_loan_balance(self):
        return self.__loan_balance

    def get_status(self):
        return self.__status

    # Methods
    def approved(self):
        if self.__status == "Pending":
            self.__status = "Approved"
            print("Loan Approved!")
        else:
            print(f"Cannot approve loan in '{self.__status}' state.")

    def add_guarantor(self, guarantor_id: str):
        if guarantor_id not in self.guarantors:
            self.guarantors.append(guarantor_id)
            print(f"Guarantor {guarantor_id} added.")

    def reduce_balance(self, amount: int):
        if self.__status != "Approved":
            print(f"Repayment rejected: Loan is {self.__status}.")
            return
        if amount > 0:
            self.__loan_balance = self.__loan_balance - amount
            if self.__loan_balance == 0:
                self.__status = "Cleared"
            print(f"Paid: UGX {amount:,} | Balance: UGX {self.__loan_balance:,} ({self.__status})")
