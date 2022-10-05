from ..pages.home_page import HomePage
import requests
from selenium.common.exceptions import NoSuchElementException
import allure
from allure_commons.types import AttachmentType


@allure.feature('Home page')
@allure.story('Open site')
def test_home_pape_open(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.home_page_url() == 'https://www.onliner.by/'
    assert home_page.home_page_title() == 'Onliner'


# @allure.feature('Home page')
# @allure.story('Open site')
# def test_home_page_title(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.home_page_title() == 'Onliner'


@allure.feature('Home page')
@allure.story('Navigation bar')
def test_navigation_bar_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.home_page_navigation_bar().is_displayed()


@allure.feature('Home page')
@allure.story('Logo site')
def test_logo_site_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.logo_onliner().is_displayed()


@allure.feature('Home page')
@allure.story('Search field')
def test_search_field_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.search_field().is_displayed()


@allure.feature('Home page')
@allure.story('User bar')
def test_user_bar_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.user_bar().is_displayed()


@allure.feature('Home page')
@allure.story('Project navigation flex')
def test_project_navigation_flex_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.project_navigation_flex().is_displayed()


@allure.feature('Home page')
@allure.story('Catalog button')
def test_catalog_button_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.catalog_button().text == 'Каталог'
    with allure.step('Catalog button click'):
        home_page.catalog_button().click()
    assert driver.current_url == 'https://catalog.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Catalog button')
# def test_catalog_open(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Catalog button click'):
#         home_page.catalog_button().click()
#     assert driver.current_url == 'https://catalog.onliner.by/'


@allure.feature('Home page')
@allure.story('News button')
def test_news_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.news_button().is_displayed()
    assert home_page.news_button().text == 'Новости'


# @allure.feature('Home page')
# @allure.story('News button')
# def test_news_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.news_button().text == 'Новости'


@allure.feature('Home page')
@allure.story('Car market button')
def test_car_market_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.car_market_button().is_displayed()
    assert home_page.car_market_button().text == 'Автобарахолка'
    with allure.step('Car market button click'):
        home_page.car_market_button().click()
    assert driver.current_url == 'https://ab.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Car market button')
# def test_car_market_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.car_market_button().text == 'Автобарахолка'


# @allure.feature('Home page')
# @allure.story('Car market button')
# def test_car_market_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Car market button click'):
#         home_page.car_market_button().click()
#     assert driver.current_url == 'https://ab.onliner.by/'


@allure.feature('Home page')
@allure.story('Houses and apartments button')
def test_houses_and_apartments_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.houses_and_apartments_button().is_displayed()
    assert home_page.houses_and_apartments_button().text == 'Дома и квартиры'
    with allure.step('Click Houses and apartments button'):
        home_page.houses_and_apartments_button().click()
    assert driver.current_url == 'https://r.onliner.by/pk/'


# @allure.feature('Home page')
# @allure.story('Houses and apartments button')
# def test_house_and_apartment_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.houses_and_apartments_button().text == 'Дома и квартиры'


# @allure.feature('Home page')
# @allure.story('Houses and apartments button')
# def test_house_and_apartment_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Click Houses and apartments button'):
#         home_page.houses_and_apartments_button().click()
#     assert driver.current_url == 'https://r.onliner.by/pk/'


@allure.feature('Home page')
@allure.story('Services button')
def test_services_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.services_button().is_displayed()
    assert home_page.services_button().text == 'Услуги'
    with allure.step('Click services button'):
        home_page.services_button().click()
    assert driver.current_url == 'https://s.onliner.by/tasks'


# @allure.feature('Home page')
# @allure.story('Services button')
# def test_services_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.services_button().text == 'Услуги'


# @allure.feature('Home page')
# @allure.story('Services button')
# def test_services_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Click services button'):
#         home_page.services_button().click()
#     assert driver.current_url == 'https://s.onliner.by/tasks'


@allure.feature('Home page')
@allure.story('Flea market button')
def test_flea_market_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.flea_market_button().is_displayed()
    assert home_page.flea_market_button().text == 'Барахолка'
    with allure.step('Flea market button click'):
        home_page.flea_market_button().click()
    assert driver.current_url == 'https://baraholka.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Flea market button')
