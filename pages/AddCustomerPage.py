"""
Модуль для работы со страницей Add Customer.

Содержит класс и функции для работы со страницей Add Customer.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import allure
from pages.BasePage import BasePage

FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
POST_CODE_INPUT = (By.XPATH, "//input[@placeholder='Post Code']")
ADD_CUSTOMER_BTN = (By.XPATH, '//button[text()="Add Customer"]')


class AddCustomerPage(BasePage):
    """
    Класс для работы со страницей Add Customer.
    """

    def fill_first_name(self, first_name: str) -> None:
        """
        Вставляет имя в поле First Name.
        :param first_name: Имя.
        :return: None.
        """
        with allure.step('Ввод имени в поле First Name'):
            self.fill_value(*FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name: str) -> None:
        """
        Вставляет фамилию в поле Last Name.
        :param last_name: Фамилия.
        :return: None.
        """
        with allure.step('Ввод фамилии в поле Last Name'):
            self.fill_value(*LAST_NAME_INPUT, last_name)

    def fill_post_code(self, post_code: str) -> None:
        """
        Вставляет номер в поле Post Code.
        :param post_code: Номер.
        :return: None.
        """
        with allure.step('Ввод номера в поле Post Code'):
            self.fill_value(*POST_CODE_INPUT, post_code)

    def click_add_customer_btn(self) -> None:
        """
        Нажимает на кнопку Add Customer.
        :return: None.
        """
        with allure.step('Нажатие на кнопку Add Customer'):
            self.click_element(*ADD_CUSTOMER_BTN)

    def get_text_alert(self) -> str:
        """
        Получает текст из алерта.
        :return: Текст алерта.
        """
        self.wait.until(
            expected_conditions.alert_is_present(),
            message='Алерт не найден'
        )
        alert = self.get_alert()
        text = alert.text.split(" :")[0]
        alert.accept()
        return text
