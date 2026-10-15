import json
from member import Member

class Guarantor(Member):
    Guarantor_count = 0

    def __init__(self, member_id, first_name, last_name, phone, amount_guaranteed, loan_id):
        super().__init__(first_name, last_name, gender="N/A", phone=phone, national_id="N/A")
        Guarantor.Guarantor_count += 1
        self.__guarantor_id = f"G{Guarantor.Guarantor_count:03d}"
        self.__member_id = member_id
        self.__amount_guaranteed = amount_guaranteed
        self.__loan_id = loan_id

    # Getters
    def get_guarantor_id(self):
        return self.__guarantor_id

    def get_member_id(self):
        return self.__member_id

    def get_loan_id(self):
        return self.__loan_id

    def get_amount_guaranteed(self):
        return self.__amount_guaranteed

    def get_role(self):
        return "Guarantor"

    # Methods
    def register_guarantor(self):
        # 1. Update loan in loans.json
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == self.__loan_id:
                loan["guarantor_id"] = self.__guarantor_id
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        # 2. Add to guarantors.json
        with open("guarantors.json", "r") as f:
            guarantors = json.load(f)

        guarantors.append({
            "guarantor_id": self.__guarantor_id,
            "member_id": self.__member_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "amount_guaranteed": self.__amount_guaranteed,
            "loan_id": self.__loan_id
        })

        with open("guarantors.json", "w") as f:
            json.dump(guarantors, f, indent=4)

        print(f"Guarantor [{self.__guarantor_id}] (Member: {self.__member_id}) registered for Loan [{self.__loan_id}]!")