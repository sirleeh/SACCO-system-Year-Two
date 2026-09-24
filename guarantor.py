import json
import uuid

class Guarantor:
    def __init__(self, member_id, first_name, last_name, phone, amount_guaranteed, loan_id):
        # Private attributes
        self.__guarantor_id = f"GNT-{uuid.uuid4().hex[:8].upper()}"
        self.__member_id = member_id
        self.__amount_guaranteed = amount_guaranteed
        self.__loan_id = loan_id

        # Public attributes
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    # Getters
    def get_guarantor_id(self):
        return self.__guarantor_id
    def get_member_id(self):
        return self.__member_id
    def get_amount_guaranteed(self):
        return self.__amount_guaranteed
    def get_loan_id(self):
        return self.__loan_id

    # Methods
    def register_guarantor(self,):
        with open("loans.json", "r") as f:
                    loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == self.__loan_id:
                break

        with open("loans.json", "r") as f:
                    loans = json.load(f)
        
        for loan in loans:
            if loan["guarantor_id"] == "":
                loan["guarantor_id"] = self.__guarantor_id
                break

        with open("loans.json", "w") as f:
                    json.dump(loans, f, indent=4)

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