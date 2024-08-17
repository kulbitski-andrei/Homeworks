"""SERVICE METHODS"""

import string
import random


def generate_random_email():
    """
    Generate a random email address.

    This function creates a random email address by generating
    a random username consisting of 10 lowercase letters and appending it
    to a randomly selected domain from a predefined list.

    Returns:
        str: A randomly generated email address.
    """
    domains = ["example.com", "mail.com", "test.com"]
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email
