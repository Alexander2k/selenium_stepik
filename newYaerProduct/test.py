import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get(link)


try:
    button = browser.find_element(By.XPATH,  "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    button.click()

except Exception as e:
    print(e)

finally:
    time.sleep(5)
    browser.close()