"""
Модуль для работы с тестовыми данными.

Содержит функции для генерации тестовых данных.
"""

import random
from faker import Faker
from helpers.str_helper import get_two_digit_numbers


def generate_post_code() -> str:
    """
    Генерирует номер из 10 цифр.
    :return: Номер из 10 цифр.
    """
    number_list = [random.randint(0, 9) for _ in range(10)]
    number = ''.join(map(str, number_list))
    return number


def generate_first_name(post_code: str) -> str:
    """
    Генерация имени на основе Post Code. Каждое двузначное
    число из номера преобразовывается в букву английского алфавита.
    :param post_code: Номер в виде строки.
    :return: Имя.
    """
    two_digit_numbers = get_two_digit_numbers(post_code)
    first_name = ''
    for number in two_digit_numbers:
        first_name += chr((number % 26) + ord('a'))
    return first_name


def generate_last_name(post_code: str) -> str:
    """
    Генерация фамилии.
    :return: Фамилия.
    """
    fake = Faker('en_US')
    last_name = fake.last_name()
    return last_name


def generate_new_customer_test_data() -> tuple[str, str, str]:
    """
    Генерирует номер, имя и фамилию.
    :return: Номер из 10 цифр, имя, фамилия.
    """
    postcode = generate_post_code()
    first_name = generate_first_name(postcode)
    last_name = generate_last_name(postcode)
    return postcode, first_name, last_name
