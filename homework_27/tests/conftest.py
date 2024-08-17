"""FIXTURE MODULE"""

import pytest
import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods
from log_dir.log_setup import logger


@pytest.fixture
def pre_create_user():
    """
    Fixture to pre-create a test user.

    This fixture generates a random email and sends a POST request
    to create the user, and stores the user's ID in the 'variables.id_value'
    for use in subsequent tests.
    This ensures that a test user is available for tests that require
    an existing user.
    """
    test_email = service_methods.generate_random_email()
    url = f"{variables.url}/functions/createUser"
    logger.info("Pre-creating test user...")

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

    response = requests.post(url, headers=headers, json=data, timeout=10)
    variables.id_value = response.json().get("id")
    print(f"Test user is pre-created. "
          f"Test user id is {variables.id_value}")
