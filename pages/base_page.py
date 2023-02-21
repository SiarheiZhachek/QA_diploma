from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import base_page_locators as loc
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

    @property
    def home_page_navigation_bar(self):
        return self.find_element(loc.navigation_bar)

    @property
    def logo_onliner(self):
        return self.find_element(loc.logo)

    @property
    def search_field(self):
        return self.find_element(loc.search_field)

    @property
    def user_bar(self):
        return self.find_element(loc.user_bar)

    @property
    def project_navigation_flex(self):
        return self.find_element(loc.project_navigation_flex)

    @property
    def catalog_button(self):
        return self.find_elements(loc.main_navigator_button)[0]

    @property
    def news_button(self):
        return self.find_elements(loc.main_navigator_button)[1]

    @property
    def car_market_button(self):
        return self.find_elements(loc.main_navigator_button)[2]

    @property
    def houses_and_apartments_button(self):
        return self.find_elements(loc.main_navigator_button)[3]

    @property
    def services_button(self):
        return self.find_elements(loc.main_navigator_button)[4]

    @property
    def flea_market_button(self):
        return self.find_elements(loc.main_navigator_button)[5]

    @property
    def forum_button(self):
        return self.find_elements(loc.main_navigator_button)[6]

    @property
    def making_a_credit_card(self):
        return self.find_element(loc.credit_card_button)

    @property
    def currency_exchange_rate(self):
        return self.find_element(loc.currency_exchange_rate_link)

    def currency_exchange_rate_click(self):
        return self.driver_wait(loc.currency_exchange_rate_link, time=5).click()

    @property
    def weather_link(self):
        return self.find_element(loc.weather)

    @property
    def age_restriction(self):
        return self.find_element(loc.age_restriction)

    @property
    def iframe_search_field(self):
        return self.find_element(loc.iframe_search_field)

    @property
    def search_page(self):
        return self.find_element(loc.search_page)

    @property
    def search_result(self):
        return self.find_elements(loc.search_result)

    def search_field_close(self):
        return self.find_element(loc.search_field_close).click()

    @property
    def search_bar_iframe(self):
        return self.find_element(loc.search_bar)

    @property
    def shopping_cart(self):
        return self.find_element(loc.cart)

    @property
    def google_account_link(self):
        return self.find_element(loc.google_account_link)

    def google_account_link_click(self):
        element = self.find_element(loc.google_account_link)
        return self.down_control(element)

    @property
    def vk_account_link(self):
        return self.find_element(loc.vk_account_link)

    def vk_account_link_click(self):
        element = self.find_element(loc.vk_account_link)
        return self.down_control(element)

    @property
    def facebook_account_link(self):
        return self.find_element(loc.facebook_account_link)

    def facebook_account_link_click(self):
        element = self.find_element(loc.facebook_account_link)
        return self.down_control(element)

    @property
    def user_login_button(self):
        return self.find_element(loc.user_login_button)
