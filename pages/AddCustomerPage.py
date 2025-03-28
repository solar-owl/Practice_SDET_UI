import allure
from selenium.webdriver.support import expected_conditions

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
POST_CODE_INPUT = (By.XPATH, "//label[contains(text(), \"Post Code\")]/following-sibling::input")
ADD_CUSTOMER_BTN = (By.XPATH, '//button[text()="Add Customer"]')


class AddCustomerPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def fill_first_name(self, first_name: str):
        with allure.step('Ввод имени в поле First Name'):
            self.find_element(*FIRST_NAME_INPUT).send_keys(first_name)

    def fill_last_name(self, last_name: str):
        with allure.step('Ввод фамилии в поле Last Name'):
            self.find_element(*LAST_NAME_INPUT).send_keys(last_name)

    def fill_post_code(self, postCode: str):
        with allure.step('Ввод номера в поле Post Code'):
            self.find_element(*POST_CODE_INPUT).send_keys(postCode)

    def click_add_customer_btn(self):
        with allure.step('Нажатие на кнопку Add Customer'):
            self.click_element(*ADD_CUSTOMER_BTN)

    def get_text_alert(self):
        self.wait.until(expected_conditions.alert_is_present(),
                   message=f'Алерт не найден')
        alert = self.driver.switch_to.alert
        text = alert.text.split(" :")[0]
        alert.accept()
        return text