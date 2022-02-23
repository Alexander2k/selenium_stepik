import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome('../chromedriver.exe')

try:

    browser.get(link)

    treasure = browser.find_element_by_xpath("//img[@id='treasure']")
    print(treasure)
    tr_v = treasure.get_attribute('valuex')
    print(tr_v)
    y = calc(tr_v)

    inputY = browser.find_element_by_xpath("//input[@id='answer']")
    inputY.send_keys(y)

    check_box = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    check_box.click()

    robot_check = browser.find_element_by_xpath("//input[@id='robotsRule']")
    robot_check.click()

    submit_btn = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
