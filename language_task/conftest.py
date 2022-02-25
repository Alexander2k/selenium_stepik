import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='ru',
                     help="Choose user language")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    browser = None
    if browser_name == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(service=service, firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
