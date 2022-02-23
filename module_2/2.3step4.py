import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    alert = browser.switch_to.alert
    alert.accept()

    num = browser.find_element(By.XPATH, "//span[@id='input_value']")

    answer = calc(int(num.text))

    input_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(answer)

    button2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    text = browser.switch_to.alert
    print(text.text)

    time.sleep(5)
    browser.quit()





