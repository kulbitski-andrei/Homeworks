import pytest
import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods
from log_dir.log_setup import logger


@pytest.fixture
def pre_create_user():
    test_email = service_methods.generate_random_email()
    url = f"{variables.url}/functions/createUser"
    print("create_user")

    headers = variables.headers

    data = {
        "name": "John Doe",
        "email": test_email,
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }

    response = requests.post(url, headers=headers, json=data)
    variables.id_value = response.json().get("id")
    print(f"Test urer pre-created. Id is {variables.id_value}")

