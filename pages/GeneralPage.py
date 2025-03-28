import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

ADD_CUSTOMER_TAB = (By.XPATH, '//button[contains(text(), "Add Customer") and ./b[@id="notch"]]')
CUSTOMERS_TAB = (By.XPATH, '//button[contains(text(), "Customers") and ./b[@id="notch"]]')
class GeneralPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_customer_tab(self):
        with allure.step('Навигация на вкладку Add Customer'):
            self.click_element(*ADD_CUSTOMER_TAB)

    def click_customers_tab(self):
        with allure.step('Навигация на вкладку Customers'):
            self.click_element(*CUSTOMERS_TAB)