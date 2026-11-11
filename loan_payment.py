# Class to represent a loan repayment transaction
class LoanPayment:

    count = 0

    # Class method for auto-incrementing Payment ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"P{cls.count:03d}"

    def __init__(self, loan, amount_paid, payment_method, payment_date, payment_id=None):
        if payment_id is None:
            self.__payment_id = LoanPayment.generate_id()
        else:
            self.__payment_id = payment_id
        self.loan = loan  # Composition: LoanPayment has a Loan object
        self.__amount_paid = amount_paid
        self.payment_method = payment_method
        self.__payment_date = payment_date

    # Getter methods
    def get_payment_id(self):
        return self.__payment_id

    def get_amount_paid(self):
        return self.__amount_paid

    def get_payment_date(self):
        return self.__payment_date

    # Delegation: call the loan's receive_payment method
    def make_payment(self):
        return self.loan.receive_payment(self)

    def __str__(self):
        return f"{self.__payment_id}\t{self.__payment_date}\tUGX {self.__amount_paid}\t{self.payment_method}"

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "payment_id": self.__payment_id,
            "loan_id": self.loan.get_loan_id(),
            "amount_paid": self.__amount_paid,
            "payment_method": self.payment_method,
            "payment_date": self.__payment_date
        }
