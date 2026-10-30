import json
from datetime import datetime

class Member:
    member_count = 0

    @classmethod
    def generate_member_id(cls):
        cls.member_count += 1
        return f"M{cls.member_count:03d}"

    def __init__(self, first_name, last_name, gender, phone, national_id):
        self.__member_id= self.generate_member_id()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.national_id = national_id
        self.__join_date = datetime.now().strftime("%Y-%m-%d")
        self.__status = "Active"

    # Getters
    def get_member_id(self):
        return self.__member_id

    def get_join_date(self):
        return self.__join_date

    def get_status(self):
        return self.__status
    

    # Polymorphism implementation
    def display_details(self):
        return f"----Member details----\nNames: {self.get_full_name()}\nMember ID: {self.__member_id}\nDate joined: {self.__join_date}\nStatus: {self.__status}"

    # Methods
    def register_member(self):
        with open("members.json", "r") as f:
            members = json.load(f)

        members.append({
            "member_id": self.__member_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "phone": self.phone,
            "national_id": self.national_id,
            "join_date": self.__join_date,
            "status": self.__status
        })

        with open("members.json", "w") as f:
            json.dump(members, f, indent=4)

        print(f"Member [{self.__member_id}] {self.first_name} {self.last_name} registered!")