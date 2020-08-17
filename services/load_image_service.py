from gateways.images_api.api import Api
from gateways.cache.redis import Redis
from settings import EXPIRATION_CACHE


class LoadImageService:
    expiration = EXPIRATION_CACHE

    def __init__(self):
        self.load_images()

    def load_images(self):
        has_more = True
        page = None
        while has_more:
            images_response = Api.get_images(page)
            self.process_pictures(images_response['pictures'])
            has_more = images_response['hasMore'] and images_response['page']+1 < images_response['pageCount']
            page = images_response['page'] + 1

    def process_pictures(self, pictures):
        for picture in pictures:
            if not Redis.get(picture['id']):
                image_response = Api.get_image(picture['id'])
                Redis.set(picture['id'], image_response, self.expiration)
                if 'tags' in image_response:
                    tags = self.get_tags(image_response['tags'])
                    for tag in tags:
                        Redis.add("tag-"+tag, picture['id'])
                if 'author' in image_response:
                    Redis.add("author-"+image_response['author'].replace(" ", "_"), picture['id'])
                if 'camera' in image_response:
                    Redis.add("camera-" + image_response['camera'].replace(" ", "_"), picture['id'])

    def get_tags(self, tag_string):
        tag_string = tag_string.split(" ")
        return list(filter(self.clean, tag_string))

    @staticmethod
    def clean(tag):
        if len(tag.strip()) == 0:
            return False
        return True
