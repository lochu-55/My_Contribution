from Base.Libraries.config import Config
import requests
from Base.Libraries.logging import logger


class Methods:
    def __init__(self):
        config = Config()
        self.log_obj = logger(r"Base/utils/Logs/API_logs/API.log")
        self.url = config.get_url()
        self.authorization = config.get_authorization_token()

    def get_records(self):
        try:
            r = requests.get(url=self.url, headers={"Authorization": self.authorization})
            r.raise_for_status()  # Raise an error for non-2xx responses
            self.log_obj.logger.info(f"data fetched from the api")
            return r
        except requests.exceptions.RequestException as e:
            self.log_obj.logger.info(f"Error fetching records: {e}")
            return None

    def get_record(self, id):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.get(url=endpoint, headers={"Authorization": self.authorization})
            r.raise_for_status()
            self.log_obj.logger.info(f"data fetched from the api using get request")
            return r
        except requests.exceptions.RequestException as e:
            self.log_obj.logger.info(f"Error fetching record with ID {id}: {e}")
            return None

    def put(self, id, data):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.put(url=endpoint, headers={"Authorization": self.authorization}, json=data)
            r.raise_for_status()
            self.log_obj.logger.info(f"modified the data using put request")
            return r
        except requests.exceptions.RequestException as e:
            self.log_obj.logger.info(f"Error updating record with ID {id}: {e}")
            return None

    def post(self, data):
        try:
            r = requests.post(url=self.url, headers={"Authorization": self.authorization}, json=data)
            r.raise_for_status()
            self.log_obj.logger.info(f"data sent to the api using post request")
            return r
        except requests.exceptions.RequestException as e:
            self.log_obj.logger.info(f"Error creating record: {e}")
            return None

    def delete(self, id):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.delete(url=endpoint, headers={"Authorization": self.authorization})
            r.raise_for_status()
            self.log_obj.logger.info(f"deleting data from the api using delete request")
            return r
        except requests.exceptions.RequestException as e:
            self.log_obj.logger.info(f"Error deleting record with ID {id}: {e}")
            return None