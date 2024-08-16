import pytest
import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods


@pytest.mark.positive
def test_create_user():
    test_email = service_methods.generate_random_email()
    endpoint = f"{variables.url}/functions/createUser"
    print("create_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "John Doe",
        "email": test_email,
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }

    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
    print("id is:", response.json().get("id"))
    assert response.status_code == 200
    assert response.json().get("name") == "John Doe"
    assert response.json().get("email") == test_email
    assert response.json().get("age") == 30
    assert response.json().get("phoneNumber") == "+12345678901"
    assert response.json().get("address") == "123 Main St"
    assert response.json().get("role") == "user"
    assert response.json().get("referralCode") == "ABCDEFGH"
    assert response.json().get("status") == "created"


@pytest.mark.positive
def test_get_user():
    endpoint = f"{variables.url}/functions/getUser/{variables.id_value}"
    print("get_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)
    assert response.status_code == 200
    assert response.text == '{"error":"Invalid User ID format"}'


def test_update_user(user_id):
    endpoint = f"{variables.url}/functions/updateUser/{user_id}"
    print("update_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "Aaaaaaa:)",
        "email": "johnsmith@example.com",
        "age": 31,
        "phoneNumber": "+1234567890",
        "address": "456 Elm Stanciya Zavodskaya",
        "role": "user",
        "referralCode": "777"
    }

    response = requests.put(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)


def test_delete_user(user_id):
    endpoint = f"{variables.url}/functions/deleteUser/{user_id}"
    print("delete_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.delete(endpoint, headers=headers)
    print(response)
    print(response.text)


def test_check_status(user_id):
    endpoint = f"{variables.url}/functions/checkUserStatus/{user_id}"
    print("check_status")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)


def test_get_users():
    endpoint = f"{variables.url}/functions/getUsers"
    print("get_users")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)
