from locators import Locators
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPeronalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.header_profile))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
