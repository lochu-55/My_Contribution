import json


class Config:
    def __init__(self):
        # Load JSON data from file
        with open(r"Base/Elements/Data/resources.json", 'r') as json_file:
            api_config = json.load(json_file)

        # Extract URL and authorization token
        self.url = api_config['scheme'] + api_config['host'] + api_config['path']
        self.authorization_token = 'Bearer ' + api_config['authorization_token']

    def get_url(self):
        return self.url

    def get_authorization_token(self):
        return self.authorization_token
