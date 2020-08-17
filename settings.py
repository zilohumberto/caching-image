from decouple import config

API_URL = config("API_URL")
API_KEY = config("API_KEY")
EXPIRATION_CACHE = config("EXPIRATION_CACHE", cast=int)
REDIS_HOST = config("REDIS_HOST", default="127.0.0.1")
REDIS_PORT = 6379
DEVELOPMENT_API_HOST = config("DEVELOPMENT_API_HOST", default="127.0.0.1")
DEVELOPMENT_API_PORT = config("DEVELOPMENT_API_PORT", cast=int, default=5000)
DEVELOPMENT_API_DEBUG = config("DEVELOPMENT_API_DEBUG", cast=bool, default=False)
