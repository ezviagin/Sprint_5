import random
import string

ATTRIBUTE_WAIT_TIMEOUT = 10



def get_email():
    username_length = random.randint(6, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))

    number = random.randrange(1000, 1999)

    domains = ['mail.ru', 'yahoo.com', 'hotmail.com', 'outlook.com', 'yandex.ru', 'ya.ru', 'outlook.com', 'gmail.com']
    domain = random.choice(domains)

    return f"{username}{str(number)}@{domain}"


def get_password():
    # Generate a random password of length 6-12
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 64)))
