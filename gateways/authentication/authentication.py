from requests import post
from settings import API_URL, API_KEY
from json import loads, dumps
from urllib.parse import urljoin


class Auth:

    login_url = urljoin(API_URL, "/auth")
    auth_token = None

    @classmethod
    def login(cls):
        return post(cls.login_url, data=dumps({"apiKey": API_KEY}), headers={'content-type': 'application/json'})

    @classmethod
    def get_token(cls):
        response = cls.login()
        if response.status_code != 200:
            raise ValueError(response.status_code)
        data = loads(response.text)

        return data.get("token", "")

    @classmethod
    def token(cls):
        if not cls.auth_token:
            cls.auth_token = cls.get_token()

        return cls.auth_token
