import pytest
from selenium import webdriver
from data import UrlPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument('--window-size=1920,1080')
    driver.get(UrlPage.main_page)
    yield driver
    driver.quit()
