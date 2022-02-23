import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome('../chromedriver.exe')

try:

    browser.get(link)
    num1 = browser.find_element_by_xpath("//span[@id='num1']")
    num2 = browser.find_element_by_xpath("//span[@id='num2']")

    answer = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))

    select.select_by_value(str(answer))

    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()


except Exception as e:
    print(e)

finally:
    time.sleep(5)
    browser.close()
    browser.quit()
