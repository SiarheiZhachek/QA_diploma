from selenium.webdriver.common.by import By


navigation_bar = (By.CSS_SELECTOR, '.b-top-navigation')
logo = (By.CLASS_NAME, 'onliner_logo')
search_field = (By.CLASS_NAME, 'fast-search__input')
user_bar = (By.ID, 'userbar')
project_navigation_flex = (By.CLASS_NAME, "project-navigation__flex")
main_navigator_button = (By.CSS_SELECTOR, '.b-main-navigation__link')
credit_card_button = (By.CLASS_NAME, 'b-top-navigation-clover')
currency_exchange_rate_link = (By.CSS_SELECTOR, '._u.js-currency-amount')
weather = (
    By.CSS_SELECTOR, '.b-top-navigation-informers__item.top-informer-weather.js-weather-widget'
)
age_restriction = (By.CLASS_NAME, 'b-top-navigation-age')
iframe_search_field = (By.CSS_SELECTOR, '.modal-iframe')
search_page = (By.CLASS_NAME, 'search-page')
search_result = (By.CLASS_NAME, 'result__item_product')
search_field_close = (By.CLASS_NAME, 'search__close')
search_bar = (By.CSS_SELECTOR, '.search__bar')
cart = (By.CSS_SELECTOR, '.auth-bar__item.auth-bar__item--cart')
google_account_link = (By.CSS_SELECTOR, '[title="Google"]')
vk_account_link = (By.CSS_SELECTOR, '[title="ВКонтакте"]')
facebook_account_link = (By.CSS_SELECTOR, '[title="Facebook"]')
user_login_button = (By.CSS_SELECTOR, '.auth-bar__item.auth-bar__item--text')
