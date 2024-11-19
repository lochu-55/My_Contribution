import pytest
import yaml
# Fixture to load data from YAML file


yaml_file_path = "login.yaml"
@pytest.fixture
def account_data():
    with open(yaml_file_path, "r") as file:
        data = yaml.safe_load(file)
    return data

# Test function that uses the account data
@pytest.mark.parametrize("account_data",["login.yaml"], indirect=True)
def test_login(account_data):
    print("Account data:", account_data)  # Debugging: Print account data
    assert isinstance(account_data, dict)  # Verify type of account data

    for account in account_data["accounts"]:# Iterate over accounts
        print(account)
        username = account["username"]
        password = account["password"]
        # Your test logic here
        print(f"Logging in with username: {username}, password: {password}")
        assert username is not None
        assert password is not None