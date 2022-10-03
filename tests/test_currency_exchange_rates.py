from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from ..pages.home_page import HomePage
from ..pages.currency_exchange_rates_page import CurrencyExchange
import requests
import pytest
from decimal import Decimal
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
import re
from datetime import datetime


def test_currency_convertor_panel_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_convertor_panel().is_displayed()


def test_currency_convertor_panel_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_convertor_panel_text().text == 'Конвертер валют по лучшим курсам'


def test_to_sell_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.to_sell_button().is_displayed()


def test_to_sell_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.to_sell_button().text == 'Продать'


def test_buy_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.buy_button().is_displayed()


def test_buy_button_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.buy_button().text == 'Купить'


def test_buy_button_selected(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.buy_button().click()
    assert currency_exchange.buy_button().is_enabled()


def test_to_sell_button_selected(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.buy_button().click()
    currency_exchange.to_sell_button().click()
    assert currency_exchange.to_sell_button().is_enabled()


def test_amount_input_field_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.amount_input_field().is_displayed()

#


def test_type_of_input_currency_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.type_of_input_currency().is_displayed()


def test_select_euro(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    # currency_exchange.type_of_input_currency().click()
    currency_exchange.selected_eur()
    assert currency_exchange.type_of_input_currency_select_eur().is_selected()


def test_select_rub(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_rub()
    assert currency_exchange.type_of_input_currency_select_rub().is_selected()


def test_select_byn(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_byn()
    assert currency_exchange.type_of_input_currency_select_byn().is_selected()


def test_select_usd(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_byn()
    currency_exchange.selected_usd()
    assert currency_exchange.type_of_input_currency_select_usd().is_selected()


def test_select_out_eur(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.type_currency_out().click()
    currency_exchange.selected_out_eur()
    assert currency_exchange.money_logo().text == '€'


def test_select_out_rub(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_out_rub()
    assert currency_exchange.money_logo().text == 'RUB'


def test_select_out_byn(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_out_byn()
    assert currency_exchange.money_logo().text == 'BYN'


def test_select_out_usd(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_rub()
    currency_exchange.selected_out_usd()
    assert currency_exchange.money_logo().text == '$'


def test_nbrb_usd_course(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
    dollar_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    exchange_rate = currency_exchange.nbrb_course().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    assert str_exchange_rate == f'{dollar_exchange_rate}'


def test_nbrb_eur_course(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
    euro_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_eur()
    exchange_rate = currency_exchange.nbrb_course().text
    str_exchange_rate = exchange_rate.replace(',', '.')
    assert str_exchange_rate == f'{euro_exchange_rate}'


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_correct_course_calculation_nbrb_usd(domain, the_amount, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
    dollar_exchange_rate = response['Cur_OfficialRate']
    correct_result = dollar_exchange_rate * the_amount
    result = float("{0:.2f}".format(correct_result))
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.course_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_correct_course_calculation_nbrb_eur(domain, the_amount, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
    euro_exchange_rate = response['Cur_OfficialRate']
    correct_result = euro_exchange_rate * the_amount
    result = float("{0:.2f}".format(correct_result))
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.amount_input_field().clear()
    currency_exchange.selected_eur()
    currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.course_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_correct_course_calculation_nbrb_rub(domain, the_amount, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/RUB?parammode=2').json()
    rub_exchange_rate = response['Cur_OfficialRate']
    correct_result = (rub_exchange_rate / 100) * the_amount
    result = float("{0:.2f}".format(correct_result))
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.amount_input_field().clear()
    currency_exchange.selected_rub()
    currency_exchange.amount_input_field().send_keys(the_amount)
    course_calculation_site = currency_exchange.course_calculation_nbrb().text
    course_calculation = course_calculation_site.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    assert course == result


def test_course_nbrb_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.course_nbrb_text().is_displayed()


def test_the_best_course_in_the_converter(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_best_course_in_the_converter().is_displayed()


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_usd_byn_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_by_one_usd().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = course * the_amount
    result = float("{0:.3f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_eur_byn_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_eur()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_by_one_eur().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = course * the_amount
    result = float("{0:.3f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [100, 100000, 10000000000])
def test_course_calculation_rub_byn_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_rub()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_by_one_hundred_rub().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    course = float("{0:.3f}".format(course))
    result = (the_amount / 100) * course
    result = float("{0:.3f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_usd_byn_by(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.buy_button().click()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_sell_one_usd().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = course * the_amount
    result = float("{0:.3f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_eur_byn_by(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    sleep(2)
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.buy_button().click()
    currency_exchange.selected_eur()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_sell_one_eur().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount * course
    result = float("{0:.3f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [100, 100000, 99999999999])
def test_course_calculation_rub_byn_by(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.buy_button().click()
    currency_exchange.selected_rub()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_sell_one_hundred_rub().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount * (course / 100)
    result = float("{0:.4f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.skip('позже')
@pytest.mark.parametrize('the_amount', [1, 100000, 99999999999])
def test_course_calculation_usd_eur_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    sleep(2)
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_out_eur()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.bank_by_one_eur().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount * course
    result = float("{0:.4f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    sleep(5)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_usd_rub_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_out_rub()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = course * the_amount
    result = float("{0:.2f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    course_site = float("{0:.2f}".format(course_site))
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_eur_usd_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_eur()
    currency_exchange.selected_out_usd()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount / course
    result = float("{0:.2f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    course_site = float("{0:.2f}".format(course_site))
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_eur_rub_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_eur()
    currency_exchange.selected_out_rub()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = course * the_amount
    result = float("{0:.2f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    course_site = float("{0:.2f}".format(course_site))
    assert course_site == result


@pytest.mark.parametrize('the_amount', [100, 100000, 10000000000])
def test_course_calculation_rub_usd_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_rub()
    currency_exchange.selected_out_usd()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course_rub = float(course)
    result = the_amount / course_rub
    result = float("{0:.2f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    course_site = float("{0:.2f}".format(course_site))
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_byn_usd_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_byn()
    currency_exchange.selected_out_usd()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount / course
    result = float("{0:.4f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_byn_eur_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_byn()
    currency_exchange.selected_out_eur()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount / course
    result = float("{0:.4f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.skip('bag')
@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_byn_rub_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_byn()
    currency_exchange.selected_out_rub()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount * course
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result


@pytest.mark.parametrize('the_amount', [1, 100000, 10000000000])
def test_course_calculation_rub_eur_sell(driver, the_amount):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    currency_exchange.selected_rub()
    currency_exchange.selected_out_eur()
    currency_exchange.amount_input_field().clear()
    currency_exchange.amount_input_field().send_keys(the_amount)
    best_course = currency_exchange.the_best_course().text
    course_calculation = best_course.replace(',', '.')
    course = course_calculation.replace(' ', '')
    course = float(course)
    result = the_amount / course
    result = float("{0:.4f}".format(result))
    calculation_site = currency_exchange.estimated_mount().text
    course_calculation = calculation_site.replace(',', '.')
    course_site = course_calculation.replace(' ', '')
    course_site = float(course_site)
    assert course_site == result



def test_the_best_exchange_rates_line(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_best_exchange_rates_line().text == 'Лучшие курсы валют'


def test_information_about_updating_courses_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.information_about_updating_courses().is_displayed()


def test_date_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.date_is_displayed()


def test_data_now(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    date = datetime.now().strftime('%d %m')
    if date[0] == '0':
        date = date[1:]
    assert currency_exchange.date() == date


def test_the_bank_buys_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_bank_buys_text() == 'Банк покупает'


def test_the_bank_sell_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_bank_sells_text() == 'Банк продаёт'


def test_check_the_nbrb_course_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.the_nbrb_course_text() == 'Курс НБРБ'


def test_check_exchange_rate_fluctuations_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.exchange_rate_fluctuations_text() == 'Колебания лучших курсов за последние 14 дней'


def test_currency_information_panel_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_usd().is_displayed()


def test_currency_information_panel_eur_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur().is_displayed()


def test_currency_information_panel_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_rub().is_displayed()


def test_currency_information_panel_eur_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur_usd().is_displayed()


def test_currency_information_panel_eur_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_eur_rub().is_displayed()


def test_currency_information_panel_usd_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.currency_information_panel_usd_rub().is_displayed()


def test_one_usd_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_usd().text == '1 USD'


def test_bank_by_one_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_one_usd().is_displayed()


def test_bank_sell_one_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_usd().is_displayed()


def test_nbrb_rate_one_usd(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/431').json()
    dollar_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    rate_nbrb = currency_exchange.nbrb_rate_one_usd().text
    rate_nbrb = rate_nbrb.replace(',', '.')
    assert rate_nbrb == f'{dollar_exchange_rate}'


def test_one_eur_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_eur().text == '1 EUR'


def test_bank_by_one_eur_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_one_eur().is_displayed()


def test_bank_sell_one_eur_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_eur().is_displayed()


def test_nbrb_rate_one_eur(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/EUR?parammode=2').json()
    euro_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    rate_nbrb = currency_exchange.nbrb_rate_one_eur().text
    rate_nbrb = rate_nbrb.replace(',', '.')
    assert rate_nbrb == f'{euro_exchange_rate}'


def test_one_hundred_rub(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.one_hundred_rub().text == '100 RUB'


def test_bank_by_one_hundred_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_one_hundred_rub().is_displayed()


def test_bank_sell_one_hundred_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_one_hundred_rub().is_displayed()


def test_nbrb_rate_hundred_rub(domain, driver):
    response = requests.request('GET', f'{domain}api/exrates/rates/RUB?parammode=2').json()
    rub_exchange_rate = response['Cur_OfficialRate']
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    rate_nbrb = currency_exchange.nbrb_rate_one_hundred_rub().text
    rate_nbrb = rate_nbrb.replace(',', '.')
    assert rate_nbrb == f'{rub_exchange_rate}'


def test_cross_course_eur_usd_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_course_eur_usd().text == 'Кросс-курс EUR / USD'


def test_bank_by_eur_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_eur_usd().is_displayed()


def test_bank_sell_eur_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_eur_usd().is_displayed()


def test_nbrb_rate_eur_usd_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_eur_usd().is_displayed()


def test_cross_course_eur_rub_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_course_eur_rub().text == 'Кросс-курс EUR / RUB'


def test_bank_by_eur_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_eur_rub().is_displayed()


def test_bank_sell_eur_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_eur_rub().is_displayed()


def test_nbrb_rate_eur_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_eur_rub().is_displayed()


def test_cross_course_usd_rub_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.cross_course_usd_rub().text == 'Кросс-курс USD / RUB'


def test_bank_by_usd_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_by_usd_rub().is_displayed()


def test_bank_sell_usd_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.bank_sell_usd_rub().is_displayed()


def test_nbrb_rate_usd_rub_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.currency_exchange_rate().click()
    currency_exchange = CurrencyExchange(driver)
    assert currency_exchange.nbrb_rate_usd_rub().is_displayed()



def test_hz(driver):
    driver.get('https://kurs.onliner.by/')
    driver.find_element(
        By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr/td/table[1]/tbody/tr/td[1]/p[2]/a'
    ).click()
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 2000);")
    # driver.find_element(By.XPATH, '//tr[@class="merge"]/td').click()
    catalog_list = []
    my_list = []
    element = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr/td/table[2]/tbody/tr')
    for i in element:
        c = i
        f = c.text
        d = f.replace(',', '.')
        catalog_list.append(d)

    pass
    s = ' '.join(catalog_list)
    nums = re.findall(r'\d*\.\d+|\d+', s)

    nums = [float(i) for i in nums]

    print(nums)

    for i in catalog_list:
        print(i[0:14])




