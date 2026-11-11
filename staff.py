from person import Person


# Staff inherits from Person (Inheritance)
class Staff(Person):

    count = 0

    # Class method for auto-incrementing Staff ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"ST{cls.count:03d}"

    def __init__(self, first_name, last_name, gender, phone, national_id, position, staff_id=None):
        super().__init__(first_name, last_name, gender, phone, national_id)
        if staff_id is None:
            self.__staff_id = Staff.generate_id()
        else:
            self.__staff_id = staff_id
        self.position = position

    def get_staff_id(self):
        return self.__staff_id

    # Delegation: Staff calls the Loan's approve and reject methods
    def approve_loan(self, loan):
        return loan.approve(self)

    def reject_loan(self, loan):
        return loan.reject(self)

    # Method overriding (Polymorphism)
    def display_details(self):
        person_details = super().display_details()
        return (f"---- Staff Details ----\n"
                f"Staff ID:\t{self.__staff_id}\n"
                f"{person_details}\n"
                f"Position:\t{self.position}")

    def __str__(self):
        return f"{self.__staff_id}\t{self.get_full_name()}\t{self.position}"

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "staff_id": self.__staff_id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "gender": self._gender,
            "phone": self.get_phone(),
            "national_id": self.get_national_id(),
            "position": self.position
        }
