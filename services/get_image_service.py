from urllib import parse
from services.search_engine_service import SearchEngine
from gateways.cache.redis import Redis


class GetImageService:
    keys_to_search = {
        "author": SearchEngine.get_by_author,
        "camera": SearchEngine.get_by_camera,
        "tag": SearchEngine.get_by_tag,
    }

    @staticmethod
    def parse_query_string(query_string):
        """
        Converts the given query_string into a dictionary. Returns an empty dict if the operation fails.
        :param query_string:
        :return: query string as dict.
        """
        try:
            query_string = query_string.decode('utf-8')
            return dict(parse.parse_qsl(query_string))
        except (UnicodeDecodeError, AttributeError):
            return dict()

    @classmethod
    def search(cls, query_string):
        query = cls.parse_query_string(query_string)
        result_raw = set()
        for key, value in query.items():
            if key in cls.keys_to_search:
                _result = cls.keys_to_search[key](value)
                for r in _result:
                    result_raw.add(r)

        result = []
        for _id in result_raw:
            result.append(Redis.get(_id.decode('utf-8')))
        return result
