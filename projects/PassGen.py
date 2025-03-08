import random

def gen_pass(length) :
    lowercase = "abcdefghijklmopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    special = "!@#$%&"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special),
    ]

    all_chars = lowercase + uppercase + digits + special
    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)
if __name__ == "__main__":
    pwd = gen_pass(12)
    print(f"Generated password: {pwd}")

