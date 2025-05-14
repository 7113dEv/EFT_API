import json
from typing import Optional
from api import settings
import redis


class RedisClient:
    def __init__(self, client: Optional[redis.Redis] = None):
        
        self._redis= client or redis.Redis.from_url(
            settings.REDIS_URL, decode_responses=True
        )

    def set_value(self, key: str, value: dict, expire_in_seconds: Optional[int] = None) -> bool:
        """
        Save data to the Redis cache

        :param key: cache key name
        :type key: str
        :param value: data to be saved in cache
        :type value: dict
        :param expire_in_seconds: data expiration after save in seconds, defaults to None
        :type expire_in_seconds: Optional[int], optional
        :return: boolean to determine successful/failed run
        :rtype: bool
        """

        payload = value if isinstance(value, (str, bytes)) else json.dumps(value)
        return self._redis.set(name=key, value=payload, ex=expire_in_seconds)
    
    def get_value(self, key: str, default: dict = {}) -> dict:
        """
        Retrieves cached data

        :param key: cache key
        :type key: str
        :param default: default return value, defaults to {}
        :type default: dict, optional
        :return: _description_
        :rtype: dict
        """
        cached_data = self._redis.get(name=key)
        if cached_data:
            try:
                return json.loads(cached_data)
            except (json.JSONDecodeError, TypeError) as err:
                # TODO: Custom exception
                # TODO: Logging
                print(f"Internal exception occurred: {err}. Line no. {err.__traceback__.tb_lineno}")

        return default
        
    def delete_key(self, key: str) -> bool:
        
        return bool(self._redis.delete(key))

    def key_exists(self, key: str) -> bool:

        return self._redis.exists(key)

    def set_key_expiration(self, key: str, time_in_seconds: int) -> bool:

        return self._redis.expire(name=key, time=time_in_seconds)

    def flush_db(self) -> str:

        return self._redis.flushdb()
