from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "div .alertinner p strong")
    ITEM_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']")

    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    BASKET_PRODUCT_NAME = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    BASKET_PAGE = (By.XPATH, "//a[@class='btn btn-default']")


class BasketPageLocators(object):
    TOTAL_BASKET = (By.XPATH, "//th[@class='total align-right']//h3[@class='price_color']")
