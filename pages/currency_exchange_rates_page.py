from pages.base_page import BasePage
from pages.locators import currency_exchange_rates_page_locators as loc
from pages.base_page import int_value_from_ru_month


class CurrencyExchange(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def currency_convertor_panel(self):
        return self.find_element(loc.currency_convertor_panel)

    def currency_convertor_panel_text(self):
        return self.find_element(loc.currency_convertor_panel_text).text

    @property
    def to_sell_button(self):
        return self.find_element(loc.to_sell_button)

    @property
    def buy_button(self):
        return self.find_element(loc.buy_button)

    @property
    def amount_input_field(self):
        return self.find_element(loc.amount_input_field)

    @property
    def type_of_input_currency(self):
        return self.find_element(loc.type_of_input_currency)

    def selected_usd(self):
        self.select(loc.type_of_input_currency).select_by_value('usd')

    @property
    def type_of_input_currency_select_usd(self):
        return self.find_element(loc.currency_in_usd)

    def selected_eur(self):
        self.select(loc.type_of_input_currency).select_by_index('1')

    @property
    def type_of_input_currency_select_eur(self):
        return self.find_element(loc.currency_in_eur)

    def selected_rub(self):
        self.select(loc.type_of_input_currency).select_by_visible_text('RUB')

    @property
    def type_of_input_currency_select_rub(self):
        return self.find_element(loc.currency_in_rub)

    def selected_byn(self):
        self.select(loc.type_of_input_currency).select_by_index('3')

    @property
    def type_of_input_currency_select_byn(self):
        return self.find_element(loc.currency_in_byn)

    @property
    def type_currency_out(self):
        return self.find_element(loc.type_currency_out)

    def selected_out_eur(self):
        self.select(loc.type_currency_out).select_by_value('eur')

    @property
    def money_logo(self):
        return self.find_element(loc.money_logo)

    def selected_out_rub(self):
        self.select(loc.type_currency_out).select_by_value('rub')

    def selected_out_byn(self):
        self.select(loc.type_currency_out).select_by_value('byn')

    def selected_out_usd(self):
        self.select(loc.type_currency_out).select_by_value('usd')

    @property
    def exchange_rate_nbrb(self):
        return self.find_element(loc.nbrb_course)

    @property
    def exchange_rate_calculation_nbrb(self):
        return self.find_element(loc.exchange_rate_calculation_nbrb)

    def exchange_rate_nbrb_text_is_displayed(self):
        return self.find_element(loc.exchange_rate_nbrb_text).is_displayed()

    def the_best_exchange_rate_in_the_converter_is_displayed(self):
        return self.find_element(loc.the_best_exchange_rate_in_the_converter).is_displayed()

    @property
    def the_best_exchange_rate(self):
        return self.find_element(loc.the_best_exchange_rate)

    @property
    def estimated_mount(self):
        return self.find_element(loc.estimated_mount)

    def the_best_exchange_rates_line_text(self):
        return self.find_element(loc.the_best_exchange_rates_line).text

    def information_about_updating_exchange_rate_is_displayed(self):
        return self.find_element(
            loc.information_about_updating_exchange_rate
        ).is_displayed()

    def date_is_displayed(self):
        return self.find_element(loc.date).is_displayed()

    @property
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

    def currency_information_panel_usd_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[0].is_displayed()

    def currency_information_panel_eur_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[1].is_displayed()

    def currency_information_panel_rub_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[2].is_displayed()

    def currency_information_panel_eur_usd_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[3].is_displayed()

    def currency_information_panel_eur_rub_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[4].is_displayed()

    def currency_information_panel_usd_rub_is_displayed(self):
        return self.find_elements(loc.currency_information_panel)[5].is_displayed()

    def one_usd_text(self):
        return self.find_elements(loc.information_panel_attribute)[0].text

    @property
    def bank_buy_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[1]

    @property
    def bank_sell_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[2]

    @property
    def nbrb_rate_one_usd(self):
        return self.find_elements(loc.information_panel_attribute)[3]

    def one_eur_text(self):
        return self.find_elements(loc.information_panel_attribute)[4].text

    @property
    def bank_buy_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[5]

    @property
    def bank_sell_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[6]

    @property
    def nbrb_rate_one_eur(self):
        return self.find_elements(loc.information_panel_attribute)[7]

    def one_hundred_rub_text(self):
        return self.find_elements(loc.information_panel_attribute)[8].text

    @property
    def bank_buy_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[9]

    @property
    def bank_sell_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[10]

    @property
    def nbrb_rate_one_hundred_rub(self):
        return self.find_elements(loc.information_panel_attribute)[11]

    def cross_course_eur_usd_text(self):
        return self.find_elements(loc.information_panel_attribute)[12].text

    @property
    def bank_buy_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[13]

    @property
    def bank_sell_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[14]

    @property
    def nbrb_rate_eur_usd(self):
        return self.find_elements(loc.information_panel_attribute)[15]

    def cross_exchange_rate_eur_rub_text(self):
        return self.find_elements(loc.information_panel_attribute)[16].text

    @property
    def bank_buy_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[17]

    @property
    def bank_sell_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[18]

    @property
    def nbrb_rate_eur_rub(self):
        return self.find_elements(loc.information_panel_attribute)[19]

    def cross_exchange_rate_usd_rub_text(self):
        return self.find_elements(loc.information_panel_attribute)[20].text

    @property
    def bank_buy_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[21]

    @property
    def bank_sell_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[22]

    @property
    def nbrb_rate_usd_rub(self):
        return self.find_elements(loc.information_panel_attribute)[23]

    def exchange_rate_in_other_banks_usd(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[0]
        return self.move_to_element(element).click().perform()

    def banks(self):
        return self.find_elements(loc.banks)

    def exchange_rate_in_banks_buy_usd_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[1].click()

    def map_is_displayed(self):
        return self.find_element(loc.maps).is_displayed()

    def exchange_rate_in_banks_sell_usd_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[2].click()

    def exchange_rate_in_other_banks_eur(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[3]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_eur_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[4].click()

    def exchange_rate_in_banks_sell_eur_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[5].click()

    def exchange_rate_in_other_banks_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[6]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[7].click()

    def exchange_rate_in_banks_sell_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[8].click()

    def exchange_rate_in_other_banks_cross_course_eur_usd(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[9]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_eur_usd_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[10].click()

    def exchange_rate_in_banks_sell_cross_course_eur_usd_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[11].click()

    def exchange_rate_in_other_banks_cross_course_eur_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[12]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_eur_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[13].click()

    def exchange_rate_in_banks_sell_cross_course_eur_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[14].click()

    def exchange_rate_in_other_banks_cross_course_usd_rub(self):
        element = self.find_elements(loc.exchange_rate_in_banks)[15]
        return self.move_to_element(element).click().perform()

    def exchange_rate_in_banks_buy_cross_course_usd_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[16].click()

    def exchange_rate_in_banks_sell_cross_course_usd_rub_click(self):
        return self.find_elements(loc.exchange_rate_in_banks)[17].click()

    @property
    def button_fluctuations_in_the_best_rates_usd_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[1]

    @property
    def button_fluctuations_in_the_best_rates_usd_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[2]

    @property
    def button_fluctuations_in_the_best_rates_usd_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[0]

    @property
    def button_fluctuations_in_the_best_rates_eur_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[4]

    @property
    def button_fluctuations_in_the_best_rates_eur_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[5]

    @property
    def button_fluctuations_in_the_best_rates_eur_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[3]

    @property
    def button_fluctuations_in_the_best_rates_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[7]

    @property
    def button_fluctuations_in_the_best_rates_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[8]

    @property
    def button_fluctuations_in_the_best_rates_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[6]

    @property
    def button_fluctuations_in_the_best_rates_eur_usd_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[10]

    @property
    def button_fluctuations_in_the_best_rates_eur_usd_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[11]

    @property
    def button_fluctuations_in_the_best_rates_eur_usd_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[9]

    @property
    def button_fluctuations_in_the_best_rates_eur_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[13]

    @property
    def button_fluctuations_in_the_best_rates_eur_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[14]

    @property
    def button_fluctuations_in_the_best_rates_eur_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[12]

    @property
    def button_fluctuations_in_the_best_rates_usd_rub_sell(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[16]

    @property
    def button_fluctuations_in_the_best_rates_usd_rub_nbrb(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[17]

    @property
    def button_fluctuations_in_the_best_rates_usd_rub_buy(self):
        return self.find_elements(loc.button_fluctuations_in_the_best_rates)[15]
