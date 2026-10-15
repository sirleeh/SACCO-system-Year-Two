import json
from member import Member

class Staff(Member):
    staff_count = 0

    def __init__(self, first_name, last_name, gender, phone, position):
        super().__init__(first_name, last_name, gender, phone, national_id="N/A")
        Staff.staff_count += 1
        self.__staff_ID = f"S{Staff.staff_count:03d}"
        self.position = position

    # Getters
    def get_staff_ID(self):
        return self.__staff_ID

    # Polymorphism implementation
    def get_role(self):
        return f"Staff-{self.position}"

    def display_details(self):
        return f"Staff: {self.get_full_name()}\nStaffID: {self.__staff_ID}\nPosition: {self.position}"

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

    # Loan Approval / Rejection
    @staticmethod
    def approve_loan(loan_id):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == loan_id:
                loan["status"] = "Approved"
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        print(f"Loan [{loan_id}] Approved!")

    @staticmethod
    def reject_loan(loan_id):
        with open("loans.json", "r") as f:
            loans = json.load(f)

        for loan in loans:
            if loan["loan_id"] == loan_id:
                loan["status"] = "Rejected"
                break

        with open("loans.json", "w") as f:
            json.dump(loans, f, indent=4)

        print(f"Loan [{loan_id}] Rejected!")
