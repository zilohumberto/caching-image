from gateways.cache.redis import Redis


class SearchEngine:
    @classmethod
    def get_by_author(cls, value):
        return Redis.lget("author-"+value.replace(" ", "_"))

    @classmethod
    def get_by_camera(cls, value):
        return Redis.lget("camera-"+value.replace(" ", "_"))

    @classmethod
    def get_by_tag(cls, value):
        return Redis.lget("tag-"+value.replace(" ", "_"))
