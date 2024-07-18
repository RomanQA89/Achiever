import os
import string
import random
from dotenv import load_dotenv

load_dotenv()

base_url = 'https://api.achiever.skroy.ru'
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')


def generate_string(n):
    return 'j' * n


def english_chars():
    return 'abcdefghklmnipqstuywxz'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'


def numbers():
    return random.randint(10000000000, 99999999999)


def digits():
    return random.randint(1000000000000000000000000000000, 9000000000000000000000000000000)


# Для генерации случайных логинов
def gen_alphanum_random_str(length):
    letters_and_digits = string.ascii_lowercase + string.digits * 100 + string.ascii_lowercase * 100
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
