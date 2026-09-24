import json
import uuid

class Staff:
    def __init__(self, first_name, last_name, gender, phone, position):
        # Private attributes
        self.__staff_ID = f"STF-{uuid.uuid4().hex[:8].upper()}"

        # Public attributes
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.position = position

    # Getters
    def get_staff_ID(self):
        return self.__staff_ID

    # Loan Approval / Rejection connected to loans.json
    def approve_loan(self, loan_id ,staff_id):
        with open("staff.json", "r") as f:
            staff = json.load(f)

        for st in staff:
            if st["staff_id"] == staff_id:
                break
        
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

    def register_staff(self):
            with open("staff.json", "r") as f:
                staff = json.load(f)
    
            staff.append({
                "staff_id": self.__staff_ID,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "gender": self.gender,
                "phone": self.phone,
                "position": self.position
            })
    
            with open("staff.json", "w") as f:
                json.dump(staff, f, indent=4)
    
            print(f"Staff [{self.__staff_ID}] {self.first_name} {self.last_name} registered!")