from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY), "Basket not empty"
