"""POSITIVE API TESTS"""

import pytest
import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods
from log_dir.log_setup import logger


def test_create_user():
    """
    Test the creation of a new user.

    This function generates a random email, sends a POST request
    to create the user, and verifies the response to ensure the user
    was created successfully with the expected data.
    """
    test_email = service_methods.generate_random_email()
    url = f"{variables.url}/functions/createUser"
    logger.info("Create user")

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

    expected_keys = {"id", "name", "email", "age", "phoneNumber", "address", "role", "referralCode", "status"}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert set(response.json().keys()) == expected_keys
    assert response.json().get("name") == data["name"]
    assert response.json().get("email") == test_email
    assert response.json().get("age") == data["age"]
    assert response.json().get("phoneNumber") == data["phoneNumber"]
    assert response.json().get("address") == data["address"]
    assert response.json().get("role") == data["role"]
    assert response.json().get("referralCode") == data["referralCode"]
    assert response.json().get("status") == "created"


@pytest.mark.positive
def test_get_user(pre_create_user):
    """
    Test retrieving a user's details.

    This function sends a GET request to retrieve the details
    of a selected user, and verifies the response to ensure
    correct user was returned.
    """
    url = f"{variables.url}/functions/getUser/{variables.id_value}"
    logger.info("Get user")

    headers = variables.headers

    response = requests.get(url, headers=headers)
    expected_keys = {
        "id", "name", "email", "age", "phoneNumber", "address", "role", "referralCode", "createdAt", "createdBy"}
    assert response.status_code == 200
    assert set(response.json().keys()) == expected_keys
    assert response.json().get("id") == variables.id_value


def test_update_user(pre_create_user):
    """
    Test updating a user's details.

    This function provides the necessary data to update a user's details,
    sends a PUT request, and verifies the response to ensure
    the user's data was updated successfully with the expected values.
    """
    url = f"{variables.url}/functions/updateUser/{variables.id_value}"
    logger.info("Update user")

    headers = variables.headers

    data = {
        "name": "Salah ad-Din Yusuf ibn Ayyub",
        "email": "crusaders@go.home",
        "age": 45,
        "phoneNumber": "+1234567890",
        "address": "456 Elm Stanciya Zavodskaya",
        "role": "user",
        "referralCode": "777"
    }

    expected_keys = {"id", "name", "email", "age", "phoneNumber", "address", "role", "referralCode", "status"}
    response = requests.put(url, headers=headers, json=data)
    assert response.status_code == 200
    assert set(response.json().keys()) == expected_keys
    assert response.json().get("name") == data["name"]
    assert response.json().get("email") == data["email"]
    assert response.json().get("age") == data["age"]
    assert response.json().get("phoneNumber") == data["phoneNumber"]
    assert response.json().get("address") == data["address"]
    assert response.json().get("role") == data["role"]
    assert response.json().get("referralCode") == data["referralCode"]
    assert response.json().get("status") == "updated"


def test_check_status(pre_create_user):
    """
    Test checking a user's status.

    This function sends a GET request to check the status
    of a selected user, and verifies the response to ensure
    the status data matches the expected value.
    """
    url = f"{variables.url}/functions/checkUserStatus/{variables.id_value}"
    logger.info("Check status")

    headers = variables.headers

    response = requests.get(url, headers=headers)
    expected_keys = {"id", "name", "email", "createdAt", "createdBy", "status"}
    assert response.status_code == 200
    assert set(response.json().keys()) == expected_keys


def test_get_users():
    """
    Test retrieving a list of users.

    This function sends a GET request to retrieve a list of users,
    and verifies the response to ensure the data matches
    the expected structure and values.
    """
    url = f"{variables.url}/functions/getUsers"
    logger.info("Get users")

    headers = variables.headers

    response = requests.get(url, headers=headers)
    expected_keys = {"users", "totalPages"}
    assert response.status_code == 200
    assert set(response.json().keys()) == expected_keys
