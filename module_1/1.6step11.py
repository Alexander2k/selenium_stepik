import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fn = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys('Napoleon')

    ln = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys('Bonaparte')

    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys('napole@on.com')

    # phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']").send_keys('555555555')
    #
    # address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys('France')

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
