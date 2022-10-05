from selenium.webdriver.common.by import By


navigation_bar = (By.CSS_SELECTOR, 'nav[class="b-top-navigation"]')
logo = (By.CLASS_NAME, 'onliner_logo')
search_field = (By.CLASS_NAME, 'fast-search__input')
user_bar = (By.ID, 'userbar')
project_navigation_flex = (By.CLASS_NAME, "project-navigation__flex")
main_navigator_button = (By.CSS_SELECTOR, 'a[class="b-main-navigation__link"]')
credit_card_button = (By.XPATH, '//div[@id="container"]/div/div/header/div[2]/div/nav/a')
currency_exchange_rate_link = (
    By.XPATH, '//div[@id="container"]/div/div/header/div[2]/div/nav/ul[2]/li[1]/a'
)
weather = (By.XPATH, '//div[@id="container"]/div/div/header/div[2]/div/nav/ul[2]/li[2]/a')
age_restriction = (By.CLASS_NAME, 'b-top-navigation-age')
iframe_search_field = (By.XPATH, '//div[@id="fast-search-modal"]/div/div/iframe')
search_page = (By.CLASS_NAME, 'search-page')
search_result = (By.CLASS_NAME, 'result__item_product')
search_field_close = (By.CLASS_NAME, 'search__close')
search_bar = (By.XPATH, '//*[@id="search-page"]/div[1]/div[1]')
cart = (By.CSS_SELECTOR, 'a[title="Корзина"]')
google_account_link = (By.XPATH, '//*[@id="userbar"]/div[1]/div/div/div[4]')
vk_account_link = (By.CSS_SELECTOR, 'div[title="ВКонтакте"]')
facebook_account_link = (By.CSS_SELECTOR, 'div[title="Facebook"]')
user_login_button = (By.XPATH, '//div[@id="userbar"]/div[1]/div/div/div[1]')
user_login_field = (By.XPATH, '//div[@id="auth-container"]/div/div[2]')
