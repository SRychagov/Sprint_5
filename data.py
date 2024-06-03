from random import randint


class Data:
    name = 'Сергей'
    email = 'srychagov@ya.ru'
    password = 'QWERTY123'


class UrlPage:
    main_page = 'https://stellarburgers.nomoreparties.site/'
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    registration_page = 'https://stellarburgers.nomoreparties.site/register'
    personal_account_page = 'https://stellarburgers.nomoreparties.site/account/profile'


class RandomUser:
    name = f'Random{randint(0, 999)}Name'
    email = f'Random{randint(000, 999)}adress@ya.ru'
    password = f'Random{randint(000, 999)}'
