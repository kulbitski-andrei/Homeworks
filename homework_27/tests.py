import requests
import string
import random

# from requests.auth import HTTPBasicAuth
# import pytest

url = "https://alexqa.netlify.app/.netlify"
token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
         ".eyJ1c2VySWQiOiIxMTY4NzI0NzY5MjY4MDM1NjM4MDIiLCJpYXQiOjE3MjM4MTM4OTgsImV4cCI6MTcyMzgxNzQ5OH0"
         ".fydgbQjxfvtI98GHkLtL32Lg9fwxBWEI9l_F9wMIwmY")
id_value = None


def generate_random_email():
    domains = ["example.com", "mail.com", "test.com"]
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email


def create_user():
    endpoint = f"{url}/functions/createUser"
    print("create_user")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "John Doe",
        "email": generate_random_email(),
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
    global id_value
    id_value = a.get("id")
    print("id is:", id_value)


def get_user(user_id):
    endpoint = f"{url}/functions/getUser/{user_id}"
    print("get_user")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)


def update_user(user_id):
    endpoint = f"{url}/functions/updateUser/{user_id}"
    print("update_user")

    headers = {
        "Authorization": f"Bearer {token}",
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


def delete_user(user_id):
    endpoint = f"{url}/functions/deleteUser/{user_id}"
    print("delete_user")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.delete(endpoint, headers=headers)
    print(response)
    print(response.text)


def check_status(user_id):
    endpoint = f"{url}/functions/checkUserStatus/{user_id}"
    print("check_status")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)


def get_users():
    endpoint = f"{url}/functions/getUsers"
    print("get_users")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(endpoint, headers=headers)
    print(response)
    print(response.text)


create_user()
print()
get_user(id_value)
print()
update_user(id_value)
print()
get_user(id_value)
print()
check_status(id_value)
print()
get_users()
print()
delete_user(id_value)
print()
