import requests
from homework_27.test_data import variables
from homework_27.service_methods import service_methods


def test_create_user():
    endpoint = f"{variables.url}/functions/createUser"
    print("create_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "John Doe",
        "email": service_methods.generate_random_email(),
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }

    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
    a = response.json()
    print(a)
    variables.id_value = a.get("id")
    print("id is:", variables.id_value)


def test_get_user(user_id):
    endpoint = f"{variables.url}/functions/getUser/{user_id}"
    print("get_user")

    headers = {
        "Authorization": f"Bearer {variables.token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)


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


test_create_user()
print()
test_get_user(variables.id_value)
print()
test_update_user(variables.id_value)
print()
test_get_user(variables.id_value)
print()
test_check_status(variables.id_value)
print()
test_get_users()
print()
test_delete_user(variables.id_value)
print()
