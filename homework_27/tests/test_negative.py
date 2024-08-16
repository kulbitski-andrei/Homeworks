import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods


def test_create_user_email_already_exists():
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
    assert response.status_code == 200
    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
    assert response.status_code == 409
    assert response.text == '{"error":"User with this email already exists"}'


def test_create_user_with_empty_data():
    endpoint = f"{variables.url}/functions/createUser"
    print("create_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "",
        "email": "",
        "age": None,
        "phoneNumber": "",
        "address": "",
        "role": "",
        "referralCode": ""
    }

    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
    assert response.status_code == 400
    assert response.text == '{"error":"Invalid name: it must be a string with at least 3 characters"}'


def test_delete_unexisting_user():
    endpoint = f"{variables.url}/functions/deleteUser/0123456789"
    print("delete_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.delete(endpoint, headers=headers)
    print(response)
    print(response.text)
    assert response.status_code == 400
    assert response.text == '{"error":"Invalid Order ID format"}'
