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

    @property
    def user_login_field(self):
        return self.find_element(loc.user_login_field)

    def the_search_field_is_working(self):
        return self.find_element(loc.search_field).send_keys('а')

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

    def search_bar_iframe_is_displayed(self):
        return self.find_element(loc.search_bar).is_displayed()
