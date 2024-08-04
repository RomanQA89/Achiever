import pytest


def test_get_list_avatar_achieve(get_list_avatar_achieve):
    """Метод GET. Проверяем что запрос списка изображений наград возвращает не пустой список."""
    assert get_list_avatar_achieve


def test_get_list_templates_achieve(get_list_templates_achieve):
    """Метод GET. Проверяем что запрос списка фоновых изображений наград возвращает не пустой список."""
    assert get_list_templates_achieve


                                  # Негативные тесты.

@pytest.mark.parametrize('method', ['POST', 'PUT', 'PATCH', 'DELETE'],
                         ids=['method_POST', 'method_PUT', 'method_PATCH', 'method_DELETE'])
def test_get_list_avatar_achieve_destructive(method, get_list_avatar_achieve_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_avatar_achieve_destructive


@pytest.mark.parametrize('method', ['POST', 'PUT', 'PATCH', 'DELETE'],
                         ids=['method_POST', 'method_PUT', 'method_PATCH', 'method_DELETE'])
def test_get_list_templates_achieve_destructive(method, get_list_templates_achieve_destructive):
    """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
    вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT/PATCH/DELETE."""
    assert get_list_templates_achieve_destructive
