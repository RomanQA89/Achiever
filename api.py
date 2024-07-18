from tests.log import log_request


# Апи библиотека.
@log_request
def api_request(session, method, url,
                headers='',
                data='',
                json='',
                files=None):  # Добавил аргумент files по умолчанию None
    if headers:
        session.headers.update(headers)
    if method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']:
        if files:
            response = session.request(method, url, data=data, json=json, files=files)
        else:
            response = session.request(method, url, data=data, json=json)
    else:
        response = ''
    return response
