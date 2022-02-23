import math
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/file_input.html'

service = Service(executable_path=ChromeDriverManager().install())

try:

    browser = webdriver.Chrome(service=service)
    browser.get(link)

    fn = browser.find_element(By.NAME, "firstname").send_keys('Napoleon')
    ln = browser.find_element(By.NAME, "lastname").send_keys('Bonaparte')
    email = browser.find_element(By.NAME, "email").send_keys('napole@on.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, '../virus')
    # print(file)

    f = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    f.send_keys(file)

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    text = browser.switch_to.alert
    print(text.text)


finally:
    time.sleep(10)
    browser.quit()
