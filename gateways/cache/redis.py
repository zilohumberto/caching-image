import redis
from settings import REDIS_HOST, REDIS_PORT
from json import loads, dumps


class Redis:
    """
        Interface to cache gateway
        Gateway Redis Cache
        - set data to cache
        - get data cached
        - set list of values
        - get list of values
    """
    queue = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password="",
        )

    @classmethod
    def get(cls, key):
        result = cls.queue.get(key)
        if result:
            return loads(result)
        return result

    @classmethod
    def set(cls, key, value, expires=None):
        if expires:
            cls.queue.setex(key, expires, dumps(value))
        else:
            cls.queue.set(key, dumps(value))

    @classmethod
    def add(cls, key, value):
        return cls.queue.rpush(key, value)

    @classmethod
    def lget(cls, key):
        return cls.queue.lrange(key, 0, -1)
