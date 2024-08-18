"""SERVICE METHODS"""

import string
import random
import json
from log_dir.log_setup import logger


def get_token():
    with open("../test_data/config.json") as config_file:
        config = json.load(config_file)
        token = config["api_token"]
        logger.info(f"[Service methods] - TOKEN IS {token}")
        return token


def generate_random_email():
    """
    Generate a random email address.

    This function creates a random email address by generating
    a random username consisting of 10 lowercase letters and appending it
    to a randomly selected domain from a predefined list.

    Returns:
        str: A randomly generated email address.
    """

    random_char = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    email = random_char + "@gmail.com"
    print(email)
    return email


a = get_token()
print(a)
