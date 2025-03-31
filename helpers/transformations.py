"""
Модуль для работы с преобразованиями данных для тестов.

Содержит функции для преобразования данных для выполнения и проверок в тестах.
"""
import numpy as np


def get_sorted_names(values:  [str]) -> [str]:
    """
    Сортирует данные в алфавитном порядке.
    :param values: Список из строк.
    :return: Отсортированный список из строк.
    """
    sorted_values = sorted(values)
    return sorted_values


def get_sorted_reverse_names(values:  [str]) -> [str]:
    """
    Сортирует данные в обратном алфавитном порядке.
    :param values: Список из строк.
    :return: Отсортированный список из строк.
    """
    sorted_values_reverse = sorted(values, reverse=True)
    return sorted_values_reverse


def get_names_for_delete(names:  [str]) -> [str]:
    """
    Возвращает имена, у которых длина ближе к среднему арифметическому всех длин.
    :param names: Список из имен.
    :return: Список имен для удаления.
    """
    names_dict = {name: len(name) for name in names}
    values = list(names_dict.values())
    average = np.mean(values)
    min_difference = min(abs(values - average))
    del_names = []
    for key, value in names_dict.items():
        if abs(value - average) == min_difference:
            del_names.append(key)
    return del_names


def get_names_after_delete(first_names: [str], del_names: [str]) -> list[str]:
    """
    Возвращает список имен, которые не были удалены.
    :param first_names: Список всех имен.
    :param del_names: Список имен для удаления.
    :return: Список имен, которые остались после удаления.
    """
    return list(filter(lambda x: x not in del_names, first_names))
