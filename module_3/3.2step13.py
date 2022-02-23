import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_registration_one(self):
        browser = self.driver
        browser.get('http://suninjuly.github.io/registration1.html')
        fn = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        fn.send_keys('Napoleon')
        ln = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        ln.send_keys('Bonaparte')
        email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys('napole@on.com')
        button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
        button.click()
        # time.sleep(2)
        welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_el.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_two(self):
        browser = self.driver
        browser.get('http://suninjuly.github.io/registration2.html')
        fn = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        fn.send_keys('Napoleon')
        ln = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        ln.send_keys('Bonaparte')
        email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys('napole@on.com')
        button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
        button.click()
        # time.sleep(2)
        welcome_text_el = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_el.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
