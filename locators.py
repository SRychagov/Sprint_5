from selenium.webdriver.common.by import By

class Locators:

    # Локаторы для главной страницы
    button_login = (By.XPATH, "//button[text()='Войти в аккаунт']")
    button_order = (By.XPATH, "//button[text()='Оформить заказ']")
    pack_burger = By.XPATH, './/h1[text() = "Соберите бургер"]'
    sauces_span = By.XPATH, './/span[text() = "Соусы"]'
    fill_span = By.XPATH, './/span[text() = "Начинки"]'
    buns_span = By.XPATH, './/span[text() = "Булки"]'
    BREAD_LIST = (By.XPATH, "//h2[contains(text(),'Булки')]")
    SAUCE_LIST = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    FILLING_LIST = (By.XPATH, "//h2[contains(text(),'Начинки')]")
    active_div_in_constructor = By.XPATH, './/div[contains(@class, "current")]/span'

    # Локаторы для хедера
    account_button = By.XPATH, './/p[text() = "Личный Кабинет"]'
    button_constructor = (By.XPATH, './/p[text()="Конструктор"]')
    logo = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')
    logo2 = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    logo3 = (By.XPATH, '//a[@class="active" and @aria-current="page"]')

    # Локаторы для логина
    input_email = (By.XPATH, './/label[text() = "Email"]/following-sibling::input')
    input_password = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input')
    button_login_page = (By.XPATH, './/button[text() = "Войти"]')
    forgot_password_button = (By.XPATH, './/a[text() = "Восстановить пароль"]')
    label_login = (By.XPATH, './/h2[text() = "Вход"]')

    # Локаторы для регистрации
    label_registation = header_registration = By.XPATH, './/h2[text() = "Регистрация"]'
    input_name_reg = By.XPATH, './/label[text() = "Имя"]/following-sibling::input'
    input_email_reg = (By.XPATH, '//label[text()="Email"]/following-sibling::input[@type="text"]')
    input_password_reg = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    invalid_password = (By.XPATH, './/p[text(),"Некорректный пароль"]')
    header_exist_user = By.XPATH, './/p[text() = "Такой пользователь уже существует"]'
    button_registration = (By.XPATH, './/button[text() = "Зарегистрироваться"]')
    button_login_on_screen_reg = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти" на экране регистрации у "Уже зарегестрированны?"

    # Локаторы для восстановления пароля
    button_recovery_password = (By.XPATH, "//button[text()='Восстановить']")  # кнопка "Восстановить" на экране восстановления пароля
    button_login_on_screen_rec = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти" на экране восстановления пароля

    # Локаторы для личного кабинета
    button_log_out = (By.XPATH, "//button[text()='Выход']")
    header_profile = By.XPATH, './/a[text() = "Профиль"]'
