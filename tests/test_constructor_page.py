from locators import Locators
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorPage:
    # Переход к разделу "Булки"
    def test_go_to_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.fill_span).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.fill_span))
        driver.find_element(*Locators.buns_span).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.buns_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Булки'

    #Переход к разделу "Соусы"
    def test_go_to_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.sauces_span).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.sauces_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Соусы'


    # Переход к разделу "Начинки"
    def test_go_to_fil(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.fill_span).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.fill_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Начинки'
