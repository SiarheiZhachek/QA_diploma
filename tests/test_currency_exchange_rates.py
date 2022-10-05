from datetime import datetime
import pytest
import allure
import requests
from pages.home_page import HomePage
from pages.currency_exchange_rates_page import CurrencyExchange


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_currency_convertor_panel_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_convertor_panel().is_displayed()
    assert currency_exchange.currency_convertor_panel_text().text == (
        'Конвертер валют по лучшим курсам'
    )


# @allure.feature('Currency exchange page')
# @allure.story('Currency convertor panel')
# def test_currency_convertor_panel_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Open currency exchange page'):
#         home_page.currency_exchange_rate_click()
#         currency_exchange = CurrencyExchange(driver)
#     assert currency_exchange.currency_convertor_panel_text().text ==
#     'Конвертер валют по лучшим курсам'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_to_sell_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.to_sell_button().is_displayed()
    assert currency_exchange.to_sell_button().text == 'Продать'


# @allure.feature('Currency exchange page')
# @allure.story('Currency convertor panel')
# def test_to_sell_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Open currency exchange page'):
#         home_page.currency_exchange_rate_click()
#         currency_exchange = CurrencyExchange(driver)
#     assert currency_exchange.to_sell_button().text == 'Продать'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_buy_button_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.buy_button().is_displayed()
    assert currency_exchange.buy_button().text == 'Купить'


