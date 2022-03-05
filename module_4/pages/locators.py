from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.XPATH,  "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRICE = (By.XPATH, "//p[@class='price_color']")
    TOTAL_BASKET_PRICE = (By.XPATH, "//th[@class='total align-right']")
    ITEM_IN_BASKET = (By.CLASS_NAME, "//div[@class='alertinner ']//text()[contains(.,' был добавлен в вашу корзину')]")
