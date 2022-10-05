from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings


def int_value_from_ru_month(date_str):
    month = settings.RU_MONTH_VALUES
    for key, value in month.items():
        date_str = date_str.replace(key, str(value))
    return date_str


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.domain = settings.DOMAIN
        # self.domain_nbrb = settings.domain_nbrb

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
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
