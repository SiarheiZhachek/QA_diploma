import pytest
from selenium import webdriver

domain_nbrb = 'https://www.nbrb.by/'


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def domain():
    yield domain_nbrb

