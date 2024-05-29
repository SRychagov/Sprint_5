### Фикстуры - conftest.py
- driver - настройки веб-драйвера

### Локаторы описаны в файле - locators.py

### Регистрация пользователя - test_registration.py
- test_registration_success - Проверка успешная регистрации пользователя
- test_registration_without_name - Проверка регистрации без имени
- test_registration_password_less_6_symbols - Проверка регистрации с невалидным паролем
- test_registration_with_invalid_email - Проверка регистрации с некорректным email
- test_registration_existent_user - Проверка регистрации уже существующего пользователя

### Вход в аккаунт - test_login_account.py
- test_login_from_main_page - 
- test_login_via_account_button - 
- test_login_via_registration_page - 
- test_login_via_password_recovery - 

### Переход в личный кабинет - test_go_to_person_account.py
- test_go_to_personal_account - Проверка перехода по клику "Личный кабинет"

### Переход из личного кабинета в конструктор - test_go_to_constructor_from_person_account.py
- test_go_to_constructor_from_person_account - Проверка перехода по клику на "Конструктор"
- test_go_to_constructor_from_account_by_click_on_logo - Провервка перехода по клику на лого "Stellar Burgers"

### Выход из аккаунта - test_logout_account.py
- test_log_out_account - Проверка выхода из аккаунта по кнопке "Выйти" в личном кабинете

### Раздел "Конструктор" - test_constructor_page.py
- test_go_to_buns - Проверка перехода к разделу "Булки"
- test_go_to_sauces - Проверка перехода к разделу "Соусы"
- test_go_to_fil - Проверка перехода к разделу "Начинки"

