import pytest


def test_get_list_avatar_achieve(get_list_avatar_achieve):
    """Метод GET. Проверяем что запрос списка изображений наград возвращает не пустой список."""
    assert get_list_avatar_achieve


def test_get_list_templates_achieve(get_list_templates_achieve):
    """Метод GET. Проверяем что запрос списка фоновых изображений наград возвращает не пустой список."""
    assert get_list_templates_achieve


                                  # Негативные тесты.

def test_get_list_avatar_achieve_destruction(get_list_avatar_achieve_destruction):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_avatar_achieve_destruction


def test_get_list_templates_achieve_destructive(get_list_templates_achieve_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_templates_achieve_destructive
