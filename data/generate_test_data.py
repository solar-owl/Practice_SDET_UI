"""
Модуль для работы с тестовыми данными.

Содержит функции для генерации тестовых данных.
"""

import random

GENERAL_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
ADD_CUST_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
CUSTOMERS_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
ALERT_MESSAGE = 'Customer added successfully with customer id'


def generate_post_code() -> str:
    """
    Генерирует номер из 10 цифр.
    :return: Номер из 10 цифр.
    """
    number_list = [random.randint(0, 9) for _ in range(10)]
    number = ''.join(map(str, number_list))
    return number


def get_two_digit_numbers(post_code: str) -> [int]:
    """
    Делит строку с номером на двухзначные числа.
    :param post_code: Номер в виде строки.
    :return: Список из двухзначных чисел.
    """
    two_digit_numbers = [int(post_code[i:i + 2])
                         for i in range(0, len(post_code), 2)]
    return two_digit_numbers


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
    Генерация фамилии на основе Post Code. Каждое двузначное
    число из номера преобразовывается в букву английского алфавита в обратном порядке.
    :param post_code: Номер в виде строки.
    :return: Фамилия.
    """
    two_digit_numbers = get_two_digit_numbers(post_code)
    last_name = ''
    for number in two_digit_numbers:
        last_name += chr(ord('z') - (number % 26))
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
