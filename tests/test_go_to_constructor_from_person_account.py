from locators import Locators
from conftest import driver
from data import Data, UrlPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTransitionToConstructor:
    def test_go_to_constructor_from_person_account(self, driver):
        driver.get(UrlPage.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.button_constructor).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.button_constructor).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.pack_burger))
        assert driver.find_element(*Locators.pack_burger).is_displayed()

    def test_go_to_constructor_from_account_by_click_on_logo(self, driver):
        driver.get(UrlPage.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.pack_burger))
        assert driver.find_element(*Locators.pack_burger).is_displayed()
