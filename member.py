from person import Person


# Member inherits from Person (Inheritance)
class Member(Person):

    count = 0

    # Class method for auto-incrementing Member ID
    @classmethod
    def generate_id(cls):
        cls.count += 1
        return f"M{cls.count:03d}"

    def __init__(self, first_name, last_name, gender, phone, national_id, join_date, member_id=None):
        super().__init__(first_name, last_name, gender, phone, national_id)
        if member_id is None:
            self.__member_id = Member.generate_id()
        else:
            self.__member_id = member_id
        self.__join_date = join_date
        self.__status = "Active"
        self.accounts = []  # Composition: Member has Account objects

    # Attach an account to this member
    def add_account(self, account):
        if account not in self.accounts:
            self.accounts.append(account)

    # Total current balance across all of the member's accounts
    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    # Getter methods
    def get_member_id(self):
        return self.__member_id

    def get_join_date(self):
        return self.__join_date

    def get_status(self):
        return self.__status

    # Setter method for member status
    def set_status(self, status):
        if status == "Active" or status == "Inactive":
            self.__status = status
            return True
        else:
            print("Status must be Active or Inactive")
            return False

    # Method overriding (Polymorphism)
    def __str__(self):
        return f"{self.__member_id}\t{self.get_full_name()}\t{self.get_phone()}\t{self.__status}"

    # Convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "member_id": self.__member_id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "gender": self._gender,
            "phone": self.get_phone(),
            "national_id": self.get_national_id(),
            "join_date": self.__join_date,
            "status": self.__status
        }
