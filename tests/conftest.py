import pytest
import requests
from settings import *
from api import api_request
from tests.test_achieve_lib import *


# Фикстура для запроса списка ачивок.
@pytest.fixture(scope='module')
def get_list_of_achievements():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements/', headers=headers)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для создания достижений с title и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_title(title):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": title,
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=headers)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    assert ach_id
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с description и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_desc(description):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "description": description,
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=headers)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    assert ach_id
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с description_full и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_desc_full(description_full):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "description": "testing description",
        "description_full": description_full,
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=headers)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    assert ach_id
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с tag и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_tag(tag):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data = {
        "tag": tag,
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=headers)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    assert ach_id
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для возвращения id определенной ачивки.
@pytest.fixture(scope='function')
def get_achievement():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = requests.get(f'{base_url}/achievements/', headers=headers)
    id_achieve = response.json()[0].get('id')  # ID самой первой ачивки, если нужна другая то меняем цифру в [].
    response_get = api_request(session, 'GET', f'{base_url}/achievements/{id_achieve}/')
    yield session
    assert response_get.status_code == 200
    assert len(response_get.json()) > 0


# Фикстура для обновления данных ачивки для параметра title.
@pytest.fixture(scope='function')
def update_achieve_title(title):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        "title": title
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    response_title = response_patch.json().get('data').get('title')
    yield session
    assert response_patch.status_code == 200
    assert data_create['title'] != response_title              # Проверка на обновление title.
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления данных ачивки для параметра description.
@pytest.fixture(scope='function')
def update_achieve_desc(description):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        "description": description
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    response_desc = response_patch.json().get('data').get('title')
    yield session
    assert response_patch.status_code == 200
    assert data_create['description'] != response_desc             # Проверка на обновление description.
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления данных ачивки для параметра description_full.
@pytest.fixture(scope='function')
def update_achieve_desc_full(desc_full):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        "description_full": desc_full
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    response_desc_full = response_patch.json().get('data').get('title')
    yield session
    assert response_patch.status_code == 200
    assert data_create['description_full'] != response_desc_full         # Проверка на обновление description_full.
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления данных ачивки для параметра tag.
@pytest.fixture(scope='function')
def update_achieve_tag(tag):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        "tag": tag
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    response_tag = response_patch.json().get('data').get('title')
    yield session
    assert response_patch.status_code == 200
    assert data_create['tag'] != response_tag              # Проверка на обновление tag.
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для получения списка неактивных наград.
@pytest.fixture(scope='function')
def get_list_inactive_achieve():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/', headers=headers)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для восстановления неактивной награды.
@pytest.fixture(scope='function')
def return_achievement():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_get = requests.get(f'{base_url}/achievements-archive/', headers=headers)
    ach_id = response_get.json()[5].get('id')             # Номер ачивки [] из списка, можно номер изменить
    response = api_request(session, 'PATCH', f'{base_url}/achievements-archive/{ach_id}/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для получения списка изображений наград.
@pytest.fixture(scope='function')
def get_list_avatar_achieve():
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/avatar-images/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения списка фоновых изображений наград.
@pytest.fixture(scope='function')
def get_list_templates_achieve():
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/templates-images/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения списка связей пользователей с организацией.
@pytest.fixture(scope='function')
def get_list_connections_org():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/link/', headers=headers)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения связи пользователя с организацией.
@pytest.fixture(scope='function')
def get_connection_id_profile_id_org():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_get = requests.get(f'{base_url}/link/', headers=headers)
    profile_id = response_get.json()[0].get('profile_id')
    response = api_request(session, 'GET', f'{base_url}/link/{profile_id}/', headers=headers)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для обновления связи пользователя/админа с организацией.
@pytest.fixture(scope='function')
def update_connect_id_profile_id_org(link_weight, specialty):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_link = requests.get(f'{base_url}/link/', headers=headers)
    link_id = response_link.json()[0].get('link_id')
    data = {
        "link_weight": link_weight,
        "start_work_date": "2024-05-12",
        "specialty": specialty
    }
    response = api_request(session, 'PATCH', f'{base_url}/link/{link_id}/', data=data)
    yield session
    assert response.status_code == 200


# Фикстура для запроса списка организаций и регистрации пользователя и последующая его деактивация.
@pytest.fixture(scope='function')
def registration_user():
    session = requests.Session()
    response_org = api_request(session, 'GET', f'{base_url}/organization/')
    assert response_org.status_code == 200
    assert len(response_org.json()) > 0
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    assert response_reg.status_code == 201
    yield profile_id
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_del = api_request(session, 'DELETE', f'{base_url}/profiles/{profile_id}', headers=headers)
    assert response_del.status_code == 200
    print('logout')


# Фикстура для запроса списка организаций и регистрации админа и последующая его деактивация.
@pytest.fixture(scope='module')
def registration_admin():
    session = requests.Session()
    response_org = api_request(session, 'GET', f'{base_url}/organization/')
    assert response_org.status_code == 200
    assert len(response_org.json()) > 0
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?link_weight=1&organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    assert response_reg.status_code == 201
    yield session
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_del = api_request(session, 'DELETE', f'{base_url}/profiles/{profile_id}', headers=headers)
    assert response_del.status_code == 200
    print('logout')


# Фикстура для регистрации и проверки позитивных граничных значений login.
@pytest.fixture(scope='function')
def registration_login(login):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": login,
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    assert response_reg.status_code == 201
    yield profile_id
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений specialty.
@pytest.fixture(scope='function')
def registration_specialty(specialty):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": specialty,
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    assert response_reg.status_code == 201
    yield profile_id
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений start_work_date.
@pytest.fixture(scope='function')
def reg_start_work_date(start_work_date):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": start_work_date,
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений password.
@pytest.fixture(scope='function')
def reg_password(password):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": password,
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений first_name.
@pytest.fixture(scope='function')
def reg_first_name(first_name):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": first_name,
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений last_name.
@pytest.fixture(scope='function')
def reg_last_name(last_name):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": last_name,
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки позитивных граничных значений phone.
@pytest.fixture(scope='function')
def reg_phone(phone):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": phone,
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для регистрации и проверки значений email.
@pytest.fixture(scope='function')
def reg_email(email):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": email
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    profile_id = response_reg.json().get('profile_id')
    yield session
    assert response_reg.status_code == 201
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для аутентификации пользователя.
@pytest.fixture(scope='function')
def auth_user():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    login = response_reg.json().get('login')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_auth = {
        "login": login,
        "password": data_reg['password']
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    yield session
    assert response_auth.status_code == 200
    assert len(response_auth.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для аутентификации админа.
@pytest.fixture(scope='function')
def auth_admin():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?link_weight=1&organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    login = response_reg.json().get('login')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_auth = {
        "login": login,
        "password": data_reg['password']
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    yield session
    assert response_auth.status_code == 200
    assert len(response_auth.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для обновления логина.
@pytest.fixture(scope='function')
def update_login():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    user_id = response_reg.json().get('user_id')
    login = response_reg.json().get('login')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_update = {
        "login": gen_alphanum_random_str(6)
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    login_update = response_update.json().get('login')
    yield session
    assert response_update.status_code == 200
    assert len(response_update.json()) > 0
    assert login != login_update   # Проверка на обновление логина
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для обновления пароля.
@pytest.fixture(scope='function')
def update_password():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    user_id = response_reg.json().get('user_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_update = {
        "password": gen_alphanum_random_str(6)
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    pass_update = response_update.json().get('password')
    yield session
    assert response_update.status_code == 200
    assert len(response_update.json()) > 0
    assert data_reg['password'] != pass_update  # Проверка на обновление пароля
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


                               # Фикстуры для негативных тестов.


# Фикстура для запроса списка наград с параметром rank.
@pytest.fixture(scope='function')
def get_list_of_achieve_rank_neg(rank):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements/?rank={rank}', headers=headers)
    yield session
    assert response.status_code == 400
    assert len(response.json()) > 0


# Фикстура для запроса списка наград с параметром title.
@pytest.fixture(scope='function')
def get_list_of_achieve_title_neg():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements/?title={"+)(*?"}', headers=headers)
    yield session
    assert response.status_code == 404
    assert len(response.json()) > 0


# Фикстура для запроса списка наград с невалидными методами запроса.
@pytest.fixture(scope='function')
def get_list_of_achieve_destructive():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_put = api_request(session, 'PUT', f'{base_url}/achievements/', headers=headers)
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/', headers=headers)
    response_del = api_request(session, 'DELETE', f'{base_url}/achievements/', headers=headers)
    yield session
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для запроса списка наград с невалидным ORGANIZATION-ID.
@pytest.fixture(scope='function')
def get_list_of_achieve_invalid_org_id(org_id):
    session = requests.Session()
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    if org_id == '':
        response = api_request(session, 'GET', f'{base_url}/achievements/', headers=headers)
        yield session
        assert response.status_code == 404
    else:
        response = api_request(session, 'GET', f'{base_url}/achievements/', headers=headers)
        yield session
        assert response.status_code == 400


# Фикстура для создания достижений с невалидным boby.
@pytest.fixture(scope='function')
def create_achieve_body_neg(body):
    session = requests.Session()
    if body == '':
        response = api_request(session, 'POST', f'{base_url}/achievements/', data=body)
        yield session
        assert response.status_code == 400
    else:
        response = api_request(session, 'POST', f'{base_url}/achievements/', data=body)
        yield session
        assert response.status_code == 500


# Фикстура для создания достижений с невалидным title.
@pytest.fixture(scope='function')
def create_achieve_title_neg(title):
    session = requests.Session()
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": title,
        "description": "testing description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data)
    yield session
    assert response.status_code == 400


# Фикстура для создания достижений с невалидным description.
@pytest.fixture(scope='function')
def create_achieve_negative_desc(description):
    session = requests.Session()
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": description,
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data)
    yield session
    assert response.status_code == 400


# Фикстура для создания достижений с невалидным description_full.
@pytest.fixture(scope='function')
def create_achieve_negative_desc_full(description_full):
    session = requests.Session()
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "test description",
        "description_full": description_full,
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data)
    yield session
    assert response.status_code == 400


# Фикстура для создания достижений с невалидным tag.
@pytest.fixture(scope='function')
def create_achieve_negative_tag(tag):
    session = requests.Session()
    data = {
        "tag": tag,
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "test description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data)
    yield session
    assert response.status_code == 400


# Фикстура для создания достижений с невалидными методами запросов.
@pytest.fixture(scope='function')
def create_achievement_destructive():
    session = requests.Session()
    data = {
        "tag": "Achievement tag",
        "rank": 101,
        "color": "green",
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "description": "test description",
        "description_full": "description_full",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_put = api_request(session, 'PUT', f'{base_url}/achievements/', data=data)
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/', data=data)
    response_del = api_request(session, 'DELETE', f'{base_url}/achievements/', data=data)
    yield session
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для создания достижений с невалидным ORGANIZATION-ID.
@pytest.fixture(scope='function')
def create_achieve_invalid_org_id(org_id):
    session = requests.Session()
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', headers=headers)
    yield session
    assert response.status_code == 400


# Фикстура для получения информации о награде с невалидным id.
@pytest.fixture(scope='function')
def get_achieve_invalid_id(uuid):
    session = requests.Session()
    if uuid == '':
        response = api_request(session, 'GET', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 404
    else:
        response = api_request(session, 'GET', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 400


# Фикстура для обновления информации о награде с невалидным id.
@pytest.fixture(scope='function')
def update_achieve_id_negative(uuid):
    session = requests.Session()
    if uuid == '':
        response = api_request(session, 'PATCH', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 405
    else:
        response = api_request(session, 'PATCH', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 400


# Фикстура для обновления информации о награде с невалидным title.
@pytest.fixture(scope='function')
def update_achieve_title_negative(title):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        'title': title
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 404
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным description.
@pytest.fixture(scope='function')
def update_achieve_desc_negative(description):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        'description': description
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 404
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным description_full.
@pytest.fixture(scope='function')
def update_achieve_desc_full_neg(desc_full):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        'description_full': desc_full
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 404
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным tag.
@pytest.fixture(scope='function')
def update_achieve_tag_neg(tag):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=headers)
    ach_id = response_create.json().get('id')
    data_update = {
        'tag': tag
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 404
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидными методами запроса.
@pytest.fixture(scope='function')
def update_achieve_destructive():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = requests.get(f'{base_url}/achievements/', headers=headers)
    ach_id = response.json()[0].get('id')  # ID самой первой ачивки, если нужна другая то меняем цифру в [].
    response_patch_neg1 = api_request(session, 'POST', f'{base_url}/achievements/{ach_id}/')
    response_patch_neg2 = api_request(session, 'PUT', f'{base_url}/achievements/{ach_id}/')
    yield session
    assert response_patch_neg1.status_code == 405
    assert response_patch_neg2.status_code == 405


# Фикстура для удаления награды с невалидным id.
@pytest.fixture(scope='function')
def delete_achieve_negative(uuid):
    session = requests.Session()
    if uuid == '':
        response = api_request(session, 'DELETE', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 405
    else:
        response = api_request(session, 'DELETE', f'{base_url}/achievements/{uuid}/')
        yield session
        assert response.status_code == 400


# Фикстура для получения списка неактивных наград с невалидным rank.
@pytest.fixture(scope='function')
def get_list_inactive_achieve_negative_rank(rank):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/?rank={rank}', headers=headers)
    yield session
    assert response.status_code == 400
    assert len(response.json()) > 0


# Фикстура для получения списка неактивных наград с невалидным title.
@pytest.fixture(scope='function')
def get_list_inactive_achieve_negative_title():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/?title={"+)(*?"}', headers=headers)
    yield session
    assert response.status_code == 404
    assert len(response.json()) > 0


# Фикстура для получения списка неактивных наград с невалидным ORGANIZATION-ID.
@pytest.fixture(scope='function')
def get_list_inactive_achieve_neg_org_id(org_id):
    session = requests.Session()
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/', headers=headers)
    assert response.status_code == 400
    assert len(response.json()) > 0


# Фикстура для получения списка неактивных наград с невалидными методами запроса.
@pytest.fixture(scope='function')
def get_list_inactive_achieve_destructive():
    session = requests.Session()
    response_post = api_request(session, 'POST', f'{base_url}/achievements-archive/')
    response_put = api_request(session, 'PUT', f'{base_url}/achievements-archive/')
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements-archive/')
    response_del = api_request(session, 'DELETE', f'{base_url}/achievements-archive/')
    yield session
    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для восстановления ачивки с невалидным id.
@pytest.fixture(scope='function')
def return_achieve_id_negative(uuid):
    session = requests.Session()
    response = api_request(session, 'PATCH', f'{base_url}/achievements-archive/{uuid}/')
    yield session
    assert response.status_code == 400


# Фикстура для получения списка изображений наград с невалидным типом запроса.
@pytest.fixture(scope='function')
def get_list_avatar_achieve_destruction():
    session = requests.Session()
    response_post = api_request(session, 'POST', f'{base_url}/avatar-images/')
    response_put = api_request(session, 'PUT', f'{base_url}/avatar-images/')
    response_patch = api_request(session, 'PATCH', f'{base_url}/avatar-images/')
    response_del = api_request(session, 'DELETE', f'{base_url}/avatar-images/')
    yield session
    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для получения списка фоновых изображений наград с невалидным типом запроса.
@pytest.fixture(scope='function')
def get_list_templates_achieve_destructive():
    session = requests.Session()
    response_post = api_request(session, 'POST', f'{base_url}/templates-images/')
    response_put = api_request(session, 'PUT', f'{base_url}/templates-images/')
    response_patch = api_request(session, 'PATCH', f'{base_url}/templates-images/')
    response_del = api_request(session, 'DELETE', f'{base_url}/templates-images/')
    yield session
    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для получения списка связей пользователей с организацией с невалидным ORGANIZATION-ID.
@pytest.fixture(scope='function')
def get_list_connections_invalid_org_id(org_id):
    session = requests.Session()
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    if org_id == '':
        response = api_request(session, 'GET', f'{base_url}/link/', headers=headers)
        yield session
        assert response.status_code == 404
    else:
        response = api_request(session, 'GET', f'{base_url}/link/', headers=headers)
        yield session
        assert response.status_code == 400


# Фикстура для получения связи пользователя с организацией с невалидным profile_id.
@pytest.fixture(scope='function')
def get_connection_invalid_id_profile(profile_id):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response = api_request(session, 'GET', f'{base_url}/link/{profile_id}/', headers=headers)
    yield session
    assert response.status_code == 404


# Фикстура для обновления связи пользователя с организацией с невалидным profile_id.
@pytest.fixture(scope='function')
def update_connect_invalid_id_profile(link_id):
    session = requests.Session()
    data = {
        "link_weight": 0,
        "start_work_date": "2024-05-12",
        "specialty": "string"
    }
    if link_id == '':
        response = api_request(session, 'PATCH', f'{base_url}/link/{link_id}/', data=data)
        yield session
        assert response.status_code == 405
    else:
        response = api_request(session, 'PATCH', f'{base_url}/link/{link_id}/', data=data)
        yield session
        assert response.status_code == 404


# Фикстура для обновления связи пользователя с организацией с невалидным specialty.
@pytest.fixture(scope='function')
def update_connect_invalid_specialty():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_link = requests.get(f'{base_url}/link/', headers=headers)
    link_id = response_link.json()[0].get('link_id')
    data = {
        "link_weight": 0,
        "start_work_date": "2024-05-12",
        "specialty": generate_string(126)
    }
    response = api_request(session, 'PATCH', f'{base_url}/link/{link_id}/', data=data)
    yield session
    assert response.status_code == 404


# Фикстура для получения списка связей пользователей с организацией с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_list_connect_org_destructive():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_post = api_request(session, 'POST', f'{base_url}/link/', headers=headers)
    response_put = api_request(session, 'PUT', f'{base_url}/link/', headers=headers)
    response_patch = api_request(session, 'PATCH', f'{base_url}/link/', headers=headers)
    response_del = api_request(session, 'DELETE', f'{base_url}/link/', headers=headers)
    yield session
    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_patch.status_code == 405
    assert response_del.status_code == 405


# Фикстура для получения связи пользователя с организацией с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_connection_id_profile_destructive():
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_get = requests.get(f'{base_url}/link/', headers=headers)
    profile_id = response_get.json()[0].get('profile_id')
    response_post = api_request(session, 'POST', f'{base_url}/link/{profile_id}/', headers=headers)
    response_put = api_request(session, 'PUT', f'{base_url}/link/{profile_id}/', headers=headers)
    response_del = api_request(session, 'DELETE', f'{base_url}/link/{profile_id}/', headers=headers)
    yield session
    assert response_post.status_code == 405
    assert response_put.status_code == 405
    assert response_del.status_code == 405


# Фикстура для регистрации с невалидными значениями login.
@pytest.fixture(scope='function')
def reg_login_neg(login):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": login,
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}',
                               data=data)
    if login == 'User1':
        yield session
        assert response_reg.status_code == 403
    else:
        yield session
        assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями specialty.
@pytest.fixture(scope='function')
def reg_specialty_neg(specialty):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": specialty,
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями start_work_date.
@pytest.fixture(scope='function')
def reg_start_work_date_neg(start_work_date):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": start_work_date,
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 403


# Фикстура для регистрации с невалидными значениями password.
@pytest.fixture(scope='function')
def reg_password_neg(password):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": password,
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями first_name.
@pytest.fixture(scope='function')
def reg_first_name_neg(first_name):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": first_name,
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями last_name.
@pytest.fixture(scope='function')
def reg_last_name_neg(last_name):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": last_name,
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями phone.
@pytest.fixture(scope='function')
def reg_phone_neg(phone):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": phone,
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями email.
@pytest.fixture(scope='function')
def reg_email_neg(email):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": email
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными типами запроса.
@pytest.fixture(scope='function')
def reg_destructive(method):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, f'{method}', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    yield session
    assert response_reg.status_code == 405


# Фикстура для регистрации с невалидными значениями organization_id.
@pytest.fixture(scope='function')
def reg_org_id_neg(org_id):
    session = requests.Session()
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = api_request(session, 'POST', f'{base_url}/registrations/?organization_id={org_id}', data=data)
    if org_id == '':
        yield session
        assert response_reg.status_code == 403
    else:
        yield session
        assert response_reg.status_code == 400


# Фикстура для регистрации с невалидными значениями link_weight.
# @pytest.fixture(scope='function')
# def reg_link_weight_neg(link_weight):
#     session = requests.Session()
#     response_org = api_request(session, 'GET', f'{base_url}/organization/')
#     org_id = response_org.json()[0].get('organization_id')
#     data = {
#         "login": gen_alphanum_random_str(8),
#         "specialty": "Бармен",
#         "start_work_date": "2024-05-12",
#         "password": "string",
#         "first_name": "TEST_PERSON",
#         "last_name": "Васильев",
#         "phone": "+79244663456",
#         "email": "user@example.com"
#     }
#     response_reg = api_request(session, 'POST', f'{base_url}/registrations/?link_weight={link_weight}&organization_id={org_id}',
#                                data=data)
#     yield session
#     assert response_reg.status_code == 400


# Фикстура для аутентификации с невалидными значениями login.
@pytest.fixture(scope='function')
def auth_login_neg(login):
    session = requests.Session()
    data_auth = {
        "login": login,
        "password": "string"
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    if login == '' or login == ' ' or login == generate_string(4) or login == generate_string(51):
        yield session
        assert response_auth.status_code == 400
        assert len(response_auth.json()) > 0
    else:
        yield session
        assert response_auth.status_code == 403
        assert len(response_auth.json()) > 0


# Фикстура для аутентификации с невалидными значениями password.
@pytest.fixture(scope='function')
def auth_password_neg(password):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data)
    profile_id = response_reg.json().get('profile_id')
    login = response_reg.json().get('login')
    data_auth = {
        "login": login,
        "password": password
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    if password == '' or password == ' ' or password == generate_string(4) or password == generate_string(51):
        yield session
        assert response_auth.status_code == 400
        assert len(response_auth.json()) > 0
    else:
        yield session
        assert response_auth.status_code == 403
        assert len(response_auth.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для аутентификации с невалидными типами запроса.
@pytest.fixture(scope='function')
def auth_destructive(method):
    session = requests.Session()
    response_auth = api_request(session, f'{method}', f'{base_url}/login/')
    yield session
    assert response_auth.status_code == 405


# Фикстура для обновления логина и пароля с невалидным user_id.
@pytest.fixture(scope='function')
def update_user_id_neg(user_id):
    session = requests.Session()
    data_update = {
        "login": gen_alphanum_random_str(6),
        "password": "123456"
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    yield session
    assert response_update.status_code == 422


# Фикстура для обновления логина на невалидный.
@pytest.fixture(scope='function')
def update_login_neg(login):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    user_id = response_reg.json().get('user_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_update = {
        "login": login
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    yield session
    assert response_update.status_code == 422
    assert len(response_update.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для обновления пароля на невалидный.
@pytest.fixture(scope='function')
def update_password_neg(password):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    user_id = response_reg.json().get('user_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    data_update = {
        "password": password
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    yield session
    assert response_update.status_code == 422
    assert len(response_update.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)


# Фикстура для обновления логина и пароля с невалидными типами запроса.
@pytest.fixture(scope='function')
def update_destructive(method):
    session = requests.Session()
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    data_reg = {
        "login": gen_alphanum_random_str(8),
        "specialty": "Бармен",
        "start_work_date": "2024-05-12",
        "password": "string",
        "first_name": "TEST_PERSON",
        "last_name": "Васильев",
        "phone": "+79244663456",
        "email": "user@example.com"
    }
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_reg = requests.post(f'{base_url}/registrations/?organization_id={org_id}', data=data_reg)
    profile_id = response_reg.json().get('profile_id')
    user_id = response_reg.json().get('user_id')
    response_update = api_request(session, f'{method}', f'{base_url}/login/{user_id}/')
    yield session
    assert response_update.status_code == 405
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=headers)
