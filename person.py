# Parent class for Member and Staff
class Person:

    def __init__(self, first_name, last_name, gender, phone, national_id):
        # Protected attributes (accessible by child classes)
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        # Private attributes (encapsulation)
        self.__phone = phone
        self.__national_id = national_id

    # Getter methods
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_phone(self):
        return self.__phone

    def get_national_id(self):
        return self.__national_id

    # Setter method with validation
    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone
            return True
        else:
            print("Phone number must be 10 digits")
            return False

    # Method to be overridden by child classes (Polymorphism)
    def display_details(self):
        return (f"Names:\t\t{self.get_full_name()}\n"
                f"Gender:\t\t{self._gender}\n"
                f"Phone:\t\t{self.__phone}\n"
                f"National ID:\t{self.__national_id}")

    def __str__(self):
        return f"{self.get_full_name()}\t{self.__phone}"
