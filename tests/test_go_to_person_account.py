from locators import Locators
from conftest import driver
from data import Data, UrlPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPeronalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get(UrlPage.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.header_profile))
        assert driver.current_url == UrlPage.personal_account_page
