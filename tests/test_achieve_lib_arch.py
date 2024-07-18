import pytest
import requests
from settings import *


def test_get_list_inactive_achieve(get_list_inactive_achieve):
    """Метод GET. Проверяем что запрос списка неактивных наград возвращает не пустой список."""
    assert get_list_inactive_achieve


def test_return_achievement(return_achievement):
    """Метод PATCH. Проверяем что запрос возвращает неактивную награду. Далее удаляем восстановленную награду."""
    assert return_achievement

                                  # Негативные тесты.


@pytest.mark.parametrize('rank', [' ', 'пример', 'aotee', '@$$%&*(', 78979],
                         ids=['space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_get_list_inactive_achieve_negative_rank(rank, get_list_inactive_achieve_negative_rank):
    """Метод GET. Негативная проверка параметра rank."""
    assert get_list_inactive_achieve_negative_rank


def test_get_list_inactive_achieve_negative_title(get_list_inactive_achieve_negative_title):
    """Метод GET. Негативная проверка параметра title."""
    assert get_list_inactive_achieve_negative_title


@pytest.mark.parametrize('org_id', ['', ' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                         ids=['empty', 'space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_get_list_inactive_achieve_neg_org_id(org_id, get_list_inactive_achieve_neg_org_id):
    """Метод GET. Негативная проверка параметра title."""
    assert get_list_inactive_achieve_neg_org_id


def test_get_list_inactive_achieve_destructive(get_list_inactive_achieve_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_inactive_achieve_destructive


@pytest.mark.parametrize('uuid', [' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                         ids=['space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
def test_return_achieve_id_negative(uuid, return_achieve_id_negative):
    """Метод PATCH. Негативный тест с некорректным вводом."""
    assert return_achieve_id_negative
