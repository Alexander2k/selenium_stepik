import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ['newYear'])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo={promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.item_in_basket()
    # time.sleep(3000)