# @allure.feature('Currency exchange page')
# @allure.story('Currency convertor panel')
# def test_buy_button_text(driver):
#     with allure.step('Open home page'):
#         home_page = HomePage(driver)
#         home_page.open()
#     with allure.step('Open currency exchange page'):
#         home_page.currency_exchange_rate_click()
#         currency_exchange = CurrencyExchange(driver)
#     assert currency_exchange.buy_button().text == 'Купить'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_buy_button_selected(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Buy button click'):
        currency_exchange.buy_button().click()
    assert currency_exchange.buy_button().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_to_sell_button_selected(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('To_sell button click'):
        currency_exchange.buy_button().click()
        currency_exchange.to_sell_button().click()
    assert currency_exchange.to_sell_button().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_amount_input_field_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.amount_input_field().is_displayed()

#

@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_type_of_input_currency_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.type_of_input_currency().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_euro(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected eur in currency convertor panel'):
        currency_exchange.selected_eur()
    assert currency_exchange.type_of_input_currency_select_eur().is_selected()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    assert currency_exchange.type_of_input_currency_select_rub().is_selected()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_byn(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected byn in currency convertor panel'):
        currency_exchange.selected_byn()
    assert currency_exchange.type_of_input_currency_select_byn().is_selected()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_usd(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected byn in currency convertor panel'):
        currency_exchange.selected_byn()
    with allure.step('Selected usd in currency convertor panel'):
        currency_exchange.selected_usd()
    assert currency_exchange.type_of_input_currency_select_usd().is_selected()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_out_eur(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out eur in currency convertor panel'):
        currency_exchange.type_currency_out().click()
        currency_exchange.selected_out_eur()
    assert currency_exchange.money_logo().text == '€'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_out_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out rub in currency convertor panel'):
        currency_exchange.selected_out_rub()
    assert currency_exchange.money_logo().text == 'RUB'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_out_byn(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out byn in currency convertor panel'):
        currency_exchange.selected_out_byn()
    assert currency_exchange.money_logo().text == 'BYN'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_select_out_usd(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Selected out usd in currency convertor panel'):
        currency_exchange.selected_out_usd()
    assert currency_exchange.money_logo().text == '$'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_nbrb_usd_exchange_rate_convertor_panel(domain, driver):
    with allure.step("getting the National Bank's API of the usd exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
        dollar_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    exchange_rate = currency_exchange.exchange_rate_nbrb().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    assert float(str_exchange_rate) == dollar_exchange_rate


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_nbrb_eur_exchange_rate_convertor_panel(domain, driver):
    with allure.step("getting the National Bank's API of the eur exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
        euro_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected usd in currency convertor panel'):
        currency_exchange.selected_eur()
    exchange_rate = currency_exchange.exchange_rate_nbrb().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    assert str_exchange_rate == f'{euro_exchange_rate}'


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99900000000])
def test_correct_exchange_rate_calculation_nbrb_usd_convertor_panel(domain, the_amount, driver):
    with allure.step("getting the National Bank's API of the usd exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
        dollar_exchange_rate = response['Cur_OfficialRate']
        correct_result = the_amount * dollar_exchange_rate
        result = float(f'{correct_result:.2f}')
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.exchange_rate_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99900000000])
def test_correct_exchange_rate_calculation_nbrb_eur_convertor_panel(domain, the_amount, driver):
    with allure.step("Getting the National Bank's API of the eur exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
        euro_exchange_rate = response['Cur_OfficialRate']
        correct_result = euro_exchange_rate * the_amount
        result = float(f'{correct_result:.2f}')
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Selected usd in currency convertor panel'):
        currency_exchange.selected_eur()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.exchange_rate_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99900000000])
def test_correct_exchange_rate_calculation_nbrb_rub_convertor_panel(domain, the_amount, driver):
    with allure.step("getting the National Bank's API of the rub exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/RUB?parammode=2').json()
        rub_exchange_rate = response['Cur_OfficialRate']
        correct_result = (the_amount * rub_exchange_rate) / 100
        result = float(f'{correct_result:.2f}')
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.exchange_rate_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_exchange_rate_nbrb_text_convertor_panel(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.exchange_rate_nbrb_text().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_the_best_exchange_rate_in_the_convertor_panel(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_best_exchange_rate_in_the_converter().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_usd_byn_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_buy_one_usd().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = course * the_amount
        result = float(f'{result:.3f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_eur_byn_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected eur in currency convertor panel'):
        currency_exchange.selected_eur()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_buy_one_eur().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = course * the_amount
        result = float(f'{result:.3f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [100, 100000, 99999999999])
def test_exchange_rate_calculation_rub_byn_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_buy_one_hundred_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        course = float(f'{course:.3f}')
        result = (the_amount / 100) * course
        result = float(f'{result:.3f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_usd_byn_by_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click the by button'):
        currency_exchange.buy_button().click()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_one_usd().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount * course
        result = float(f'{result:.3f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_eur_byn_by_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click the by button'):
        currency_exchange.buy_button().click()
    with allure.step('Selected eur in currency convertor panel'):
        currency_exchange.selected_eur()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_one_eur().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount * course
        result = float(f'{result:.3f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [100, 100000, 99999999999])
def test_exchange_rate_calculation_rub_byn_by_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click the by button'):
        currency_exchange.buy_button().click()
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_one_hundred_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = (the_amount * course) / 100
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_usd_eur_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out eur in currency convertor panel'):
        currency_exchange.selected_out_eur()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_eur_usd().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount / course
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_usd_rub_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected out rub in currency convertor panel'):
        currency_exchange.selected_out_rub()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.the_best_exchange_rate().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount * course
        result = float(f'{result:.2f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
        course_site = float(f'{course_site:.2f}')
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_eur_usd_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected eur in currency convertor panel'):
        currency_exchange.selected_eur()
    with allure.step('Selected out usd in currency convertor panel'):
        currency_exchange.selected_out_usd()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_buy_eur_usd().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount * course
        result = float(f'{result:.2f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
        course_site = float(f'{course_site:.2f}')
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_eur_rub_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected eur in currency convertor panel'):
        currency_exchange.selected_eur()
    with allure.step('Selected out rub in currency convertor panel'):
        currency_exchange.selected_out_rub()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_buy_eur_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount * course
        result = float(f'{result:.2f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
        course_site = float(f'{course_site:.2f}')
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [100, 100000, 99999999999])
def test_exchange_rate_calculation_rub_usd_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Selected out usd in currency convertor panel'):
        currency_exchange.selected_out_usd()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_usd_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course_rub = float(course)
        result = the_amount / course_rub
        result = float(f'{result:.2f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
        course_site = float(f'{course_site:.2f}')
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_byn_usd_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected byn in currency convertor panel'):
        currency_exchange.selected_byn()
    with allure.step('Selected out usd in currency convertor panel'):
        currency_exchange.selected_out_usd()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.the_best_exchange_rate().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount / course
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_byn_eur_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected byn in currency convertor panel'):
        currency_exchange.selected_byn()
    with allure.step('Selected out eur in currency convertor panel'):
        currency_exchange.selected_out_eur()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_one_eur().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount / course
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_byn_rub_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected byn in currency convertor panel'):
        currency_exchange.selected_byn()
    with allure.step('Selected out rub in currency convertor panel'):
        currency_exchange.selected_out_rub()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_one_hundred_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = (the_amount / course) * 100
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_exchange_rate_calculation_rub_eur_sell_convertor_panel(driver, the_amount):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Selected rub in currency convertor panel'):
        currency_exchange.selected_rub()
    with allure.step('Selected out eur in currency convertor panel'):
        currency_exchange.selected_out_eur()
    with allure.step('Amount input field clear'):
        currency_exchange.amount_input_field().clear()
    with allure.step('Enter the amount'):
        currency_exchange.amount_input_field().send_keys(the_amount)
    with allure.step('Calculation exchange rate'):
        best_course = currency_exchange.bank_sell_eur_rub().text
        course_calculation = best_course.replace(',', '.')
        course = course_calculation.replace(' ', '')
        course = float(course)
        result = the_amount / course
        result = float(f'{result:.4f}')
        calculation_site = currency_exchange.estimated_mount().text
        course_calculation = calculation_site.replace(',', '.')
        course_site = course_calculation.replace(' ', '')
        course_site = float(course_site)
    assert course_site == result


@allure.feature('Currency exchange page')
@allure.story('Currency convertor panel')
def test_the_best_exchange_rates_line(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_best_exchange_rates_line().text == 'Лучшие курсы валют'


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_information_about_updating_exchange_rate_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.information_about_updating_exchange_rate().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_date_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.date_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_data_now(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Welding dates'):
        date = datetime.now().strftime('%d %m')
        if date[0] == '0':
            date = date[1:]
    assert currency_exchange.date() == date


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_the_bank_buys_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_bank_buys_text() == 'Банк покупает'


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_the_bank_sell_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate().click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_bank_sells_text() == 'Банк продаёт'


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_check_the_nbrb_course_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_nbrb_exchange_rate_text() == 'Курс НБРБ'


@allure.feature('Currency exchange page')
@allure.story('The best exchange rates')
def test_check_exchange_rate_fluctuations_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate().click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.exchange_rate_fluctuations_text() == (
        'Колебания лучших курсов за последние 14 дней'
    )


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_currency_information_panel_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_currency_information_panel_eur_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('RUB exchange rate field')
def test_currency_information_panel_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_currency_information_panel_eur_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_currency_information_panel_eur_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_currency_information_panel_usd_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_usd_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_one_usd_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_usd().text == '1 USD'


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_bank_by_one_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_one_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_bank_sell_one_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_nbrb_rate_one_usd(domain, driver):
    with allure.step("getting the National Bank's API of the usd exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
        dollar_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
        rate_nbrb = currency_exchange.nbrb_rate_one_usd().text
        rate_nbrb = rate_nbrb.replace(',', '.')
    assert float(rate_nbrb) == dollar_exchange_rate


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_one_eur_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_eur().text == '1 EUR'


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_bank_by_one_eur_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_one_eur().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_bank_sell_one_eur_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_eur().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_nbrb_rate_one_eur(domain, driver):
    with allure.step("getting the National Bank's API of the eur exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
        euro_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
        rate_nbrb = currency_exchange.nbrb_rate_one_eur().text
        rate_nbrb = rate_nbrb.replace(',', '.')
    assert rate_nbrb == f'{euro_exchange_rate}'


@allure.feature('Currency exchange page')
@allure.story('100 RUB exchange rate field')
def test_one_hundred_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_hundred_rub().text == '100 RUB'


@allure.feature('Currency exchange page')
@allure.story('100 RUB exchange rate field')
def test_bank_by_one_hundred_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_one_hundred_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('100 RUB exchange rate field')
def test_bank_sell_one_hundred_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_hundred_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('100 RUB exchange rate field')
def test_nbrb_rate_hundred_rub(domain, driver):
    with allure.step("Getting the National Bank's API of the hundred rub exchange rate"):
        response = requests.request('GET', f'{domain}api/exrates/rates/RUB?parammode=2').json()
        rub_exchange_rate = response['Cur_OfficialRate']
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
        rate_nbrb = currency_exchange.nbrb_rate_one_hundred_rub().text
        rate_nbrb = rate_nbrb.replace(',', '.')
    assert rate_nbrb == f'{rub_exchange_rate}'


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_cross_course_eur_usd_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_course_eur_usd().text == 'Кросс-курс EUR / USD'


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_bank_by_eur_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_eur_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_bank_sell_eur_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_eur_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_nbrb_rate_eur_usd_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_eur_usd().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_cross_course_eur_rub_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_exchange_rate_eur_rub().text == 'Кросс-курс EUR / RUB'


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_bank_by_eur_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_eur_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_bank_sell_eur_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_eur_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_nbrb_rate_eur_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_eur_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_cross_course_usd_rub_text(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_exchange_rate_usd_rub().text == 'Кросс-курс USD / RUB'


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_bank_by_usd_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_buy_usd_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_bank_sell_usd_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_usd_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_nbrb_rate_usd_rub_is_displayed(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_usd_rub().is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
@pytest.mark.skip('a very long test')
def test_exchange_rate_in_other_banks_usd(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "dollar exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_usd()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 500);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_exchange_rate_in_banks_by_usd_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks'):
        currency_exchange.exchange_rate_in_banks_buy_usd().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD exchange rate field')
def test_exchange_rate_in_banks_sell_usd_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks sell usd'):
        currency_exchange.exchange_rate_in_banks_sell_usd().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
@pytest.mark.skip('a very long test')
def test_exchange_rate_in_other_banks_eur(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "usd exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_eur()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 800);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_exchange_rate_in_banks_by_eur_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks in euro purchase'):
        currency_exchange.exchange_rate_in_banks_buy_eur().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR exchange rate field')
def test_exchange_rate_in_banks_sell_eur_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks sell eur'):
        currency_exchange.exchange_rate_in_banks_sell_eur().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('RUB exchange rate field')
@pytest.mark.skip('a very long test')
def test_exchange_rate_in_other_banks_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "rub exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_rub()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 1000);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('RUB exchange rate field')
def test_exchange_rate_in_banks_by_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks in rub purchase'):
        currency_exchange.exchange_rate_in_banks_buy_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('RUB exchange rate field')
def test_exchange_rate_in_banks_sell_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Exchange rate in banks sell rub'):
        currency_exchange.exchange_rate_in_banks_sell_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
@pytest.mark.skip('a very long test')
def test_xchange_rate_in_other_banks_cross_course_eur_usd(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "eur/usd exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_cross_course_eur_usd()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 1200);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_exchange_rate_in_banks_by_cross_course_eur_usd_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('click on "Exchange rate in banks in eur/usd purchase"'):
        currency_exchange.exchange_rate_in_banks_buy_cross_course_eur_usd().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/USD exchange rate field')
def test_exchange_rate_in_banks_sell_cross_course_eur_usd_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('click on "Exchange rate in banks sell rub"'):
        currency_exchange.exchange_rate_in_banks_sell_cross_course_eur_usd().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
@pytest.mark.skip('a very long test')
def test_xchange_rate_in_other_banks_cross_course_eur_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "eur/rub exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_cross_course_eur_rub()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 1400);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_exchange_rate_in_banks_by_cross_course_eur_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('click on "Exchange rate in banks in eur/rub purchase"'):
        currency_exchange.exchange_rate_in_banks_buy_cross_course_eur_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('EUR/RUB exchange rate field')
def test_exchange_rate_in_banks_sell_cross_course_eur_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on "Exchange rate in banks sell eur/rub"'):
        currency_exchange.exchange_rate_in_banks_sell_cross_course_eur_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
@pytest.mark.skip('a very long test')
def test_xchange_rate_in_other_banks_cross_course_usd_rub(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on the "usd/rub exchange rate in other banks"'):
        currency_exchange.exchange_rate_in_other_banks_cross_course_usd_rub()
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 1600);")
        count = 0
        for _ in currency_exchange.banks():
            if len(currency_exchange.banks()) >= 1:
                count += 1
    assert count >= 1


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_exchange_rate_in_banks_by_cross_course_usd_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('click on "Exchange rate in banks in usd/rub purchase"'):
        currency_exchange.exchange_rate_in_banks_buy_cross_course_usd_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('USD/RUB exchange rate field')
def test_exchange_rate_in_banks_sell_cross_course_usd_rub_open_map(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('Click on "Exchange rate in banks sell eur/rub"'):
        currency_exchange.exchange_rate_in_banks_sell_cross_course_usd_rub().click()
    assert currency_exchange.map_is_displayed()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_usd_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section USD, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section USD, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section USD, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_usd_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_usd_nbrb().is_enabled()
#
#
#
# def test_button_fluctuations_in_the_best_rates_usd_by_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_by().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_usd_by().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_eur_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section EUR, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_nbrb().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_by_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_by().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_by().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_rub_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section RUB, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_rub_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_rub_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section RUB, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_rub_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_rub_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section RUB, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_rub_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_rub_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_rub_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_rub_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_rub_nbrb().is_enabled()


# def test_button_fluctuations_in_the_best_rates_rub_buy_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_rub_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_rub_by().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_rub_by().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_rub_eur_usd_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section EUR/USD, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/USD, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/USD, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_usd_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_nbrb().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_usd_buy_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_buy().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_usd_buy().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_eur_rub_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_rub_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_nbrb().is_enabled()


# def test_button_fluctuations_in_the_best_rates_eur_rub_by_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_buy().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_eur_rub_buy().is_enabled()


@allure.feature('Currency exchange page')
@allure.story('Fluctuations in the best rates')
def test_button_fluctuations_in_the_best_rates_rub_usd_rub_enabled(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open currency exchange page'):
        home_page.currency_exchange_rate_click()
        currency_exchange = CurrencyExchange(driver)
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click sell'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_sell().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_sell().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click nbrb'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_nbrb().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_nbrb().is_enabled()
    with allure.step('In the Fluctuations of the best rates section EUR/RUB, click buy'):
        currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_buy().click()
    assert currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_buy().is_enabled()


# def test_button_fluctuations_in_the_best_rates_usd_rub_nbrb_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_nbrb().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_nbrb().is_enabled()


# def test_button_fluctuations_in_the_best_rates_usd_rub_by_enabled(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.currency_exchange_rate_click()
#     currency_exchange = CurrencyExchange(driver)
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_sell().click()
#     currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_buy().click()
#     assert currency_exchange.button_fluctuations_in_the_best_rates_usd_rub_buy().is_enabled()
