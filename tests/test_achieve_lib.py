import pytest
from settings import *


class TestAchievementsLibraryPositive:

    def test_get_list_of_achievements(self, get_list_of_achievements):
        """Метод GET. Проверяем что запрос списка наград возвращает не пустой список."""
        assert get_list_of_achievements

    @pytest.mark.parametrize('title', ['oio', 'koio', 'aoteereeaoeoraetgrtnergr', 'aoteereeaoeoraetgrtnergr1'],
                             ids=['3_symbols', '4_symbols', '24_symbols', '25_symbols'])
    def test_create_achieve_title(self, create_achieve_title, title):
        """Создание и удаление ачивки через методы POST и DELETE.
        Проверка позитивных граничных значений для title."""
        assert create_achieve_title

    @pytest.mark.parametrize('description', ['oio', 'koio', generate_string(254), generate_string(255)],
                             ids=['3_symbols', '4_symbols', '254_symbols', '255_symbols'])
    def test_create_achieve_desc(self, create_achieve_desc, description):
        """Создание и удаление ачивки через методы POST и DELETE.
        Проверка позитивных граничных значений для description."""
        assert create_achieve_desc

    @pytest.mark.parametrize('description_full', [generate_string(10), generate_string(11),
                                                  generate_string(254), generate_string(255)],
                             ids=['10_symbols', '11_symbols', '999_symbols', '1000_symbols'])
    def test_create_achieve_desc_full(self, create_achieve_desc_full, description_full):
        """Создание и удаление ачивки через методы POST и DELETE.
        Проверка позитивных граничных значений для description_full."""
        assert create_achieve_desc_full

    @pytest.mark.parametrize('tag', ['oio', 'koio', generate_string(39), generate_string(40)],
                             ids=['3_symbols', '4_symbols', '39_symbols', '40_symbols'])
    def test_create_achieve_tag(self, create_achieve_tag, tag):
        """Создание и удаление ачивки через методы POST и DELETE.
        Проверка позитивных граничных значений для tag."""
        assert create_achieve_tag

    def test_get_achievement(self, get_achievement):
        """Метод GET. Проверяем что запрос возвращает награду по её идентификатору."""
        assert get_achievement

    @pytest.mark.parametrize('title', ['oio', 'koio', 'aoteereeaoeoraetgrtnergr', 'aoteereeaoeoraetgrtnergr1'],
                             ids=['3_symbols', '4_symbols', '24_symbols', '25_symbols'])
    def test_update_achieve_title(self, update_achieve_title, title):
        """Метод PATCH. Проверяем что запрос может обновлять данные награды по её идентификатору.
        Сначала создается ачивка и извлекается её id для PATCH запроса, потом она удаляется через DELETE.
        Проверка позитивных граничных значений для title."""
        assert update_achieve_title

    @pytest.mark.parametrize('description', ['oio', 'koio', generate_string(254), generate_string(255)],
                             ids=['3_symbols', '4_symbols', '254_symbols', '255_symbols'])
    def test_update_achieve_desc(self, update_achieve_desc, description):
        """Метод PATCH. Проверяем что запрос может обновлять данные награды по её идентификатору.
        Сначала создается ачивка и извлекается её id для PATCH запроса, потом она удаляется через DELETE.
        Проверка позитивных граничных значений для description."""
        assert update_achieve_desc

    @pytest.mark.parametrize('desc_full', [generate_string(10), generate_string(11),
                                           generate_string(999), generate_string(1000)],
                             ids=['10_symbols', '11_symbols', '999_symbols', '1000_symbols'])
    def test_update_achieve_desc_full(self, update_achieve_desc_full, desc_full):
        """Метод PATCH. Проверяем что запрос может обновлять данные награды по её идентификатору.
        Сначала создается ачивка и извлекается её id для PATCH запроса, потом она удаляется через DELETE.
        Проверка позитивных граничных значений для description_full."""
        assert update_achieve_desc_full

    @pytest.mark.parametrize('tag', [generate_string(3), generate_string(4),
                                     generate_string(39), generate_string(40)],
                             ids=['3_symbols', '4_symbols', '39_symbols', '40_symbols'])
    def test_update_achieve_tag(self, update_achieve_tag, tag):
        """Метод PATCH. Проверяем что запрос может обновлять данные награды по её идентификатору.
        Сначала создается ачивка и извлекается её id для PATCH запроса, потом она удаляется через DELETE.
        Проверка позитивных граничных значений для tag."""
        assert update_achieve_tag


