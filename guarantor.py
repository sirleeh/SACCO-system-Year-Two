from member import Member
import json

class Guarantor(Member):
    Guarantor_count=0
    def __init__(self, first_name,last_name,gender,phone,national_id,amount_guaranteed, loan_id):
        Guarantor.Guarantor_count += 1
        super().__init__(self,first_name,last_name,gender,phone,national_id)
        self.__guarantor_id = f"G{Guarantor.Guarantor_count:03d}"
        self.amount_guaranteed = amount_guaranteed
        self.__loan_id = loan_id


     # Getters
    def get_guarantor_id(self):
        return self.__guarantor_id
    def get_loan_id(self):
        return self.__loan_id

    # Methods
    def register_guarantor(self):
        with open("guarantors.json", "r") as f:
            guarantors = json.load(f)

        guarantors.append({
            "guarantor_id": self.__guarantor_id,
            "member_id": self.__member_id,
            "name": self.name,
            "phone": self.phone,
            "amount_guaranteed": self.__amount_guaranteed,
            "loan_id": self.__loan_id
        })

        with open("guarantors.json", "w") as f:
            json.dump(guarantors, f, indent=4)

        print(f"Guarantor [{self.__guarantor_id}] (Member: {self.__member_id}) registered for Loan [{self.__loan_id}]!")