import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from calc import calc

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

try:

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100')
    )
    button_add = browser.find_element(By.XPATH, "//button[@id='book']").click()

    num = browser.find_element(By.XPATH, "//span[@id='input_value']")

    y = calc(int(num.text))

    input_y = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)

    button_submit = browser.find_element(By.XPATH, "//button[@id='solve']").click()

    text = browser.switch_to.alert
    print(text.text)
    text.accept()

except Exception as e:
    print(e)

finally:
    time.sleep(5)
    browser.close()