class TestAchievementsLibraryNegative:

    @pytest.mark.parametrize('rank', [' ', 'пример', 'aotee', '@$$%&*(', 78979],
                             ids=['space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_get_list_of_achieve_rank_neg(self, get_list_of_achieve_rank_neg, rank):
        """Метод GET. Негативная проверка параметра rank."""
        assert get_list_of_achieve_rank_neg

    def test_get_list_of_achieve_title_neg(self, get_list_of_achieve_title_neg):
        """Метод GET. Негативная проверка параметра title."""
        assert get_list_of_achieve_title_neg

    def test_get_list_of_achieve_destructive(self, get_list_of_achieve_destructive):
        """Метод GET. Деструктивное тестирование. Мы пытаемся сломать систему,
         вызывая известный эндпоинт с неподдерживаемым типом запроса PUT/PATCH/DELETE."""
        assert get_list_of_achieve_destructive

    @pytest.mark.parametrize('org_id', ['', 'aotee', '@$$%&*(', '78979'],
                             ids=['empty', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_get_list_of_achieve_invalid_org_id(self, get_list_of_achieve_invalid_org_id, org_id):
        """Метод GET. Негативная проверка параметра ORGANIZATION-ID."""
        assert get_list_of_achieve_invalid_org_id

    @pytest.mark.parametrize('body', ['', ' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                             ids=['empty', 'space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_create_achieve_body_neg(self, create_achieve_body_neg, body):
        """Метод POST. Негативный тест с некорректным вводом."""
        assert create_achieve_body_neg

    @pytest.mark.parametrize('title', ['oi', generate_string(26)],
                             ids=['2_symbols', '26_symbols'])
    def test_create_achieve_negative_title(self, create_achieve_title_neg, title):
        """Метод POST. Негативный тест с некорректным вводом.
         Проверка на анализ граничных значений и эквивалентное разбиение строки title."""
        assert create_achieve_title_neg

    @pytest.mark.parametrize('description', ['oi', generate_string(256)],
                             ids=['2_symbols', '256_symbols'])
    def test_create_achieve_negative_desc(self, create_achieve_negative_desc, description):
        """Метод POST. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки description."""
        assert create_achieve_negative_desc

    @pytest.mark.parametrize('description_full', [generate_string(9), generate_string(1001)],
                             ids=['9_symbols', '1001_symbol'])
    def test_create_achieve_negative_desc_full(self, create_achieve_negative_desc_full, description_full):
        """Метод POST. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки description_full."""
        assert create_achieve_negative_desc_full

    @pytest.mark.parametrize('tag', [generate_string(2), generate_string(41)],
                             ids=['2_symbols', '41_symbol'])
    def test_create_achieve_negative_tag(self, create_achieve_negative_tag, tag):
        """Метод POST. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки tag."""
        assert create_achieve_negative_tag

    def test_create_achievement_destructive(self, create_achievement_destructive):
        """Метод POST. Деструктивное тестирование. Мы пытаемся сломать систему,
         вызывая известный эндпоинт с неподдерживаемым типом запроса PUT/PATCH/DELETE."""
        assert create_achievement_destructive

    @pytest.mark.parametrize('org_id', ['', english_chars(), special_chars(), '78979'],
                             ids=['empty', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_create_achieve_invalid_org_id(self, create_achieve_invalid_org_id, org_id):
        """Метод POST. Негативный тест с невалидным вводом ORGANIZATION-ID"""
        assert create_achieve_invalid_org_id

    @pytest.mark.parametrize('uuid', ['', ' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                             ids=['empty', 'space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_get_achieve_invalid_id(self, get_achieve_invalid_id, uuid):
        """Метод GET. Негативный тест с невалидным вводом id награды."""
        assert get_achieve_invalid_id

    @pytest.mark.parametrize('uuid', ['', ' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                             ids=['empty', 'space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_update_achieve_id_negative(self, update_achieve_id_negative, uuid):
        """Метод PATCH. Негативный тест с некорректным вводом."""
        assert update_achieve_id_negative

    @pytest.mark.parametrize('title', ['oi', generate_string(26)],
                             ids=['2_symbols', '26_symbols'])
    def test_update_achieve_title_negative(self, update_achieve_title_negative, title):
        """Метод PATCH. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки title."""
        assert update_achieve_title_negative

    @pytest.mark.parametrize('description', ['oi', generate_string(256)],
                             ids=['2_symbols', '256_symbols'])
    def test_update_achieve_desc_negative(self, update_achieve_desc_negative, description):
        """Метод PATCH. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки description."""
        assert update_achieve_desc_negative

    @pytest.mark.parametrize('desc_full', [generate_string(9), generate_string(1001)],
                             ids=['9_symbols', '1001_symbols'])
    def test_update_achieve_desc_full_neg(self, update_achieve_desc_full_neg, desc_full):
        """Метод PATCH. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки description_full."""
        assert update_achieve_desc_full_neg

    @pytest.mark.parametrize('tag', [generate_string(2), generate_string(41)],
                             ids=['2_symbols', '41_symbols'])
    def test_update_achieve_tag_neg(self, update_achieve_tag_neg, tag):
        """Метод PATCH. Негативный тест с некорректным вводом.
        Проверка на анализ граничных значений и эквивалентное разбиение строки tag."""
        assert update_achieve_tag_neg

    def test_update_achieve_destructive(self, update_achieve_destructive):
        """Метод PATCH. Деструктивное тестирование. Мы пытаемся сломать систему,
         вызывая известный эндпоинт с неподдерживаемым типом запроса POST/PUT."""
        assert update_achieve_destructive

    @pytest.mark.parametrize('uuid', [' ', 'пример', 'aotee', '@$$%&*(', '78979'],
                             ids=['space', 'rus_symbols', 'eng_symbols', 'spec_symbols', 'numeric'])
    def test_delete_achieve_negative(self, delete_achieve_negative, uuid):
        """Метод DELETE. Негативный тест с некорректным вводом."""
        assert delete_achieve_negative
