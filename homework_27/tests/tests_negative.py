"""NEGATIVE API TESTS"""

import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods
from log_dir.log_setup import logger


def test_create_user_email_already_exists():
    """
    Test creating a user with an email that already exists.

    This function generates a random email, creates a user with that email,
    and then attempts to create another user with the same email.
    It verifies that the first creation attempts is successful and
    the second attempt returns a 409 status code with an appropriate
    error message indicating that the email already exists.
    """
    test_email = service_methods.generate_random_email()
    url = f"{variables.url}/functions/createUser"
    logger.info("Create user. 409 expected")

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
    assert response.status_code == 200
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 409
    assert response.text == '{"error":"User with this email already exists"}'


def test_create_user_with_empty_data():
    """
    Test creating a user with empty data fields.

    This function attempts to create a user with empty data fields
    and verifies that the request failswith a 400 status code
    and an appropriate error message indicating the invalid input.
    """
    url = f"{variables.url}/functions/createUser"
    print("Create user. 400 expected")

    headers = variables.headers

    data = {
        "name": "",
        "email": "",
        "age": None,
        "phoneNumber": "",
        "address": "",
        "role": "",
        "referralCode": ""
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    assert response.text == '{"error":"Invalid name: it must be a string with at least 3 characters"}'


def test_delete_unexisting_user():
    """
    Test deleting a user that does not exist.

    This function attempts to delete a user with a non-existent ID
    and verifies that the request fails with a 400 status code
    and an appropriate error message indicating the invalid ID format.
    """
    url = f"{variables.url}/functions/deleteUser/0123456789"
    print("Delete user. 400 expected")

    headers = variables.headers

    response = requests.delete(url, headers=headers)
    assert response.status_code == 400
    assert response.text == '{"error":"Invalid Order ID format"}'
