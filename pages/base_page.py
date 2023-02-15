from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import settings
import requests


def int_value_from_ru_month(date_str):
    month = settings.RU_MONTH_VALUES
    for key, value in month.items():
        date_str = date_str.replace(key, str(value))
    return date_str


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.domain = settings.DOMAIN
        self.domain_nbrb = settings.DOMAIN_NBRB

    def find_element(self, *args):
        element, value = args[0]
        return self.driver.find_element(element, value)

    def find_elements(self, *args):
        element, value = args[0]
        return self.driver.find_elements(element, value)

    def move_to_element(self, element):
        return ActionChains(self.driver).move_to_element(element)

    def down_control(self, element):
        return ActionChains(self.driver).key_down(
            Keys.CONTROL
        ).click(element).key_up(
            Keys.CONTROL
        ).perform()

    def select(self, *args):
        element, value = args[0]
        return Select(self.driver.find_element(element, value))

    def driver_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def get_api_nbrb_usd_method(self):
        response = requests.request(
            'GET', f'{self.domain_nbrb}api/exrates/rates/431'
        ).json()
        dollar_exchange_rate = response['Cur_OfficialRate']
        return dollar_exchange_rate

    def get_api_nbrb_eur_method(self):
        response = requests.request(
            'GET', f'{self.domain_nbrb}api/exrates/rates/EUR?parammode=2'
        ).json()
        euro_exchange_rate = response['Cur_OfficialRate']
        return euro_exchange_rate

    def get_api_nbrb_rus_rub(self):
        response = requests.request(
            'GET', f'{self.domain_nbrb}api/exrates/rates/RUB?parammode=2'
        ).json()
        rub_exchange_rate = response['Cur_OfficialRate']
        return rub_exchange_rate
