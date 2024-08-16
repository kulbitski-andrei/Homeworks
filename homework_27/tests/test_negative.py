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
    # assert response.text == "<Response [200]>"
    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
    assert response.status_code == 409
    # assert response.text == "<Response [409]>"

