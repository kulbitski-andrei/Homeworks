import string
import random


def generate_random_email():
    domains = ["example.com", "mail.com", "test.com"]
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email
