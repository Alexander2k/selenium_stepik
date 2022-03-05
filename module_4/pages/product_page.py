from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def item_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)

    def right_item_in_basket(self):
        # todo
        pass

    def equals_price_item_and_basket(self):
        # todo
        pass
