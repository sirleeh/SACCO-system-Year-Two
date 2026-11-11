# Composite class representing a SACCO Loan
class Loan:

    count = 0

    # Class method for auto-incrementing Loan ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"L{cls.count:03d}"

    LOAN_LIMIT_MULTIPLIER = 3

    # Loan limit = 3 times the current balance of the member's account(s)
    @classmethod
    def calculate_loan_limit(cls, member, accounts):
        total_balance = 0
        for account in accounts:
            if account.member.get_member_id() == member.get_member_id():
                total_balance += account.balance
        return cls.LOAN_LIMIT_MULTIPLIER * total_balance

    # Check that the amount being borrowed falls within the member's loan limit
    @classmethod
    def is_within_limit(cls, member, amount, accounts):
        return 0 < amount <= cls.calculate_loan_limit(member, accounts)

    def __init__(self, member, loan_amount, payment_period, payment_method, loan_purpose, start_date, loan_id=None):
        if loan_id is None:
            self.__loan_id = Loan.generate_id()
        else:
            self.__loan_id = loan_id
        self.member = member  # Composition: Loan has a Member (borrower)
        self.__loan_amount = loan_amount
        self.__current_balance = loan_amount
        self.payment_period = payment_period
        self.payment_method = payment_method
        self.loan_purpose = loan_purpose
        self.__start_date = start_date
        self.__status = "Pending"
        self.approved_by = None
        self.guarantors = []  # List of Guarantor objects
        self.payments = []    # List of LoanPayment objects
        self.max_guarantors = 3

    # Getter methods
    def get_loan_id(self):
        return self.__loan_id

    def get_loan_amount(self):
        return self.__loan_amount

    def get_current_balance(self):
        return self.__current_balance

    def get_start_date(self):
        return self.__start_date

    def get_status(self):
        return self.__status

    # Add a guarantor to the loan (maximum 3 guarantors)
    def add_guarantor(self, guarantor):
        if self.__status != "Pending":
            print(f"Guarantors can only be added to a Pending loan. Loan {self.__loan_id} is {self.__status}")
            return False
        elif guarantor.member == self.member:
            print("A member cannot guarantee their own loan")
            return False
        elif len(self.guarantors) >= self.max_guarantors:
            print(f"Loan {self.__loan_id} already has {self.max_guarantors} guarantors")
            return False
        else:
            self.guarantors.append(guarantor)
            return True

    # Approve the loan if it is Pending and has at least one guarantor
    def approve(self, staff):
        if self.__status != "Pending":
            print(f"Loan {self.__loan_id} is already {self.__status}")
            return False
        elif len(self.guarantors) == 0:
            print(f"Loan {self.__loan_id} needs at least one guarantor before approval")
            return False
        else:
            self.__status = "Approved"
            self.approved_by = staff
            return True

    # Reject a pending loan
    def reject(self, staff):
        if self.__status != "Pending":
            print(f"Loan {self.__loan_id} is already {self.__status}")
            return False
        else:
            self.__status = "Rejected"
            self.approved_by = staff
            return True

    # Record a loan repayment and reduce the current balance
    def receive_payment(self, payment):
        amount = payment.get_amount_paid()
        if self.__status != "Approved":
            print(f"Payments can only be made on an Approved loan. Loan {self.__loan_id} is {self.__status}")
            return False
        elif amount <= 0:
            print("Payment amount must be greater than zero")
            return False
        elif amount > self.__current_balance:
            print(f"Amount is more than the remaining balance of UGX {self.__current_balance}")
            return False
        else:
            self.__current_balance -= amount
            self.payments.append(payment)
            if self.__current_balance == 0:
                self.__status = "Cleared"
            return True

    def __str__(self):
        return (f"{self.__loan_id}\t{self.member.get_full_name()}\t"
                f"UGX {self.__loan_amount}\tBalance UGX {self.__current_balance}\t{self.__status}")

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        if self.approved_by != None:
            staff_id = self.approved_by.get_staff_id()
        else:
            staff_id = ""
        return {
            "loan_id": self.__loan_id,
            "member_id": self.member.get_member_id(),
            "loan_amount": self.__loan_amount,
            "current_balance": self.__current_balance,
            "payment_period": self.payment_period,
            "payment_method": self.payment_method,
            "loan_purpose": self.loan_purpose,
            "start_date": self.__start_date,
            "status": self.__status,
            "approved_by": staff_id
        }
