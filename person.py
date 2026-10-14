from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,first_name, last_name, gender,phone,national_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.__national_id=national_id

    def get_national_id(self):
        return self.__national_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def display_details(self):
        pass
