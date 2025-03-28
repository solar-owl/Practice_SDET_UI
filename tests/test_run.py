import allure
import pytest
from conftest import general_page
from conftest import add_customer_page
from data.generate_test_data import generate_new_customer_test_data
from helpers.transformations import get_sorted_descending_and_ascending, get_names_for_delete, get_names_after_delete

@allure.epic("Работа с клиентом")
@allure.feature('Создание клиента')
@allure.story('Создание клиента с использованием сгенерированных данных')
@allure.id('TC-001')
@allure.description('Тест-кейс проверяет возможность создания нового клиента с использованием сгенерированных данных')
@pytest.mark.ui
def test_add_new_customer(general_page, add_customer_page, customers_page):
    general_page.click_add_customer_tab()
    with allure.step('Получение тестовыx данныx: First Name, Last Name, Post Code'):
        postcode, first_name, last_name = generate_new_customer_test_data()
    add_customer_page.fill_first_name(first_name)
    add_customer_page.fill_last_name(last_name)
    add_customer_page.fill_post_code(postcode)
    add_customer_page.click_add_customer_btn()
    alert = add_customer_page.get_text_alert()
    general_page.click_customers_tab()
    with allure.step('Проверка на успешное создание клиента'):
        assert customers_page.customer_is_present(first_name) and alert == "Customer added successfully with customer id", "Не получилось создать нового клиента"
    customers_page.delete_row_by_name(first_name)

@allure.epic("Работа с клиентом")
@allure.feature('Сортировка в таблице')
@allure.story('Сортировка по имени в таблице')
@allure.id('TC-002')
@allure.description('Тест-кейс проверяет возможность сортировки клиентов в таблице по имени')
@pytest.mark.ui
def test_sort_customers_by_name(general_page, customers_page):
    general_page.click_customers_tab()
    first_names = customers_page.get_list_of_first_names()
    with allure.step('Нажатие на название первой колонки First Name для сортировки по убыванию'):
        customers_page.sort_by_first_name()
    first_names_after_1 = customers_page.get_list_of_first_names()
    with allure.step('Нажатие на название первой колонки First Name для сортировки по возрастанию'):
        customers_page.sort_by_first_name()
    first_names_after_2 = customers_page.get_list_of_first_names()
    sorted_result, sorted_result_reverse = get_sorted_descending_and_ascending(first_names)
    with allure.step('Проверка отсортированных данных'):
        assert first_names_after_1 == sorted_result_reverse and first_names_after_2 == sorted_result, \
            f"Список неправильно отсортирован с конца {first_names_after_1} или с начала {first_names_after_2}"

@allure.epic("Работа с клиентом")
@allure.feature('Удаление клиента из таблицы')
@allure.story('Удаление клиента по имени из таблицы')
@allure.id('TC-003')
@allure.description('Тест-кейс проверяет возможность удаления клиентов из таблицы')
@pytest.mark.ui
def test_delete_customer(general_page, customers_page):
    general_page.click_customers_tab()
    first_names = customers_page.get_list_of_first_names()
    with allure.step('Получение имен для удаления'):
        del_names = get_names_for_delete(first_names)
    with allure.step('Удаление клиентов из таблицы Customers'):
        customers_page.delete_multiple_by_name(del_names)
        result_names = get_names_after_delete(first_names, del_names)
    new_name_list = customers_page.get_list_of_first_names()
    with allure.step('Проверка, что ожидаемый результат после удаления, отобразился в таблице'):
        assert result_names == new_name_list, f"Ожидаемый результат {result_names}, не равен результату на странице {new_name_list}"