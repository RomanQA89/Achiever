import pytest
from settings import *


def test_get_list_profiles(get_list_profiles):
    """Метод GET. Получение списка профилей."""
    assert get_list_profiles


def test_get_profile(get_profile):
    """Метод GET. Получение профиля по его id."""
    assert get_profile


@pytest.mark.parametrize('f_name_update', [gen_alphanum_random_str(1), gen_alphanum_random_str(49),
                                           gen_alphanum_random_str(50)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_update_first_name_profile(f_name_update, update_first_name_profile):
    """Метод PATCH. Обновление имени профиля по его id."""
    assert update_first_name_profile


@pytest.mark.parametrize('l_name_update', [gen_alphanum_random_str(1), gen_alphanum_random_str(49),
                                           gen_alphanum_random_str(50)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_update_last_name_profile(l_name_update, update_last_name_profile):
    """Метод PATCH. Обновление last_name профиля по его id."""
    assert update_last_name_profile


@pytest.mark.parametrize('m_name_update', [gen_alphanum_random_str(1), gen_alphanum_random_str(49),
                                           gen_alphanum_random_str(50)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_update_middle_name_profile(m_name_update, update_middle_name_profile):
    """Метод PATCH. Обновление middle_name профиля по его id."""
    assert update_middle_name_profile


@pytest.mark.parametrize('b_date_update', ['0001-05-12', '9999-05-12', '2024-01-12', '2024-12-12', '2024-03-01',
                                           '2024-03-31'],
                         ids=['1_year', '9999_year', '1_month', '12_month', '1_day', '31_day'])
def test_update_birth_date_profile(b_date_update, update_birth_date_profile):
    """Метод PATCH. Обновление birth_date профиля по его id."""
    assert update_birth_date_profile


@pytest.mark.parametrize('ph_update', [gen_alphanum_random_str(1), gen_alphanum_random_str(29),
                                       gen_alphanum_random_str(30)],
                         ids=['1_symbol', '49_symbols', '50_symbols'])
def test_update_phone_profile(ph_update, update_phone_profile):
    """Метод PATCH. Обновление phone профиля по его id."""
    assert update_phone_profile


@pytest.mark.parametrize('em_update', ['u@example.com', 'user@e.com', 'user@example.ru'],
                         ids=['1_symbol_name_user', '1_symbol_domain_name', '2_symbol_domain'])
def test_update_email_profile(em_update, update_email_profile):
    """Метод PATCH. Обновление email профиля по его id."""
    assert update_email_profile


def test_update_photo_main_profile(update_photo_main_profile):
    """Метод PATCH. Обновление photo_main профиля по его id."""
    assert update_photo_main_profile


def test_update_photo_small_profile(update_photo_small_profile):
    """Метод PATCH. Обновление photo_small профиля по его id."""
    assert update_photo_small_profile


def test_delete_profile(delete_profile):
    """Метод DELETE. Удаление профиля по его id."""
    assert delete_profile


                                     # Негативные тесты.


@pytest.mark.parametrize('org_id', ['', english_chars(), special_chars(), 'organization id'],
                         ids=['empty', 'eng_symbols', 'spec_chars', 'words_with_space'])
def test_get_list_profiles_neg(org_id, get_list_profiles_neg):
    """Метод GET. Негативные проверки параметра organization_id."""
    assert get_list_profiles_neg


@pytest.mark.parametrize('method', ['POST', 'PUT', 'PATCH', 'DELETE'],
                         ids=['method_POST', 'method_PUT', 'method_PATCH', 'method_DELETE'])
def test_get_list_profiles_destructive(method, get_list_profiles_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_profiles_destructive


@pytest.mark.parametrize('profile_id', ['', ' ', generate_string(1), generate_string(37), russian_chars(),
                                        special_chars(), 123456, gen_alphanum_random_str(256),
                                        gen_alphanum_random_str(1000)],
                         ids=['empty', 'spase', '1_symbol', '37_symbols', 'rus_chars', 'spec_chars', 'digits',
                              '256_symbols', '1000_symbols'])
def test_get_profile_neg(profile_id, get_profile_neg):
    """Метод GET. Негативные проверки параметра profile_id."""
    assert get_profile_neg


@pytest.mark.parametrize('method', ['POST', 'PUT'],
                         ids=['method_POST', 'method_PUT'])
def test_get_profile_destructive(method, get_profile_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT."""
    assert get_profile_destructive


@pytest.mark.parametrize('profile_id', [' ', generate_string(1), generate_string(37), russian_chars(), 123456,
                                        gen_alphanum_random_str(256), gen_alphanum_random_str(1000)],
                         ids=['spase', '1_symbol', '37_symbols', 'rus_chars', 'digits', '256_symbols', '1000_symbols'])
def test_update_profile_id_neg(profile_id, update_profile_id_neg):
    """Метод PATCH. Негативные проверки параметра profile_id."""
    assert update_profile_id_neg


@pytest.mark.parametrize('first_name', [' ', generate_string(1), generate_string(51), special_chars(),
                                        123456, gen_alphanum_random_str(256), gen_alphanum_random_str(1000)],
                         ids=['spase', '1_symbol', '51_symbols', 'spec_chars', 'digits', '256_symbols', '1000_symbols'])
def test_update_profile_first_name_neg(first_name, update_profile_first_name_neg):
    """Метод PATCH. Негативные проверки параметра first_name."""
    assert update_profile_first_name_neg


@pytest.mark.parametrize('last_name', [' ', generate_string(1), generate_string(51), special_chars(), 123456,
                                       gen_alphanum_random_str(256), gen_alphanum_random_str(1000)],
                         ids=['spase', '1_symbol', '51_symbols', 'spec_chars', 'digits', '256_symbols', '1000_symbols'])
def test_update_profile_last_name_neg(last_name, update_profile_last_name_neg):
    """Метод PATCH. Негативные проверки параметра last_name."""
    assert update_profile_last_name_neg


@pytest.mark.parametrize('middle_name', [' ', generate_string(1), generate_string(51), special_chars(), 123456,
                                         gen_alphanum_random_str(256), gen_alphanum_random_str(1000)],
                         ids=['spase', '1_symbol', '51_symbols', 'spec_chars', 'digits', '256_symbols', '1000_symbols'])
def test_update_profile_middle_name_neg(middle_name, update_profile_middle_name_neg):
    """Метод PATCH. Негативные проверки параметра middle_name."""
    assert update_profile_middle_name_neg


@pytest.mark.parametrize('birth_date', ['0000-05-12', '10000-05-12', '2024-00-12', '2024-13-12', '2024-03-00',
                                        '2024-03-32', ' ', russian_chars(), english_chars(), special_chars(), 865],
                         ids=['0_year', '10000_year', '0_month', '13_month', '0_day', '32_day', 'space', 'rus_symbols',
                              'eng_symbols', 'spec_chars', 'digits'])
def test_update_profile_birth_date_neg(birth_date, update_profile_birth_date_neg):
    """Метод PATCH. Негативные проверки параметра birth_date."""
    assert update_profile_birth_date_neg


@pytest.mark.parametrize('phone', [' ', gen_alphanum_random_str(31), russian_chars(), english_chars(), special_chars()],
                         ids=[' ', '31_symbols', 'rus_symbols', 'eng_symbols', 'spec_chars'])
def test_update_profile_phone_neg(phone, update_profile_phone_neg):
    """Метод PATCH. Негативные проверки параметра phone."""
    assert update_profile_phone_neg


@pytest.mark.parametrize('email', ['@example.com', 'user@.com', 'user@example.', 'userexample.com', 'user@examplecom',
                                   f'{generate_string(308)}@example.com', 'us er@example.com', 'user@exam ple.com',
                                   'login@домен.рф)'],
                         ids=['without_name_user', 'without_domain_name', 'without_first_domain', 'without_@',
                              'without_dot', 'more_than_320_symbols', 'space_in_name', 'space_in_domain',
                              'domain_with_rus_symbols'])
def test_update_profile_email_neg(email, update_profile_email_neg):
    """Метод PATCH. Негативные проверки параметра email."""
    assert update_profile_email_neg


@pytest.mark.parametrize('photo_main', [' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['spase', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_update_profile_photo_main_neg(photo_main, update_profile_photo_main_neg):
    """Метод PATCH. Негативные проверки параметра photo_main."""
    assert update_profile_photo_main_neg


@pytest.mark.parametrize('photo_small', [' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['spase', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_update_profile_photo_small_neg(photo_small, update_profile_photo_small_neg):
    """Метод PATCH. Негативные проверки параметра photo_small."""
    assert update_profile_photo_small_neg


        # ПОКА ДАННЫЕ ТЕСТЫ РАБОТАЮТ НЕКОРРЕКТНО, В ЛЮБОМ СЛУЧАЕ ПОЯВЛЯЕТСЯ 200 СТАТУС-КОД!


@pytest.mark.parametrize('organ_id', ['', english_chars(), special_chars(), 'organization id'],
                         ids=['empty', 'eng_symbols', 'spec_chars', 'words_with_space'])
def test_delete_profile_org_id_neg(organ_id, delete_profile_org_id_neg):
    """Метод DELETE. Негативные проверки параметра ORGANIZATION-ID."""
    assert delete_profile_org_id_neg


@pytest.mark.parametrize('profile_id', [' ', generate_string(1), generate_string(37), russian_chars(), 123456,
                                        gen_alphanum_random_str(256), gen_alphanum_random_str(1000), special_chars()],
                         ids=['spase', '1_symbol', '37_symbols', 'rus_chars', 'digits', '256_symbols', '1000_symbols',
                              'spec_chars'])
def test_delete_profile_id_neg(profile_id, delete_profile_id_neg):
    """Метод DELETE. Негативные проверки параметра profile_id."""
    assert delete_profile_id_neg
