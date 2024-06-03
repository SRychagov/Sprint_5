from locators import Locators
from conftest import driver
from data import Data, UrlPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogOutAccount:
    def test_log_out_account(self, driver):
        driver.get(UrlPage.login_page)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.button_login_page).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.button_log_out).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.label_login))

        assert driver.current_url == UrlPage.login_page
