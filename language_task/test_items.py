import time

from selenium.webdriver.common.by import By

link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_have_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button_basket, "Error button not exist"

