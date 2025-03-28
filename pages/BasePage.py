from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(self.driver, timeout)


    def find_element(self, by: By or int, value: str)-> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент c локатором {by} и значением {value} не найден')


    def find_elements(self,  by: By or int, value: str)-> [WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы c локатором {by} и значением {value} не найдены')

    def click_element(self, by: By or int, value: str):
        self.find_element(by, value).click()

    def assert_that_present(self, by: By or int, value: str) -> bool:
        return type(self.find_element(by, value)) == WebElement
