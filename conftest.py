import pytest
import allure
from selenium import webdriver
import settings


@pytest.fixture(scope='function')
def driver(browser_options):
    if browser_options == 'firefox':
        with allure.step('Run Firefox browser'):
            driver_browser = webdriver.Firefox()
    else:
        with allure.step('Run Chrome browser'):
            driver_browser = webdriver.Chrome()
    driver_browser.maximize_window()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Specify the browser value, by default chrome'
    )


@pytest.fixture(scope='session')
def browser_options(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def domain():
    yield settings.DOMAIN_NBRB
