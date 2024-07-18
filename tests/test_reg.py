import pytest
from settings import *


def test_registration_user(registration_user):
    """Метод POST. Регистрация пользователя."""
    assert registration_user


def test_registration_admin(registration_admin):
    """Метод POST. Регистрация админа."""
    assert registration_admin


@pytest.mark.parametrize('login', [gen_alphanum_random_str(5), gen_alphanum_random_str(6),
                                   gen_alphanum_random_str(49), gen_alphanum_random_str(50)],
                         ids=['5_symbols', '6_symbols', '49_symbols', '50_symbols'])
def test_registration_login(login, registration_login):
    """Метод POST. Позитивная проверка граничных значений параметра login."""
    assert registration_login


@pytest.mark.parametrize('specialty', [generate_string(124), generate_string(125)],
                         ids=['124_symbols', '125_symbols'])
def test_registration_specialty(specialty, registration_specialty):
    """Метод POST. Позитивная проверка граничных значений параметра specialty."""
    assert registration_specialty


@pytest.mark.parametrize('start_work_date', ['0001-01-01', '9999-01-01', '9999-01-01', '9999-12-01',
                                             '0001-01-01', '0001-01-31'],
                         ids=['1_year', '9999_year', '1_month', '12_month', '1_day', '31_day'])
def test_reg_start_work_date(start_work_date, reg_start_work_date):
    """Метод POST. Позитивная проверка граничных значений параметра start_work_date."""
    assert reg_start_work_date


@pytest.mark.parametrize('password', [generate_string(5), generate_string(6),
                                      generate_string(49), generate_string(50)],
                         ids=['5_symbols', '6_symbols', '49_symbols', '50_symbols'])
def test_reg_password(password, reg_password):
    """Метод POST. Позитивная проверка граничных значений параметра password."""
    assert reg_password


