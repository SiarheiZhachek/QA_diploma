from .base_page import BasePage
from ..pages.locators import home_psge_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(f'{self.domain}')

    def home_page_url(self):
        return self.driver.current_url

    def home_page_title(self):
        return self.driver.title

    def home_page_navigation_bar(self):
        return self.find_element(loc.navigation_bar)

    def logo_onliner(self):
        return self.find_element(loc.logo)

    def search_field(self):
        return self.find_element(loc.search_field)

    def user_bar(self):
        return self.find_element(loc.user_bar)

    def project_navigation_flex(self):
        return self.find_element(loc.project_navigation_flex)

    def catalog_button(self):
        return self.find_element(loc.catalog_button)

    def news_button(self):
        return self.find_element(loc.news_button)

    def car_market_button(self):
        return self.find_element(loc.car_market_button)

    def houses_and_apartments_button(self):
        return self.find_element(loc.houses_and_apartments_button)

    def services_button(self):
        return self.find_element(loc.services_button)

    def flea_market_button(self):
        return self.find_element(loc.flea_market_button)

    def forum_button(self):
        return self.find_element(loc.forum_button)

    def making_a_credit_card(self):
        return self.find_element(loc.credit_card_button)

    def currency_exchange_rate(self):
        return self.find_element(loc.currency_exchange_rate_link)

    def weather_link(self):
        return self.find_element(loc.weather)

    def age_restriction(self):
        return self.find_element(loc.age_restriction)

    def shopping_cart(self):
        return self.find_element(loc.cart)

    def google_account_link(self):
        return self.find_element(loc.google_account_link)

    def google_account_link_click(self):
        element = self.find_element(loc.google_account_link)
        return self.down_control(element)

    def vk_account_link(self):
        return self.find_element(loc.vk_account_link)

    def vk_account_link_click(self):
        element = self.find_element(loc.vk_account_link)
        return self.down_control(element)

    def facebook_account_link(self):
        return self.find_element(loc.facebook_account_link)

    def facebook_account_link_click(self):
        element = self.find_element(loc.facebook_account_link)
        return self.down_control(element)

    def user_login_button(self):
        return self.find_element(loc.user_login_button)

    def user_login_field(self):
        return self.find_element(loc.user_login_field)

    def the_search_field_is_working(self):
        return self.find_element(loc.search_field).send_keys('а')

    def iframe_search_field(self):
        return self.find_element(loc.iframe_search_field)

    def search_page(self):
        return self.find_element(loc.search_page)

    def search_result(self):
        return self.find_elements(loc.search_result)

    def search_field_close(self):
        return self.find_element(loc.search_field_close)

    def search_bar_iframe(self):
        return self.find_element(loc.search_bar)
