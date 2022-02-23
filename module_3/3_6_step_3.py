import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.quit()


@pytest.mark.parametrize('ids', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_answer(browser, ids):
    answer = math.log(int(time.time()))

    link = f'https://stepik.org/lesson/{ids}/step/1'
    browser.get(link)
    browser.implicitly_wait(5)

    input_answer = browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
    input_answer.send_keys(answer)

    button = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
    button.click()

    browser.implicitly_wait(10)

    correct = browser.find_element(By.XPATH, "//pre[@class='smart-hints__hint']")
    assert correct.text == "Correct!", "ERROR"
