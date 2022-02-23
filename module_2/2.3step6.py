import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

service = Service(executable_path=ChromeDriverManager().install())

try:

    browser = webdriver.Chrome(service=service)
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()
    time.sleep(1)

    browser.switch_to.window(browser.window_handles[1])

    num = browser.find_element(By.XPATH, "//span[@id='input_value']")

    answer = calc(int(num.text))

    input_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(answer)

    button2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    text = browser.switch_to.alert
    print(text.text)


finally:
    time.sleep(5)
    browser.quit()
