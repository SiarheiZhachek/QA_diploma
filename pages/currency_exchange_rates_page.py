from pages.base_page import BasePage
from pages.locators import currency_exchange_rates_page_locators as loc
from pages.base_page import int_value_from_ru_month


class CurrencyExchange(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def currency_convertor_panel(self):
        return self.find_element(loc.currency_convertor_panel)

    def currency_convertor_panel_text(self):
        return self.find_element(loc.currency_convertor_panel_text)

    def to_sell_button(self):
        return self.find_element(loc.to_sell_button)

    def buy_button(self):
        return self.find_element(loc.buy_button)

    def amount_input_field(self):
        return self.find_element(loc.amount_input_field)

    def type_of_input_currency(self):
        return self.find_element(loc.type_of_input_currency)

    def selected_usd(self):
        return self.select(loc.type_of_input_currency).select_by_value('usd')

    def type_of_input_currency_select_usd(self):
        return self.find_element(loc.currency_in_usd)

    def selected_eur(self):
        return self.select(loc.type_of_input_currency).select_by_index('1')

    def type_of_input_currency_select_eur(self):
        return self.find_element(loc.currency_in_eur)

    def selected_rub(self):
        return self.select(loc.type_of_input_currency).select_by_visible_text('RUB')

    def type_of_input_currency_select_rub(self):
        return self.find_element(loc.currency_in_rub)

    def selected_byn(self):
        return self.select(loc.type_of_input_currency).select_by_index('3')

    def type_of_input_currency_select_byn(self):
        return self.find_element(loc.currency_in_byn)

    def type_currency_out(self):
        return self.find_element(loc.type_currency_out)

    def selected_out_eur(self):
        return self.select(loc.type_currency_out).select_by_value('eur')

    def money_logo(self):
        return self.find_element(loc.money_logo)

    def selected_out_rub(self):
        return self.select(loc.type_currency_out).select_by_value('rub')

    def selected_out_byn(self):
        return self.select(loc.type_currency_out).select_by_value('byn')

    def selected_out_usd(self):
        return self.select(loc.type_currency_out).select_by_value('usd')

    def exchange_rate_nbrb(self):
        return self.find_element(loc.nbrb_course)

    def exchange_rate_calculation_nbrb(self):
        return self.find_element(loc.exchange_rate_calculation_nbrb)

    def exchange_rate_nbrb_text(self):
        return self.find_element(loc.exchange_rate_nbrb_text)

    def the_best_exchange_rate_in_the_converter(self):
        return self.find_element(loc.the_best_exchange_rate_in_the_converter)

    def the_best_exchange_rate(self):
        return self.find_element(loc.the_best_exchange_rate)

    def estimated_mount(self):
        return self.find_element(loc.estimated_mount)

    def the_best_exchange_rates_line(self):
        return self.find_element(loc.the_best_exchange_rates_line)

    def information_about_updating_exchange_rate(self):
        return self.find_element(loc.information_about_updating_exchange_rate)

    def date_is_displayed(self):
        return self.find_element(loc.date).is_displayed()

    def date_site(self):
        return self.find_element(loc.date)

    def date(self):
        date = self.find_element(loc.date).text
        return int_value_from_ru_month(date)

    def the_bank_buys_text(self):
        return self.find_element(loc.the_bank_buys).text

    def the_bank_sells_text(self):
        return self.find_element(loc.the_bank_sells).text

    def the_nbrb_exchange_rate_text(self):
        return self.find_element(loc.nbrb_exchange_rate_text).text

    def exchange_rate_fluctuations_text(self):
        return self.find_element(loc.exchange_rate_fluctuations).text

    def currency_information_panel_usd(self):
        return self.find_elements(loc.currency_information_panel)[0]

    def currency_information_panel_eur(self):
        return self.find_elements(loc.currency_information_panel)[1]

    def currency_information_panel_rub(self):
        return self.find_elements(loc.currency_information_panel)[2]

    def currency_information_panel_eur_usd(self):
        return self.find_elements(loc.currency_information_panel)[3]

    def currency_information_panel_eur_rub(self):
        return self.find_elements(loc.currency_information_panel)[4]

    def currency_information_panel_usd_rub(self):
        return self.find_elements(loc.currency_information_panel)[5]

    def one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[0]

    def bank_buy_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[1]

    def bank_sell_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[2]

    def nbrb_rate_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[3]

    def one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[4]

    def bank_buy_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[5]

    def bank_sell_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[6]

    def nbrb_rate_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[7]

    def one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[8]

    def bank_buy_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[9]

    def bank_sell_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[10]

    def nbrb_rate_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[11]

    def cross_course_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[12]

    def bank_buy_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[13]

    def bank_sell_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[14]

    def nbrb_rate_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[15]

    def cross_exchange_rate_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[16]

    def bank_buy_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[17]

    def bank_sell_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[18]

    def nbrb_rate_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[19]

    def cross_exchange_rate_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[20]

    def bank_buy_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[21]

    def bank_sell_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[22]

    def nbrb_rate_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[23]

    def exchange_rate_in_other_banks_usd(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[0]
        return self.move_to_element(element).click().perform()

    def banks(self):
        return self.find_elements(loc.banks)

    def exchange_rate_in_banks_buy_usd(self):
        return self.find_elements(loc.exchange_rate_in_banks)[1]

    def map_is_displayed(self):
        return self.find_element(loc.maps).is_displayed()

    def exchange_rate_in_banks_sell_usd(self):
        return self.find_elements(loc.exchange_rate_in_banks)[2]

    def exchange_rate_in_other_banks_eur(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[3]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_eur(self):
        return self.find_elements(loc.exchange_rate_in_banks)[4]

    def exchange_rate_in_banks_sell_eur(self):
        return self.find_elements(loc.exchange_rate_in_banks)[5]

    def exchange_rate_in_other_banks_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[6]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[7]

    def exchange_rate_in_banks_sell_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[8]

    def exchange_rate_in_other_banks_cross_course_eur_usd(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[9]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_eur_usd(self):
        return self.find_elements(loc.exchange_rate_in_banks)[10]

    def exchange_rate_in_banks_sell_cross_course_eur_usd(self):
        return self.find_elements(loc.exchange_rate_in_banks)[11]

    def exchange_rate_in_other_banks_cross_course_eur_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[12]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_eur_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[13]

    def exchange_rate_in_banks_sell_cross_course_eur_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[14]

    def exchange_rate_in_other_banks_cross_course_usd_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[15]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_usd_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[16]

    def exchange_rate_in_banks_sell_cross_course_usd_rub(self):
        return self.find_elements(loc.exchange_rate_in_banks)[17]

    def button_fluctuations_in_the_best_rates_usd_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[1]

    def button_fluctuations_in_the_best_rates_usd_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[2]

    def button_fluctuations_in_the_best_rates_usd_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[0]

    def button_fluctuations_in_the_best_rates_eur_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[4]

    def button_fluctuations_in_the_best_rates_eur_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[5]

    def button_fluctuations_in_the_best_rates_eur_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[3]

    def button_fluctuations_in_the_best_rates_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[7]

    def button_fluctuations_in_the_best_rates_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[8]

    def button_fluctuations_in_the_best_rates_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[6]

    def button_fluctuations_in_the_best_rates_eur_usd_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[10]

    def button_fluctuations_in_the_best_rates_eur_usd_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[11]

    def button_fluctuations_in_the_best_rates_eur_usd_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[9]

    def button_fluctuations_in_the_best_rates_eur_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[13]

    def button_fluctuations_in_the_best_rates_eur_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[14]

    def button_fluctuations_in_the_best_rates_eur_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[12]

    def button_fluctuations_in_the_best_rates_usd_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[16]

    def button_fluctuations_in_the_best_rates_usd_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[17]

    def button_fluctuations_in_the_best_rates_usd_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[15]
