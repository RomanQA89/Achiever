import pytest
from settings import *


def test_get_list_connections(get_list_connections):
    """Метод GET. Получение списка связей награда-пользователь."""
    assert get_list_connections


def test_get_achieves_of_user(get_achieves_of_user):
    """Метод GET. Получение списка наград определенного пользователя."""
    assert get_achieves_of_user


def test_assign_achieve_to_user(assign_achieve_to_user):
    """Метод POST. Присваивание награды определенному пользователю и последующее её удаление."""
    assert assign_achieve_to_user


def test_update_connect_achieve_user(update_connect_achieve_user):
    """Метод PATCH. Обновление связи награда-пользователь."""
    assert update_connect_achieve_user


                                     # Негативные тесты.


@pytest.mark.parametrize('method', ['PUT', 'PATCH', 'DELETE'],
                         ids=['method_PUT', 'method_PATCH', 'method_DELETE'])
def test_get_list_connect_destructive(method, get_list_connect_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса PUT/PATCH/DELETE."""
    assert get_list_connect_destructive


@pytest.mark.parametrize('user_id', [special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_get_achieves_of_user_id_neg(user_id, get_achieves_of_user_id_neg):
    """Метод GET. Негативные проверки параметра user_id."""
    assert get_achieves_of_user_id_neg


@pytest.mark.parametrize('method', ['POST', 'PUT'],
                         ids=['method_POST', 'method_PUT'])
def test_get_achieves_of_user_id_destructive(method, get_achieves_of_user_id_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
        вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT."""
    assert get_achieves_of_user_id_destructive


@pytest.mark.parametrize('user_id', ['', ' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['empty', 'space', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_assign_achieve_to_user_id_neg(user_id, assign_achieve_to_user_id_neg):
    """Метод POST. Негативные проверки параметра user_id."""
    assert assign_achieve_to_user_id_neg


@pytest.mark.parametrize('achieve_id', ['', ' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['empty', 'space', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_assign_achievement_id_neg(achieve_id, assign_achievement_id_neg):
    """Метод POST. Негативные проверки параметра achievement_id."""
    assert assign_achievement_id_neg


@pytest.mark.parametrize('method', ['PUT', 'PATCH', 'DELETE'],
                         ids=['method_PUT', 'method_PATCH', 'method_DELETE'])
def test_assign_achieve_to_user_destructive(method, assign_achieve_to_user_destructive):
    """Метод POST. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса PUT/PATCH/DELETE."""
    assert assign_achieve_to_user_destructive


@pytest.mark.parametrize('connect_id', [' ', 123456, english_chars(), russian_chars()],
                         ids=['space', 'digits', 'eng_symbols', 'rus_symbols'])
def test_update_connect_id_neg(connect_id, update_connect_id_neg):
    """Метод PATCH. Негативные проверки параметра id связи награда-пользователь."""
    assert update_connect_id_neg


@pytest.mark.parametrize('user_id', ['', ' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['empty', 'space', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_update_connect_user_id_neg(user_id, update_connect_user_id_neg):
    """Метод PATCH. Негативные проверки параметра user_id."""
    assert update_connect_user_id_neg


@pytest.mark.parametrize('achieve_id', ['', ' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['empty', 'space', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_update_connect_achieve_id_neg(achieve_id, update_connect_achieve_id_neg):
    """Метод PATCH. Негативные проверки параметра achievement_id."""
    assert update_connect_achieve_id_neg


@pytest.mark.parametrize('method', ['POST', 'PUT'],
                         ids=['method_POST', 'method_PUT'])
def test_update_connect_destructive(method, update_connect_destructive):
    """Метод PATCH. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT."""
    assert update_connect_destructive


@pytest.mark.parametrize('connect_id', [' ', special_chars(), 123456, english_chars(), russian_chars()],
                         ids=['space', 'spec_chars', 'digits', 'eng_symbols', 'rus_symbols'])
def test_deactivate_connect_id_neg(connect_id, deactivate_connect_id_neg):
    """Метод DELETE. Негативные проверки параметра id связи награда-пользователь."""
    assert deactivate_connect_id_neg


@pytest.mark.parametrize('method', ['POST', 'PUT'],
                         ids=['method_POST', 'method_PUT'])
def test_deactivate_connect_destructive(method, deactivate_connect_destructive):
    """Метод DELETE. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT."""
    assert deactivate_connect_destructive
