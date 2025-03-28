import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

TITLE_FIRST_NAME = (By.XPATH, "//a[contains(text(), \"First Name\")]")
LIST_FIRST_NAMES = (By.XPATH, "//tr[contains(@ng-repeat, \"cust in Customers\")]/td[1]")
DELETE_BUTTON_BY_NAME = (By.XPATH, '//td[contains(text(), "{}")]/following-sibling::td/button')
FIRST_NAME = (By.XPATH, '//td[contains(text(), "{}")]')

class CustomersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sort_by_first_name(self):
        self.find_element(*TITLE_FIRST_NAME).click()

    def get_list_of_first_names(self):
        first_names_values = []
        elements = self.find_elements(*LIST_FIRST_NAMES)
        for row in elements:
            first_names_values.append(row.text)
        with allure.step('Получение имен из таблицы Customers'):
            return first_names_values

    def delete_row_by_name(self, name: str):
        locator = (By.XPATH, DELETE_BUTTON_BY_NAME[1].format(name))
        self.click_element(*locator)

    def delete_multiple_by_name(self, names):
        for name in names:
            with allure.step(f'Удаление клиента по имени {name}'):
                self.delete_row_by_name(name)

    def customer_is_present(self, name: str):
        locator = (By.XPATH, FIRST_NAME[1].format(name))
        return self.assert_that_present(*locator)