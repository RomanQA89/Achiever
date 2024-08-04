import pytest
import requests
from settings import *


def test_get_list_connections_org(get_list_connections_org):
    """Метод GET. Проверяем что запрос списка связей пользователей
     с организацией возвращает не пустой список."""
    assert get_list_connections_org


def test_get_connection_id_profile_id_org(get_connection_id_profile_id_org):
    """Метод GET. Проверяем что запрос связи пользователя
    с организацией возвращает не пустой список."""
    assert get_connection_id_profile_id_org


@pytest.mark.parametrize('link_weight', [0, 1], ids=['user', 'admin'])
@pytest.mark.parametrize('specialty', [generate_string(124), generate_string(125)],
                         ids=['124_symbols', '125_symbols'])
def test_update_connect_id_profile_id_org(link_weight, specialty, update_connect_id_profile_id_org):
    """Метод PATCH. Проверяем что запрос обновляет связь пользователя/админа с организацией.
    Проверка на граничные значения параметра specialty."""
    assert update_connect_id_profile_id_org

                                  # Негативные тесты.


@pytest.mark.parametrize('org_id', ['', 'aotee', '@$$%&*(', '78979'],
                         ids=['empty', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_get_list_connections_invalid_org_id(org_id, get_list_connections_invalid_org_id):
    """Метод GET. Негативная проверка параметра ORGANIZATION-ID."""
    assert get_list_connections_invalid_org_id


@pytest.mark.parametrize('profile_id', [' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                         ids=['space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_get_connection_invalid_id_profile(profile_id, get_connection_invalid_id_profile):
    """Метод GET. Негативная проверка параметра profile_id."""
    assert get_connection_invalid_id_profile


@pytest.mark.parametrize('link_id', ['', ' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                         ids=['empty', 'space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_update_connect_invalid_id_profile(link_id, update_connect_invalid_id_profile):
    """Метод PATCH. Проверяем что запрос обновляет связь пользователя/админа с организацией
     с невалидным link_id."""
    assert update_connect_invalid_id_profile


def test_update_connect_invalid_specialty(update_connect_invalid_specialty):
    """Метод PATCH. Негативная проверка на граничные значения параметра specialty."""
    assert update_connect_invalid_specialty


@pytest.mark.parametrize('method', ['POST', 'PUT', 'PATCH', 'DELETE'],
                         ids=['method_POST', 'method_PUT', 'method_PATCH', 'method_DELETE'])
def test_get_list_connect_org_destructive(method, get_list_connect_org_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_connect_org_destructive


@pytest.mark.parametrize('method', ['POST', 'PUT', 'DELETE'],
                         ids=['method_POST', 'method_PUT', 'method_DELETE'])
def test_get_connection_id_profile_destructive(method, get_connection_id_profile_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/DELETE."""
    assert get_connection_id_profile_destructive
