from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "div .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alert-success")

    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    BASKET_PRODUCT_NAME = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    BASKET_PAGE = (By.XPATH, "//a[@class='btn btn-default']")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div .basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators(object):
    BASKET_EMPTY = (By.CSS_SELECTOR, "div #content_inner >p")
    TOTAL_BASKET = (By.XPATH, "//th[@class='total align-right']//h3[@class='price_color']")
