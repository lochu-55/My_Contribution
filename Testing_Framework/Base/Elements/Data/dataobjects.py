import json
from Base.Libraries.logging import logger


class Objects:

    def __init__(self, filename):
        self.data = []  # Create an empty list to store
        self.filename = filename
        self.log_obj = logger(r"Base/utils/Logs/API_logs/API.log")
        self.log_obj.logger.info(f"Objects class initialised for {self.filename}")

    def read_data(self):
        with open(self.filename, 'r') as json_file:
            users_data = json.load(json_file)

        for person in users_data['person']:
            if person['id'] is not None:
                person_dict = {
                    'name': person['name'],
                    'email': person['email'],
                    'gender': person['gender'],
                    'status': person['status'],
                    'id': person['id']
                }
            else:
                person_dict = {
                    'name': person['name'],
                    'email': person['email'],
                    'gender': person['gender'],
                    'status': person['status'],
                    'id': None
                }
            self.data.append(person_dict)
            self.log_obj.logger.info(f"data in the file {self.filename} loaded")

    def write_data(self):
        with open(self.filename, 'w') as json_file:
            json.dump({"person": self.data}, json_file, indent=4)
        self.log_obj.logger.info(f"sent data to the file {self.filename}")