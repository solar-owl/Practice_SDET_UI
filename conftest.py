"""
Модуль содержит фикстуры для проекта.
Фикстуры описывают пред- и постусловия, которые необходимы для выполнения тестов.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from data.generate_test_data import GENERAL_URL, CUSTOMERS_URL
from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage
from pages.GeneralPage import GeneralPage


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request) -> None:
    """
    Фикстура для создания веб-драйвера.
    :param request: Объект запроса фикстуры.
    :return: None
    """
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.page_load_strategy = 'eager'
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging']
        )
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.page_load_strategy = 'eager'
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(3)
    driver.set_window_size(1920, 1080)
    driver.get(GENERAL_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def general_page(driver) -> GeneralPage:
    """
    Фикстура для создания экземпляра основной страницы.
    :param driver: Веб-драйвер.
    :return: Объект основной страницы.
    """
    return GeneralPage(driver)


@pytest.fixture(scope="function")
def add_customer_page(driver) -> AddCustomerPage:
    """
    Фикстура для создания экземпляра страницы Add Customer.
    :param driver: Веб-драйвер.
    :return: Объект страницы Add Customer.
    """
    return AddCustomerPage(driver)


@pytest.fixture(scope="function")
def customers_page(driver) -> CustomersPage:
    """
    Фикстура для создания экземпляра страницы Customers.
    :param driver: Веб-драйвер.
    :return: Объект страницы Customers.
    """
    return CustomersPage(driver)

@pytest.fixture(scope="function")
def cleanup_names(customers_page) -> None:
    """
    Фикстура для очистки созданных данных.
    :param customers_page: Объект страницы Customers.
    :return: None
    """
    names_to_cleanup = []
    yield names_to_cleanup
    customers_page.move_to_url(CUSTOMERS_URL)
    customers_page.delete_multiple_by_name(names_to_cleanup)
