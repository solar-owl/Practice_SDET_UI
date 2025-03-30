"""
Модуль для работы со страницей Customers.

Содержит класс и функции для работы со страницей Customers.
"""
from selenium.webdriver.common.by import By
import allure
from pages.BasePage import BasePage

TITLE_FIRST_NAME = (By.XPATH, "//a[contains(text(), \"First Name\")]")
LIST_FIRST_NAMES = (
    By.XPATH,
    "//tr[contains(@ng-repeat, \"cust in Customers\")]/td[1]")
DELETE_BUTTON_BY_NAME = (
    By.XPATH,
    '//td[contains(text(), "{}")]/following-sibling::td/button'
                         )
FIRST_NAME = (By.XPATH, '//td[contains(text(), "{}")]')


class CustomersPage(BasePage):
    """
    Класс для работы со страницей Customers.
    """
    def sort_by_first_name(self) -> None:
        """
        Нажимает на заголовок колонки First Name
        в таблице Customers для сортировки.
        :return: None.
        """
        self.click_element(*TITLE_FIRST_NAME)

    def get_list_of_first_names(self) -> [str]:
        """
        Получает список имен в колонке First Name в таблице Customers.
        :return: Список имен.
        """
        first_names_values = []
        elements = self.search_elements(*LIST_FIRST_NAMES)
        for row in elements:
            first_names_values.append(row.text)
        with allure.step('Получение имен из таблицы Customers'):
            return first_names_values

    def delete_row_by_name(self, name: str) -> None:
        """
        Удаление строки с именем в таблице Customers.
        :param name:
        :return: None.
        """
        locator = (By.XPATH, DELETE_BUTTON_BY_NAME[1].format(name))
        self.click_element(*locator)

    def delete_multiple_by_name(self, names) -> None:
        """
        Удаляет строки c именами из списка из таблицы Customers.
        :param names: Список имен.
        :return: None.
        """
        for name in names:
            with allure.step(f'Удаление клиента по имени {name}'):
                self.delete_row_by_name(name)

    def customer_is_present(self, name: str) -> bool:
        """
        Проверяет, что имя кастомера присутствует в таблице Customers.
        :param name: Имя.
        :return: True, если имя есть в таблице Customers,
        False в противном случае.
        """
        locator = (By.XPATH, FIRST_NAME[1].format(name))
        return self.assert_that_present(*locator)
