from selenium.webdriver.common.by import By


currency_convertor_panel = (By.CSS_SELECTOR, 'div[class="b-currency-converter"]')
currency_convertor_panel_text = (By.CSS_SELECTOR, 'p[class="title"]')
to_sell_button = (By.CSS_SELECTOR, 'label[for="sale"]')
buy_button = (By.CSS_SELECTOR, 'label[for="buy"]')
amount_input_field = (By.ID, 'amount-in')
type_of_input_currency = (By.ID, 'currency-in')
currency_in_eur = (By.XPATH, '//select[@id="currency-in"]/option[2]')
currency_in_usd = (By.XPATH, '//select[@id="currency-in"]/option[1]')
currency_in_rub = (By.XPATH, '//select[@id="currency-in"]/option[3]')
currency_in_byn = (By.XPATH, '//select[@id="currency-in"]/option[4]')
type_currency_out = (By.ID, 'currency-out')
money_logo = (By.XPATH, '//*[@id="converter-out"]/li[2]/span')
nbrb_course = (By.XPATH, '//*[@id="currency-converter"]/div[2]/div/p/b[2]')
course_calculation_nbrb = (By.XPATH, '//*[@id="currency-converter"]/div[2]/div/p/b[1]')
course_nbrb_text = (By.XPATH, '//*[@id="currency-converter"]/div[2]/div/p')
the_best_course_in_the_converter = (By.XPATH, '//*[@id="converter-out"]/li[3]/i/p[1]')
the_best_course = (By.XPATH, '//*[@id="converter-out"]/li[3]/i/p[1]/b')
estimated_mount = (By.XPATH, '//*[@id="converter-out"]/li[2]/b')
# exchange_rate_usd = (By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr/td/table[1]/tbody/tr/td[2]/p[1]/b')
the_best_exchange_rates_line = (By.XPATH, '//div[@class="b-currency-main__top"]/h1')
information_about_updating_courses = (By.CLASS_NAME, 'updated')
date = (By.CLASS_NAME, 'th-first')
the_bank_buys = (By.XPATH, '//table[@class="b-currency-table"]/thead/tr/th[2]')
the_bank_sells = (By.XPATH, '//table[@class="b-currency-table"]/thead/tr/th[3]')
nbrb_course_text = (By.XPATH, '//table[@class="b-currency-table"]/thead/tr/th[4]')
exchange_rate_fluctuations = (By.XPATH, '//table[@class="b-currency-table"]/thead/tr/th[5]')
the_all_bank_sells_by_price = (By.XPATH, '//tr[@class="tr-main"]/td[2]/p/b')
currency_information_panel = (By.XPATH, '//tr[@class="tr-main"]')
information_panel_attribute = (By.XPATH, '//table[@class="b-currency-table__best"]/tbody/tr/td/p/b')
