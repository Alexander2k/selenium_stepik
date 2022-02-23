import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
try:

    browser.get(link)

    # Считать значение для переменной x.
    number = browser.find_element(By.XPATH, "//span[@id='input_value']")
    number = number.text

    # Посчитать математическую функцию от x.
    y = calc(int(number))

    # Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0,130);")

    # Ввести ответ в текстовое поле
    inp = browser.find_element(By.XPATH, "//input[@id='answer']")
    inp.send_keys(y)

    # Выбрать checkbox "I'm the robot".
    robot_check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robot_check.click()

    # Переключить radiobutton "Robots rule!".
    robot_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_radio.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    button.click()

    text = browser.switch_to.alert
    print(text.text)


except Exception as e:
    pass


finally:
    browser.quit()
    browser.close()
