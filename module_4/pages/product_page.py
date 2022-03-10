from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"

    def right_item_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME)
        assert product_name.text == basket_product_name.text

    def equals_price_item_and_basket(self):
        item_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE)
        assert item_price.text == basket_price.text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
