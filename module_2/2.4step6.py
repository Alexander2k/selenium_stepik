import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/cats.html'

browser= webdriver.Chrome()
browser.get(link)

browser.implicitly_wait(5)

browser.find_element(By.ID,"button")

time.sleep(5)
browser.quit()