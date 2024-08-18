"""VARIABLES FOR API TESTS"""
from homework_27.service_methods.service_methods import get_token

url = "https://alexqa.netlify.app/.netlify"
id_value = None
token = get_token()

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
