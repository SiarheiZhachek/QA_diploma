from ..pages.home_page import HomePage
import requests
from selenium.common.exceptions import NoSuchElementException


def test_home_pape_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.home_page_url() == 'https://www.onliner.by/'


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.home_page_title() == 'Onliner'


def test_navigation_bar_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.home_page_navigation_bar().is_displayed()


def test_logo_site_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.logo_onliner().is_displayed()


def test_search_field_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.search_field().is_displayed()


def test_user_bar_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.user_bar().is_displayed()


def test_project_navigation_flex_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.project_navigation_flex().is_displayed()


def test_catalog_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.catalog_button().text == 'Каталог'


def test_catalog_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.catalog_button().click()
    assert driver.current_url == 'https://catalog.onliner.by/'


def test_news_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.news_button().is_displayed()


def test_news_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.news_button().text == 'Новости'


def test_car_market_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.car_market_button().is_displayed()


def test_car_market_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.car_market_button().text == 'Автобарахолка'


def test_car_market_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.car_market_button().click()
    assert driver.current_url == 'https://ab.onliner.by/'


def test_houses_and_apartments_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.houses_and_apartments_button().is_displayed()


def test_house_and_apartment_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.houses_and_apartments_button().text == 'Дома и квартиры'


def test_house_and_apartment_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert driver.current_url == 'https://r.onliner.by/pk/'


def test_services_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.services_button().is_displayed()


def test_services_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.services_button().text == 'Услуги'


def test_services_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert driver.current_url == 'https://s.onliner.by/tasks'


def test_flea_market_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.flea_market_button().is_displayed()


def test_flea_market_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.flea_market_button().text == 'Барахолка'


def test_flea_market_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.flea_market_button().click()
    assert driver.current_url == 'https://baraholka.onliner.by/'


def test_forum_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.forum_button().is_displayed()


def test_forum_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.forum_button().text == 'Форум'


def test_forum_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.forum_button().click()
    assert driver.current_url == 'https://forum.onliner.by/'


def test_making_a_credit_card_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.making_a_credit_card().is_displayed()


def test_making_a_credit_card_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.making_a_credit_card().text == 'Onlíner Клевер'


def test_making_a_credit_card_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.making_a_credit_card().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.title == 'Onliner Клевер – 5% возврата на всё в Каталоге'
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def test_currency_exchange_rate_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.currency_exchange_rate().is_displayed()


def test_currency_exchange_rate_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    assert driver.current_url == 'https://kurs.onliner.by/'


def test_currency_exchange_rate_displayed_correctly(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
    dollar_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    exchange_rate = home_page.currency_exchange_rate().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    assert str_exchange_rate == f'$ {dollar_exchange_rate}'


def test_weather_link_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.weather_link().is_displayed()


def test_weather_link_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.weather_link().click()
    assert driver.current_url == 'https://pogoda.onliner.by/'


def test_age_restriction_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.age_restriction().is_displayed()


def test_age_restriction_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.age_restriction().text == '18+'


def test_shopping_cart_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.shopping_cart().is_displayed()


def test_shopping_cart_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.shopping_cart().click()
    assert driver.current_url == 'https://cart.onliner.by/'


def test_google_account_link_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.google_account_link().is_displayed()


def test_google_account_link_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.google_account_link_click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=google'


def test_vk_account_link_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.vk_account_link().is_displayed()


def test_vk_account_link_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.vk_account_link_click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=vkontakte'


def test_facebook_account_link_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.facebook_account_link().is_displayed()


def test_facebook_account_link_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.facebook_account_link_click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=facebook'


def test_user_login_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.user_login_button().is_displayed()


def test_user_login_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.user_login_button().text == 'Вход'


def test_user_login_button_click(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.user_login_button().click()
    assert home_page.user_login_field().is_displayed()


def test_the_search_field_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.the_search_field_is_working()
    iframe = home_page.iframe_search_field()
    driver.switch_to.frame(iframe)
    assert home_page.search_bar_iframe().is_displayed()


def test_the_search_field_is_working(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.the_search_field_is_working()
    iframe = home_page.iframe_search_field()
    driver.switch_to.frame(iframe)
    assert len(home_page.search_result()) > 1


def test_search_field_close(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.the_search_field_is_working()
    iframe = home_page.iframe_search_field()
    driver.switch_to.frame(iframe)
    home_page.search_field_close().click()
    try:
        home_page.search_page().is_displayed()
    except NoSuchElementException:
        return True
