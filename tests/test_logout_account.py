from locators import Locators
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogOutAccount:
    def test_log_out_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.button_log_out).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.label_login))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
