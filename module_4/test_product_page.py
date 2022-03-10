import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

promo_codes = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5',
               'offer6', pytest.param("offer7", marks=pytest.mark.xfail), 'offer8', 'offer9']


@pytest.mark.skip
@pytest.mark.parametrize('promo', promo_codes)
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message()
    product_page.right_item_in_basket()
    product_page.equals_price_item_and_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
