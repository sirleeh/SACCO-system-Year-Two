import json

class Staff:
    def __init__(self, staff_ID, first_name, last_name, gender, position):
        # Private attributes
        self.__staff_ID = staff_ID

        # Public attributes
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.position = position

    # Getters
    def get_staff_ID(self):
        return self.__staff_ID

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