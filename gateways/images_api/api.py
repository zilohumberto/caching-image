from requests import get
from urllib.parse import urljoin
from json import loads
from settings import API_URL
from gateways.authentication.authentication import Auth


class Api:
    images_url = urljoin(API_URL, "/images")
    image_url = urljoin(API_URL, "/images/{0}")

    @classmethod
    def _headers(cls):
        return {"Authorization": f"Bearer {Auth.token()}", 'content-type': 'application/json'}

    @classmethod
    def get_images(cls, page=None):
        if page:
            images_url = cls.images_url + f"?page={page}"
        else:
            images_url = cls.images_url

        response = get(images_url, headers=cls._headers())
        if response.status_code == 403:
            raise ValueError("Authentication error")

        if response.status_code == 200:
            return loads(response.text)

        raise ValueError("Unknown error")

    @classmethod
    def get_image(cls, _id):
        response = get(cls.image_url.format(_id), headers=cls._headers())
        if response.status_code == 403:
            raise ValueError("Authentication error")

        if response.status_code == 200:
            return loads(response.text)

        raise ValueError("Unknown error")