# def test_flea_market_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.flea_market_button().text == 'Барахолка'


# @allure.feature('Home page')
# @allure.story('Flea market button')
# def test_flea_market_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Flea market button click'):
#         home_page.flea_market_button().click()
#     assert driver.current_url == 'https://baraholka.onliner.by/'


@allure.feature('Home page')
@allure.story('Forum button')
def test_forum_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.forum_button().is_displayed()
    assert home_page.forum_button().text == 'Форум'
    with allure.step('Forum button click'):
        home_page.forum_button().click()
    assert driver.current_url == 'https://forum.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Forum button')
# def test_forum_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.forum_button().text == 'Форум'


# @allure.feature('Home page')
# @allure.story('Forum button')
# def test_forum_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Forum button click'):
#         home_page.forum_button().click()
#     assert driver.current_url == 'https://forum.onliner.by/'


@allure.feature('Home page')
@allure.story('Credit card button')
def test_making_a_credit_card_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.making_a_credit_card().is_displayed()
    assert home_page.making_a_credit_card().text == 'Onlíner Клевер'
    with allure.step('Credit card click'):
        home_page.making_a_credit_card().click()
    with allure.step('Switch windows'):
        driver.switch_to.window(driver.window_handles[1])
    assert driver.title == 'Onliner Клевер – 5% возврата на всё в Каталоге'
    with allure.step('Close second windows'):
        driver.close()
    with allure.step('Switch to first windows'):
        driver.switch_to.window(driver.window_handles[0])


# @allure.feature('Home page')
# @allure.story('Credit card button')
# def test_making_a_credit_card_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.making_a_credit_card().text == 'Onlíner Клевер'


# @allure.feature('Home page')
# @allure.story('Credit card button')
# def test_making_a_credit_card_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Credit card click'):
#         home_page.making_a_credit_card().click()
#     with allure.step('Switch windows'):
#         driver.switch_to.window(driver.window_handles[1])
#     assert driver.title == 'Onliner Клевер – 5% возврата на всё в Каталоге'
#     with allure.step('Close second windows'):
#         driver.close()
#     with allure.step('Switch to first windows'):
#         driver.switch_to.window(driver.window_handles[0])


@allure.feature('Home page')
@allure.story('Currency exchange')
def test_currency_exchange_rate_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.currency_exchange_rate().is_displayed()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate().click()
    assert driver.current_url == 'https://kurs.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Currency exchange')
# def test_currency_exchange_rate_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Open currency exchange page'):
#         home_page.currency_exchange_rate().click()
#     assert driver.current_url == 'https://kurs.onliner.by/'


@allure.feature('Home page')
@allure.story('Currency exchange')
def test_currency_exchange_rate_displayed_correctly(domain, driver):
    with allure.step('getting the national bank rate'):
        response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
        dollar_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    exchange_rate = home_page.currency_exchange_rate().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    str_exchange_rate = str_exchange_rate.replace('$', '')
    str_exchange_rate = float(str_exchange_rate)
    assert str_exchange_rate == dollar_exchange_rate


@allure.feature('Home page')
@allure.story('Weather link')
def test_weather_link_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.weather_link().is_displayed()
    with allure.step('Weather link click'):
        home_page.weather_link().click()
    assert driver.current_url == 'https://pogoda.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Weather link')
# def test_weather_link_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Weather link click'):
#         home_page.weather_link().click()
#     assert driver.current_url == 'https://pogoda.onliner.by/'


@allure.feature('Home page')
@allure.story('Age restriction')
def test_age_restriction_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.age_restriction().is_displayed()
    assert home_page.age_restriction().text == '18+'


# @allure.feature('Home page')
# @allure.story('Age restriction')
# def test_age_restriction_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.age_restriction().text == '18+'


@allure.feature('Home page')
@allure.story('Shopping cart')
def test_shopping_cart_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.shopping_cart().is_displayed()
    with allure.step('Shopping cart click'):
        home_page.shopping_cart().click()
    assert driver.current_url == 'https://cart.onliner.by/'


