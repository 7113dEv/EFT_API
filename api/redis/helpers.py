
import json
from api.data.serializers import BaseSerializer
from api.redis.clients import RedisClient


def add_to_redis(key: str, value: dict, expiration: int = None, redis_client: RedisClient = None) -> bool:
    try:
        r_c = redis_client or RedisClient()
        if isinstance(value, BaseSerializer):
            value_json = value.model_dump()
            value_to_save = json.dumps(value_json, default=str)
            r_c.set_value(key, value_to_save, expire_in_seconds=expiration)
        return 1
    except Exception as e:
        raise Exception(f"Exception occurred when adding to redis: {e}.")
    