@pytest.mark.parametrize('first_name', [generate_string(1), generate_string(49), generate_string(50)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_reg_first_name(first_name, reg_first_name):
    """Метод POST. Позитивная проверка граничных значений параметра first_name."""
    assert reg_first_name


@pytest.mark.parametrize('last_name', [generate_string(1), generate_string(49), generate_string(50)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_reg_last_name(last_name, reg_last_name):
    """Метод POST. Позитивная проверка граничных значений параметра last_name."""
    assert reg_last_name


@pytest.mark.parametrize('phone', [generate_string(1), generate_string(29), generate_string(30)],
                         ids=['1_symbol', '29_symbols', '30_symbols'])
def test_reg_phone(phone, reg_phone):
    """Метод POST. Позитивная проверка граничных значений параметра phone."""
    assert reg_phone


@pytest.mark.parametrize('email', ['u@example.com', 'user@e.com', 'user@example.ru'],
                         ids=['1_symbol_name_user', '1_symbol_domain_name', '2_symbol_domain'])
def test_reg_email(email, reg_email):
    """Метод POST. Позитивная проверка граничных значений параметра email."""
    assert reg_email


                                    # Негативные тесты.


@pytest.mark.parametrize('login', ['', ' ', gen_alphanum_random_str(4), gen_alphanum_random_str(51),
                                   gen_alphanum_random_str(256), gen_alphanum_random_str(1000), 'User1'],
                         ids=['empty', 'spase', '4_symbols', '51_symbol', '256_symbols',
                              '1000_symbols', 'already_existing_login'])
def test_reg_login_neg(login, reg_login_neg):
    """Метод POST. Негативные проверки параметра login."""
    assert reg_login_neg


# @pytest.mark.parametrize('login', ['', ' ', gen_alphanum_random_str(4), gen_alphanum_random_str(51), russian_chars(),
#                                    special_chars(), 123456, gen_alphanum_random_str(256),
#                                    gen_alphanum_random_str(1000), 'User'],
#                          ids=['empty', 'spase', '4_symbols', '51_symbol', 'rus_chars', 'spec_chars',
#                               'digits', '256_symbols', '1000_symbols', 'already_existing_login'])


@pytest.mark.parametrize('specialty', [gen_alphanum_random_str(126), gen_alphanum_random_str(256),
                                       gen_alphanum_random_str(1000)],
                         ids=['126_symbol', '256_symbols', '1000_symbols'])
def test_reg_specialty_neg(specialty, reg_specialty_neg):
    """Метод POST. Негативные проверки параметра specialty."""
    assert reg_specialty_neg


@pytest.mark.parametrize('start_work_date', ['', ' ', '0000-01-01', '10000-01-01', '9999-00-01', '9999-13-01',
                                             '0001-01-00', '0001-01-32', russian_chars(), english_chars(),
                                             special_chars(), 745],
                         ids=['empty', 'space', '0_year', '10000_year', '0_month', '13_month', '0_day', '32_day',
                              'rus_symbols', 'eng_chars', 'spec_cars', 'digits'])
def test_reg_start_work_date_neg(start_work_date, reg_start_work_date_neg):
    """Метод POST. Негативные проверки параметра start_work_date."""
    assert reg_start_work_date_neg


@pytest.mark.parametrize('password', ['', ' ', generate_string(4), generate_string(51),
                                      generate_string(256), generate_string(1000)],
                         ids=['empty', 'spase', '4_symbols', '51_symbol', '256_symbols', '1000_symbols'])
def test_reg_password_neg(password, reg_password_neg):
    """Метод POST. Негативные проверки параметра password."""
    assert reg_password_neg


@pytest.mark.parametrize('first_name', ['', ' ', generate_string(51), generate_string(256), generate_string(1000)],
                         ids=['empty', 'spase', '51_symbol', '256_symbols', '1000_symbols'])
def test_reg_first_name_neg(first_name, reg_first_name_neg):
    """Метод POST. Негативные проверки параметра first_name."""
    assert reg_first_name_neg


@pytest.mark.parametrize('last_name', ['', ' ', generate_string(51), generate_string(256), generate_string(1000)],
                         ids=['empty', 'spase', '51_symbol', '256_symbols', '1000_symbols'])
def test_reg_last_name_neg(last_name, reg_last_name_neg):
    """Метод POST. Негативные проверки параметра last_name."""
    assert reg_last_name_neg


@pytest.mark.parametrize('phone', ['', ' ', digits(), generate_string(256), generate_string(1000)],
                         ids=['empty', 'spase', '31_symbol', '256_symbols', '1000_symbols'])
def test_reg_phone_neg(phone, reg_phone_neg):
    """Метод POST. Негативные проверки параметра phone."""
    assert reg_phone_neg


@pytest.mark.parametrize('email', ['', ' ', generate_string(256), generate_string(1000), numbers(), special_chars(),
                                   '@example.com', 'user@.com', 'user@example.', 'юзер@example.com'],
                         ids=['empty', 'spase', '256_symbols', '1000_symbols', 'digits', 'spec_chars',
                              '0_symbol_name_user', '0_symbol_domain_name', 'without_domain', 'rus_name_user'])
def test_reg_email_neg(email, reg_email_neg):
    """Метод POST. Негативные проверки параметра email."""
    assert reg_email_neg


@pytest.mark.parametrize('method', ['GET', 'PUT', 'PATCH', 'DELETE', 'HEAD'],
                         ids=['method_GET', 'method_PUT', 'method_PATCH', 'method_DELETE', 'method_HEAD'])
def test_reg_destructive(method, reg_destructive):
    """Метод POST. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса GET/PUT/PATCH/DELETE/HEAD."""
    assert reg_destructive


@pytest.mark.parametrize('org_id', ['', ' ', generate_string(8), russian_chars(), 765, special_chars()],
                         ids=['empty', 'spase', 'eng_symbols', 'rus_symbols', 'digits', 'spec_chars'])
def test_reg_org_id_neg(org_id, reg_org_id_neg):
    """Метод POST. Негативные проверки параметра organization_id."""
    assert reg_org_id_neg


# @pytest.mark.parametrize('link_weight', [' ', generate_string(8), russian_chars(), 2, 765, special_chars()],
#                          ids=['spase', 'eng_symbols', 'rus_symbols', 'two', 'digits', 'spec_chars'])
# def test_reg_link_weight_neg(link_weight, reg_link_weight_neg):
#     """Метод POST. Негативные проверки параметра link_weight."""
#     assert reg_link_weight_neg
