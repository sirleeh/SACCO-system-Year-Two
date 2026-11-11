from member import Member


# Guarantor inherits from Member (Multilevel Inheritance: Person -> Member -> Guarantor)
class Guarantor(Member):

    count = 0

    # Class method for auto-incrementing Guarantor ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"G{cls.count:03d}"

    def __init__(self, member, loan, amount_guaranteed, guarantor_id=None):
        super().__init__(
            member._first_name,
            member._last_name,
            member._gender,
            member.get_phone(),
            member.get_national_id(),
            member.get_join_date(),
            member.get_member_id()
        )
        self.set_status(member.get_status())
        if guarantor_id is None:
            self.__guarantor_id = Guarantor.generate_id()
        else:
            self.__guarantor_id = guarantor_id
        self.member = member  # Composition: link to the Member object
        self.loan = loan      # Composition: link to the Loan object
        self.__amount_guaranteed = amount_guaranteed

    # Getter methods
    def get_guarantor_id(self):
        return self.__guarantor_id

    def get_amount_guaranteed(self):
        return self.__amount_guaranteed

    # Setter method with validation
    def set_amount_guaranteed(self, amount_guaranteed):
        if amount_guaranteed > 0:
            self.__amount_guaranteed = amount_guaranteed
            return True
        else:
            print("Amount guaranteed must be greater than zero")
            return False

    # Method overriding (Polymorphism)
    def display_details(self):
        member_details = super().display_details()
        return (f"---- Guarantor Details ----\n"
                f"Guarantor ID:\t{self.__guarantor_id}\n"
                f"Loan ID:\t\t{self.loan.get_loan_id()}\n"
                f"Amount guaranteed:\tUGX {self.__amount_guaranteed}\n"
                f"{member_details}")

    def __str__(self):
        return (f"{self.__guarantor_id}\t{self.get_member_id()}\t"
                f"{self.get_full_name()}\tUGX {self.__amount_guaranteed}")

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "guarantor_id": self.__guarantor_id,
            "member_id": self.get_member_id(),
            "loan_id": self.loan.get_loan_id(),
            "amount_guaranteed": self.__amount_guaranteed
        }
