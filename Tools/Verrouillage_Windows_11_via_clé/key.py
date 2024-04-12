import random

def generate_auth_key():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

auth_key = generate_auth_key()
print(auth_key)
