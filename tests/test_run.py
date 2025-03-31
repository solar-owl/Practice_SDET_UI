"""
Модуль для тестирования работы с клиентами.

Содержит функции для тестирования функционала создания, сортировки и удаления.
"""
import allure
import pytest
from data.generate_test_data import ALERT_MESSAGE
from data.generate_test_data import generate_new_customer_test_data
from helpers.transformations import get_names_after_delete
from helpers.transformations import get_names_for_delete
from helpers.transformations import get_sorted_names
from helpers.transformations import get_sorted_reverse_names


@allure.epic("Работа с клиентом")
@allure.feature('Создание клиента')
@allure.story('Создание клиента с использованием сгенерированных данных')
@allure.id('TC-001')
@allure.description(
    'Тест-кейс проверяет создание нового клиента на сгенерированных данных'
)
@pytest.mark.ui
@pytest.mark.usefixtures("cleanup_names")
def test_add_new_customer(general_page, add_customer_page, customers_page, cleanup_names):
    """
    Тест для добавления нового клиента.
    :param general_page: Объект основной страницы.
    :param add_customer_page: Объект страницы Add Customer.
    :param customers_page: Объект страницы Customers.
    :param cleanup_names: Список имен для очистки.
    :assert: Проверяет, что клиент создался.
    :return: None
    """
    general_page.click_add_customer_tab()
    general_page.check_page_changed_to_add_customer()
    with allure.step(
            'Получение тестовыx данныx: First Name, Last Name, Post Code'
    ):
        postcode, first_name, last_name = generate_new_customer_test_data()
    add_customer_page.fill_first_name(first_name)
    add_customer_page.fill_last_name(last_name)
    add_customer_page.fill_post_code(postcode)
    add_customer_page.click_add_customer_btn()
    cleanup_names.append(first_name)
    alert = add_customer_page.get_text_alert()
    with allure.step('Проверка, что появилось уведомление'):
        assert alert == ALERT_MESSAGE, \
         "Не получилось создать нового клиента"
    general_page.click_customers_tab()
    general_page.check_page_changed_to_customer()
    with allure.step(
            'Проверка, что новый клиент появился в таблице Customers'
    ):
        assert customers_page.customer_is_present(first_name), \
         "В таблице Customers нет нового клиента"


@allure.epic("Работа с клиентом")
@allure.feature('Сортировка в таблице')
@allure.story('Сортировка по имени в таблице')
@allure.id('TC-002')
@allure.description(
    'Тест-кейс проверяет сортировку клиентов в таблице по имени'
)
@pytest.mark.ui
def test_sort_customers_by_name(general_page, customers_page):
    """
    Тест для сортировки имен в таблице Customers.
    :param general_page: Объект основной страницы.
    :param customers_page: Объект страницы Customers.
    :assert: Проверяет, что имена сортируются
    при нажатии на заголовок колонки.
    :return: None
    """
    general_page.click_customers_tab()
    general_page.check_page_changed_to_customer()
    first_names = customers_page.get_list_of_first_names()
    with allure.step('Нажатие на First Name для сортировки по убыванию'):
        customers_page.sort_by_first_name()
    first_names_after_1 = customers_page.get_list_of_first_names()
    sorted_result_reverse = get_sorted_reverse_names(first_names)
    with allure.step('Проверка отсортированных данных'):
        assert first_names_after_1 == sorted_result_reverse, \
            f"Список неправильно отсортирован с конца {first_names_after_1}"
    with allure.step('Нажатие на First Name для сортировки по возрастанию'):
        customers_page.sort_by_first_name()
    first_names_after_2 = customers_page.get_list_of_first_names()
    sorted_result = get_sorted_names(first_names)
    with allure.step('Проверка отсортированных данных'):
        assert first_names_after_2 == sorted_result, \
            f"Список неправильно отсортирован  с начала {first_names_after_2}"


@allure.epic("Работа с клиентом")
@allure.feature('Удаление клиента из таблицы')
@allure.story('Удаление клиента по имени из таблицы')
@allure.id('TC-003')
@allure.description('Тест-кейс проверяет удаление клиентов из таблицы')
@pytest.mark.ui
def test_delete_customer(general_page, customers_page):
    """
    Тест для удаления клиентов, у которых длина имени ближе
    к среднему арифметическому всех длин из колонки First Name.
    :param general_page: Объект основной страницы.
    :param customers_page: Объект страницы Customers.
    :assert: Проверяет, что клиенты удалены.
    :return: None
    """
    general_page.click_customers_tab()
    general_page.check_page_changed_to_customer()
    first_names = customers_page.get_list_of_first_names()
    with allure.step('Получение имен для удаления'):
        del_names = get_names_for_delete(first_names)
    with allure.step('Удаление клиентов из таблицы Customers'):
        customers_page.delete_multiple_by_name(del_names)
    res_names = get_names_after_delete(first_names, del_names)
    new_name_list = customers_page.get_list_of_first_names()
    with allure.step('Проверка, что клиенты удалены из таблицы'):
        assert res_names == new_name_list, f"Клиенты {del_names} не удалены"
