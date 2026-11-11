import json


# Class to handle reading and writing data to the JSON file
class Storage:

    def __init__(self, file_path="sacco_data.json"):
        self.file_path = file_path

    # Load data from the JSON file
    def load(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data

    # Save data to the JSON file
    def save(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
