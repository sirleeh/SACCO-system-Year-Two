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
<<<<<<< HEAD
    def register_guarantor(self):
=======
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

>>>>>>> f0f518e78a1b5f790799a6fccb5750435e7fbe69
        with open("guarantors.json", "r") as f:
            guarantors = json.load(f)

        guarantors.append({
            "guarantor_id": self.__guarantor_id,
            "member_id": self.__member_id,
<<<<<<< HEAD
            "name": self.name,
=======
            "first_name": self.first_name,
            "last_name": self.last_name,
>>>>>>> f0f518e78a1b5f790799a6fccb5750435e7fbe69
            "phone": self.phone,
            "amount_guaranteed": self.__amount_guaranteed,
            "loan_id": self.__loan_id
        })

        with open("guarantors.json", "w") as f:
            json.dump(guarantors, f, indent=4)

        print(f"Guarantor [{self.__guarantor_id}] (Member: {self.__member_id}) registered for Loan [{self.__loan_id}]!")