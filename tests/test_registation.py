from locators import Locators
from conftest import driver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    #Успешная регистрация
    def test_registration_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.input_name_reg).send_keys('Пользователь')
        driver.find_element(*Locators.input_email_reg).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password_reg).send_keys('QWERTY123')
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.label_login))
        assert driver.find_element(*Locators.label_login).text == 'Вход'

    #Регистрация без имени
    def test_registration_without_name(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.input_email_reg).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password_reg).send_keys('QWERTY123')
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_registration))
        assert driver.find_element(*Locators.header_registration).text == 'Регистрация'

    #Регистрация с паролем менее 6 символов
    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_password_less_6_symbols(self, password, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.input_name_reg).send_keys('Пользователь')
        driver.find_element(*Locators.input_email_reg).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password_reg).send_keys(password)
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.invalid_password))
        assert driver.find_element(*Locators.invalid_password).text == 'Некорректный пароль'

    #Регистрация с Email вне формата логин@домен
    @pytest.mark.parametrize('email', ['@mail.com', 'srychagov@ya.ru'])
    def test_registration_with_invalid_email(self, email, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.input_name_reg).send_keys('Пользователь')
        driver.find_element(*Locators.input_email_reg).send_keys(email)
        driver.find_element(*Locators.input_password_reg).send_keys('QWERTY123')
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'

    #Регистрация уже существующего пользователя
    def test_registration_existent_user(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.input_name_reg).send_keys('Сергей')
        driver.find_element(*Locators.input_email_reg).send_keys('srychagov@ya.ru')
        driver.find_element(*Locators.input_password_reg).send_keys('QWERTY123')
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'