from pages.base_page import BasePage
from pages.locators import home_page_locators as loc


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

    @property
    def user_login_field(self):
        return self.find_element(loc.user_login_field)

    def the_search_field_is_working(self):
        return self.search_field.send_keys('a')

    def search_bar_iframe_is_displayed(self):
        return self.search_bar_iframe.is_displayed()

    def info_title_a_credit_card_is_displayed(self):
        return self.find_element(loc.info_title_a_credit_card).is_displayed()
