import json
import uuid
from datetime import datetime

class Member:
    def __init__(self, first_name, last_name, gender, phone, national_id):
        # Private attributes
        self.__member_id = f"MBR-{uuid.uuid4().hex[:8].upper()}"
        self.__national_id = national_id
        self.__join_date = datetime.now().strftime("%Y-%m-%d")

        # Public attributes
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.status = "Active"

    # Getters
    def get_member_id(self):
        return self.__member_id
    def get_national_id(self):
        return self.__national_id
    def get_join_date(self):
        return self.__join_date

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
            "national_id": self.__national_id,
            "join_date": self.__join_date,
            "status": self.status
        })

        with open("members.json", "w") as f:
            json.dump(members, f, indent=4)

        print(f"Member [{self.__member_id}] {self.first_name} {self.last_name} registered!")