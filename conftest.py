import pytest
from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage
from pages.GeneralPage import GeneralPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.page_load_strategy = 'eager'
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.page_load_strategy = 'eager'
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    #  Перейдем по ссылке https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def general_page(driver):
    return GeneralPage(driver)

@pytest.fixture(scope="function")
def add_customer_page(driver):
    return AddCustomerPage(driver)

@pytest.fixture(scope="function")
def customers_page(driver):
    return CustomersPage(driver)
