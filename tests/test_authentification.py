import pytest
from settings import *


def test_auth_user(auth_user):
    """Метод POST. Аутентификация пользователя."""
    assert auth_user


def test_auth_admin(auth_admin):
    """Метод POST. Аутентификация админа."""
    assert auth_admin


def test_update_login(update_login):
    """Метод PATCH. Обновление логина."""
    assert update_login


def test_update_password(update_password):
    """Метод PATCH. Обновление пароля."""
    assert update_password


                                       # Негативные тесты.


@pytest.mark.parametrize('login', ['', ' ', generate_string(4), generate_string(51), 'пример',
                                   'aotee', '@$$%&*(', 78979],
                         ids=['empty', 'space', '4_symbols', '51_symbols', 'rus_symbols', 'eng_symbols',
                              'spec_symbols', 'numeric'])
def test_auth_login_neg(login, auth_login_neg):
    """Метод POST. Негативный тест с невалидным вводом параметра login."""
    assert auth_login_neg


@pytest.mark.parametrize('password', ['', ' ', generate_string(4), generate_string(51), 'пример'],
                         ids=['empty', 'space', '4_symbols', '51_symbols', 'rus_symbols'])
def test_auth_password_neg(password, auth_password_neg):
    """Метод POST. Негативный тест с невалидным вводом параметра password."""
    assert auth_password_neg


@pytest.mark.parametrize('method', ['GET', 'PUT', 'PATCH', 'DELETE', 'HEAD'],
                         ids=['method_GET', 'method_PUT', 'method_PATCH', 'method_DELETE', 'method_HEAD'])
def test_auth_destructive(method, auth_destructive):
    """Метод POST. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса GET/PUT/PATCH/DELETE/HEAD."""
    assert auth_destructive


@pytest.mark.parametrize('user_id', [' ', 'пример', english_chars(), 765],
                         ids=['space', 'rus_symbols', 'eng_symbols', 'digits'])
def test_update_user_id_neg(user_id, update_user_id_neg):
    """Метод PATCH. Негативный тест с невалидным вводом параметра user_id."""
    assert update_user_id_neg


@pytest.mark.parametrize('login', [' ', 'пример', 765, gen_alphanum_random_str(4), gen_alphanum_random_str(51)],
                         ids=['space', 'rus_symbols', 'digits', '4_symbols', '51_symbols'])
def test_update_login_neg(login, update_login_neg):
    """Метод PATCH. Негативный тест с невалидным вводом параметра login."""
    assert update_login_neg


@pytest.mark.parametrize('password', [' ', 765, gen_alphanum_random_str(4), gen_alphanum_random_str(51)],
                         ids=['space', 'digits', '4_symbols', '51_symbols'])
def test_update_password_neg(password, update_password_neg):
    """Метод PATCH. Негативный тест с невалидным вводом параметра password."""
    assert update_password_neg


@pytest.mark.parametrize('method', ['GET', 'POST', 'PUT', 'DELETE', 'HEAD'],
                         ids=['method_GET', 'method_POST', 'method_PUT', 'method_DELETE', 'method_HEAD'])
def test_update_destructive(method, update_destructive):
    """Метод PATCH. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса GET/POST/PUT/DELETE/HEAD."""
    assert update_destructive
