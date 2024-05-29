from locators import Locators
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    #Вход по кнопке "Войти в аккаунт" на главной
    def test_login_from_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.button_login).click()
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        assert driver.find_element(*Locators.button_order).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_login_via_account_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        assert driver.find_element(*Locators.button_order).is_displayed()

    #Вход через кнопку в форме регистрации
    def test_login_via_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.button_login_on_screen_reg).click()
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        assert driver.find_element(*Locators.button_order).is_displayed()

    #Вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.button_login).click()
        driver.find_element(*Locators.forgot_password_button).click()
        driver.find_element(*Locators.button_login_on_screen_rec).click()
        driver.find_element(*Locators.input_email).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password).send_keys('QWERTY123')
        driver.find_element(*Locators.button_login_page).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_order))
        assert driver.find_element(*Locators.button_order).is_displayed()
