from random import SystemRandom, sample
from string import ascii_lowercase, ascii_uppercase

def generate_random_password():
    r = SystemRandom()
    u_letters = list(ascii_uppercase)
    l_letters = list(ascii_lowercase)
    key_1 = r.sample(u_letters, 2)
    key_2 = r.sample(l_letters, 2)
    first = r.randint(0, 9)
    second = r.randint(0, 9)
    symbols = ['%', '$', '&', '€', '£', '¥', '~', '|', '}', '{', '-', '^', '<', '>']
    symbols = sample(symbols, 2)
    result = [key_1[0], key_2[1], key_1[1], key_2[0], str(first), str(second), symbols[0], symbols[1]]
    result = r.sample(result, 8)
    password = ''.join(result)

    return password

def format_texts(text, type):
    if type == "name":
        return " "*5 + text.title() + (" " * (40 - len(text)))

    else:
        return text + (" " * (38 - len(text)))