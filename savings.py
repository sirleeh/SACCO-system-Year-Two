# Class to represent a savings deposit transaction
class SavingsDeposit:

    count = 0

    # Class method for auto-incrementing Savings ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"S{cls.count:03d}"

    def __init__(self, account, amount_saved, payment_method, savings_date, savings_id=None):
        if savings_id is None:
            self.__savings_id = SavingsDeposit.generate_id()
        else:
            self.__savings_id = savings_id
        self.account = account  # Composition: SavingsDeposit has an Account object
        self.__amount_saved = amount_saved
        self.payment_method = payment_method
        self.__savings_date = savings_date

    # Getter methods
    def get_savings_id(self):
        return self.__savings_id

    def get_amount_saved(self):
        return self.__amount_saved

    def get_savings_date(self):
        return self.__savings_date

    # Delegation: call the account's deposit method to update balance
    def record_savings(self):
        return self.account.deposit(self.__amount_saved)

    def __str__(self):
        return (f"{self.__savings_id}\t{self.__savings_date}\t"
                f"{self.account.get_account_id()}\tUGX {self.__amount_saved}\t{self.payment_method}")

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "savings_id": self.__savings_id,
            "member_id": self.account.member.get_member_id(),
            "account_id": self.account.get_account_id(),
            "amount_saved": self.__amount_saved,
            "payment_method": self.payment_method,
            "savings_date": self.__savings_date
        }
