import random

ascii_map = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate(length=0):
    if length:
        return ''.join(random.choice(ascii_map) for i in range(length))

    else:
        return ''.join(random.choice(ascii_map) for i in range(random.choice([8, 9, 10])))
