import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def test_registration_one():
    browser.get('http://suninjuly.github.io/registration1.html')
    fn = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    fn.send_keys('Napoleon')
    ln = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    ln.send_keys('Bonaparte')
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys('napole@on.com')
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()
    time.sleep(2)
    welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_el.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.close()


def test_registration_two():
    browser.get('http://suninjuly.github.io/registration2.html')
    fn = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    fn.send_keys('Napoleon')
    ln = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    ln.send_keys('Bonaparte')
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys('napole@on.com')
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()
    time.sleep(2)
    welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_el.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.close()
