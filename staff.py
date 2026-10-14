import json,uuid
from member import Member

class Staff(Member):
    staff_count=0
    def __init__(self, first_name, last_name, gender,phone,national_id, position):
        Staff.staff_count += 1
        super().__init__(self,first_name,last_name,gender,phone,national_id)
        self.__staff_ID=f"S{Staff.staff_count:03d}"
        self.position = position

    # Getters
    def get_staff_ID(self):
        return self.__staff_ID

    #polymorphism implementation
    def get_role(self):
        return f"Staff-{self.position}"
    def display_details(self):
        return f"Staff: {self.get_full_name()}\nStaffID:{self.__staff_ID}\nPosition:{self.position}"
        
    # Loan Approval / Rejection connected to loans.json
    def approve_loan(self, loan_id):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == loan_id:
                loan["status"] = "Approved"
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        print(f"Loan [{loan_id}] Approved!\nProcessed by: {self.first_name} {self.last_name}")

    def reject_loan(self, loan_id):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == loan_id:
                loan["status"] = "Rejected"
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        print(f"Loan [{loan_id}] Rejected!\nProcessed by: {self.first_name} {self.last_name}")