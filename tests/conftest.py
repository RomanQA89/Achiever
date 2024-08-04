import pytest
import requests
from settings import *
from api import api_request
from tests.test_achieve_lib import *


# Фикстура для получения списка организаций (организация пока одна)
@pytest.fixture(scope='function')
def get_org_id():
    response_org = requests.get(f'{base_url}/organization/')
    org_id = response_org.json()[0].get('organization_id')
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    return headers


# Фикстура для запроса списка ачивок.
@pytest.fixture(scope='function')
def get_list_of_achievements(get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements/', headers=get_org_id)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для создания достижений с title и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_title(title, get_org_id):
    session = requests.Session()
    data = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": title,
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=get_org_id)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с description и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_desc(description, get_org_id):
    session = requests.Session()
    data = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "description": description,
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=get_org_id)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с description_full и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_desc_full(description_full, get_org_id):
    session = requests.Session()
    data = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "description_full": description_full,
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=get_org_id)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для создания достижений с tag и последующего удаления.
@pytest.fixture(scope='function')
def create_achieve_tag(tag, get_org_id):
    session = requests.Session()
    data = {
        "tag": tag,
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "testing title",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response = api_request(session, 'POST', f'{base_url}/achievements/', data=data, headers=get_org_id)
    ach_id = response.json().get('id')
    yield session
    assert response.status_code == 201
    api_request(session, 'DELETE', f'{base_url}/achievements/{ach_id}/')


# Фикстура для возвращения id определенной ачивки.
@pytest.fixture(scope='function')
def get_achievement(get_org_id):
    session = requests.Session()
    response = requests.get(f'{base_url}/achievements/', headers=get_org_id)
    id_achieve = response.json()[0].get('id')  # ID самой первой ачивки, если нужна другая то меняем цифру в [].
    response_get = api_request(session, 'GET', f'{base_url}/achievements/{id_achieve}/')
    yield session
    assert response_get.status_code == 200
    assert len(response_get.json()) > 0


# Фикстура для обновления данных ачивки для параметра title.
@pytest.fixture(scope='function')
def update_achieve_title(title, get_org_id):
    session = requests.Session()
    data_create = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
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
def update_achieve_desc(description, get_org_id):
    session = requests.Session()
    data_create = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
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
def update_achieve_desc_full(desc_full, get_org_id):
    session = requests.Session()
    data_create = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
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
def update_achieve_tag(tag, get_org_id):
    session = requests.Session()
    data_create = {
        "rank": 101,
        "image": "https://www.example.com/media/imag-achievements.png",
        "title": "title",
        "achiev_style": "https://www.example.com/media/imag-back.jpg"
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
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
def get_list_inactive_achieve(get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/', headers=get_org_id)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для восстановления неактивной награды.
@pytest.fixture(scope='function')
def return_achievement(get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/achievements-archive/', headers=get_org_id)
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
def get_list_connections_org(get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/link/', headers=get_org_id)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения связи пользователя с организацией.
@pytest.fixture(scope='function')
def get_connection_id_profile_id_org(get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/link/', headers=get_org_id)
    profile_id = response_get.json()[0].get('profile_id')
    response = api_request(session, 'GET', f'{base_url}/link/{profile_id}/', headers=get_org_id)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для обновления связи пользователя/админа с организацией.
@pytest.fixture(scope='function')
def update_connect_id_profile_id_org(link_weight, specialty, get_org_id):
    session = requests.Session()
    response_link = requests.get(f'{base_url}/link/', headers=get_org_id)
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
    yield session
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
def registration_login(login, get_org_id):
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
    yield session
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений specialty.
@pytest.fixture(scope='function')
def registration_specialty(specialty, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений start_work_date.
@pytest.fixture(scope='function')
def reg_start_work_date(start_work_date, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений password.
@pytest.fixture(scope='function')
def reg_password(password, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений first_name.
@pytest.fixture(scope='function')
def reg_first_name(first_name, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений last_name.
@pytest.fixture(scope='function')
def reg_last_name(last_name, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки позитивных граничных значений phone.
@pytest.fixture(scope='function')
def reg_phone(phone, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для регистрации и проверки значений email.
@pytest.fixture(scope='function')
def reg_email(email, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для аутентификации пользователя.
@pytest.fixture(scope='function')
def auth_user(get_org_id):
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
    data_auth = {
        "login": login,
        "password": data_reg['password']
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    yield session
    assert response_auth.status_code == 200
    assert len(response_auth.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для аутентификации админа.
@pytest.fixture(scope='function')
def auth_admin(get_org_id):
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
    data_auth = {
        "login": login,
        "password": data_reg['password']
    }
    response_auth = api_request(session, 'POST', f'{base_url}/login/', data=data_auth)
    yield session
    assert response_auth.status_code == 200
    assert len(response_auth.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для обновления логина.
@pytest.fixture(scope='function')
def update_login(get_org_id):
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
    data_update = {
        "login": gen_alphanum_random_str(6)
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    login_update = response_update.json().get('login')
    yield session
    assert response_update.status_code == 200
    assert len(response_update.json()) > 0
    assert login != login_update   # Проверка на обновление логина
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для обновления пароля.
@pytest.fixture(scope='function')
def update_password(get_org_id):
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
    data_update = {
        "password": gen_alphanum_random_str(6)
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    pass_update = response_update.json().get('password')
    yield session
    assert response_update.status_code == 200
    assert len(response_update.json()) > 0
    assert data_reg['password'] != pass_update  # Проверка на обновление пароля
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для получения списка id организаций.
@pytest.fixture(scope='function')
def get_list_of_organization():
    session = requests.Session()
    response_org = api_request(session, 'GET', f'{base_url}/organization/')
    yield session
    assert response_org.status_code == 200
    assert len(response_org.json()) > 0


# Фикстура для получения списка профилей.
@pytest.fixture(scope='function')
def get_list_profiles(get_org_id):
    session = requests.Session()
    response_prof = api_request(session, 'GET', f'{base_url}/profiles/', headers=get_org_id)
    yield session
    assert response_prof.status_code == 200


# Фикстура для получения профиля по его id.
@pytest.fixture(scope='function')
def get_profile(get_org_id):
    session = requests.Session()
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    profile_id = response_prof.json()[0].get('profile_id')     # Вычленяю profile_id у первого попавшегося профиля.
    response = api_request(session, 'GET', f'{base_url}/profiles/{profile_id}/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для обновления имени профиля по его id.
@pytest.fixture(scope='function')
def update_first_name_profile(f_name_update, get_org_id):
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
    first_name = response_reg.json().get('first_name')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "first_name": f_name_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    first_name_update = response.json().get('first_name')
    yield session
    assert response.status_code == 200
    assert first_name != first_name_update      # Проверка на обновление first_name
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления last_name профиля по его id.
@pytest.fixture(scope='function')
def update_last_name_profile(l_name_update, get_org_id):
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
    last_name = response_reg.json().get('last_name')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "last_name": l_name_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    last_name_update = response.json().get('last_name')
    yield session
    assert response.status_code == 200
    assert last_name != last_name_update  # Проверка на обновление last_name
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления middle_name профиля по его id.
@pytest.fixture(scope='function')
def update_middle_name_profile(m_name_update, get_org_id):
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
    middle_name = response_reg.json().get('middle_name')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "middle_name": m_name_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    middle_name_update = response.json().get('middle_name')
    yield session
    assert response.status_code == 200
    assert middle_name != middle_name_update  # Проверка на обновление middle_name
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления birth_date профиля по его id.
@pytest.fixture(scope='function')
def update_birth_date_profile(b_date_update, get_org_id):
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
    birth_date = response_reg.json().get('birth_date')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "birth_date": b_date_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    birth_date_update = response.json().get('birth_date')
    yield session
    assert response.status_code == 200
    assert birth_date != birth_date_update  # Проверка на обновление middle_name
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления phone профиля по его id.
@pytest.fixture(scope='function')
def update_phone_profile(ph_update, get_org_id):
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
    phone = response_reg.json().get('phone')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "phone": ph_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    ph_update = response.json().get('phone')
    yield session
    assert response.status_code == 200
    assert phone != ph_update  # Проверка на обновление phone
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления email профиля по его id.
@pytest.fixture(scope='function')
def update_email_profile(em_update, get_org_id):
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
    email = response_reg.json().get('email')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "email": em_update
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    email_update = response.json().get('phone')
    yield session
    assert response.status_code == 200
    assert email != email_update  # Проверка на обновление email
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления photo_main профиля по его id.
@pytest.fixture(scope='function')
def update_photo_main_profile(get_org_id):
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
    photo_main = response_reg.json().get('photo_main')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "photo_main": "https://habrastorage.org/webt/y4/ia/yr/y4iayrhm_zwbr2onpmldhbhlrg8.png"
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    photo_main_update = response.json().get('photo_main')
    yield session
    assert response.status_code == 200
    assert photo_main != photo_main_update  # Проверка на обновление photo_main
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления photo_small профиля по его id.
@pytest.fixture(scope='function')
def update_photo_small_profile(get_org_id):
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
    photo_small = response_reg.json().get('photo_small')
    profile_id = response_reg.json().get('profile_id')
    data_update = {
        "photo_small": "https://habrastorage.org/webt/y4/ia/yr/y4iayrhm_zwbr2onpmldhbhlrg8.png"
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    photo_small_update = response.json().get('photo_small')
    yield session
    assert response.status_code == 200
    assert photo_small != photo_small_update  # Проверка на обновление photo_small
    assert len(response.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для удаления профиля по его id.
@pytest.fixture(scope='function')
def delete_profile(get_org_id):
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
    response_del = api_request(session, 'DELETE', f'{base_url}/profiles/{profile_id}/', headers=get_org_id)
    yield session
    assert response_del.status_code == 200
    assert len(response_del.json()) > 0


# Фикстура для получения списка ranks.
@pytest.fixture(scope='function')
def get_list_ranks():
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/ranks/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения rank по его id и profile_id.
@pytest.fixture(scope='function')
def get_rank():
    session = requests.Session()
    response = requests.get(f'{base_url}/ranks/')
    uuid = response.json()[0].get('id')
    profile_id = response.json()[0].get('profile_id')
    response_get = api_request(session, 'GET', f'{base_url}/ranks/?id={uuid}&profile_id={profile_id}')
    print(response_get.json())
    yield session
    assert response_get.status_code == 200
    assert len(response_get.json()) > 0


# Фикстура для получения списка связей награда-пользователь.
@pytest.fixture(scope='function')
def get_list_connections():
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/user-achievements/')
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0


# Фикстура для получения списка наград определенного пользователя.
@pytest.fixture(scope='function')
def get_achieves_of_user():
    session = requests.Session()
    response = requests.get(f'{base_url}/user-achievements/')
    user_id = response.json()[0].get('data').get('user_id')
    response_get = api_request(session, 'GET', f'{base_url}/user-achievements/{user_id}/')
    yield session
    assert response_get.status_code == 200
    assert len(response_get.json()) > 0


# Фикстура для присваивания награды определенному пользователю и последующего её удаления.
@pytest.fixture(scope='function')
def assign_achieve_to_user(get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/achievements/', headers=get_org_id)
    achieve_id = response_get.json()[0].get('id')
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    user_id = response_prof.json()[0].get('profile_id')
    data = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'POST', f'{base_url}/user-achievements/', data=data)
    connect_id = response.json().get('id')
    response_del = api_request(session, 'DELETE', f'{base_url}/user-achievements/{connect_id}/')
    yield session
    assert response.status_code == 201
    assert len(response.json()) > 0
    assert response_del.status_code == 200


# Фикстура для обновления связи награда-пользователь.
@pytest.fixture(scope='function')
def update_connect_achieve_user():
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    connect_id = response_get.json()[0].get('id')
    user_id = response_get.json()[0].get('data').get('user_id')
    achieve_id_old = response_get.json()[0].get('data').get('achievement').get('id')
    achieve_id_new = response_get.json()[2].get('data').get('achievement').get('id')
    data_update = {
        "user_id": user_id,
        "achievement_id": achieve_id_new
    }
    response = api_request(session, 'PATCH', f'{base_url}/user-achievements/{connect_id}/', data=data_update)
    yield session
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert achieve_id_new != achieve_id_old     # Проверка на обновление ачивки.
    data = {
        "user_id": user_id,
        "achievement_id": achieve_id_old
    }
    requests.patch(f'{base_url}/user-achievements/{connect_id}/', data=data)


                             # Фикстуры для негативных тестов.


# Фикстура для запроса списка наград с параметром rank.
@pytest.fixture(scope='function')
def get_list_of_achieve_rank_neg(rank, get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements/?rank={rank}', headers=get_org_id)
    yield session
    assert response.status_code == 400
    assert len(response.json()) > 0


# Фикстура для запроса списка наград с параметром title.
@pytest.fixture(scope='function')
def get_list_of_achieve_title_neg(get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements/?title={"+)(*?"}', headers=get_org_id)
    yield session
    assert response.status_code == 404
    assert len(response.json()) > 0


# Фикстура для запроса списка наград с невалидными методами запроса.
@pytest.fixture(scope='function')
def get_list_of_achieve_destructive(method, get_org_id):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/achievements/', headers=get_org_id)
    yield session
    assert response.status_code == 405


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
def create_achievement_destructive(method):
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
    response = api_request(session, f'{method}', f'{base_url}/achievements/', data=data)
    yield session
    assert response.status_code == 405


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
def update_achieve_title_negative(title, get_org_id):
    session = requests.Session()
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
    ach_id = response_create.json().get('id')
    data_update = {
        'title': title
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 422
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным description.
@pytest.fixture(scope='function')
def update_achieve_desc_negative(description, get_org_id):
    session = requests.Session()
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
    ach_id = response_create.json().get('id')
    data_update = {
        'description': description
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 422
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным description_full.
@pytest.fixture(scope='function')
def update_achieve_desc_full_neg(desc_full, get_org_id):
    session = requests.Session()
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
    ach_id = response_create.json().get('id')
    data_update = {
        'description_full': desc_full
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 422
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидным tag.
@pytest.fixture(scope='function')
def update_achieve_tag_neg(tag, get_org_id):
    session = requests.Session()
    data_create = {
        'image': 'https://www.example.com/media/imag-achievements.png',
        'title': 'string4',
        'achiev_style': 'https://www.example.com/media/imag-back.jpg',
        'rank': 1
    }
    response_create = requests.post(f'{base_url}/achievements/', data=data_create, headers=get_org_id)
    ach_id = response_create.json().get('id')
    data_update = {
        'tag': tag
    }
    response_patch = api_request(session, 'PATCH', f'{base_url}/achievements/{ach_id}/', data=data_update)
    yield session
    assert response_patch.status_code == 422
    requests.delete(f'{base_url}/achievements/{ach_id}/')


# Фикстура для обновления информации о награде с невалидными методами запроса.
@pytest.fixture(scope='function')
def update_achieve_destructive(method, get_org_id):
    session = requests.Session()
    response = requests.get(f'{base_url}/achievements/', headers=get_org_id)
    ach_id = response.json()[0].get('id')  # ID самой первой ачивки, если нужна другая то меняем цифру в [].
    response_patch = api_request(session, f'{method}', f'{base_url}/achievements/{ach_id}/')
    yield session
    assert response_patch.status_code == 405


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
def get_list_inactive_achieve_negative_rank(rank, get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/?rank={rank}', headers=get_org_id)
    yield session
    assert response.status_code == 400
    assert len(response.json()) > 0


# Фикстура для получения списка неактивных наград с невалидным title.
@pytest.fixture(scope='function')
def get_list_inactive_achieve_negative_title(get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/achievements-archive/?title={"+)(*?"}', headers=get_org_id)
    yield session
    assert response.status_code == 422
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
def get_list_inactive_achieve_destructive(method):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/achievements-archive/')
    yield session
    assert response.status_code == 405


# Фикстура для восстановления ачивки с невалидным id.
@pytest.fixture(scope='function')
def return_achieve_id_negative(uuid):
    session = requests.Session()
    response = api_request(session, 'PATCH', f'{base_url}/achievements-archive/{uuid}/')
    yield session
    assert response.status_code == 400


# Фикстура для получения списка изображений наград с невалидным типом запроса.
@pytest.fixture(scope='function')
def get_list_avatar_achieve_destructive(method):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/avatar-images/')
    yield session
    assert response.status_code == 405


# Фикстура для получения списка фоновых изображений наград с невалидным типом запроса.
@pytest.fixture(scope='function')
def get_list_templates_achieve_destructive(method):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/templates-images/')
    yield session
    assert response.status_code == 405


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
def get_connection_invalid_id_profile(profile_id, get_org_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/link/{profile_id}/', headers=get_org_id)
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
def update_connect_invalid_specialty(get_org_id):
    session = requests.Session()
    response_link = requests.get(f'{base_url}/link/', headers=get_org_id)
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
def get_list_connect_org_destructive(method, get_org_id):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/link/', headers=get_org_id)
    yield session
    assert response.status_code == 405


# Фикстура для получения связи пользователя с организацией с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_connection_id_profile_destructive(method, get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/link/', headers=get_org_id)
    profile_id = response_get.json()[0].get('profile_id')
    response_post = api_request(session, f'{method}', f'{base_url}/link/{profile_id}/', headers=get_org_id)
    yield session
    assert response_post.status_code == 405


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
def auth_password_neg(password, get_org_id):
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
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


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
def update_login_neg(login, get_org_id):
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
    data_update = {
        "login": login
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    yield session
    assert response_update.status_code == 422
    assert len(response_update.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для обновления пароля на невалидный.
@pytest.fixture(scope='function')
def update_password_neg(password, get_org_id):
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
    data_update = {
        "password": password
    }
    response_update = api_request(session, 'PATCH', f'{base_url}/login/{user_id}/', data=data_update)
    yield session
    assert response_update.status_code == 422
    assert len(response_update.json()) > 0
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для обновления логина и пароля с невалидными типами запроса.
@pytest.fixture(scope='function')
def update_destructive(method, get_org_id):
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
    response_update = api_request(session, f'{method}', f'{base_url}/login/{user_id}/')
    yield session
    assert response_update.status_code == 405
    requests.delete(f'{base_url}/profiles/{profile_id}', headers=get_org_id)


# Фикстура для получения списка id организаций с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_list_of_org_destructive(method):
    session = requests.Session()
    response_org = api_request(session, f'{method}', f'{base_url}/organization/')
    yield session
    assert response_org.status_code == 405
    assert len(response_org.json()) > 0


# Фикстура для получения списка профилей с невалидным ORGANIZATION-ID.
@pytest.fixture(scope='function')
def get_list_profiles_neg(org_id):
    session = requests.Session()
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': org_id
    }
    response_prof = api_request(session, 'GET', f'{base_url}/profiles/', headers=headers)
    if org_id == '':
        yield session
        assert response_prof.status_code == 404
    else:
        yield session
        assert response_prof.status_code == 400


# Фикстура для получения профиля с невалидным profile_id.
@pytest.fixture(scope='function')
def get_profile_neg(profile_id):
    session = requests.Session()
    response = api_request(session, 'GET', f'{base_url}/profiles/{profile_id}/')
    yield session
    assert response.status_code == 404


# Фикстура для получения списка профилей с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_list_profiles_destructive(method, get_org_id):
    session = requests.Session()
    response_prof = api_request(session, f'{method}', f'{base_url}/profiles/', headers=get_org_id)
    yield session
    assert response_prof.status_code == 405


# Фикстура для получения профиля с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_profile_destructive(method, get_org_id):
    session = requests.Session()
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    profile_id = response_prof.json()[0].get('profile_id')        # Вычленяю profile_id у первого попавшегося профиля.
    response = api_request(session, f'{method}', f'{base_url}/profiles/{profile_id}/')
    yield session
    assert response.status_code == 405


# Фикстура для обновления профиля с невалидным profile_id.
@pytest.fixture(scope='function')
def update_profile_id_neg(profile_id):
    session = requests.Session()
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/')
    yield session
    assert response.status_code == 422


# Фикстура для обновления профиля с невалидным first_name.
@pytest.fixture(scope='function')
def update_profile_first_name_neg(first_name, get_org_id):
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
    data_update = {
        "first_name": first_name
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным last_name.
@pytest.fixture(scope='function')
def update_profile_last_name_neg(last_name, get_org_id):
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
    data_update = {
        "last_name": last_name
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным middle_name.
@pytest.fixture(scope='function')
def update_profile_middle_name_neg(middle_name, get_org_id):
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
    data_update = {
        "middle_name": middle_name
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным birth_date.
@pytest.fixture(scope='function')
def update_profile_birth_date_neg(birth_date, get_org_id):
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
    data_update = {
        "birth_date": birth_date
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным phone.
@pytest.fixture(scope='function')
def update_profile_phone_neg(phone, get_org_id):
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
    data_update = {
        "phone": phone
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным email.
@pytest.fixture(scope='function')
def update_profile_email_neg(email, get_org_id):
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
    data_update = {
        "email": email
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным photo_main.
@pytest.fixture(scope='function')
def update_profile_photo_main_neg(photo_main, get_org_id):
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
    data_update = {
        "photo_main": photo_main
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


# Фикстура для обновления профиля с невалидным photo_small.
@pytest.fixture(scope='function')
def update_profile_photo_small_neg(photo_small, get_org_id):
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
    data_update = {
        "photo_small": photo_small
    }
    response = api_request(session, 'PATCH', f'{base_url}/profiles/{profile_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    requests.delete(f'{base_url}/profiles/{profile_id}/', headers=get_org_id)


        # ПОКА ДАННЫЕ ТЕСТЫ РАБОТАЮТ НЕКОРРЕКТНО, В ЛЮБОМ СЛУЧАЕ ПОЯВЛЯЕТСЯ 200 СТАТУС-КОД!
# Фикстура для удаления профиля с невалидным org_id.
@pytest.fixture(scope='function')
def delete_profile_org_id_neg(organ_id, get_org_id):
    session = requests.Session()
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    profile_id = response_prof.json()[0].get('profile_id')  # Вычленяю profile_id у первого попавшегося профиля.
    headers = {
        'accept': 'application/json',
        'ORGANIZATION-ID': organ_id
    }
    response_del = api_request(session, 'DELETE', f'{base_url}/profiles/{profile_id}/', headers=headers)
    yield session
    assert response_del.status_code == 404


# Фикстура для удаления профиля с невалидным profile_id.
@pytest.fixture(scope='function')
def delete_profile_id_neg(profile_id, get_org_id):
    session = requests.Session()
    response_del = api_request(session, 'DELETE', f'{base_url}/profiles/{profile_id}/', headers=get_org_id)
    yield session
    assert response_del.status_code == 404


# Фикстура для получения списка связей награда-пользователь с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_list_connect_destructive(method):
    session = requests.Session()
    response = api_request(session, f'{method}', f'{base_url}/user-achievements/')
    yield session
    assert response.status_code == 405
    assert len(response.json()) > 0


# Фикстура для получения списка наград определенного пользователя с невалидным user_id.
@pytest.fixture(scope='function')
def get_achieves_of_user_id_neg(user_id):
    session = requests.Session()
    response_get = api_request(session, 'GET', f'{base_url}/user-achievements/{user_id}/')
    yield session
    assert response_get.status_code == 400
    assert len(response_get.json()) > 0


# Фикстура для получения списка наград определенного пользователя с невалидными типами запроса.
@pytest.fixture(scope='function')
def get_achieves_of_user_id_destructive(method):
    session = requests.Session()
    response = requests.get(f'{base_url}/user-achievements/')
    user_id = response.json()[0].get('data').get('user_id')
    response_get = api_request(session, f'{method}', f'{base_url}/user-achievements/{user_id}/')
    yield session
    assert response_get.status_code == 405
    assert len(response_get.json()) > 0


# Фикстура для присваивания награды определенному пользователю с невалидным user_id.
@pytest.fixture(scope='function')
def assign_achieve_to_user_id_neg(user_id, get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/achievements/', headers=get_org_id)
    achieve_id = response_get.json()[0].get('id')
    data = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'POST', f'{base_url}/user-achievements/', data=data)
    yield session
    assert response.status_code == 422
    assert len(response.json()) > 0


# Фикстура для присваивания награды определенному пользователю с невалидным achievement_id.
@pytest.fixture(scope='function')
def assign_achievement_id_neg(achieve_id, get_org_id):
    session = requests.Session()
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    user_id = response_prof.json()[0].get('profile_id')
    data = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'POST', f'{base_url}/user-achievements/', data=data)
    yield session
    assert response.status_code == 422
    assert len(response.json()) > 0


# Фикстура для присваивания награды определенному пользователю с невалидными типами запроса.
@pytest.fixture(scope='function')
def assign_achieve_to_user_destructive(method, get_org_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/achievements/', headers=get_org_id)
    achieve_id = response_get.json()[0].get('id')
    response_prof = requests.get(f'{base_url}/profiles/', headers=get_org_id)
    user_id = response_prof.json()[0].get('profile_id')
    data = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, f'{method}', f'{base_url}/user-achievements/', data=data)
    yield session
    assert response.status_code == 405
    assert len(response.json()) > 0


# Фикстура для обновления связи награда-пользователь с невалидным id связи.
@pytest.fixture(scope='function')
def update_connect_id_neg(connect_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    user_id = response_get.json()[0].get('data').get('user_id')
    achieve_id = response_get.json()[2].get('data').get('achievement').get('id')
    data_update = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'PATCH', f'{base_url}/user-achievements/{connect_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    assert len(response.json()) > 0


# Фикстура для обновления связи награда-пользователь с невалидным user_id.
@pytest.fixture(scope='function')
def update_connect_user_id_neg(user_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    connect_id = response_get.json()[0].get('id')
    achieve_id = response_get.json()[2].get('data').get('achievement').get('id')
    data_update = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'PATCH', f'{base_url}/user-achievements/{connect_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    assert len(response.json()) > 0


# Фикстура для обновления связи награда-пользователь с невалидным achievement_id.
@pytest.fixture(scope='function')
def update_connect_achieve_id_neg(achieve_id):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    connect_id = response_get.json()[0].get('id')
    user_id = response_get.json()[0].get('data').get('user_id')
    data_update = {
        "user_id": user_id,
        "achievement_id": achieve_id
    }
    response = api_request(session, 'PATCH', f'{base_url}/user-achievements/{connect_id}/', data=data_update)
    yield session
    assert response.status_code == 422
    assert len(response.json()) > 0


# Фикстура для обновления связи награда-пользователь с невалидными типами запроса.
@pytest.fixture(scope='function')
def update_connect_destructive(method):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    connect_id = response_get.json()[0].get('id')
    response = api_request(session, f'{method}', f'{base_url}/user-achievements/{connect_id}/')
    yield session
    assert response.status_code == 405


# Фикстура для удаления связи награда-пользователь с невалидным id связи.
@pytest.fixture(scope='function')
def deactivate_connect_id_neg(connect_id):
    session = requests.Session()
    response = api_request(session, 'DELETE', f'{base_url}/user-achievements/{connect_id}/')
    yield session
    assert response.status_code == 422


# Фикстура для удаления связи награда-пользователь с невалидными типами запроса.
@pytest.fixture(scope='function')
def deactivate_connect_destructive(method):
    session = requests.Session()
    response_get = requests.get(f'{base_url}/user-achievements/')
    connect_id = response_get.json()[0].get('id')
    response = api_request(session, f'{method}', f'{base_url}/user-achievements/{connect_id}/')
    yield session
    assert response.status_code == 405
