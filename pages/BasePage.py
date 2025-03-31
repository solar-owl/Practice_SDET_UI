"""
Модуль для работы с веб-элементами.

Содержит класс и функции для работы с веб-элементами.
"""
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Класс для работы с веб-элементами.
    """
    def __init__(self, driver, timeout=10):
        """
        Инициализирует экземпляр класса BasePage.
        :param driver: Драйвер браузера
        :param timeout: Время ожидания в секундах. По умолчанию 10 секунд.
        """
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(self.driver, timeout)

    def search_element(self, by: By or int, value: str) -> WebElement:
        """
        Ищет элемент с ожиданием его видимости.
        :param by: Тип локатора.
        :param value: Значение локатора.
        :return: Элемент.
        """
        return self.wait.until(
            expected_conditions.visibility_of_element_located((by, value)),
            message=f'Элемент c локатором {by} и значением {value} не найден')

    def search_elements(self, by: By or int, value: str) -> [WebElement]:
        """
        Ищет элементы с ожиданием его видимости.
        :param by: Тип локатора.
        :param value: Значение локатора.
        :return: Элементы.
        """
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located((by, value)),
            message=f'Элементы c локатором {by} и значением {value} не найдены')

    def click_element(self, by: By or int, value: str) -> None:
        """
        Находит элемент и кликает по нему.
        :param by: Тип локатора.
        :param value: Значение локатора.
        """
        self.search_element(by, value).click()

    def assert_that_present(self, by: By or int, value: str) -> bool:
        """
        Проверяет, что элемент присутствует на странице.
        :param by: Тип локатора.
        :param value: Значение локатора.
        :return: True, если элемент найден на странице, False в противном случае.
        """
        return isinstance(self.search_element(by, value), WebElement)

    def fill_value(self, by: By or int, value: str, input_value: str) -> None:
        """
        Вставляет значение в поле на странице.
        :param by: Тип локатора.
        :param value: Значение локатора.
        :param input_value: Значение, которое нужно вставить в поле.
        """
        self.search_element(by, value).send_keys(input_value)

    def get_alert(self) -> Alert:
        """
        Переключает фокус на алерт.
        :return: Объект алерта.
        """
        return self.driver.switch_to.alert

    def check_that_page_changed(self, url: str) -> bool:
        """
        Проверка, что страница изменила.
        :param url: Ожидаемая ссылка.
        :return: True, если страница соответствует ожидаемой,
        False в противном случае.
        """
        return self.wait.until(expected_conditions.url_to_be(url),
                               message=f'Ошибка загрузка страницы {url}')

    def move_to_url(self, url: str) -> None:
        """
        Переходит на страницу по ссылке.
        :param url: Ссылка на страницу.
        :return: None
        """
        self.driver.get(url)
