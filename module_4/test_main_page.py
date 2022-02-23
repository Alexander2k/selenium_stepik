from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
