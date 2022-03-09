import time

import pytest

from .pages.product_page import ProductPage

promo_codes = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5',
               'offer6', pytest.param("offer7", marks=pytest.mark.xfail), 'offer8', 'offer9']


@pytest.mark.parametrize('promo', promo_codes)
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.item_in_basket()
    product_page.right_item_in_basket()
    product_page.equals_price_item_and_basket()

    # time.sleep(1000)
