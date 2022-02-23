import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome('../chromedriver.exe')
browser.get(link)

try:
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    print(y)

    inputY = browser.find_element_by_xpath("//input[@id='answer']")
    inputY.send_keys(y)

    check_box = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check_box.click()

    robot_check = browser.find_element_by_css_selector("[for='robotsRule']")
    robot_check.click()

    submit_btn = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit_btn.click()

finally:

    time.sleep(10)
    browser.quit()


