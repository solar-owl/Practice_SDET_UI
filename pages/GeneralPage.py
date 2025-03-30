"""
Модуль для работы с основной страницей.

Содержит класс и функции для работы с основной страницей.
"""
from selenium.webdriver.common.by import By
import allure
from data.generate_test_data import ADD_CUST_URL, CUSTOMERS_URL
from pages.BasePage import BasePage

ADD_CUSTOMER_TAB = (
    By.XPATH,
    '//button[contains(text(), "Add Customer") and ./b[@id="notch"]]'
)
CUSTOMERS_TAB = (
    By.XPATH,
    '//button[contains(text(), "Customers") and ./b[@id="notch"]]'
)


class GeneralPage(BasePage):
    """
    Класс для работы с основной страницей.
    """
    def click_add_customer_tab(self) -> None:
        """
        Нажимает на табу Add Customer для перехода
        на страницу Add Customer.
        :return: None.
        """
        with allure.step('Навигация на вкладку Add Customer'):
            self.click_element(*ADD_CUSTOMER_TAB)

    def click_customers_tab(self) -> None:
        """
        Нажимает на табу Customers для перехода
        на страницу Customers.
        :return: None.
        """
        with allure.step('Навигация на вкладку Customers'):
            self.click_element(*CUSTOMERS_TAB)

    def check_page_changed_to_add_customer(self) -> None:
        """
        Проверяет, что страница изменилась на страницу Add Customer.
        :assert: Проверяет, что текущая страница соответствует
        ожидаемой ссылке страницы Add Customer.
        :return: None.
        """
        with allure.step(
                'Проверка, что осуществлен переход на страницу Add Customer'
        ):
            assert self.check_that_page_changed(ADD_CUST_URL),\
                "Не получилось перейти на страницу Add Customer"

    def check_page_changed_to_customer(self) -> None:
        """
        Проверяет, что страница изменилась на страницу Customers.
        :assert: Проверяет, что текущая страница соответствует
        ожидаемой ссылке страницы Customers.
        :return: None.
        """
        with allure.step(
                'Проверка, что осуществлен переход на страницу Customers'
        ):
            assert self.check_that_page_changed(CUSTOMERS_URL),\
                "Не получилось перейти на страницу Customers"