# @allure.feature('Home page')
# @allure.story('Shopping cart')
# def test_shopping_cart_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Shopping cart click'):
#         home_page.shopping_cart().click()
#     assert driver.current_url == 'https://cart.onliner.by/'


@allure.feature('Home page')
@allure.story('Google account link')
def test_google_account_link_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.google_account_link().is_displayed()
    with allure.step('Google account link click'):
        home_page.google_account_link_click()
        driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=google'


# @allure.feature('Home page')
# @allure.story('Google account link')
# def test_google_account_link_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Google account link click'):
#         home_page.google_account_link_click()
#         driver.switch_to.window(driver.window_handles[1])
#     assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=google'


@allure.feature('Home page')
@allure.story('Vk account link')
def test_vk_account_link_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.vk_account_link().is_displayed()
    with allure.step('Vk account link click'):
        home_page.vk_account_link_click()
        driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=vkontakte'


# @allure.feature('Home page')
# @allure.story('Vk account link')
# def test_vk_account_link_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Vk account link click'):
#         home_page.vk_account_link_click()
#         driver.switch_to.window(driver.window_handles[1])
#     assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=vkontakte'


@allure.feature('Home page')
@allure.story('Facebook account link')
def test_facebook_account_link_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.facebook_account_link().is_displayed()
    with allure.step('Facebook account link click'):
        home_page.facebook_account_link_click()
        driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=facebook'


# @allure.feature('Home page')
# @allure.story('Facebook account link')
# def test_facebook_account_link_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Facebook account link click'):
#         home_page.facebook_account_link_click()
#         driver.switch_to.window(driver.window_handles[1])
#     assert driver.current_url == 'https://gc.onliner.by/views/social-auth.html?socialType=facebook'


@allure.feature('Home page')
@allure.story('User login button')
def test_user_login_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.user_login_button().is_displayed()
    assert home_page.user_login_button().text == 'Вход'
    with allure.step('User login button click'):
        home_page.user_login_button().click()
    assert home_page.user_login_field().is_displayed()


# @allure.feature('Home page')
# @allure.story('User login button')
# def test_user_login_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     assert home_page.user_login_button().text == 'Вход'


# @allure.feature('Home page')
# @allure.story('User login button')
# def test_user_login_button_click(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('User login button click'):
#         home_page.user_login_button().click()
#     assert home_page.user_login_field().is_displayed()


@allure.feature('Home page')
@allure.story('The search field')
def test_the_search_field_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('The search field is working'):
        home_page.the_search_field_is_working()
        iframe = home_page.iframe_search_field()
        driver.switch_to.frame(iframe)
    assert home_page.search_bar_iframe().is_displayed()
    with allure.step('The search field is working'):
        home_page.the_search_field_is_working()
        iframe = home_page.iframe_search_field()
        driver.switch_to.frame(iframe)
        allure.attach(
            driver.get_screenshot_as_png(),
            name='screenshot search result',
            attachment_type=AttachmentType.PNG
        )
    assert len(home_page.search_result()) > 1
    with allure.step('Close search field'):
        home_page.search_field_close().click()
        try:
            home_page.search_page().is_displayed()
        except NoSuchElementException:
            return True


# @allure.feature('Home page')
# @allure.story('The search field')
# def test_the_search_field_is_working(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('The search field is working'):
#         home_page.the_search_field_is_working()
#         iframe = home_page.iframe_search_field()
#         driver.switch_to.frame(iframe)
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name='screenshot search result',
#             attachment_type=AttachmentType.PNG
#         )
#     assert len(home_page.search_result()) > 1


# @allure.feature('Home page')
# @allure.story('The search field')
# def test_search_field_close(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Open search field'):
#         home_page.the_search_field_is_working()
#         iframe = home_page.iframe_search_field()
#         driver.switch_to.frame(iframe)
#     with allure.step('Close search field'):
#         home_page.search_field_close().click()
#         try:
#             home_page.search_page().is_displayed()
#         except NoSuchElementException:
#             return True
