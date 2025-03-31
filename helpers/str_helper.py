"""
Модуль для работы со строками.

Содержит функции для преобразования строк.
"""


def get_two_digit_numbers(post_code: str) -> [int]:
    """
    Делит строку с номером на двухзначные числа.
    :param post_code: Номер в виде строки.
    :return: Список из двухзначных чисел.
    """
    two_digit_numbers = [int(post_code[i:i + 2])
                         for i in range(0, len(post_code), 2)]
    return two_digit_numbers
